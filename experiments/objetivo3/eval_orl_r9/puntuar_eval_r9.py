"""Puntua la evaluacion A/B de R-9 (contexto original frente a suavizado) con la clave. Solo CPU.
Uso: python puntuar_eval_r9.py clave_r9_NO_ABRIR.csv respuestas_<lector>.csv [mas respuestas...]
No abrir la clave antes de que todos los lectores terminen. Descriptivo: sin regla de decision; n pequeno."""
import csv, sys
from scipy.stats import binomtest
clave={r["id"]:r for r in csv.DictReader(open(sys.argv[1]))}
for ruta in sys.argv[2:]:
    R=list(csv.DictReader(open(ruta))); lector=R[0].get("lector","?") if R else "?"
    def brazo(r):
        e=r["eleccion"]; k=clave[r["id"]]
        return "=" if e=="=" else (k["A"] if e=="A" else k["B"])
    res=[(r["id"],brazo(r),int(r["seguridad"]),clave[r["id"]]) for r in R]
    n=len(res); sua=sum(b=="ctxsuave" for _,b,_,_ in res); ori=sum(b=="ctxorig" for _,b,_,_ in res); emp=sum(b=="=" for _,b,_,_ in res)
    print(f"\n== {ruta} (lector {lector}): {n} pares | prefiere suavizado {sua} | prefiere original {ori} | sin diferencia {emp}")
    m=sua+ori
    if m:
        t=binomtest(sua,m,0.5); ci=t.proportion_ci(confidence_level=0.95,method="exact")
        print(f"   entre los que eligieron ({m}): suavizado {sua/m:.2f}, IC95 exacto [{ci.low:.2f}, {ci.high:.2f}], p bilateral {t.pvalue:.3f}")
    for s in (0,1):
        a=[b for _,b,_,k in res if int(k["semilla"])==s]; print(f"   semilla {s}: suavizado {a.count('ctxsuave')}, original {a.count('ctxorig')}, igual {a.count('=')}")
    # consistencia en repetidos
    rep=[x for x in res if int(x[3]["repetido"])]; ok=0; tot=0
    for id_,b,_,k in rep:
        orig=[y for y in res if int(y[3]["repetido"])==0 and y[3]["corte"]==k["corte"] and y[3]["semilla"]==k["semilla"]]
        if orig: tot+=1; ok+= (orig[0][1]==b)
    print(f"   consistencia en los {tot} pares repetidos (A/B intercambiados): {ok}/{tot} mismas respuestas")
    conf=[c for _,b,c,_ in res if b!="="]; print(f"   seguridad media (excluye 'sin diferencia'): {sum(conf)/len(conf):.2f}" if conf else "   sin respuestas con preferencia")
