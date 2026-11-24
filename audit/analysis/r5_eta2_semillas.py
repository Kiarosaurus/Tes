"""R-5 (C_deep_learning): variabilidad entre semillas de eta2_exc. Solo CPU, solo lectura de c4_filas.csv / c4b_filas.csv."""
import sys, pandas as pd, numpy as np
P = "/mnt/d/UTEC/CICLOX/Salvar-El-Ciclo/_plan_urgente_2026-11/tesis/c4/"
out = []
for f in ["c4_filas.csv", "c4b_filas.csv"]:
    d = pd.read_csv(P + f)
    d["fuente"] = f
    out.append(d)
d = pd.concat(out)
print(d.columns.tolist(), len(d)); print(d.groupby(["fuente","brazo","modo"]).size().head(30))
# variabilidad entre semillas: por (fuente,brazo,modo,paciente,corte,K,ventana): sd y rango sobre semillas
g = d.groupby(["fuente","brazo","modo","paciente","corte","K","ventana"])["eta2_exc"]
s = g.agg(n="count", media="mean", sd="std", rango=lambda x: x.max()-x.min()).reset_index()
s = s[s.n >= 2]
res = s.groupby(["fuente","brazo","modo","K","ventana"]).agg(n_celdas=("n","size"), n_semillas=("n","median"), media=("media","mean"), sd_semillas_media=("sd","mean"), rango_semillas_medio=("rango","mean")).reset_index()
res.to_csv("r5_eta2_semillas.csv", index=False)
print(res.to_string(max_rows=80))
