"""R-8 (C_deep_learning): energia del gradiente axial dentro de G, sintetico vs original, 13 pacientes de prueba x 5 semillas (run04_mejor).
Solo CPU, lectura de NIfTI ya generados (no se modifica nada)."""
import glob, os, numpy as np, nibabel as nib, pandas as pd
D="/mnt/c/Users/Usuario/Downloads/pesados/outputs_obj3_pose/final/run04_mejor/"
rows=[]
for gf in sorted(glob.glob(D+"a15_*_G.nii.gz")):
    caso=os.path.basename(gf)[4:-len("_G.nii.gz")]
    G=np.asarray(nib.load(gf).dataobj)>0
    o_img=nib.load(D+f"a15_{caso}_original.nii.gz"); O=np.asarray(o_img.dataobj).astype(np.float32)
    ax=[i for i,c in enumerate(nib.aff2axcodes(o_img.affine)) if c in("S","I")][0]
    def e(V):
        d=np.abs(np.diff(V,axis=ax)); m=np.take(G,range(1,G.shape[ax]),axis=ax)&np.take(G,range(0,G.shape[ax]-1),axis=ax)
        return float(d[m].mean()), int(m.sum())
    eo,n=e(O)
    for s in range(5):
        f=D+f"a15_{caso}_run04_mejor_s{s}_sintetica.nii.gz"
        if not os.path.exists(f): continue
        S=np.asarray(nib.load(f).dataobj).astype(np.float32)
        es,_=e(S); rows.append(dict(caso=caso,semilla=s,eje=ax,n_vox_G=n,grad_axial_orig=eo,grad_axial_sint=es,cociente=es/eo))
d=pd.DataFrame(rows); d.to_csv("r8_gradiente_axial.csv",index=False)
print(len(d),"filas;", d.caso.nunique(),"casos")
print(d.groupby("caso")[["grad_axial_orig","grad_axial_sint","cociente"]].mean().round(2).to_string())
print("media cociente:",round(d.cociente.mean(),3),"min",round(d.cociente.min(),3),"max",round(d.cociente.max(),3))
