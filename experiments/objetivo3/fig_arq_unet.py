"""Figura de arquitectura del sintetizador base (run04_mejor): entrada de 11 canales, U-Net de 4 escalas, salida de 3 canales
y bucle de muestreo. Las dimensiones salen de src/renderizador/modelo.py y difusion.py.
Miniaturas reales: receptor 0101, semilla 0, mismo corte y recorte que fig_pipeline_sintetizador.py. Solo lectura de datos."""
import numpy as np, nibabel as nib, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

P = "/mnt/c/Users/Usuario/Downloads/pesados/outputs_obj3_pose/delta/run04_mejor/"; caso = "dataset6_CLINIC_0101_data"; LO, HI = -500, 1300; H = 80
ld = lambda s: nib.load(P + f"a15_{caso}_{s}.nii.gz")
oi = ld("original"); O = np.asarray(oi.dataobj).astype(np.float32); S = np.asarray(ld("run04_mejor_s0_sintetica").dataobj).astype(np.float32)
M = np.asarray(ld("M").dataobj) > 0; G = np.asarray(ld("G").dataobj) > 0
ax_ = [i for i, c in enumerate(nib.aff2axcodes(oi.affine)) if c in "SI"][0]
cnt = M.sum(axis=tuple(i for i in range(3) if i != ax_)); ks = [int(k) for k in np.nonzero(cnt >= 30)[0]]; k = ks[len(ks) // 2]
sl = lambda v, j=0: np.take(v, k + j, axis=ax_)
ys, xs = np.nonzero(sl(M)); cy, cx = int(ys.mean()), int(xs.mean()); y0, x0 = max(cy - H, 0), max(cx - H, 0)
cr = lambda a: a[y0:y0 + 2 * H, x0:x0 + 2 * H]
W = lambda v: np.clip((v - LO) / (HI - LO), 0, 1)
g0 = cr(sl(G) | sl(M)); m0 = cr(sl(M))
def ctx(j):
    im = W(cr(sl(O, j))); gg = cr(sl(G, j) | sl(M, j)); im = im.copy(); im[gg] = 0; return im
rng = np.random.default_rng(0)
ruido = np.where(g0, rng.standard_normal(g0.shape), 0.0)
sal = W(cr(sl(S)))
tint = lambda b, c: np.stack([b * c[i] for i in range(3)], -1)

# paleta sobria (sin rojo)
AZ, AZ_E = "#d6e2ef", "#5b7fa6"        # codificador
VE, VE_E = "#dbe9d9", "#5f8f5a"        # decodificador
AM, AM_E = "#f3e6c4", "#b08a2e"        # cuello de botella
AT, AT_E = "#e9cf8f", "#8a6a12"        # atencion
GR, GR_E = "#ececec", "#6b6b6b"        # neutro
TEAL = (0.10, 0.62, 0.70); YEL = (0.92, 0.70, 0.12)
INK = "#222222"; FS = 8



fig = plt.figure(figsize=(6.3, 6.9)); A = fig.add_axes([0, 0, 1, 1]); A.set_xlim(0, 168); A.set_ylim(0, 185); A.axis("off")

def caja(x, y, w, h, t, fc, ec, bold=False, fs=FS):
    A.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=1.2", fc=fc, ec=ec, lw=1.0, zorder=3))
    A.text(x, y, t, ha="center", va="center", fontsize=fs, color=INK, fontweight="bold" if bold else "normal", zorder=4, linespacing=1.05)
def flecha(p, q, ls="-", col=INK, lw=1.0, z=2):
    A.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="-|>", color=col, lw=lw, ls=ls, mutation_scale=9, shrinkA=0, shrinkB=0), zorder=z)
def txt(x, y, s, ha="center", va="center", col=INK, **k):
    A.text(x, y, s, ha=ha, va=va, fontsize=FS, color=col, linespacing=1.05, **k)
def mini(x, y, s, im, titulo, cmap="gray", vmin=0, vmax=1, arriba=True):
    A.imshow(im, cmap=cmap, vmin=vmin, vmax=vmax, extent=(x, x + s, y, y + s), zorder=2, aspect="auto", interpolation="nearest")
    A.add_patch(Rectangle((x, y), s, s, fc="none", ec=GR_E, lw=1.0, zorder=3))
    if titulo:
        if arriba: A.text(x + s / 2, y + s + 1.2, titulo, ha="center", va="bottom", fontsize=FS, color=INK, linespacing=1.05)
        else: A.text(x + s / 2, y - 1.2, titulo, ha="center", va="top", fontsize=FS, color=INK, linespacing=1.05)

# ---------------- a) entrada ----------------
s = 17; yi = 153
A.text(0, 184.5, "a) Entrada: 11 canales", fontsize=FS, fontweight="bold", va="top")
xs_ = [4, 29, 48, 76, 95]
mini(xs_[0], yi, s, ruido, "$x_t \\cdot G$", vmin=-2.5, vmax=2.5)
mini(xs_[1], yi, s, ctx(-1), "corte $k-1$")
mini(xs_[2], yi, s, ctx(+1), "corte $k+1$")
mini(xs_[3], yi, s, tint(m0.astype(float), YEL), "$M$")
mini(xs_[4], yi, s, tint(g0.astype(float), TEAL), "$G$")
def llave(x1, x2, y, t):
    A.plot([x1, x1, x2, x2], [y + 1.5, y, y, y + 1.5], color=INK, lw=0.9, zorder=3)
    txt((x1 + x2) / 2, y - 1.0, t, va="top")
llave(xs_[0], xs_[0] + s, yi - 2.0, "3 canales\n(LW, MW, SW)")
llave(xs_[1], xs_[2] + s, yi - 2.0, "6 canales de contexto\n(2 cortes $\\times$ 3 ventanas)")
llave(xs_[3], xs_[4] + s, yi - 2.0, "2 canales\nde máscara")
txt(122, yi + s / 2, "contexto con $G$ borrada;\ncorte central con ruido,\nmultiplicado por $G$", ha="left", col="#333333")
yc = 135
caja(58, yc, 100, 6.5, "concatenación en canales: 11 canales, parche de $256\\times256$", GR, GR_E)
for xx in (xs_[0] + s / 2, xs_[1] + (xs_[2] + s - xs_[1]) / 2, xs_[3] + (xs_[4] + s - xs_[3]) / 2):
    A.plot([xx, xx], [yi - 10.8, yc + 3.3], color=INK, lw=0.9, zorder=2)

# ---------------- b) U-Net ----------------
A.text(168, 129.5, "b) U-Net de 4 escalas (base 64, multiplicadores 1, 2, 4, 8)", fontsize=FS, fontweight="bold", va="center", ha="right")
bw, bh = 19, 9
ex, dx = 17, 100
yr = [108, 90, 72, 54]
ch = [64, 128, 256, 512]; res = ["256", "128", "64", "32"]
yconv = yr[0] + 13
caja(ex, yconv, 30, 5.5, "Conv $3{\\times}3$, $11\\to64$", GR, GR_E)
flecha((ex, yc - 3.3), (ex, yconv + 2.8))
for i in range(4):
    prev = 64 if i == 0 else ch[i - 1]
    caja(ex, yr[i], bw, bh, f"Bloque\n{prev}$\\to${ch[i]}", AZ, AZ_E)
    cin = ch[3 - i + 1] + ch[3 - i] if i > 0 else ch[3] + ch[3]
    caja(dx, yr[3 - i], bw, bh, f"Bloque\n{cin}$\\to${ch[3 - i]}", VE, VE_E)
    txt(0, yr[i], f"{res[i]}$^2$", ha="left", col="#444444")
flecha((ex, yconv - 2.8), (ex, yr[0] + bh / 2))
for i in range(3):
    flecha((ex, yr[i] - bh / 2), (ex, yr[i + 1] + bh / 2)); txt(ex + 1.5, (yr[i] + yr[i + 1]) / 2, "conv $s{=}2$", ha="left")
    flecha((dx, yr[3 - i] + bh / 2), (dx, yr[3 - i - 1] - bh / 2)); txt(dx + 1.5, (yr[3 - i] + yr[3 - i - 1]) / 2, "$\\times2$", ha="left")
for i in range(3):
    flecha((ex + bw / 2, yr[i]), (dx - bw / 2, yr[i]), col="#555555", lw=0.9, z=1)
txt(58.5, yr[0] + 1.0, "salto (concatenación)", va="bottom", col="#333333")
y3 = yr[3]; xm = [39, 58.5, 78]
caja(xm[0], y3, 17, bh, "Bloque\n512$\\to$512", AM, AM_E)
caja(xm[1], y3, 17, bh, "Atención\n(solo $32^2$)", AT, AT_E, bold=True)
caja(xm[2], y3, 17, bh, "Bloque\n512$\\to$512", AM, AM_E)
flecha((ex + bw / 2, y3), (xm[0] - 8.5, y3)); flecha((xm[0] + 8.5, y3), (xm[1] - 8.5, y3)); flecha((xm[1] + 8.5, y3), (xm[2] - 8.5, y3)); flecha((xm[2] + 8.5, y3), (dx - bw / 2, y3))
A.plot([ex + 4, ex + 4, dx - 4], [y3 - bh / 2, y3 - 8.0, y3 - 8.0], color="#555555", lw=0.9, zorder=1)
flecha((dx - 4, y3 - 8.0), (dx - 4, y3 - bh / 2), col="#555555", lw=0.9, z=1)
# salida
yout = yr[0] + 13
caja(dx, yout, 44, 5.5, "GN, SiLU, Conv $3{\\times}3$, $64\\to3$", GR, GR_E)
flecha((dx, yr[0] + bh / 2), (dx, yout - 2.8))
flecha((dx + 22, yout), (128, yout))
caja(148, yout, 36, 11, "$\\hat{\\mathbf{v}}$: 3 canales\n(corte central en\nLW, MW y SW)", GR, GR_E)
# embedding del paso
yt = 36
caja(58.5, yt, 74, 6.5, "paso $t$: embedding sinusoidal (64) $\\to$ MLP (256)", GR, GR_E)
flecha((58.5, yt + 3.3), (58.5, y3 - bh / 2), col="#555555", lw=1.0)
txt(98, yt, "se suma en\ncada Bloque", ha="left", col="#333333")
txt(36, y3 - 10.6, "salto", col="#333333")
# ---------------- c) bucle ----------------
A.add_patch(Rectangle((0.5, 0.8), 167, 31.5, fc="#f5f5f5", ec="#bdbdbd", lw=0.9, zorder=0))
txt(3, 29.8, "c) Bucle de muestreo: calendario coseno de 1000 pasos; DDIM determinista de 50 pasos", ha="left", fontweight="bold")
sb = 13; ty = 9.0; cy_ = ty + sb / 2
mini(4, ty, sb, ruido, "ruido en $G$", vmin=-2.5, vmax=2.5, arriba=False)
caja(48, cy_, 42, 11, "U-Net: $\\hat{\\mathbf{v}}\\to\\hat{\\mathbf{x}}_0$\ny siguiente $x_t$, en $G$", AZ, AZ_E)
flecha((4 + sb, cy_), (27, cy_))
A.plot([62, 62, 34], [cy_ + 5.5, cy_ + 8.5, cy_ + 8.5], color=INK, lw=1.0, zorder=3)
flecha((34, cy_ + 8.5), (34, cy_ + 5.6))
txt(48, cy_ + 10.8, "se repite 50 veces", va="center")
caja(112, cy_, 54, 11, "copia fuera de $G$:\n$\\hat{\\mathbf{x}}_0\\cdot G+$ original $\\cdot(1-G)$", AM, AM_E)
flecha((69, cy_), (85, cy_))
flecha((139, cy_), (150, cy_))
mini(150, ty, sb, sal, "salida", arriba=False)

fig.savefig("/mnt/c/Users/Usuario/onedrive/Desktop/metalsynth-pelvis-EDIT/overleaf/figuras/arq_unet.pdf", )
fig.savefig("/tmp/arq_unet.png", dpi=170, )
print("corte", k, "eje", ax_)
