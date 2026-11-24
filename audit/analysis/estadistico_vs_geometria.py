"""Que parte de la diferencia entre D1/D2 (exceso por anillo) y E-A2/A20 (amplitud del campo de desviacion) es del ESTADISTICO y no de la geometria.
En PLANO AXIAL, 13 pacientes de prueba, run04_mejor (semillas 0-1) y Peters Ti (cond. A) con su referencia exacta sin metal:
 (a) exceso D1   = amplitud(img) - amplitud(ref)      (sobre los mismos pixeles del anillo)
 (b) amplitud Delta = amplitud(img - ref)              (la definicion de A20, pero en anillos axiales)
Solo lectura. Usa amplitud/cuerpo_2d de d1_alcance_rayas.py sin modificarlo."""
import sys, glob, os, json, numpy as np, nibabel as nib
from scipy import ndimage as ndi
R="/mnt/c/Users/Usuario/onedrive/Desktop/metalsynth-pelvis-EDIT/experiments/objetivo3/"
sys.path.insert(0,R); import d1_alcance_rayas as d1
B=d1.BORDES_MM; NR=6
F="/mnt/c/Users/Usuario/Downloads/pesados/outputs_obj3_pose/final/run04_mejor/"
def anillos(img,ref,M,px,valid):
    dist=ndi.distance_transform_edt(~M,sampling=px); a=np.full(NR,np.nan); b=np.full(NR,np.nan)
    for i in range(NR):
        s=valid&(dist>B[i])&(dist<=B[i+1])
        if s.sum()>=d1.MIN_PIX:
            a[i]=d1.amplitud(img[s])-d1.amplitud(ref[s]); b[i]=d1.amplitud((img-ref)[s])
    return a,b
mod_a,mod_b,pt_a,pt_b=[],[],[],[]
for gf in sorted(glob.glob(F+"a15_*_G.nii.gz")):
    caso=os.path.basename(gf)[4:-len("_G.nii.gz")]
    oi=nib.load(F+f"a15_{caso}_original.nii.gz"); O=np.asarray(oi.dataobj).astype(np.float32); M=np.asarray(nib.load(F+f"a15_{caso}_M.nii.gz").dataobj)>0
    ax=[i for i,c in enumerate(nib.aff2axcodes(oi.affine)) if c in "SI"][0]; z=oi.header.get_zooms()[:3]; px=tuple(float(z[i]) for i in range(3) if i!=ax)
    cnt=M.sum(axis=tuple(i for i in range(3) if i!=ax)); ks=[k for k in np.nonzero(cnt>=20)[0]]; ks=[ks[i] for i in np.unique(np.linspace(0,len(ks)-1,min(8,len(ks))).round().astype(int))]
    for s in (0,1):
        S=np.asarray(nib.load(F+f"a15_{caso}_run04_mejor_s{s}_sintetica.nii.gz").dataobj).astype(np.float32); A=[];Bb=[]
        for k in ks:
            sl=lambda v:np.take(v,k,axis=ax); m=sl(M); valid=d1.cuerpo_2d(sl(O))&~m
            a,b=anillos(sl(S),sl(O),m,px,valid); A.append(a);Bb.append(b)
        mod_a.append(np.nanmedian(np.stack(A),0)); mod_b.append(np.nanmedian(np.stack(Bb),0))
    zf=glob.glob(R+f"outputs/obj3_pose/peters_final/a19_{caso}.npz")
    if zf:
        z=np.load(zf[0]); j=json.load(open(zf[0][:-4]+".json")); p=j["pixel_mm"]; pxp=(float(p[0]),float(p[1])) if isinstance(p,list) else (float(p),)*2
        A=[];Bb=[]
        for i in range(len(z["ks"]))[::max(1,len(z["ks"])//8)][:8]:
            m=z["M"][i]
            if m.sum()<20: continue
            valid=d1.cuerpo_2d(z["original"][i])&~m; a,b=anillos(z["Ti_A"][i],z["limpia_A"][i],m,pxp,valid); A.append(a);Bb.append(b)
        if A: pt_a.append(np.nanmedian(np.stack(A),0)); pt_b.append(np.nanmedian(np.stack(Bb),0))
    print(caso,flush=True)
md=lambda L:np.nanmedian(np.stack(L),0)
print("\nANILLO(mm)  modelo: exceso(D1) | amp(Delta) ||  PetersTi: exceso(D1) | amp(Delta)   [mediana entre %d pacientes x2 semillas; Peters %d pacientes]"%(len(mod_a)//2,len(pt_a)))
for i in range(NR): print(f"{int(B[i])}-{int(B[i+1])}   {md(mod_a)[i]:8.0f} {md(mod_b)[i]:8.0f}   ||  {md(pt_a)[i]:8.0f} {md(pt_b)[i]:8.0f}")
