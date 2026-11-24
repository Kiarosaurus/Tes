"""R-3 (C): candidatos a 'validacion 2': pelvis SIN metal, de la particion train del Obj1, con corredor viable (D_TS_max >= 9 mm).
Solo CPU, solo lectura. La identidad de paciente NO esta garantizada para volumenes sin metal (cap3:600): confirmar antes de usarlos."""
import pandas as pd
R="/mnt/c/Users/Usuario/onedrive/Desktop/metalsynth-pelvis-EDIT/experiments/"
p=pd.read_csv(R+"objetivo1/p1_particion.csv", encoding="utf-8-sig")
e=pd.read_csv(R+"objetivo2/outputs/e9ts_ejes_corredor.csv", encoding="utf-8-sig", low_memory=False)
e=e[(e.modo=="default6mm")&(e.politica_metal=="hueso")].drop_duplicates("Caso")
m=p.merge(e[["Caso","cohorte","D_TS_max_mm","L_TS_mejor_mm","estado_TS"]], on="Caso")
c=m[(m.particion=="train")&(m.Metal=="no")&(m.D_TS_max_mm>=9)].sort_values("Caso")
tr=pd.read_csv(R+"objetivo3/a5_manifiesto_train_run04.csv"); c=c[~c.Caso.isin(set(tr.Caso))]
g=pd.read_csv(R+"exploration-3d/grupos.csv", encoding="utf-8-sig"); n=g.groupby("Grupo paciente").size()
c["volumenes_del_paciente"]=c["Grupo paciente"].map(n)
print(len(m),"cruzados;",len(c),"candidatos (train, sin metal, D>=9, no vistos por el sintetizador)")
print("con >1 volumen por paciente:",(c.volumenes_del_paciente>1).sum())
c.to_csv("r3_candidatos.csv",index=False); print(c[["Caso","D_TS_max_mm","estado_TS","volumenes_del_paciente"]].head(40).to_string(index=False))
