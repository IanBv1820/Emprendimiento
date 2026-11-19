"""Genera imágenes de referencia del diseño (vista isométrica y vista lateral de ángulos)."""
import os, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from cuchara_ajustable import *

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def tris(wp, tol=0.3):
    v, t = wp.val().tessellate(tol, 0.3)
    v = np.array([(p.x, p.y, p.z) for p in v])
    return v[np.array(t)]

def shade(tri, base, light=np.array([0.4, -0.5, 0.8])):
    n = np.cross(tri[:, 1] - tri[:, 0], tri[:, 2] - tri[:, 0])
    n /= np.linalg.norm(n, axis=1, keepdims=True) + 1e-12
    k = 0.35 + 0.65 * np.abs(n @ (light / np.linalg.norm(light)))
    return np.clip(np.array(base)[None, :] * k[:, None], 0, 1)

def draw(ax, parts, elev, azim, lim):
    for wp, col in parts:
        tr = tris(wp)
        pc = Poly3DCollection(tr, facecolors=shade(tr, col), edgecolor="none")
        ax.add_collection3d(pc)
    (x0, x1), (y0, y1), (z0, z1) = lim
    ax.set_xlim(x0, x1); ax.set_ylim(y0, y1); ax.set_zlim(z0, z1)
    ax.set_box_aspect((x1 - x0, y1 - y0, z1 - z0))
    ax.view_init(elev=elev, azim=azim); ax.set_axis_off()

BLUE, RED, WOOD = (0.25, 0.5, 0.9), (0.95, 0.35, 0.25), (0.6, 0.45, 0.3)
lim = ((-60, 60), (-60, 60), (-70, 120))

fig = plt.figure(figsize=(14, 7), dpi=130)
ax = fig.add_subplot(1, 3, 1, projection="3d")
draw(ax, [(brazo_ref(70), WOOD), (soporte(), BLUE), (cuchara_en(0), RED)], 22, 35, lim)
ax.set_title("Ensamble (0°)")
ax = fig.add_subplot(1, 3, 2, projection="3d")
draw(ax, [(soporte(), BLUE)], 20, -60, ((-30, 30), (-30, 30), (-50, 60)))
ax.set_title("Soporte (manguito + orejas)")
ax = fig.add_subplot(1, 3, 3, projection="3d")
draw(ax, [(cuchara(), RED)], 30, 55, ((-30, 30), (-15, 45), (-12, 100)))
ax.set_title("Cuchara")
plt.tight_layout(); plt.savefig(os.path.join(ROOT, "img", "vistas_3d.png")); plt.close()

# Vista lateral (plano YZ) con -30°, 0°, +30°
fig, ax = plt.subplots(figsize=(8, 8), dpi=130)
def side(wp, **kw):
    tr = tris(wp, 0.5)
    for t in tr:
        ax.fill(t[:, 1], t[:, 2], lw=0, **kw)
side(brazo_ref(60), color=(0.75, 0.62, 0.5))
side(soporte(), color=(0.55, 0.7, 0.95))
for a, col in ((-30, (0.2, 0.6, 0.3, 0.35)), (0, (0.95, 0.35, 0.25, 0.55)), (30, (0.6, 0.3, 0.8, 0.35))):
    side(cuchara_en(a), color=col)
    th = math.radians(a)
    ax.annotate(f"{a:+d}°", (110 * math.sin(th) + 18, PZ + 110 * math.cos(th)), fontsize=12, weight="bold")
for ang, r in positions():
    th = math.radians(ang)
    ax.add_patch(plt.Circle((r * math.sin(th), PZ + r * math.cos(th)), PIN_D / 2, fc="white", ec="k", lw=0.5))
ax.add_patch(plt.Circle((0, PZ), PIV_D / 2, fc="white", ec="k"))
ax.annotate("", xy=(55, -40), xytext=(15, -40), arrowprops=dict(arrowstyle="->", lw=2))
ax.text(18, -36, "dirección de tiro (+Y)")
ax.text(-14, -58, "brazo", rotation=90)
ax.set_aspect("equal"); ax.set_xlim(-80, 110); ax.set_ylim(-60, 140)
ax.set_xlabel("Y [mm]"); ax.set_ylabel("Z [mm] (0 = punta del brazo)"); ax.grid(alpha=0.3)
ax.set_title("Rango de ajuste: -30° a +30° en pasos de 5° (13 posiciones)")
plt.tight_layout(); plt.savefig(os.path.join(ROOT, "img", "vista_lateral_angulos.png")); plt.close()
print("ok")

# Corte del manguito (plano YZ, X = 0): hueco cónico y punta redondeada
import numpy as np
fig, ax = plt.subplots(figsize=(6, 8), dpi=130)
def prof_pts(length, clr):
    r = ARM_Y_TIP / 2; rr = r + clr / 2; wb = arm_width(length) + clr
    arc = [(rr * math.cos(t), -r + rr * math.sin(t)) for t in np.linspace(0, math.pi, 40)]
    return np.array([(wb / 2, -length)] + arc + [(-wb / 2, -length)])
ax.add_patch(plt.Rectangle((-OY / 2, -SLEEVE_L), OY, SLEEVE_L + CAP, fc=(0.55, 0.7, 0.95), ec="k"))
ax.fill(*prof_pts(SLEEVE_L, CLR).T, color="white", ec="k")
ax.fill(*prof_pts(SLEEVE_L + 15, 0).T, color=(0.75, 0.62, 0.5), alpha=0.85)
for z in VENT_Z:
    ax.add_patch(plt.Rectangle((-OY / 2, z - VENT_D / 2), WALL + 1.5, VENT_D, fc="white", ec="k", lw=0.5))
    ax.add_patch(plt.Rectangle((OY / 2 - WALL - 1.5, z - VENT_D / 2), WALL + 1.5, VENT_D, fc="white", ec="k", lw=0.5))
def dim(y0, y1, z, txt):
    ax.annotate("", (y0, z), (y1, z), arrowprops=dict(arrowstyle="<->", lw=0.8)); ax.text((y0 + y1) / 2, z + 0.8, txt, ha="center", fontsize=9)
dim(-(ARM_Y_TIP + CLR) / 2, (ARM_Y_TIP + CLR) / 2, -ARM_Y_TIP / 2, f"{ARM_Y_TIP + CLR:.1f}")
dim(-(arm_width(SLEEVE_L) + CLR) / 2, (arm_width(SLEEVE_L) + CLR) / 2, -SLEEVE_L + 3, f"{arm_width(SLEEVE_L) + CLR:.1f}")
dim(-OY / 2, OY / 2, CAP + 2, f"{OY:.1f}")
ax.annotate("", (OY / 2 + 3, 0), (OY / 2 + 3, -SLEEVE_L), arrowprops=dict(arrowstyle="<->", lw=0.8))
ax.text(OY / 2 + 4, -SLEEVE_L / 2, f"{SLEEVE_L:.0f} mm\ndentro del\nsoporte", va="center", fontsize=9)
ax.text(OY / 2 + 4, -ARM_Y_TIP / 2 + 2, f"punta R{ARM_Y_TIP/2:.0f}", fontsize=9)
for z in VENT_Z:
    ax.text(-OY / 2 - 1, z, "respiradero Ø3 ", ha="right", va="center", fontsize=8)
ax.text(0, -SLEEVE_L - 8, "brazo (MDF 13 mm de espesor)", ha="center", fontsize=9)
ax.set_aspect("equal"); ax.set_xlim(-32, 36); ax.set_ylim(-58, 10); ax.axis("off")
ax.set_title("Corte del manguito: hueco a la medida del brazo\n(cotas en mm, ya incluyen 0.5 mm de holgura para pegamento)", fontsize=10)
plt.tight_layout(); plt.savefig(os.path.join(ROOT, "img", "corte_manguito.png")); plt.close()
