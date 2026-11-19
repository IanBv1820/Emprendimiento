# Cuchara con ajuste de ángulo para la catapulta

Diseño para impresión 3D en PLA. Son dos piezas impresas más tornillería estándar:

| Pieza | Archivo STEP (abrir en Inventor) | Archivo STL (imprimir) |
|---|---|---|
| Soporte (manguito + orejas con agujeros de ángulo) | `step/soporte_cuchara.step` | `stl/soporte_cuchara.stl` |
| Cuchara (cuenco + tallo con pivote) | `step/cuchara.step` | `stl/cuchara.stl` |
| Ensamble de referencia (con trozo de brazo) | `step/ensamble_cuchara.step` | — |

![Vistas](img/vistas_3d.png)

## Cómo funciona

1. El **soporte** se mete en la punta del brazo como un capuchón y se fija con un tornillo M4 que atraviesa el brazo.
2. La **cuchara** gira sobre un perno M5 (pivote) entre las dos orejas del soporte.
3. Las orejas tienen **13 agujeros de bloqueo** en dos filas. Un pasador M3 atraviesa las dos orejas y el tallo de la cuchara para trabar el ángulo.
   - Fila interior (R = 28 mm): −30°, −20°, −10°, 0°, +10°, +20°, +30°. Usa el agujero del tallo a 28 mm del pivote.
   - Fila exterior (R = 35 mm): −25°, −15°, −5°, +5°, +15°, +25°. Usa el agujero del tallo a 35 mm del pivote.
   - Resultado: **de −30° a +30° en pasos de 5°**. Las caras exteriores de las orejas llevan una marca grabada por posición; la de 0° es más ancha.

![Ángulos](img/vista_lateral_angulos.png)

**Qué efecto tiene cada ángulo** (es la tendencia esperada; hay que confirmarla con disparos de prueba):

- **Negativo** (cuchara inclinada hacia atrás, con la boca mirando hacia afuera del brazo): la pelota sale antes durante el giro y el tiro es **más alto y parabólico**.
- **Positivo** (cuchara inclinada hacia la dirección de tiro): la pelota se retiene más tiempo y el tiro es **más bajo y tenso**.

> El soporte es simétrico: si el brazo gira hacia el otro lado, se gira el soporte 180° antes de fijarlo.

## Tornillería

| Uso | Elemento |
|---|---|
| Pivote de la cuchara | Tornillo M5 × 25 (o × 30 con mariposa) + tuerca mariposa o tuerca de seguridad (nyloc) |
| Pasador de ángulo | Tornillo M3 × 25 + tuerca, o varilla/clavo de 3 mm |
| Fijación al brazo | Tornillo M4 × 25–30 + tuerca nyloc (hay que perforar el brazo con broca de 4 mm a 10 mm de la punta) |

## Parámetros (para modelar en Inventor: *Administrar → Parámetros (fx)*)

| Parámetro | Valor | Descripción |
|---|---|---|
| `arm_x` | 13 mm | espesor del brazo en dirección del eje (**medido**) |
| `arm_y` | 13 mm | ancho del brazo en dirección de tiro (**POR CONFIRMAR**) |
| `clr` | 0.4 mm | holgura de impresión |
| `wall` | 3 mm | pared del manguito |
| `sleeve_l` | 45 mm | profundidad del manguito |
| `cap` | 3 mm | tapa del manguito |
| `hole_tip` | 10 mm | distancia de la punta del brazo al tornillo M4 |
| `piv_d` | 5.3 mm | agujero del pivote (M5) |
| `pin_d` | 3.2 mm | agujeros de bloqueo (M3) |
| `stem_t` | 8 mm | espesor del tallo |
| `stem_w` | 12 mm | ancho del tallo |
| `hub_r` | 9 mm | radio del cubo del pivote |
| `gap` | stem_t + 0.6 = 8.6 mm | separación entre orejas |
| `r1` / `r2` | 28 / 35 mm | radios de las filas de agujeros |
| `cheek_r` | 41 mm | radio del sector de las orejas |
| `ball_d` | 40 mm | diámetro del proyectil (**POR CONFIRMAR**) |
| `cup_ri` | ball_d/2 + 2 = 22 mm | radio interior del cuenco |
| `cup_wall` | 2.5 mm | pared del cuenco |
| `cup_depth` | 16 mm | profundidad interior del cuenco |
| `cup_dist` | 68 mm | distancia del pivote al centro del cuenco |

Valores derivados:

- Exterior del manguito: `arm_x + clr + 2·wall` = **19.4 mm** (igual en Y).
- Altura del pivote sobre la punta del brazo: `cap + 2 + hub_r` = **14 mm**.
- Espesor de cada oreja: `(19.4 − 8.6)/2` = **5.4 mm**.

## Paso a paso en Inventor

Ejes del modelo: **X** = dirección del eje de acero, **Y** = dirección de tiro, **Z** = a lo largo del brazo. La punta del brazo está en Z = 0.

### Pieza 1: Soporte (`soporte_cuchara.ipt`)

1. **Boceto en plano XY**: cuadrado de 19.4 × 19.4 centrado. Extruir **48 mm** hacia −Z (45 de manguito + 3 de tapa). Ubicar la cara superior en Z = +3.
2. **Cavidad**: en la cara inferior, cuadrado de 13.4 × 13.4 centrado. Extruir un corte de **45 mm** (queda la tapa de 3 mm arriba). Añadir un chaflán de 0.6 mm en la entrada.
3. **Orejas**: boceto en el plano YZ con este perfil:
   - Base de Y = −9.7 a +9.7 en Z = 0.
   - Dos líneas hasta (±26.35, 45.41).
   - Arco de **R41** con centro en (0, 14) que pasa por (0, 55).

   Extruir el perfil de X = 4.3 a X = 9.7, es decir **5.4 mm**. Hacer una simetría de esa extrusión respecto del plano YZ.
4. **Pivote**: agujero pasante de Ø5.3 en X, centrado en (Y 0, Z 14).
5. **Agujeros de bloqueo** (Ø3.2, pasantes en X). Centro de cada agujero en Y = r·sen(θ), Z = 14 + r·cos(θ):
   - Fila r = 28: θ = −30, −20, −10, 0, 10, 20, 30.
   - Fila r = 35: θ = −25, −15, −5, 5, 15, 25.

   Lo más cómodo es dibujar un agujero y usar un **patrón circular** con centro en el pivote: 7 instancias × 10° para la fila 1 y 6 instancias × 10° para la fila 2, empezando en −25°.
6. **Marcas** (opcional): ranuras de 0.7 × 0.6 mm de profundidad entre R38 y R41, cada 5°, en las dos caras exteriores.
7. **Tornillo de fijación**: agujero pasante de Ø4.3 en dirección Y, en (X 0, Z −10).

### Pieza 2: Cuchara (`cuchara.ipt`)

Origen en el pivote. El tallo va hacia +Z y el cuenco abre hacia +Y.

1. **Cubo**: boceto en plano YZ, círculo de R9 en el origen. Extruir **8 mm** simétrico (X ±4).
2. **Tallo**: rectángulo en plano XY de 8 (X) × 12 (Y), centrado. Extruir de Z = 0 a Z = 68.
3. **Cuenco**:
   - Revolución o esfera de **R24.5** con centro en (Y 18, Z 68), unida al tallo.
   - Esfera de **R22** en el mismo centro, como **corte**.
   - Corte con plano en **Y = 12**: elimina todo lo que esté en Y > 12 y deja la boca del cuenco con 16 mm de profundidad.
4. **Base plana**: corte de todo lo que esté en **Y < −6**. Esa cara es la que apoya en la cama de la impresora.
5. **Agujeros**: Ø5.3 en el origen (pivote) y dos de Ø3.2 en el tallo, a **Z = 28** y **Z = 35**, todos pasantes en X.
6. Redondeo de 0.8 mm en el borde del cuenco.

### Ensamble (`catapulta_cuchara.iam`)

1. Restricción **Insertar** entre el agujero de Ø5.3 de la cuchara y el del soporte.
2. Restricción **Simetría** (o Coincidente con offset) para que el tallo quede centrado entre las orejas: 0.3 mm de holgura por lado.
3. Restricción **Ángulo** entre el tallo y el eje Z del soporte, usando un parámetro `theta`. Así se puede mostrar cada posición de −30° a +30°.
4. Para el brazo: restricción Coincidente entre la cara interior de la tapa y la punta del brazo, más un eje del tornillo M4.

## Impresión (PLA)

- **Capa**: 0.2 mm. **Paredes**: 4 perímetros. **Superior/inferior**: 5 capas. **Relleno**: 40–50 % giroide.
- **Soporte**: imprimir de pie, con la boca del manguito **hacia la cama**. No necesita soportes; la tapa de 13 mm se imprime como puente.
- **Cuchara**: imprimir acostada sobre su cara plana (Y = −6), con el cuenco **hacia arriba**. Activar soportes **solo desde la cama** bajo el cuenco.
- **Volumen** (sólido): soporte 29 cm³ y cuchara 12 cm³. Con el relleno indicado son unos 20 g + 10 g de PLA.
- Si los agujeros salen chicos, pasar una broca del diámetro nominal: 3, 4 y 5 mm.

## A tener en cuenta

- El centro del cuenco queda **82 mm por encima de la punta del brazo** y 18 mm adelantado. Con el brazo de 30 cm hasta el pivote, el radio efectivo es de unos **38 cm**. Si el radio total debe ser 30 cm, hay que acortar el brazo unos 8 cm.
- Para un ajuste fino del alcance conviene combinar esta cuchara con un **tope** que frene el brazo (barra transversal entre las placas laterales).

## Modelo paramétrico (código)

`cad/cuchara_ajustable.py` (CadQuery) regenera todos los STEP/STL. Se cambian los parámetros al inicio del archivo y se ejecuta:

```bash
pip install cadquery
python cad/cuchara_ajustable.py   # genera step/ y stl/ y verifica que no haya choques de -30° a +30°
python cad/render.py              # regenera las imágenes
```
