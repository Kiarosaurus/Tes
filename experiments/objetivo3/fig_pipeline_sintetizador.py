"""Figura del flujo del sintetizador (inpainting) con la miniatura real de cada etapa.
Caso fijo: receptor de validacion 0101, semilla 0, corte central con M (eje SI, >=30 px de M, el del medio), recorte 160x160, ventana [-500,1300]. Solo lectura."""
import numpy as np, nibabel as nib, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
P="/mnt/c/Users/Usuario/Downloads/pesados/outputs_obj3_pose/delta/run04_mejor/"; caso="dataset6_CLINIC_0101_data"; LO,HI=-500,1300; H=80
ld=lambda s:nib.load(P+f"a15_{caso}_{s}.nii.gz")
oi=ld("original"); O=np.asarray(oi.dataobj).astype(np.float32); S=np.asarray(ld("run04_mejor_s0_sintetica").dataobj).astype(np.float32)
M=np.asarray(ld("M").dataobj)>0; G=np.asarray(ld("G").dataobj)>0
ax=[i for i,c in enumerate(nib.aff2axcodes(oi.affine)) if c in "SI"][0]
cnt=M.sum(axis=tuple(i for i in range(3) if i!=ax)); ks=[int(k) for k in np.nonzero(cnt>=30)[0]]; k=ks[len(ks)//2]
sl=lambda v:np.take(v,k,axis=ax)
ys,xs=np.nonzero(sl(M)); cy,cx=int(ys.mean()),int(xs.mean()); y0,x0=max(cy-H,0),max(cx-H,0)
cr=lambda a:a[y0:y0+2*H,x0:x0+2*H]
W=lambda v:np.clip((v-LO)/(HI-LO),0,1)
o,s,m,g=[cr(sl(v)) for v in (O,S,M,G)]; g=g|m
def over(mask,col):
    rgb=np.stack([W(o)]*3,-1); c=np.array(col); rgb[mask]=0.55*rgb[mask]+0.45*c; return rgb
ctx=np.stack([W(o)]*3,-1); ctx[g]=0
d=np.where(g,s-o,0); vm=max(np.percentile(np.abs(d[g]),99),1)
fs=8
fig=plt.figure(figsize=(6.3,5.0))
tit=["1. TC sin metal\ndel receptor","2. Máscara del\nimplante $M$","3. Región de generación\n$G = M \\cup B_\\delta$","4. Contexto: original\nfuera de $G$","5. Salida del\nsintetizador","6. Diferencia\nsalida $-$ original"]
ims=[(W(o),"gray"),(over(m,(1,0.1,0.1)),None),(over(g,(0.1,0.8,1)),None),(ctx,None),(W(s),"gray"),(d,"RdBu_r")]
pos=[(0.03,0.52),(0.37,0.52),(0.71,0.52),(0.03,0.04),(0.37,0.04),(0.71,0.04)]
w,h=0.26,0.36
for t,(im,cm),(px,py) in zip(tit,ims,pos):
    a=fig.add_axes([px,py,w,h*0.9*1.0]); 
    if cm=="RdBu_r": a.imshow(im,cmap=cm,vmin=-vm,vmax=vm)
    elif cm: a.imshow(im,cmap=cm,vmin=0,vmax=1)
    else: a.imshow(im)
    a.set_xticks([]); a.set_yticks([])
    for sp in a.spines.values(): sp.set_linewidth(1.2)
    a.set_title(t,fontsize=fs,pad=3)
    if cm=="RdBu_r":
        cax=fig.add_axes([px,py-0.035,w,0.015]); cb=fig.colorbar(a.images[0],cax=cax,orientation="horizontal"); cb.ax.tick_params(labelsize=7); cb.set_label("HU (dentro de $G$)",fontsize=7,labelpad=1)
def arr(p,q,txt=None):
    fig.add_artist(FancyArrowPatch(p,q,transform=fig.transFigure,arrowstyle="-|>",mutation_scale=12,lw=1.3,color="k"))
    if txt: fig.text((p[0]+q[0])/2,(p[1]+q[1])/2+0.012,txt,ha="center",fontsize=7)
yt=0.52+h*0.45
arr((0.30,yt),(0.36,yt)); arr((0.64,yt),(0.70,yt),"+ $B_\\delta$")
arr((0.30,0.04+h*0.45),(0.36,0.04+h*0.45),"modelo"); arr((0.64,0.04+h*0.45),(0.70,0.04+h*0.45),"$-$ orig.")
arr((0.84,0.50),(0.16,0.43),"copia fuera de $G$")
fig.savefig("/mnt/c/Users/Usuario/onedrive/Desktop/metalsynth-pelvis-EDIT/overleaf/figuras/pipeline_sintetizador.pdf",bbox_inches="tight")
fig.savefig("/tmp/pipeline_sintetizador.png",dpi=150,bbox_inches="tight")
print("corte",k,"eje",ax)
