"""Figura de ejemplos (version para la tesis): fila 1 = cadena sintetica (caso CLINIC_0012, corte con M, semilla 0, run04_mejor);
fila 2 = implante real (metal_0039, el caso real que ya usa el cotejo de cascaras). Valores impresos = los registrados
(resumen.csv de a15, a20_ea2_test.csv) o calculados del NIfTI. Ventana [-500, 1300] HU. Solo lectura. Salida: ejemplos_implantes.pdf/png."""
import os, numpy as np, nibabel as nib, pandas as pd, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from scipy import ndimage as ndi
R="/mnt/c/Users/Usuario/onedrive/Desktop/metalsynth-pelvis-EDIT/"
F="/mnt/c/Users/Usuario/Downloads/pesados/outputs_obj3_pose/final/run04_mejor/"
caso="dataset6_CLINIC_0012_data"; sem=0; LO,HI=-500,1300
oi=nib.load(F+f"a15_{caso}_original.nii.gz"); orig=np.asarray(oi.dataobj).astype(np.float32)
M=np.asarray(nib.load(F+f"a15_{caso}_M.nii.gz").dataobj)>0; G=np.asarray(nib.load(F+f"a15_{caso}_G.nii.gz").dataobj)>0
syn=np.asarray(nib.load(F+f"a15_{caso}_run04_mejor_s{sem}_sintetica.nii.gz").dataobj).astype(np.float32)
ax=[i for i,c in enumerate(nib.aff2axcodes(oi.affine)) if c in "SI"][0]
k=int(np.argmax(M.sum(axis=tuple(i for i in range(3) if i!=ax)))); sl=lambda v: np.take(v,k,axis=ax)
ys,xs=np.nonzero(sl(M)|sl(G)); y0,y1,x0,x1=max(ys.min()-60,0),ys.max()+60,max(xs.min()-60,0),xs.max()+60
crop=lambda v: sl(v)[y0:y1,x0:x1]
r=pd.read_csv(F+f"a15_{caso}_resumen.csv").query("semilla==@sem").iloc[0]
a=pd.read_csv(R+"experiments/objetivo3/outputs/obj3_pose/a20_test/a20_ea2_test.csv").query("caso==@caso")
amp_s=a[a.condicion==f"run04_mejor_s{sem}"].amp_HU.iloc[0]; amp_ti=a[a.condicion=="Ti_A"].amp_HU.iloc[0]; amp_fe=a[a.condicion=="Fe_A"].amp_HU.iloc[0]
real="dataset7_CLINIC_metal_0039_data"; img=nib.load(R+f"data/dataset7/{real}.nii.gz"); V=np.asarray(img.dataobj).astype(np.float32)
axr=[i for i,c in enumerate(nib.aff2axcodes(img.affine)) if c in "SI"][0]
lab,n=ndi.label(V>2500); z=img.header.get_zooms()[:3]; vol=np.bincount(lab.ravel())*float(np.prod(z)); vol[0]=0
ok=[c for c in range(1,n+1) if 500<=vol[c]<=4000] or [int(vol.argmax())]
comp=np.isin(lab,ok); cnt=comp.sum(axis=tuple(i for i in range(3) if i!=axr)); kr=int(np.argmax(cnt))
S=np.take(V,kr,axis=axr); Mr=np.take(comp,kr,axis=axr); yy,xx=np.nonzero(Mr)
ry0,ry1,rx0,rx1=max(yy.min()-90,0),yy.max()+90,max(xx.min()-90,0),xx.max()+90
W=lambda v:np.clip((v-LO)/(HI-LO),0,1)
fig,axs=plt.subplots(2,3,figsize=(7.4,5.4))
def show(a_,im,t,sub): a_.imshow(im,cmap="gray",vmin=0,vmax=1); a_.set_xticks([]); a_.set_yticks([]); a_.set_title(t,fontsize=8.5); a_.set_xlabel(sub,fontsize=7)
show(axs[0,0],W(crop(orig)),"(a) Pelvis sin metal","TC receptora original")
im=np.dstack([W(crop(orig))]*3); m=crop(M); g=crop(G); im[g&~m]=0.6*im[g&~m]+0.4*np.array([0.2,0.4,1.0]); im[m]=[1,0.15,0.15]
show(axs[0,1],im,"(b) Máscara $M$ y región $G$",f"$M$: {int(M.sum())} vóxeles; $G$: {int(G.sum())} vóxeles")
show(axs[0,2],W(crop(syn)),"(c) Sintético con artefacto",f"HU en $M$: p50 {r.hu_p50:.0f}; >2500 HU: {100*r.frac_sobre_2500:.0f} %\namplitud {amp_s:.0f} HU (Peters Ti {amp_ti:.0f})")
RS=S[ry0:ry1,rx0:rx1]; show(axs[1,0],W(RS),"(d) Implante real","caso metal_0039, corte "+str(kr))
im2=np.dstack([W(RS)]*3); im2[Mr[ry0:ry1,rx0:rx1]]=[1,0.15,0.15]
show(axs[1,1],im2,"(e) Metal real (HU > 2500)",f"{int(Mr.sum())} píxeles en el corte; {int(comp.sum())} vóxeles")
mv=V[comp]; axs[1,2].hist(np.clip(mv,0,9000),bins=50,color="#555"); axs[1,2].set_title("(f) HU del metal real",fontsize=8.5); axs[1,2].tick_params(labelsize=7)
axs[1,2].set_xlabel(f"HU; p50 {np.percentile(mv,50):.0f}, p95 {np.percentile(mv,95):.0f}",fontsize=7)
fig.tight_layout(); fig.savefig("ejemplos_implantes.pdf"); fig.savefig("ejemplos_implantes.png",dpi=130)
print("ok",k,kr,int(Mr.sum()),int(comp.sum()),"hu real p50",np.percentile(mv,50))
