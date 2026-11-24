"""Peters (Ti, Fe) vs real por anillo, con la MISMA metrica que D1 (amplitud 5 %/5 %, exceso = con metal - sin metal en los mismos pixeles).
Verificacion independiente de un calculo hecho en otra sesion. Solo lectura de outputs existentes; usa funciones de d1_alcance_rayas.py sin modificarlas."""
import sys, glob, json, numpy as np, csv, os
from scipy import ndimage as ndi
R="/mnt/c/Users/Usuario/onedrive/Desktop/metalsynth-pelvis-EDIT/experiments/objetivo3/"
sys.path.insert(0,R); import d1_alcance_rayas as d1
B=d1.BORDES_MM
def casos(): return sorted(glob.glob(R+"outputs/obj3_pose/peters_final/a19_*.npz"))+sorted(glob.glob(R+"outputs/obj3_pose/peters_val/a19_*.npz"))
res={"Ti":[], "Fe":[]}; names=[]
for f in casos():
    z=np.load(f); j=json.load(open(f[:-4]+".json")); px=(tuple(float(v) for v in j["pixel_mm"][:2]) if isinstance(j["pixel_mm"],list) else (float(j["pixel_mm"]),)*2); names.append(os.path.basename(f)[4:-4])
    ks=list(range(len(z["ks"])))[:: max(1,len(z["ks"])//8)][:8]
    for mat in ("Ti","Fe"):
        per=[]
        for i in ks:
            M=z["M"][i]
            if M.sum()<20: continue
            ref=(z["limpia_A"][i]+z["limpia_B"][i])/2.0 if False else z["limpia_A"][i]
            img=(z[mat+"_A"][i])
            dist=ndi.distance_transform_edt(~M,sampling=px)
            valido=d1.cuerpo_2d(z["original"][i])&~M
            per.append(d1.perfil(img,ref,dist,valido))
        res[mat].append(np.nanmedian(np.stack(per),0) if per else np.full(B.size-1,np.nan))
real=list(csv.DictReader(open(R+"outputs/d1_tornillo/d1_por_paciente.csv")))
rm=lambda k:np.median([float(x[k]) for x in real if x[k] not in("","nan")])
print(len(names),"pacientes Peters"); print("anillo   Ti_med  Ti_min..max   Fe_med   real_tornillo  Ti/real  pac_Ti>real_max?")
out=[]
for i in range(0,7):
    lab=f"{int(B[i])}-{int(B[i+1])}"; ti=np.array([r[i] for r in res['Ti']]); fe=np.array([r[i] for r in res['Fe']])
    rv=[float(x[lab]) for x in real if x[lab] not in("","nan")]; r=np.median(rv)
    print(f"{lab:6} {np.nanmedian(ti):8.0f} {np.nanmin(ti):6.0f}..{np.nanmax(ti):6.0f} {np.nanmedian(fe):8.0f} {r:8.0f} {np.nanmedian(ti)/r:7.1f} {int((ti>max(rv)).sum())}/{int(np.isfinite(ti).sum())}")
