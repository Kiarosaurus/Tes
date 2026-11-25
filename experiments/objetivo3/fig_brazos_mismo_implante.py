"""Figura para la regla (c): el MISMO implante (misma pose, paciente de validacion 0101, corte central con M, semilla 0) con distintos brazos,
ordenados por el puntaje medio de credibilidad que les dio la autora a ciegas (01-decisiones 2026-11-21 (15)). Real: metal_0039. Solo lectura."""
import numpy as np, nibabel as nib, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from scipy import ndimage as ndi
P="/mnt/c/Users/Usuario/Downloads/pesados/outputs_obj3_pose/"; R="/mnt/c/Users/Usuario/onedrive/Desktop/metalsynth-pelvis-EDIT/"
caso="dataset6_CLINIC_0101_data"; LO,HI=-500,1300; H=80
arms=[("Protocolo físico (Ti)",None,5.00),("Real (otro paciente)",None,4.83),("50:0.3",P+f"b_min/run04_mejor_p50_e0.3/a15_{caso}_run04_mejor_p50_e0.3_s0_sintetica.nii.gz",3.33),
("B300",P+f"b_min/b_min_l3_t300/a15_{caso}_b_min_l3_t300_s0_sintetica.nii.gz",3.00),("100:0.3",P+f"b_min/run04_mejor_p100_e0.3/a15_{caso}_run04_mejor_p100_e0.3_s0_sintetica.nii.gz",2.33),
("Control de ajuste fino",P+f"b_min/b_min_l0/a15_{caso}_b_min_l0_s0_sintetica.nii.gz",2.17),("B1000",P+f"b_min/b_min_l0.8_t1000/a15_{caso}_b_min_l0.8_t1000_s0_sintetica.nii.gz",1.67),
("Modelo evaluado",P+f"delta/run04_mejor/a15_{caso}_run04_mejor_s0_sintetica.nii.gz",1.33),("Pelvis sin metal",None,None)]
base=P+"delta/run04_mejor/"; oi=nib.load(base+f"a15_{caso}_original.nii.gz"); O=np.asarray(oi.dataobj).astype(np.float32)
M=np.asarray(nib.load(base+f"a15_{caso}_M.nii.gz").dataobj)>0
ax=[i for i,c in enumerate(nib.aff2axcodes(oi.affine)) if c in "SI"][0]
cnt=M.sum(axis=tuple(i for i in range(3) if i!=ax)); ks=[int(k) for k in np.nonzero(cnt>=30)[0]]; k=ks[len(ks)//2]
sl=lambda v,kk: np.take(v,kk,axis=ax)
ys,xs=np.nonzero(sl(M,k)); cy,cx=int(ys.mean()),int(xs.mean()); y0,x0=max(cy-H,0),max(cx-H,0)
crop=lambda a: a[y0:y0+2*H,x0:x0+2*H]
W=lambda v:np.clip((v-LO)/(HI-LO),0,1)
z=np.load(R+f"experiments/objetivo3/outputs/obj3_pose/peters_val/a19_{caso}.npz"); kk=z["ks"]; ip=int(np.argmin(np.abs(kk-k)))
panel={"Protocolo físico (Ti)":crop(z["Ti_A"][ip]),"Pelvis sin metal":crop(sl(O,k))}
for n,f,_ in arms:
    if f: panel[n]=crop(sl(np.asarray(nib.load(f).dataobj).astype(np.float32),k))
rimg=nib.load(R+"data/dataset7/dataset7_CLINIC_metal_0039_data.nii.gz"); V=np.asarray(rimg.dataobj).astype(np.float32)
axr=[i for i,c in enumerate(nib.aff2axcodes(rimg.affine)) if c in "SI"][0]; lab,nn=ndi.label(V>2500); zz=rimg.header.get_zooms()[:3]
vol=np.bincount(lab.ravel())*float(np.prod(zz)); vol[0]=0; ok=[c for c in range(1,nn+1) if 500<=vol[c]<=4000] or [int(vol.argmax())]
comp=np.isin(lab,ok); cc=comp.sum(axis=tuple(i for i in range(3) if i!=axr)); kr=int(np.argmax(cc)); S=np.take(V,kr,axis=axr); Mr=np.take(comp,kr,axis=axr)
yy,xx=np.nonzero(Mr); ry,rx=max(int(yy.mean())-H,0),max(int(xx.mean())-H,0); panel["Real (otro paciente)"]=S[ry:ry+2*H,rx:rx+2*H]
fig,axs=plt.subplots(3,3,figsize=(7.2,7.6))
for a,(n,f,sc) in zip(axs.ravel(),arms):
    a.imshow(W(panel[n]),cmap="gray",vmin=0,vmax=1); a.set_xticks([]); a.set_yticks([]); a.set_title(n,fontsize=9)
    a.set_xlabel(f"puntaje medio (c): {sc:.2f}" if sc is not None else "referencia, sin implante",fontsize=8)
fig.tight_layout(); fig.savefig("brazos_mismo_implante.pdf"); fig.savefig("brazos_mismo_implante.png",dpi=130); print("ok corte",k,"peters idx",ip,"real corte",kr)
