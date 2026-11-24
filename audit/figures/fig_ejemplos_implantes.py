"""Borrador de figura (NO toca la tesis): fila 1 = cadena sintetica (pelvis limpia -> mascara M/G -> sintetico con artefacto),
fila 2 = implante real de la cohorte. Valores impresos = los registrados en resumen.csv / a20_ea2_test.csv / calculados del NIfTI.
Ventana [-500, 1300] HU (la del criterio visual c2b). Solo lectura de resultados existentes."""
import numpy as np, nibabel as nib, pandas as pd, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
R="/mnt/c/Users/Usuario/onedrive/Desktop/metalsynth-pelvis-EDIT/"
F="/mnt/c/Users/Usuario/Downloads/pesados/outputs_obj3_pose/final/run04_mejor/"
caso="dataset6_CLINIC_0012_data"; sem=0; LO,HI=-500,1300
orig=np.asarray(nib.load(F+f"a15_{caso}_original.nii.gz").dataobj).astype(np.float32)
M=np.asarray(nib.load(F+f"a15_{caso}_M.nii.gz").dataobj)>0; G=np.asarray(nib.load(F+f"a15_{caso}_G.nii.gz").dataobj)>0
syn=np.asarray(nib.load(F+f"a15_{caso}_run04_mejor_s{sem}_sintetica.nii.gz").dataobj).astype(np.float32)
ax=[i for i,c in enumerate(nib.aff2axcodes(nib.load(F+f"a15_{caso}_original.nii.gz").affine)) if c in "SI"][0]
cnt=M.sum(axis=tuple(i for i in range(3) if i!=ax)); k=int(np.argmax(cnt))
sl=lambda v: np.take(v,k,axis=ax)
ys,xs=np.nonzero(sl(M)|sl(G)); y0,y1,x0,x1=max(ys.min()-60,0),ys.max()+60,max(xs.min()-60,0),xs.max()+60
crop=lambda v: sl(v)[y0:y1,x0:x1]
res=pd.read_csv(F+f"a15_{caso}_resumen.csv"); r=res[res.semilla==sem].iloc[0]
a20=pd.read_csv(R+"experiments/objetivo3/outputs/obj3_pose/a20_test/a20_ea2_test.csv"); a=a20[a20.caso==caso]
amp_syn=a[a.condicion==f"run04_mejor_s{sem}"].amp_HU.iloc[0]; amp_pTi=a[a.condicion=="Ti_A"].amp_HU.iloc[0]; amp_pFe=a[a.condicion=="Fe_A"].amp_HU.iloc[0]
# real
p=pd.read_csv(R+"experiments/objetivo1/p1_particion.csv",encoding="utf-8-sig"); real=p[(p.Metal=="si")&(p.particion=="test")].Caso.iloc[1]
img=nib.load(R+f"data/dataset6/{real}.nii.gz") if (R+f"data/dataset6/{real}.nii.gz") and __import__('os').path.exists(R+f"data/dataset6/{real}.nii.gz") else nib.load(R+f"data/dataset7/{real}.nii.gz")
V=np.asarray(img.dataobj).astype(np.float32); axr=[i for i,c in enumerate(nib.aff2axcodes(img.affine)) if c in "SI"][0]
mr=V>2500; kr=int(np.argmax(mr.sum(axis=tuple(i for i in range(3) if i!=axr)))); S=np.take(V,kr,axis=axr); Mr=S>2500
yy,xx=np.nonzero(Mr); ry0,ry1,rx0,rx1=max(yy.min()-80,0),yy.max()+80,max(xx.min()-80,0),xx.max()+80
fig,axs=plt.subplots(2,4,figsize=(14,7.4)); W=lambda a:np.clip((a-LO)/(HI-LO),0,1)
def show(a,im,title,sub): 
    a.imshow(im,cmap="gray",vmin=0,vmax=1); a.set_xticks([]); a.set_yticks([]); a.set_title(title,fontsize=10); a.set_xlabel(sub,fontsize=8)
show(axs[0,0],W(crop(orig)),"(a) Pelvis limpia (receptor)","sin metal; original de la cohorte")
im=np.dstack([W(crop(orig))]*3); m=crop(M); g=crop(G); im[g&~m]=0.6*im[g&~m]+0.4*np.array([0.2,0.4,1.0]); im[m]=[1,0.15,0.15]
show(axs[0,1],im,"(b) Mascara M (rojo) y region G (azul)",f"M = {int(M.sum())} voxeles; G = {int(G.sum())} voxeles")
show(axs[0,2],W(crop(syn)),"(c) Sintetico con artefacto (run04_mejor)",f"HU en M: p50 {r.hu_p50:.0f}; >2500 HU: {100*r.frac_sobre_2500:.0f} %\namplitud de rayas {amp_syn:.0f} HU")
axs[0,3].axis("off"); axs[0,3].text(0,0.95,"Referencias medidas en el mismo caso\n(ver Cap. 3, protocolo de apariencia)\n\nProtocolo fisico (Peters):\n  amplitud Ti = %.0f HU\n  amplitud Fe = %.0f HU\nCopia y pegado: amplitud = 0 HU\n(por construccion)\n\nCaso %s, semilla %d,\ncorte %d, ventana [%d, %d] HU"%(amp_pTi,amp_pFe,caso[9:-5],sem,k,LO,HI),va="top",fontsize=9,family="monospace")
RS=S[ry0:ry1,rx0:rx1]; show(axs[1,0],W(RS),"(d) Implante real de la cohorte","caso "+real.replace("_data","")+f"; corte {kr}")
im2=np.dstack([W(RS)]*3); im2[Mr[ry0:ry1,rx0:rx1]]=[1,0.15,0.15]; show(axs[1,1],im2,"(e) Metal real (HU > 2500, rojo)",f"{int(Mr.sum())} pixeles > 2500 HU en este corte")
mv=V[mr]; axs[1,2].hist(np.clip(mv,0,9000),bins=60,color="#555"); axs[1,2].set_title("(f) HU del metal real (todo el volumen)",fontsize=10); axs[1,2].set_xlabel("HU (recortado a 9000)",fontsize=8)
axs[1,3].axis("off"); axs[1,3].text(0,0.95,"Metal real, voxeles > 2500 HU\n  n = %d\n  p50 = %.0f HU\n  p95 = %.0f HU\n\nSintetico (c): p50 %.0f HU,\n  p95 %.0f HU en M"%(mv.size,np.percentile(mv,50),np.percentile(mv,95),r.hu_p50,r.hu_p95),va="top",fontsize=9,family="monospace")
fig.suptitle("Borrador: ejemplos de implante y artefacto (solo descriptivo; no afirma realismo visual)",fontsize=11); fig.tight_layout()
fig.savefig("ejemplos_implantes_borrador.png",dpi=140); fig.savefig("ejemplos_implantes_borrador.pdf"); print("ok",caso,k,real,kr)
