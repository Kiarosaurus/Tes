"""Figura de pipeline del muestreador de colocacion. MISMO caso que fig_brazos_mismo_implante.py (0101, semilla 0, corte central con M,
eje SI, recorte 160x160, ventana [-500,1300] HU). Etapas: TC sin metal -> corredor oseo medido y su eje (e9ts_ejes_corredor.csv, modo default6mm,
F_limpieza 0) -> M rasterizada con esa pose (a15; sin --perturbar: pose = eje del corredor) -> M sobre la TC. Eje y corredor se PROYECTAN al corte. Solo lectura."""
import sys, csv, numpy as np, nibabel as nib, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
R="/mnt/c/Users/Usuario/onedrive/Desktop/metalsynth-pelvis-EDIT/"; P="/mnt/c/Users/Usuario/Downloads/pesados/outputs_obj3_pose/"
sys.path.insert(0,R+"experiments/objetivo3"); from a11_rasterizar_tornillo import pose_a_marco_crudo
caso="dataset6_CLINIC_0101_data"; LO,HI=-500,1300; H=80
base=P+"delta/run04_mejor/"; oi=nib.load(base+f"a15_{caso}_original.nii.gz"); O=np.asarray(oi.dataobj).astype(np.float32)
M=np.asarray(nib.load(base+f"a15_{caso}_M.nii.gz").dataobj)>0
ax=[i for i,c in enumerate(nib.aff2axcodes(oi.affine)) if c in "SI"][0]
cnt=M.sum(axis=tuple(i for i in range(3) if i!=ax)); ks=[int(k) for k in np.nonzero(cnt>=30)[0]]; k=ks[len(ks)//2]
sl=lambda v,kk: np.take(v,kk,axis=ax)
ys,xs=np.nonzero(sl(M,k)); cy,cx=int(ys.mean()),int(xs.mean()); y0,x0=max(cy-H,0),max(cx-H,0)
crop=lambda a: a[y0:y0+2*H,x0:x0+2*H]
W=lambda v:np.clip((v-LO)/(HI-LO),0,1)
e=[r for r in csv.DictReader(open(R+"experiments/objetivo2/outputs/e9ts_ejes_corredor.csv",encoding="utf-8")) if r["Caso"]==caso and r["modo"]=="default6mm" and not r["Error"]][0]
c=np.array([float(e["c_x_mm"]),float(e["c_y_mm"]),float(e["c_z_mm"])]); u=np.array([float(e["u_x"]),float(e["u_y"]),float(e["u_z"])]); L=float(e["L_TS_mejor_mm"]); D=float(e["D_TS_max_mm"])
img=nib.load(base+f"a15_{caso}_original.nii.gz"); zo=np.array(img.header.get_zooms()[:3],float)
cr,ur=pose_a_marco_crudo(nib.load(R+"data/dataset6/"+caso+".nii.gz"),c,u)  # los NIfTI del a15 son el array crudo (LPS) con afin ficticia
pl=[i for i in range(3) if i!=ax]
t=np.linspace(-L/2,L/2,200); pts=cr[None]+t[:,None]*ur[None]; pv=pts/zo[None]   # voxeles
rr=pv[:,pl[0]]-y0; cc=pv[:,pl[1]]-x0
# normal en el plano, para el borde del corredor (ancho D mm, proyectado)
d=np.array([ur[pl[0]]/zo[pl[0]]*zo[pl[0]],ur[pl[1]]*1.0]); d=np.array([ur[pl[0]],ur[pl[1]]]); d/=np.linalg.norm(d); n=np.array([-d[1],d[0]])
off=(D/2)/np.array([zo[pl[0]],zo[pl[1]]])
orig=crop(sl(O,k)); Mc=crop(sl(M,k)); g=W(orig)
fig=plt.figure(figsize=(6.3,1.45)); pw,gap,x=1.0/6.3,0.62/6.3,0.02; yb,ph=0.03,1.0/1.45
def mk(i,title):
    a_=fig.add_axes([x+i*(pw+gap),yb,pw,ph]); a_.set_xticks([]); a_.set_yticks([]); a_.set_title(title,fontsize=8,pad=3); return a_
def clipaxes(a_): a_.set_xlim(-0.5,2*H-0.5); a_.set_ylim(2*H-0.5,-0.5)
a1=mk(0,"TC sin metal"); a1.imshow(g,cmap="gray",vmin=0,vmax=1)
a2=mk(1,"Corredor óseo medido\ny su eje"); a2.imshow(g,cmap="gray",vmin=0,vmax=1)
for s in (+1,-1): a2.plot(cc+s*n[1]*off[1],rr+s*n[0]*off[0],color="yellow",lw=0.8,ls="--")
a2.plot(cc,rr,color="red",lw=1.0); clipaxes(a2)
a3=mk(2,"Pose del tornillo:\nmáscara M"); a3.imshow(np.zeros_like(g),cmap="gray",vmin=0,vmax=1); a3.imshow(np.ma.masked_where(~Mc,Mc),cmap=matplotlib.colors.ListedColormap(["white"]),vmin=0,vmax=1)
a4=mk(3,"M sobre la TC"); a4.imshow(g,cmap="gray",vmin=0,vmax=1); a4.imshow(np.ma.masked_where(~Mc,Mc),cmap=matplotlib.colors.ListedColormap(["red"]),alpha=0.85,vmin=0,vmax=1)
labs=["medición\ndel\ncorredor","pose =\neje del\ncorredor","superponer\nsobre la\nTC"]
for i in range(3):
    xa=x+i*(pw+gap)+pw; yc=yb+ph/2
    fig.add_artist(FancyArrowPatch((xa+0.008,yc),(xa+gap-0.008,yc),transform=fig.transFigure,arrowstyle="-|>",mutation_scale=9,lw=1,color="k"))
    fig.text(xa+gap/2,yc+0.03,labs[i],ha="center",va="bottom",fontsize=8)
fig.savefig(R+"overleaf/figuras/pipeline_muestreador.pdf"); fig.savefig("/tmp/pipeline_muestreador.png",dpi=200)
print("corte",k,"L",L,"D",D,"d",d)
