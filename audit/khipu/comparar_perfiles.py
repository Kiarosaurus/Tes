#!/usr/bin/env python3
"""Compara perfiles por anillo (a15_*_perfil.csv: r_lo_mm,r_hi_mm,n,hu_p50,hu_p05,hu_p95). Solo CPU/lectura.
  r4 : python comparar_perfiles.py r4  <dir_referencia> <dir_nuevo> [etiqueta_ref etiqueta_nueva]   -> diferencia maxima por archivo
  anillos : python comparar_perfiles.py anillos <dir> <etiqueta>                                      -> p05/p50/p95 medio por anillo (piso de ruido)
  var : python comparar_perfiles.py var <dir> <etiqA> <etiqB>                                          -> diferencia por anillo de p95 y p05 entre dos etiquetas
Uso del entorno: ~/.venvs/audit/bin/python"""
import glob, os, re, sys
import numpy as np, pandas as pd

def cargar(d, etiq):
    out = {}
    for f in glob.glob(os.path.join(d, f"a15_*_{etiq}_s*_perfil.csv")):
        m = re.match(rf"a15_(.+)_{re.escape(etiq)}_s(\d+)_perfil\.csv", os.path.basename(f))
        if m: out[(m.group(1), int(m.group(2)))] = pd.read_csv(f)
    return out

def media_anillos(P):
    d = pd.concat([x.assign(caso=k[0], semilla=k[1]) for k, x in P.items()])
    return d.groupby(["r_lo_mm", "r_hi_mm"])[["hu_p05", "hu_p50", "hu_p95"]].mean().round(1), d.caso.nunique(), d.semilla.nunique()

modo = sys.argv[1]
if modo == "r4":
    ref, nuevo = sys.argv[2], sys.argv[3]; er = sys.argv[4] if len(sys.argv) > 4 else "run04_mejor"; en = sys.argv[5] if len(sys.argv) > 5 else er
    A, B = cargar(ref, er), cargar(nuevo, en); comun = sorted(set(A) & set(B))
    print(f"archivos comparables: {len(comun)} (ref {len(A)}, nuevo {len(B)})")
    mx = []
    for k in comun:
        a, b = A[k], B[k]; n = min(len(a), len(b))
        dif = max(float(np.nanmax(np.abs(a[c].values[:n] - b[c].values[:n]))) for c in ("hu_p05", "hu_p50", "hu_p95"))
        mx.append((dif, k))
    mx.sort(reverse=True); print("diferencia maxima (HU) por archivo, peores 10:"); [print(f"  {d:8.3f}  {k}") for d, k in mx[:10]]
    print("MAXIMA GLOBAL:", round(mx[0][0], 3) if mx else None, "HU  (referencia fijada en cap3:313: 0.04 HU para misma GPU)")
elif modo == "anillos":
    t, n, s = media_anillos(cargar(sys.argv[2], sys.argv[3])); print(f"{n} casos x {s} semillas"); print(t.to_string())
elif modo == "var":
    d = sys.argv[2]; A, nA, _ = media_anillos(cargar(d, sys.argv[3])); B, nB, _ = media_anillos(cargar(d, sys.argv[4]))
    print(f"A={sys.argv[3]} ({nA} casos)  B={sys.argv[4]} ({nB} casos)"); print((B - A).round(1).to_string())
