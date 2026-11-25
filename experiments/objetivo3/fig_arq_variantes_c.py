"""Figura de arquitectura de las variantes del criterio (c), exploratorias y post hoc, sobre la misma U-Net de arq_unet.pdf.
Dimensiones tomadas de src/renderizador/{entrenar,datos,difusion,angular,texturas}.py:
  B: canal T (en el texto, Gamma_M) -> 11 + 1 = 12 canales de entrada (cache_T); termino angular perdida_ang = L_v + lam * L_ang.
  A: PatchD (5 canales: x 3 + M + G; 3 conv 4x4 s2 + conv 3x3 s1; salida H/8 x W/8; spectral_norm; LeakyReLU 0.2; hinge).
  P/T: perdida_percep (piramide laplaciana de 3 niveles + residuo, pesos 1,1,1,0.5; L1 en G) y perdida_textura (MW, SW).
Solo bloques, sin datos."""
import matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

AZ, AZ_E = "#d6e2ef", "#5b7fa6"
VE, VE_E = "#dbe9d9", "#5f8f5a"
AM, AM_E = "#f3e6c4", "#b08a2e"
GR, GR_E = "#ececec", "#6b6b6b"
INK = "#222222"; FS = 8; MUT = "#444444"


fig = plt.figure(figsize=(6.3, 7.3)); A = fig.add_axes([0, 0, 1, 1]); A.set_xlim(0, 168); A.set_ylim(0, 194); A.axis("off")

def caja(x, y, w, h, t, fc, ec, bold=False, ls="-", fs=FS):
    A.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=1.2", fc=fc, ec=ec, lw=1.0, ls=ls, zorder=3))
    A.text(x, y, t, ha="center", va="center", fontsize=fs, color=INK, fontweight="bold" if bold else "normal", zorder=4, linespacing=1.05)
def flecha(p, q, col=INK, lw=1.0, z=2):
    A.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="-|>", color=col, lw=lw, mutation_scale=9, shrinkA=0, shrinkB=0), zorder=z)
def linea(xs, ys, col=INK, lw=1.0):
    A.plot(xs, ys, color=col, lw=lw, zorder=2, solid_capstyle="butt")
def txt(x, y, s, ha="center", va="center", col=INK, **k):
    A.text(x, y, s, ha=ha, va=va, fontsize=FS, color=col, linespacing=1.05, **k)
def marco(y0, y1, titulo):
    A.add_patch(Rectangle((0.5, y0), 167, y1 - y0, fc="#f7f7f7", ec="#bdbdbd", lw=0.9, zorder=0))
    txt(3, y1 - 3.4, titulo, ha="left", fontweight="bold")
def solo_entren(x0, y0, x1, y1):
    A.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc="none", ec="#555555", lw=1.0, ls=(0, (4, 2.5)), zorder=1))
    A.text(x1 - 1.5, y1 - 1.2, "solo en entrenamiento", ha="right", va="top", fontsize=FS, color="#333333", style="italic", zorder=2)

# =====================================================  B  =====================================================
y0, y1 = 130, 193
marco(y0, y1, "B: canal $\\Gamma_M$ (canal $T$ en el código) y término angular")
caja(22, 177, 38, 9, "11 canales de entrada\n(modelo base)", GR, GR_E)
caja(22, 162, 38, 11, "canal $\\Gamma_M$: 1 canal,\ncalculado solo desde $M$", AM, AM_E, ls=(0, (3, 2)))
txt(3, 153, "se usa en entrenamiento y en síntesis", ha="left", col=MUT)
caja(68, 169.5, 25, 20, "U-Net\n(entrada de\n12 canales)", AZ, AZ_E)
flecha((41, 177), (55.5, 173)); flecha((41, 162), (55.5, 166))
caja(94, 177, 13, 7, "$\\hat{\\mathbf{v}}$", GR, GR_E)
caja(94, 160, 13, 7, "$\\hat{\\mathbf{x}}_0$", GR, GR_E)
flecha((81, 173), (87.5, 176)); flecha((94, 173.4), (94, 163.6))
txt(96, 168.5, "$\\mathbf{x}_0$ estimada", ha="left", col=MUT)
solo_entren(109, 134, 166, 187)
caja(139, 176.5, 50, 8, "$L_v$: MSE de $\\mathbf{v}$ en $G$", AM, AM_E)
caja(139, 158, 50, 17, "$L_{ang}$: amplitud angular de\n$\\hat{\\mathbf{x}}_0$ frente a la de $\\mathbf{x}_0$\n(anillos de 2 a 11 px alrededor\nde $M$, en $G$)", AM, AM_E)
caja(139, 140, 50, 7, "$L = L_v + \\lambda\\,L_{ang}$", AM, AM_E, bold=True)
flecha((100.5, 177), (114, 177)); flecha((100.5, 160), (114, 160))
flecha((139, 149.5), (139, 143.6))
txt(3, 138, "El canal y $L_{ang}$ se usan por separado:\ncon $L_{ang}$ la entrada sigue en 11 canales.", ha="left", col=MUT)

# =====================================================  A  =====================================================
y0, y1 = 70, 126
marco(y0, y1, "A: generador y discriminador PatchGAN condicionado a $M$ y $G$")
caja(15, 106, 25, 9, "U-Net\n(generador)", AZ, AZ_E)
caja(62, 106, 42, 10, "$\\hat{\\mathbf{x}}_0$ (3 canales) + $M$ + $G$\n= 5 canales", GR, GR_E)
caja(62, 88, 42, 10, "$\\mathbf{x}_0$ real (3 canales) + $M$ + $G$\n= 5 canales", GR, GR_E)
flecha((27.5, 106), (41, 106))
solo_entren(90, 73, 166, 120)
caja(128, 96, 72, 29, "Discriminador $D$ (5 canales de entrada)\nConv 4$\\times$4, $s{=}2$: 5$\\to$32$\\to$64$\\to$128\n(LeakyReLU 0.2 tras cada una)\nConv 3$\\times$3, $s{=}1$: 128$\\to$1\nnormalización espectral en todas", VE, VE_E)
flecha((83, 106), (92, 101)); flecha((83, 88), (92, 91))
txt(128, 78.5, "salida de $H/8 \\times W/8$: un puntaje por parche", col=MUT)
txt(3, 77, "pérdida hinge: $L_D$ para $D$\ny $L_{adv}$ para el generador,\nen los parches de $G$, con $t < t_{max}$", ha="left", col=INK)

# =====================================================  P/T  =====================================================
y0, y1 = 0.5, 66
marco(y0, y1, "P y T: pérdidas perceptual-proxy y de textura sobre $\\hat{\\mathbf{x}}_0$")
caja(15, 31, 26, 14, "$\\hat{\\mathbf{x}}_0$ y $\\mathbf{x}_0$ real\n(3 canales cada\nuno)", GR, GR_E)
solo_entren(31, 3, 166, 60)
caja(65, 46, 40, 15, "Pirámide laplaciana\nde 3 niveles + residuo\n(sin red preentrenada)", VE, VE_E)
caja(65, 17, 40, 15, "Alta frecuencia (imagen\nmenos media de 5$\\times$5) y\ndesviación local de 9$\\times$9", VE, VE_E)
linea([28, 33], [31, 31]); linea([33, 33], [17, 46]); flecha((33, 46), (45, 46)); flecha((33, 17), (45, 17))
caja(128, 46, 58, 15, "$L_{per}$: L1 por nivel (pesos 1, 1, 1\ny 0.5), enmascarado a $G$", AM, AM_E)
caja(128, 17, 58, 15, "$L_{tex}$: diferencia cuadrática de los\nlogaritmos de la desviación local\n(MW y SW), en $G$ sin $M$ dilatada", AM, AM_E)
flecha((85, 46), (99, 46)); flecha((85, 17), (99, 17))
caja(128, 31.5, 58, 7, "$L = L_v + \\lambda_{per} L_{per} + \\lambda_{tex} L_{tex}$", AM, AM_E, bold=True)
flecha((128, 38.5), (128, 35.1), lw=0.9); flecha((128, 24.5), (128, 28.0), lw=0.9)
txt(98.5, 6.3, "cada término cuenta solo con $t < t_{max}$", col=MUT)

fig.savefig("/mnt/c/Users/Usuario/onedrive/Desktop/metalsynth-pelvis-EDIT/overleaf/figuras/arq_variantes_c.pdf", )
fig.savefig("/tmp/arq_variantes_c.png", dpi=170, )
