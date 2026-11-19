"""
Cuchara con ajuste de ángulo para catapulta - modelo paramétrico (CadQuery).

Ejes:  X = dirección del eje de giro del brazo (eje de acero)
       Y = dirección de lanzamiento (hacia donde abre la cuchara)
       Z = a lo largo del brazo, hacia la punta (punta del brazo en Z = 0)
Unidades: mm.   Ejecutar:  python cuchara_ajustable.py
"""
import math
import cadquery as cq

# ---------------- PARÁMETROS (cámbialos aquí) ----------------
ARM_X = 13.0      # espesor del brazo en dirección del eje (medido: 1.3 cm)
ARM_Y = 13.0      # ancho del brazo en dirección de lanzamiento  (CONFIRMAR)
CLR = 0.5         # holgura total: deja ~0.25 mm por lado para la capa de pegamento
WALL = 3.0        # pared del manguito
SLEEVE_L = 50.0   # largo que entra el brazo en el manguito (más área de pegado, abraza la rajadura)
CAP = 3.0         # espesor de la tapa del manguito
VENT_D = 3.0      # respiraderos para que salga el exceso de pegamento
VENT_Z = (-15.0, -35.0)  # posición de los respiraderos (bajo la punta del brazo)

PIV_D = 5.3       # perno del pivote (M5)
PIN_D = 3.2       # pasador de bloqueo (M3 o varilla de 3 mm)
STEM_T = 8.0      # espesor del tallo de la cuchara (en X)
STEM_W = 12.0     # ancho del tallo
HUB_R = 9.0       # radio del cubo del pivote
GAP = STEM_T + 0.6  # separación entre orejas
R1, R2 = 28.0, 35.0           # radios de las dos filas de agujeros
CHEEK_R = 41.0                # radio de las orejas (sector)
CHEEK_HALF = 40.0             # medio ángulo del sector de las orejas
ANG_MIN, ANG_MAX, STEP = -30, 30, 5   # rango de ajuste (grados)

BALL_D = 30.0     # proyectil: bolita de plastilina de 20 g (~29-30 mm de diámetro)
CUP_WALL = 2.5
CUP_DEPTH = 13.0  # profundidad interior del cuenco
CUP_DIST = 62.0   # distancia pivote -> centro del cuenco (a lo largo del tallo)
# --------------------------------------------------------------

OX = ARM_X + CLR + 2 * WALL           # ancho exterior del manguito en X
OY = ARM_Y + CLR + 2 * WALL           # ancho exterior del manguito en Y
PZ = CAP + 2.0 + HUB_R                # altura del pivote sobre la punta del brazo
RI = BALL_D / 2 + 2.0                 # radio interior del cuenco
RO = RI + CUP_WALL
CUT = CUP_DEPTH - RI                  # posición del plano del borde respecto al centro
CY = -STEM_W / 2 + RI + 2.0            # centro del cuenco en Y (2 mm de fondo sobre la base plana)
FLAT_Y = -STEM_W / 2                  # cara plana inferior (apoyo en la cama)


def positions():
    """Lista (ángulo, radio) de los agujeros de bloqueo: múltiplos de 10° en R1, el resto en R2."""
    out = []
    for a in range(ANG_MIN, ANG_MAX + 1, STEP):
        out.append((a, R1 if a % 10 == 0 else R2))
    return out


def soporte():
    # Manguito
    body = cq.Workplane("XY").box(OX, OY, SLEEVE_L + CAP, centered=(True, True, False)) \
        .translate((0, 0, -SLEEVE_L))
    pocket = cq.Workplane("XY").box(ARM_X + CLR, ARM_Y + CLR, SLEEVE_L, centered=(True, True, False)) \
        .translate((0, 0, -SLEEVE_L))
    body = body.cut(pocket)
    # Orejas (sector)
    a = math.radians(CHEEK_HALF)
    pts_end = (CHEEK_R * math.sin(a), PZ + CHEEK_R * math.cos(a))
    def prof():
        return (cq.Workplane("YZ").moveTo(-OY / 2, 0).lineTo(OY / 2, 0)
                .lineTo(*pts_end).threePointArc((0, PZ + CHEEK_R), (-pts_end[0], pts_end[1])).close())
    t = (OX - GAP) / 2
    for s in (1, -1):
        cheek = prof().extrude(t).translate((GAP / 2 if s > 0 else -OX / 2, 0, 0))
        body = body.union(cheek)
    # Agujero del pivote y agujeros de bloqueo (en X)
    def xhole(y, z, d):
        return cq.Workplane("YZ").center(y, z).circle(d / 2).extrude(OX + 2).translate((-OX / 2 - 1, 0, 0))
    body = body.cut(xhole(0, PZ, PIV_D))
    for ang, r in positions():
        th = math.radians(ang)
        body = body.cut(xhole(r * math.sin(th), PZ + r * math.cos(th), PIN_D))
    # Marcas grabadas cada 5° en las caras exteriores (0° más ancha)
    for ang, _ in positions():
        th = math.radians(ang)
        w = 1.4 if ang == 0 else 0.7
        for xs in (OX / 2 - 0.6, -OX / 2 - 0.4):
            tick = (cq.Workplane("XY").box(1.0, w, CHEEK_R - 38.0 + 1, centered=(False, True, False))
                    .translate((0, 0, 38.0))
                    .rotate((0, 0, 0), (1, 0, 0), -ang)
                    .translate((xs, 0, PZ)))
            body = body.cut(tick)
    # Respiraderos de pegamento (en Y, atraviesan solo las paredes del manguito; el brazo NO se perfora)
    for z in VENT_Z:
        body = body.cut(cq.Workplane("XZ").center(0, z).circle(VENT_D / 2).extrude(OY + 2, both=True))
    # Chaflán de entrada
    body = body.faces("<Z").edges().chamfer(0.6)
    return body


def cuchara():
    """Cuchara en coordenadas locales: pivote en el origen, tallo a lo largo de +Z, abre hacia +Y."""
    hub = cq.Workplane("YZ").circle(HUB_R).extrude(STEM_T).translate((-STEM_T / 2, 0, 0))
    stem = cq.Workplane("XY").box(STEM_T, STEM_W, CUP_DIST, centered=(True, True, False))
    outer = cq.Workplane("XY").sphere(RO).translate((0, CY, CUP_DIST))
    body = hub.union(stem).union(outer)
    # Vaciado del cuenco y corte del borde
    body = body.cut(cq.Workplane("XY").sphere(RI).translate((0, CY, CUP_DIST)))
    body = body.cut(cq.Workplane("XY").box(200, 200, 200, centered=(True, False, True))
                    .translate((0, CY + CUT, CUP_DIST)))
    # Base plana para imprimir (cara Y = -STEM_W/2)
    body = body.cut(cq.Workplane("XY").box(200, 200, 400, centered=(True, False, True))
                    .translate((0, -200 + FLAT_Y, 0)))
    # Pivote y agujeros de bloqueo en el tallo
    def xhole(z, d):
        return cq.Workplane("YZ").center(0, z).circle(d / 2).extrude(40).translate((-20, 0, 0))
    body = body.cut(xhole(0, PIV_D)).cut(xhole(R1, PIN_D)).cut(xhole(R2, PIN_D))
    # Redondeo del borde del cuenco
    try:
        body = body.faces(">Y").edges().fillet(0.8)
    except Exception:
        pass
    return body


def brazo_ref(length=120):
    return cq.Workplane("XY").box(ARM_X, ARM_Y, length, centered=(True, True, False)).translate((0, 0, -length))


def cuchara_en(theta):
    """Cuchara montada a un ángulo theta (grados). Positivo = inclinada hacia la dirección de tiro."""
    return cuchara().rotate((0, 0, 0), (1, 0, 0), -theta).translate((0, 0, PZ))


if __name__ == "__main__":
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    s, c = soporte(), cuchara()
    for name, part in (("soporte_cuchara", s), ("cuchara", c)):
        cq.exporters.export(part, os.path.join(root, "step", name + ".step"))
        cq.exporters.export(part, os.path.join(root, "stl", name + ".stl"), tolerance=0.02, angularTolerance=0.1)
    asm = cq.Assembly()
    asm.add(brazo_ref(), name="brazo_referencia", color=cq.Color(0.45, 0.33, 0.22))
    asm.add(s, name="soporte", color=cq.Color(0.15, 0.4, 0.8))
    asm.add(cuchara_en(0), name="cuchara", color=cq.Color(0.9, 0.3, 0.2))
    asm.save(os.path.join(root, "step", "ensamble_cuchara.step"))
    print("PZ (pivote sobre punta) =", PZ, "mm")
    print("Centro del cuenco sobre la punta del brazo (0°):", PZ + CUP_DIST, "mm; adelantado", CY, "mm")
    for n, (a, r) in enumerate(positions(), 1):
        print(f"posición {n:2d}: {a:+d}°  fila {'1 (R%.0f)' % R1 if r == R1 else '2 (R%.0f)' % R2}")
    print("Volumen soporte cm3:", round(s.val().Volume() / 1000, 1), " cuchara cm3:", round(c.val().Volume() / 1000, 1))
    # Comprobación de choques en todo el rango
    for a, _ in positions():
        inter = s.intersect(cuchara_en(a)).val().Volume()
        if inter > 1e-3:
            print("  CHOQUE a", a, "° volumen", inter)
