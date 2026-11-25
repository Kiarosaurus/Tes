"""Figura de pipeline del protocolo fisico hibrido (comparador). MISMO caso que fig_brazos_mismo_implante.py:
dataset6_CLINIC_0101_data, semilla 0, corte central con M (eje SI, >=30 px de M), recorte 160x160, ventana [-500,1300] HU.
Etapas: TC sin metal -> implante de titanio (M) -> simulacion con titanio -> simulacion con titanio menos simulacion sin metal. Solo lectura."""
import numpy as np, nibabel as nib, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
P="/mnt/c/Users/Usuario/Downloads/pesados/outputs_obj3_pose/"; R="/mnt/c/Users/Usuario/onedrive/Desktop/metalsynth-pelvis-EDIT/"
caso="dataset6_CLINIC_0101_data"; LO,HI=-500,1300; H=80; DW=500  # DW: ventana simetrica del residuo (solo visualizacion)
base=P+"delta/run04_mejor/"; oi=nib.load(base+f"a15_{caso}_original.nii.gz"); O=np.asarray(oi.dataobj).astype(np.float32)
M=np.asarray(nib.load(base+f"a15_{caso}_M.nii.gz").dataobj)>0
ax=[i for i,c in enumerate(nib.aff2axcodes(oi.affine)) if c in "SI"][0]
cnt=M.sum(axis=tuple(i for i in range(3) if i!=ax)); ks=[int(k) for k in np.nonzero(cnt>=30)[0]]; k=ks[len(ks)//2]
sl=lambda v,kk: np.take(v,kk,axis=ax)
ys,xs=np.nonzero(sl(M,k)); cy,cx=int(ys.mean()),int(xs.mean()); y0,x0=max(cy-H,0),max(cx-H,0)
crop=lambda a: a[y0:y0+2*H,x0:x0+2*H]
W=lambda v:np.clip((v-LO)/(HI-LO),0,1)
z=np.load(R+f"experiments/objetivo3/outputs/obj3_pose/peters_val/a19_{caso}.npz"); kk=z["ks"]; ip=int(np.argmin(np.abs(kk-k)))
orig=crop(sl(O,k)); Mc=crop(sl(M,k)); ti=crop(z["Ti_A"][ip]); sin=crop(z["limpia_A"][ip]); res=ti-sin
fig=plt.figure(figsize=(6.3,1.45)); pw,gap,x=1.0/6.3,0.62/6.3,0.02; yb,ph=0.03,1.0/1.45
stages=[("TC sin metal",W(orig),"gray",0,1,False),("Implante de titanio\ninsertado (M)",W(orig),"gray",0,1,True),
        ("Artefacto simulado\n(imagen con titanio)",W(ti),"gray",0,1,False),("Diferencia con la\nsimulación sin metal",res,"gray",-DW,DW,False)]
labs=["inserción\nde M","simulación\nfísica","resta"]
for i,(t,im,cm,a,b,ov) in enumerate(stages):
    a_=fig.add_axes([x+i*(pw+gap),yb,pw,ph]); a_.imshow(im,cmap=cm,vmin=a,vmax=b); a_.set_xticks([]); a_.set_yticks([])
    if ov: a_.imshow(np.ma.masked_where(~Mc,Mc),cmap=matplotlib.colors.ListedColormap(["red"]),alpha=0.85,vmin=0,vmax=1)
    a_.set_title(t,fontsize=8,pad=3)
    for s in a_.spines.values(): s.set_linewidth(0.8)
    if i<3:
        xa=x+i*(pw+gap)+pw; yc=yb+ph/2
        fig.add_artist(FancyArrowPatch((xa+0.008,yc),(xa+gap-0.008,yc),transform=fig.transFigure,arrowstyle="-|>",mutation_scale=9,lw=1,color="k"))
        fig.text(xa+gap/2,yc+0.04,labs[i],ha="center",va="bottom",fontsize=8)
fig.savefig(R+"overleaf/figuras/pipeline_peters.pdf"); fig.savefig("/tmp/pipeline_peters.png",dpi=200)
print("corte",k,"idx peters",ip,"ks[ip]",int(kk[ip]),"res p1/p99",np.percentile(res,[1,99]))
