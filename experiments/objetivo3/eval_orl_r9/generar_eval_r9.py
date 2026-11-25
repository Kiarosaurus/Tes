"""Genera la evaluacion ciega A/B de R-9 (contexto original frente a contexto suavizado) para el lector otorrinolaringologo y la autora.
Entradas (solo lectura): khipu_out/r9v (paciente 0101, run04_mejor, semillas 0 y 1, ctxorig y ctxsuave, con NIfTI).
Salidas: eval_orl_r9_ciego.html (autocontenido, sin clave) y clave_r9_NO_ABRIR.csv (que imagen es A y B en cada par).
Recorte fijo de 160 px centrado en M. Aleatorizacion con semilla fija 20261124. Ventana [-500, 1300] HU. 12 cortes con M repartidos x 2 semillas = 24 pares + 4 repetidos (con A/B intercambiados)."""
import io, base64, csv, json, random, sys
import numpy as np, nibabel as nib, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
D="/home/kiara/audit_ws/khipu_out/r9v/"; caso="dataset6_CLINIC_0101_data"; LO,HI=-500,1300
M=np.asarray(nib.load(D+f"a15_{caso}_M.nii.gz").dataobj)>0; G=np.asarray(nib.load(D+f"a15_{caso}_G.nii.gz").dataobj)>0
oi=nib.load(D+f"a15_{caso}_original.nii.gz"); ax=[i for i,c in enumerate(nib.aff2axcodes(oi.affine)) if c in "SI"][0]
cnt=M.sum(axis=tuple(i for i in range(3) if i!=ax)); ks=[int(k) for k in np.nonzero(cnt>=30)[0]]
pos=np.unique(np.linspace(0,len(ks)-1,12).round().astype(int)); sel=[ks[i] for i in pos]
vol={}
for et in ("ctxorig","ctxsuave"):
    for s in (0,1): vol[(et,s)]=np.asarray(nib.load(D+f"a15_{caso}_run04_mejor_{et}_s{s}_sintetica.nii.gz").dataobj).astype(np.float32)
sl=lambda v,k: np.take(v,k,axis=ax)
rng=random.Random(20261124)
def png(img):
    b=io.BytesIO(); plt.imsave(b,np.clip((img-LO)/(HI-LO),0,1),cmap="gray",vmin=0,vmax=1,format="png"); return base64.b64encode(b.getvalue()).decode()
# recorte comun por corte: caja de G (+50 px), cuadrado
def caja(k):
    ys,xs=np.nonzero(sl(M,k)); cy,cx=int(ys.mean()),int(xs.mean()); h=80
    y0=min(max(cy-h,0),M.shape[1 if ax!=1 else 0]-2*h if False else 10**9); y0=max(cy-h,0); x0=max(cx-h,0)
    return y0,y0+2*h,x0,x0+2*h
pares=[]
for k in sel:
    for s in (0,1): pares.append((k,s,False))
for (k,s,_) in rng.sample([(k,s,False) for k in sel for s in (0,1)],4): pares.append((k,s,True))   # repetidos
rng.shuffle(pares)
items=[]; clave=[]
for n,(k,s,rep) in enumerate(pares,1):
    y0,y1,x0,x1=caja(k); a_is_orig=rng.random()<0.5
    A="ctxorig" if a_is_orig else "ctxsuave"; B="ctxsuave" if a_is_orig else "ctxorig"
    if rep: A,B=B,A
    items.append(dict(id=f"P{n:02d}",A=png(sl(vol[(A,s)],k)[y0:y1,x0:x1]),B=png(sl(vol[(B,s)],k)[y0:y1,x0:x1])))
    clave.append(dict(id=f"P{n:02d}",A=A,B=B,corte=k,semilla=s,repetido=int(rep)))
with open("clave_r9_NO_ABRIR.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(clave[0])); w.writeheader(); w.writerows(clave)
html="""<!doctype html><html lang="es"><meta charset="utf-8"><title>Evaluación visual A/B</title>
<style>body{font-family:system-ui,sans-serif;max-width:1000px;margin:20px auto;padding:0 12px;background:#fff;color:#111}
.par{display:flex;gap:16px;justify-content:center}.par div{text-align:center}img{width:440px;height:440px;image-rendering:auto;border:1px solid #888}
button{font-size:16px;padding:8px 18px;margin:4px;cursor:pointer}.sel{background:#cde;border:2px solid #036}small{color:#555}input,select{font-size:15px;padding:4px}</style>
<div id="app"></div><script>
const ITEMS=__ITEMS__;let i=0,t0=Date.now();const R=[];let lector={};
function inicio(){document.getElementById('app').innerHTML=`<h2>Evaluación visual: ¿cuál artefacto parece más real?</h2>
<p>Verá <b>__N__ pares</b> de imágenes de TC pélvica axial. En cada par, ambas imágenes son <b>el mismo corte de la misma pelvis</b>, con un tornillo metálico <b>generado por computador</b> y el artefacto (rayas claras y oscuras) que produce. Las dos imágenes <b>difieren en el aspecto del artefacto y de la anatomía cercana</b>.</p>
<p><b>Tarea:</b> en cada par, marque cuál de las dos imágenes le parece <b>más real</b> (el artefacto metálico más natural, como el de una TC real) y cuán seguro está. Si de verdad no ve diferencia, marque «Sin diferencia». No hay respuestas correctas ni se evalúa su desempeño clínico; <b>no use información de otras fuentes</b>. Las imágenes tienen la misma ventana de visualización (-500 a 1300 HU).</p>
<p>Tiempo aproximado: 10 a 15 minutos. Puede hacer una pausa entre pares; sus respuestas se guardan en este navegador.</p>
<p>Nombre o iniciales: <input id="nom"> &nbsp; Especialidad: <input id="esp"> &nbsp; Años de experiencia: <input id="anios" size="4"></p>
<button onclick="empezar()">Comenzar</button>`}
function empezar(){lector={nombre:nom.value,especialidad:esp.value,anios:anios.value};if(!lector.nombre){alert('Escriba su nombre o iniciales');return}mostrar()}
function mostrar(){if(i>=ITEMS.length){fin();return}const it=ITEMS[i];t0=Date.now();
document.getElementById('app').innerHTML=`<p><small>Par ${i+1} de ${ITEMS.length}</small></p><div class="par"><div><b>A</b><br><img src="data:image/png;base64,${it.A}"></div><div><b>B</b><br><img src="data:image/png;base64,${it.B}"></div></div>
<p style="text-align:center">¿Cuál le parece más real? &nbsp;<button onclick="el('A',this)">A</button><button onclick="el('B',this)">B</button><button onclick="el('=',this)">Sin diferencia</button></p>
<p style="text-align:center">Seguridad: <button onclick="co(1,this)">1 (poca)</button><button onclick="co(2,this)">2</button><button onclick="co(3,this)">3 (mucha)</button></p>
<p style="text-align:center"><button id="sig" onclick="sig()" disabled>Siguiente</button></p>`;ch=null;cf=null}
let ch=null,cf=null;function el(v,b){ch=v;mk(b)}function co(v,b){cf=v;mk(b)}
function mk(b){[...b.parentNode.children].forEach(x=>x.classList.remove('sel'));b.classList.add('sel');if(ch&&cf)document.getElementById('sig').disabled=false}
function sig(){R.push({id:ITEMS[i].id,eleccion:ch,seguridad:cf,segundos:((Date.now()-t0)/1000).toFixed(1)});localStorage.setItem('evalr9',JSON.stringify({lector,R}));i++;mostrar()}
function fin(){const csv='id,eleccion,seguridad,segundos,lector,especialidad,anios\\n'+R.map(r=>[r.id,r.eleccion,r.seguridad,r.segundos,lector.nombre,lector.especialidad,lector.anios].join(',')).join('\\n');
const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([csv],{type:'text/csv'}));a.download='respuestas_'+(lector.nombre||'lector')+'.csv';
document.getElementById('app').innerHTML='<h2>Gracias</h2><p>Se descargó el archivo de respuestas. Envíelo a la persona que coordina la evaluación.</p>';a.click()}
inicio();</script></html>"""
html=html.replace("__ITEMS__",json.dumps(items)).replace("__N__",str(len(items)))
open("eval_orl_r9_ciego.html","w",encoding="utf-8").write(html); print("pares",len(items),"tamano MB",round(len(html)/1e6,1),"cortes",sel)
