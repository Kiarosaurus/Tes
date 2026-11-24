"""F-H5 (Obj3): solapamiento de grupos de paciente entre entrenamiento (manifiesto run04), validacion y los 13 de prueba."""
import pandas as pd
R="/mnt/c/Users/Usuario/onedrive/Desktop/metalsynth-pelvis-EDIT/experiments/"
g=pd.read_csv(R+"exploration-3d/grupos.csv", encoding="utf-8-sig"); gp=dict(zip(g.Caso,g["Grupo paciente"]))
tr=pd.read_csv(R+"objetivo3/a5_manifiesto_train_run04.csv"); va=pd.read_csv(R+"objetivo3/a5_manifiesto_val.csv")
te=pd.read_csv(R+"objetivo3/outputs/obj3_pose/a20_test/a20_ea2_test.csv")
print(te.columns.tolist()[:8])
cc=[c for c in te.columns if c.lower() in("caso","case","paciente")][0]
S={"train":set(tr.Caso),"val":set(va.Caso),"test":set(te[cc])}
print({k:len(v) for k,v in S.items()})
G={k:{gp.get(c,"?"+c) for c in v} for k,v in S.items()}
for a,b in [("train","val"),("train","test"),("val","test")]:
    print(a,b,"casos comunes:",len(S[a]&S[b]),"grupos comunes:",sorted(G[a]&G[b]))
print("sin grupo asignado:", {k:[c for c in v if c not in gp] for k,v in S.items()})
