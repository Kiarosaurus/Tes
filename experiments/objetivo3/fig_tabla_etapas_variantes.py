"""Figura-tabla: etapas del pipeline por variante del criterio (c). Mismo caso (0101, semilla 0, corte central con M, recorte 160x160, ventana HU [-500,1300]).
Columnas: contexto (original fuera de G, G vacia), salida del modelo, diferencia salida - original dentro de G (escala comun). Solo lectura."""
import numpy as np, nibabel as nib, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
P="/mnt/c/Users/Usuario/Downloads/pesados/outputs_obj3_pose/"; R="/mnt/c/Users/Usuario/onedrive/Desktop/metalsynth-pelvis-EDIT/"
caso="dataset6_CLINIC_0101_data"; LO,HI=-500,1300; H=80; DL=1000  # DL: limite de la escala divergente (solo visual)
f=lambda d,v: P+f"{d}/a15_{caso}_{v}_s0_sintetica.nii.gz"
arms=[("Modelo evaluado",f("delta/run04_mejor","run04_mejor"),1.33),("100:0.3",f("b_min/run04_mejor_p100_e0.3","run04_mejor_p100_e0.3"),2.33),
("50:0.3",f("b_min/run04_mejor_p50_e0.3","run04_mejor_p50_e0.3"),3.33),("B300",f("b_min/b_min_l3_t300","b_min_l3_t300"),3.00),
("B1000",f("b_min/b_min_l0.8_t1000","b_min_l0.8_t1000"),1.67),("Control de\najuste fino",f("b_min/b_min_l0","b_min_l0"),2.17)]
base=P+"delta/run04_mejor/"; oi=nib.load(base+f"a15_{caso}_original.nii.gz"); O=np.asarray(oi.dataobj).astype(np.float32)
M=np.asarray(nib.load(base+f"a15_{caso}_M.nii.gz").dataobj)>0; G=np.asarray(nib.load(base+f"a15_{caso}_G.nii.gz").dataobj)>0
ax=[i for i,c in enumerate(nib.aff2axcodes(oi.affine)) if c in "SI"][0]
cnt=M.sum(axis=tuple(i for i in range(3) if i!=ax)); ks=[int(k) for k in np.nonzero(cnt>=30)[0]]; k=ks[len(ks)//2]
sl=lambda v: np.take(v,k,axis=ax)
ys,xs=np.nonzero(sl(M)); cy,cx=int(ys.mean()),int(xs.mean()); y0,x0=max(cy-H,0),max(cx-H,0)
crop=lambda a: a[y0:y0+2*H,x0:x0+2*H]
W=lambda v:np.clip((v-LO)/(HI-LO),0,1)
o=crop(sl(O)); g=crop(sl(G))
ctx=np.where(g,np.nan,W(o)); cm=plt.get_cmap("gray").copy(); cm.set_bad("#d9d9d9")  # G vacia = gris claro plano
dm=plt.get_cmap("RdBu_r").copy(); dm.set_bad("white")
fig,axs=plt.subplots(len(arms),3,figsize=(6.3,9.2),gridspec_kw=dict(left=0.17,right=0.87,top=0.95,bottom=0.02,wspace=0.04,hspace=0.06))
cols=["Contexto\n(original fuera de G)","Salida del modelo","Diferencia salida − original\n(dentro de G)"]
for j,t in enumerate(cols): axs[0,j].set_title(t,fontsize=8)
for i,(n,fn,sc) in enumerate(arms):
    s=crop(sl(np.asarray(nib.load(fn).dataobj).astype(np.float32)))
    axs[i,0].imshow(ctx,cmap=cm,vmin=0,vmax=1); axs[i,1].imshow(W(s),cmap="gray",vmin=0,vmax=1)
    im=axs[i,2].imshow(np.where(g,s-o,np.nan),cmap=dm,vmin=-DL,vmax=DL)
    for a in axs[i]: a.set_xticks([]); a.set_yticks([])
    axs[i,0].set_ylabel(f"{n}\n(c): {sc:.2f}",fontsize=8,rotation=0,ha="right",va="center",labelpad=6)
cb=fig.colorbar(im,ax=axs[:,2],fraction=0.05,pad=0.02,shrink=0.5); cb.set_label("HU",fontsize=8); cb.ax.tick_params(labelsize=8)
fig.savefig(R+"overleaf/figuras/tabla_etapas_variantes.pdf"); fig.savefig("/tmp/tabla_etapas_variantes.png",dpi=130); print("ok corte",k,"axis",ax)
