"""Verifica con una medida objetiva el criterio visual de la autora en la lectura A/B de R-9: la 'transicion' en el borde de G.
Razon = desviacion estandar de la componente de alta frecuencia (img - gauss 2 px) en tejido blando (-100..200 HU) DENTRO de G (sin M dilatada 4 px)
dividida por la de una corona de 6 mm FUERA de G, por corte con M. ctxorig vs ctxsuave vs la imagen original. Solo lectura de khipu_out/r9v."""
import numpy as np, nibabel as nib
from scipy import ndimage as ndi
D="/home/kiara/audit_ws/khipu_out/r9v/"; caso="dataset6_CLINIC_0101_data"
oi=nib.load(D+f"a15_{caso}_original.nii.gz"); O=np.asarray(oi.dataobj).astype(np.float32)
M=np.asarray(nib.load(D+f"a15_{caso}_M.nii.gz").dataobj)>0; G=np.asarray(nib.load(D+f"a15_{caso}_G.nii.gz").dataobj)>0
ax=[i for i,c in enumerate(nib.aff2axcodes(oi.affine)) if c in "SI"][0]; z=oi.header.get_zooms()[:3]; px=tuple(float(z[i]) for i in range(3) if i!=ax)
cnt=M.sum(axis=tuple(i for i in range(3) if i!=ax)); ks=[int(k) for k in np.nonzero(cnt>=30)[0]]
V={"original":O}
for et in ("ctxorig","ctxsuave"):
    for s in (0,1): V[(et,s)]=np.asarray(nib.load(D+f"a15_{caso}_run04_mejor_{et}_s{s}_sintetica.nii.gz").dataobj).astype(np.float32)
def razon(img2d,m,g):
    hf=img2d-ndi.gaussian_filter(img2d,2); soft=(img2d>-100)&(img2d<200)
    dm=ndi.binary_dilation(m,iterations=int(round(4/px[0])))
    dist_out=ndi.distance_transform_edt(~g,sampling=px)
    ain=g&~dm&soft; aout=(~g)&(dist_out<=6)&soft
    if ain.sum()<200 or aout.sum()<200: return np.nan
    return hf[ain].std()/hf[aout].std()
res={}
for key,v in V.items():
    r=[razon(np.take(v,k,axis=ax),np.take(M,k,axis=ax),np.take(G,k,axis=ax)) for k in ks]; res[key]=np.nanmedian(r)
print("corte con M:",len(ks))
print("razon alta frecuencia dentro/fuera de G (mediana de cortes):")
print("  imagen original (sin sintesis):",round(res["original"],3))
for et in ("ctxorig","ctxsuave"):
    print(f"  {et}: semilla 0 {res[(et,0)]:.3f} | semilla 1 {res[(et,1)]:.3f}")
