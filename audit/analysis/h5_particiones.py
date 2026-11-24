"""F-H5: ¿algun grupo de paciente aparece en mas de una particion? Solo CPU, lectura de CSV."""
import pandas as pd
R="/mnt/c/Users/Usuario/onedrive/Desktop/metalsynth-pelvis-EDIT/experiments/"
p=pd.read_csv(R+"objetivo1/p1_particion.csv", encoding="utf-8-sig")
g=pd.read_csv(R+"exploration-3d/grupos.csv", encoding="utf-8-sig")
print("p1_particion:", len(p), p.particion.value_counts().to_dict(), "Metal:", p.Metal.value_counts().to_dict())
x=p.groupby("Grupo paciente").particion.nunique()
print("grupos en >1 particion:", (x>1).sum(), list(x[x>1].index)[:10])
print("casos por grupo (max):", p.groupby("Grupo paciente").size().max(), "grupos con >1 volumen:", (p.groupby("Grupo paciente").size()>1).sum())
print(pd.crosstab(p.particion, p.Metal))
# grupos.csv: grupos con >1 volumen y mezcla de metal / sin metal
g2=g.rename(columns=lambda c:c.strip())
cols=[c for c in g2.columns if c.lower() in("caso","grupo paciente","metal","elegible obj3")]
print(cols, len(g2))
m=g2.groupby("Grupo paciente").agg(n=("Caso","size"), metal=("Metal", lambda s:",".join(sorted(set(map(str,s))))))
print("grupos con >1 volumen:", (m.n>1).sum(), "| de ellos mezcla metal/sin metal:", ((m.n>1)&m.metal.str.contains(",")).sum())
# cruce: grupos con >1 volumen y su particion
mp=p.merge(m, left_on="Grupo paciente", right_index=True)
mm=mp[mp.n>1].groupby("Grupo paciente").particion.agg(lambda s:",".join(sorted(set(s))))
print("grupos multi-volumen por particion:\n", mm.value_counts())
