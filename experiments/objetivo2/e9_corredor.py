"""E9 / Objetivo 2 e implicancia #31 — diametro del corredor oseo sacro en cada volumen.

**ESTADO (2026-09-11): NO VALIDO. NO CORRER SOBRE LA COHORTE NI CITAR SUS CIFRAS.** El piloto
dio corredores de 1.6-7.8 mm donde hay tornillos transsacros reales de ~7 mm (`metal_0008`):
la mascara HU > 150 no captura el esponjoso del ala sacra (HU 0-100 a lo largo del tornillo),
y ni el cierre ni el relleno 3D lo arreglan. Ver `e9b_densidad_s1.py` e implicancia #48.
Requiere una segmentacion osea rellena (p. ej. TotalSegmentator, #29). La logica de
trayectorias, EDT, salida por el ilion y restriccion #31 se conserva para reutilizarla.

QUE MIDE
--------
Para cada paciente con S1 localizado (R1), el **diametro del mayor cilindro recto** que cabe
en hueso a lo largo de trayectorias casi transversales (izquierda-derecha) del sacro
superior. Es la magnitud de `grass2016` ("maximum cylindrical diameter"), no la seccion
axial de `lee2014` ni el diametro limitante de `wagner2017` (#30: no son intercambiables).

- **Transsacro (`D_TS`)**: el cilindro debe atravesar de la cortical externa de un ilion a
  la del otro.
- **Iliosacro por lado (`D_IS_izq`, `D_IS_der`)**: de la cortical externa del ilion hasta el
  plano medio.

RESTRICCION (#31, decision del 2026-09-11)
-----------------------------------------
`Dmax >= d_implante + 2c`. Calibres `d_implante` de 6.5, 7.3 y 8.0 mm (6.5-8.0 mm,
`gardner2010safezones`; 7.3 mm, `grass2016`). Holgura radial `c` de 1 y 2 mm por lado,
**operacionalizacion propia** de la frase de `kaiser2014dysmorphism` *"1 to 2 mm of
circumference around a 6.3 to 8-mm-diameter screw"* (el paper no publica la cuenta: es
derivacion, no cita). Se reporta tambien la convencion heredada `Dmax >= 10 mm`.

METODO (heuristico, auditable)
------------------------------
1. Recorte alrededor del S1 de R1. Hueso = HU > 150 (el mismo umbral que R1), con cierre
   morfologico de ~2 mm para que la articulacion sacroiliaca (espacio blando) no corte el
   corredor, y relleno 3D de cavidades cerradas (el esponjoso bajo 150 HU queda dentro de la
   envolvente cortical; conducto y forámenes, abiertos al exterior, no se rellenan).
   **Limitacion:** si la estria oscura rompe la cortical, la cavidad deja de estar cerrada, no
   se rellena y el corredor medido **se estrecha**; el metal existente (HU > 2500) cuenta como hueso.
2. Centros candidatos en el plano sagital del S1 de R1: rejilla de 3 mm entre 3 y 75 mm por
   debajo del platillo y de 45 mm por detras a 10 mm por delante, solo sobre hueso.
3. En cada centro, 81 direcciones: inclinacion axial y coronal de -20 a +20 grados, en pasos
   de 5, respecto al eje izquierda-derecha.
4. Por trayectoria: tramo oseo continuo que contiene el centro (se toleran huecos de hasta
   2 mm), que debe salir por ambos extremos a tejido blando **sin volver a encontrar hueso en
   40 mm** (salida real por la cortical externa del ilion, no por un foramen sacro), y
   cada salida al menos tan lateral como la EIPS de su lado (landmark de R1): el tramo cruza
   la articulacion sacroiliaca.
   `D = 2 x min EDT` sobre el tramo, con EDT = distancia euclidea de cada punto al no-hueso
   mas cercano. Es exacto para un cilindro recto: si todo punto del eje dista >= r del
   no-hueso, el cilindro de radio r cabe. Se excluyen 8 mm en cada extremo, donde la EDT la
   limita la propia salida por la cortical y no la anchura del corredor; por eso **los
   diametros por encima de 16 mm quedan truncados** a lo que permite ese recorte.
5. Perfil por nivel: el mejor `D_TS` a cada altura. **S1 y S2 no se segmentan**: se reportan
   el maximo global y los dos picos del perfil separados por al menos 12 mm, el superior
   como candidato S1 y el inferior como candidato S2. Es una heuristica declarada.

Lee `data/`, `r1_landmarks.csv`, `r1_estados.csv` y `grupos.csv`. Escribe
`e9_corredor.csv` (una fila por volumen), `e9_perfiles.csv` (perfil por nivel) y laminas de
QC en `outputs/e9_qc/`. Reanudable por lotes (`--max`).
"""
from __future__ import annotations

import argparse
import csv
import gc
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import ndimage as ndi

from r1_landmarks import cargar

BONE_HU = 150.0
METAL_HU = 2500.0
CIERRE_MM = 2.0
PASO_MM = 1.0
RECORTE_EXTREMO_MM = 8.0
HUECO_MAX_MM = 2.0
SALIDA_BLANDO_MM = 40.0
ANGULOS = np.deg2rad(np.arange(-20, 20.01, 5))
CALIBRES = (6.5, 7.3, 8.0)
HOLGURAS = (1.0, 2.0)


def recortar(arr: np.ndarray, zoom: np.ndarray, s1: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Recorte de HU y mascara osea cerrada alrededor de S1. Devuelve (hu, hueso, origen_mm)."""
    lo_mm = s1 + np.array([-130.0, -110.0, -110.0])
    hi_mm = s1 + np.array([130.0, 60.0, 40.0])
    lo = np.maximum(np.floor(lo_mm / zoom).astype(int), 0)
    hi = np.minimum(np.ceil(hi_mm / zoom).astype(int), arr.shape)
    hu = np.asarray(arr[lo[0]:hi[0], lo[1]:hi[1], lo[2]:hi[2]])
    hueso = hu > BONE_HU
    it = max(1, int(round(CIERRE_MM / float(zoom.min()))))
    hueso = ndi.binary_closing(np.pad(hueso, it), iterations=it)[it:-it, it:-it, it:-it]
    # El esponjoso del sacro y del ilion puede quedar bajo 150 HU: sin rellenar, la mascara es
    # un cascaron cortical y el corredor sale de 1-3 mm (piloto del 2026-09-11). El corredor oseo
    # es el interior de la envolvente cortical: se rellenan las cavidades CERRADAS en 3D. El
    # conducto sacro y los forámenes se comunican con el exterior y no se rellenan.
    hueso = ndi.binary_fill_holes(hueso)
    return hu, hueso, lo.astype(np.float32) * zoom


def muestrear(mask: np.ndarray, zoom: np.ndarray, origen: np.ndarray, pts: np.ndarray) -> np.ndarray:
    """Vecino mas proximo; fuera del recorte cuenta como no hueso."""
    idx = np.rint((pts - origen) / zoom).astype(np.int64)
    dentro = np.all((idx >= 0) & (idx < np.array(mask.shape)), axis=-1)
    out = np.zeros(pts.shape[:-1], dtype=bool)
    i = idx[dentro]
    out[dentro] = mask[i[..., 0], i[..., 1], i[..., 2]]
    return out


def base_perpendicular(u: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Dos vectores unitarios perpendiculares a u."""
    a = np.array([0.0, 0.0, 1.0]) if abs(u[2]) < 0.9 else np.array([0.0, 1.0, 0.0])
    e1 = np.cross(u, a)
    e1 /= np.linalg.norm(e1)
    return e1, np.cross(u, e1)


def tramo(b: np.ndarray, i0: int) -> tuple[int, int] | None:
    """Tramo oseo que contiene i0, tolerando huecos cortos; None si no sale a blando."""
    hueco = int(round(HUECO_MAX_MM / PASO_MM))
    salida = int(round(SALIDA_BLANDO_MM / PASO_MM))
    if not b[i0]:
        return None
    ext = []
    for paso in (-1, 1):
        i, ultimo = i0, i0
        while True:
            i += paso
            if not 0 <= i < len(b):
                return None  # borde del muestreo sin salir a blando
            if b[i]:
                ultimo = i
            elif abs(i - ultimo) > hueco:
                break
        # Salida real por la cortical externa del ilion: ningun hueso en los 40 mm siguientes.
        # Sin esto, un agujero sacro (foramen) se tomaba por salida y el 'corredor' era un
        # tramo corto dentro del cuerpo vertebral (piloto del 2026-09-11: L_TS de 25-44 mm).
        rng = ultimo + paso * np.arange(1, salida + 1)
        rng = rng[(rng >= 0) & (rng < len(b))]
        if b[rng].any():
            return None
        ext.append(ultimo)
    return ext[0], ext[1]


def evaluar_linea(mask: np.ndarray, edt: np.ndarray, zoom: np.ndarray, origen: np.ndarray,
                  c: np.ndarray, u: np.ndarray, x_mid: float,
                  lat_min: tuple[float, float]) -> dict | None:
    """Diametros transsacro e iliosacros de la trayectoria c + t u (EDT a lo largo del eje)."""
    t = np.arange(-160.0, 160.01, PASO_MM)
    centro = c[None, :] + t[:, None] * u[None, :]
    idx = np.rint((centro - origen) / zoom).astype(np.int64)
    dentro = np.all((idx >= 0) & (idx < np.array(mask.shape)), axis=1)
    b = np.zeros(len(t), dtype=bool)
    r = np.zeros(len(t), dtype=np.float32)
    ii = idx[dentro]
    b[dentro] = mask[ii[:, 0], ii[:, 1], ii[:, 2]]
    r[dentro] = edt[ii[:, 0], ii[:, 1], ii[:, 2]]
    tr = tramo(b, len(t) // 2)
    if tr is None:
        return None
    iL, iR = tr
    # Cada salida al menos tan lateral como la EIPS de su lado: el tramo cruza la
    # articulacion sacroiliaca y sale por el ilion (condicion anclada en landmarks de R1).
    if not (x_mid - centro[iL, 0] >= lat_min[0] and centro[iR, 0] - x_mid >= lat_min[1]):
        return None
    k = int(round(RECORTE_EXTREMO_MM / PASO_MM))
    sel = np.arange(iL + k, iR - k + 1)
    if len(sel) < 10:
        return None
    libre = r[sel]
    izq = centro[sel, 0] < x_mid
    fila = {'D_TS': 2 * float(libre.min()), 'L_TS': float(t[iR] - t[iL])}
    for nombre, m in (('D_IS_izq', izq), ('D_IS_der', ~izq)):
        fila[nombre] = 2 * float(libre[m].min()) if m.any() else np.nan
    return fila


def angulos_kaiser(u: np.ndarray, fila_r1: pd.Series) -> tuple[float, float]:
    """Angulo coronal contra la linea de crestas y axial contra la de EIPS (grados)."""
    def ang(v1: np.ndarray, v2: np.ndarray) -> float:
        c = abs(float(v1 @ v2)) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        return float(np.degrees(np.arccos(np.clip(c, -1, 1))))
    out = [np.nan, np.nan]
    try:
        cr = np.array([fila_r1['cresta_der_x_mm'] - fila_r1['cresta_izq_x_mm'], 0.0,
                       fila_r1['cresta_der_z_mm'] - fila_r1['cresta_izq_z_mm']])
        if np.all(np.isfinite(cr)):
            out[0] = ang(np.array([u[0], 0.0, u[2]]), cr)
        ei = np.array([fila_r1['eips_der_x_mm'] - fila_r1['eips_izq_x_mm'],
                       fila_r1['eips_der_y_mm'] - fila_r1['eips_izq_y_mm'], 0.0])
        if np.all(np.isfinite(ei)):
            out[1] = ang(np.array([u[0], u[1], 0.0]), ei)
    except KeyError:
        pass
    return out[0], out[1]


def picos(z: np.ndarray, d: np.ndarray) -> tuple[tuple[float, float] | None, tuple[float, float] | None]:
    """Dos picos del perfil separados >= 12 mm: (z, D) superior e inferior."""
    orden = np.argsort(-d)
    elegidos: list[int] = []
    for i in orden:
        if d[i] <= 0:
            break
        if all(abs(z[i] - z[j]) >= 12.0 for j in elegidos):
            # debe haber un minimo real entre picos (caida >= 1 mm)
            if elegidos:
                j = elegidos[0]
                a, b_ = sorted((i, j))
                if d[a:b_ + 1].min() > min(d[i], d[j]) - 1.0:
                    continue
            elegidos.append(i)
        if len(elegidos) == 2:
            break
    if not elegidos:
        return None, None
    elegidos.sort(key=lambda i: -z[i])  # superior primero (z mayor)
    sup = (float(z[elegidos[0]]), float(d[elegidos[0]]))
    inf = (float(z[elegidos[1]]), float(d[elegidos[1]])) if len(elegidos) == 2 else None
    return sup, inf


def lamina(hu: np.ndarray, zoom: np.ndarray, origen: np.ndarray, mejor: dict, zs: np.ndarray,
           perfil: np.ndarray, s1z: float, destino: Path, titulo: str) -> None:
    """Perfil D(z) y corte coronal por el centro del mejor corredor con el cilindro."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ejes = plt.subplots(1, 2, figsize=(14, 5.5))
    ejes[0].plot(perfil, zs - s1z, 'k.-')
    for v in (10.0, 8.5, 12.0):
        ejes[0].axvline(v, color='gray', ls=':' if v != 10 else '--', lw=0.8)
    ejes[0].set_xlabel('mejor D_TS en el nivel (mm)')
    ejes[0].set_ylabel('z respecto al platillo de S1 (mm)')
    ejes[0].set_title('perfil (lineas: 8.5 / 10 / 12 mm)', fontsize=9)
    if mejor:
        c, u, dd = mejor['c'], mejor['u'], mejor['D_TS']
        j = int(np.clip(round((c[1] - origen[1]) / zoom[1]), 0, hu.shape[1] - 1))
        img = hu[:, j, :].T
        ejes[1].imshow(np.clip(img, -200, 1500), cmap='gray', origin='lower',
                       extent=(origen[0], origen[0] + img.shape[1] * zoom[0],
                               origen[2], origen[2] + img.shape[0] * zoom[2]))
        t = np.array([-mejor['L_TS'] / 2 - 10, mejor['L_TS'] / 2 + 10])
        n = np.array([-u[2], u[0]]) / np.hypot(u[0], u[2])
        for off in (-dd / 2, 0.0, dd / 2):
            xs = c[0] + t * u[0] + off * n[0]
            zz = c[2] + t * u[2] + off * n[1]
            ejes[1].plot(xs, zz, 'r-' if off == 0 else 'y--', lw=1)
        ejes[1].set_title(f'coronal en y={c[1]:.0f} mm; mejor D_TS={dd:.1f} mm', fontsize=9)
    fig.suptitle(titulo, fontsize=10)
    fig.tight_layout()
    fig.savefig(destino, dpi=70)
    plt.close(fig)


def analizar(path: Path, r1: pd.Series, qc_dir: Path | None) -> tuple[dict, list[dict]]:
    """Mide un volumen: fila resumen y perfil por nivel."""
    arr, zoom = cargar(path)
    caso = r1.name
    s1 = np.array([r1['S1_x_mm'], r1['S1_y_mm'], r1['S1_z_mm']], dtype=np.float32)
    x_mid = float(r1['S1_x_mm'])
    hu, hueso, origen = recortar(arr, zoom, s1)
    del arr
    edt = ndi.distance_transform_edt(hueso, sampling=zoom).astype(np.float32)
    lat_min = (abs(float(r1['eips_izq_x_mm']) - x_mid), abs(float(r1['eips_der_x_mm']) - x_mid))
    zs = s1[2] - np.arange(3.0, 75.01, 3.0)
    ys = s1[1] + np.arange(-45.0, 10.01, 3.0)
    direcciones = []
    for a in ANGULOS:
        for b in ANGULOS:
            u = np.array([1.0, np.tan(a), np.tan(b)])
            direcciones.append(u / np.linalg.norm(u))

    perfil_rows: list[dict] = []
    mejor_global: dict = {}
    mejor_por_z = np.zeros(len(zs))
    mejores_is = {'D_IS_izq': 0.0, 'D_IS_der': 0.0}
    for iz, z in enumerate(zs):
        mejor_z: dict = {}
        for y in ys:
            c = np.array([x_mid, y, z], dtype=np.float32)
            if not muestrear(hueso, zoom, origen, c[None, :])[0]:
                continue
            for u in direcciones:
                r = evaluar_linea(hueso, edt, zoom, origen, c, u, x_mid, lat_min)
                if r is None:
                    continue
                for k in mejores_is:
                    if np.isfinite(r[k]):
                        mejores_is[k] = max(mejores_is[k], r[k])
                if r['D_TS'] > mejor_z.get('D_TS', -1):
                    mejor_z = {**r, 'c': c, 'u': u}
        d = mejor_z.get('D_TS', 0.0)
        mejor_por_z[iz] = d
        perfil_rows.append({'Caso': caso, 'z_rel_S1_mm': round(float(z - s1[2]), 1),
                            'D_TS_mejor_mm': round(d, 1)})
        if d > mejor_global.get('D_TS', -1):
            mejor_global = mejor_z

    sup, inf = picos(zs, mejor_por_z)
    fila: dict = {'Caso': caso, 'D_TS_max_mm': round(mejor_global.get('D_TS', 0.0), 1),
                  'L_TS_mejor_mm': round(mejor_global.get('L_TS', np.nan), 1),
                  'D_IS_izq_max_mm': round(mejores_is['D_IS_izq'], 1),
                  'D_IS_der_max_mm': round(mejores_is['D_IS_der'], 1)}
    if sup:
        fila.update({'pico_sup_z_rel_mm': round(sup[0] - s1[2], 1), 'pico_sup_D_mm': round(sup[1], 1)})
    if inf:
        fila.update({'pico_inf_z_rel_mm': round(inf[0] - s1[2], 1), 'pico_inf_D_mm': round(inf[1], 1)})
    if mejor_global:
        u, c = mejor_global['u'], mejor_global['c']
        fila['z_mejor_rel_mm'] = round(float(c[2] - s1[2]), 1)
        fila['y_mejor_rel_mm'] = round(float(c[1] - s1[1]), 1)
        cor, axi = angulos_kaiser(u, r1)
        fila['ang_coronal_crestas_deg'] = round(cor, 1) if np.isfinite(cor) else np.nan
        fila['ang_axial_eips_deg'] = round(axi, 1) if np.isfinite(axi) else np.nan
        t = np.arange(-mejor_global['L_TS'] / 2, mejor_global['L_TS'] / 2 + 0.1, PASO_MM)
        idx = np.rint(((c[None, :] + t[:, None] * u[None, :]) - origen) / zoom).astype(int)
        idx = idx[np.all((idx >= 0) & (idx < np.array(hu.shape)), axis=1)]
        fila['frac_metal_eje'] = round(float((hu[idx[:, 0], idx[:, 1], idx[:, 2]] > METAL_HU).mean()), 3)
    for d_imp in CALIBRES:
        for c_h in HOLGURAS:
            umbral = d_imp + 2 * c_h
            fila[f'viable_TS_d{d_imp}_c{c_h:.0f}'] = 'si' if fila['D_TS_max_mm'] >= umbral else 'no'
    fila['viable_TS_10mm'] = 'si' if fila['D_TS_max_mm'] >= 10.0 else 'no'
    if qc_dir is not None:
        lamina(hu, zoom, origen, mejor_global, zs, mejor_por_z, float(s1[2]),
               qc_dir / f'{caso}.png', f'{caso}: D_TS max {fila["D_TS_max_mm"]} mm; '
               f'IS izq {fila["D_IS_izq_max_mm"]} / der {fila["D_IS_der_max_mm"]} mm')
    return fila, perfil_rows


def main() -> None:
    """Punto de entrada: cohorte = unidades con S1 hallado, en orden, reanudable."""
    here = Path(__file__).resolve().parent
    root = here.parents[1]
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--cohorte', default='evaluacion', help="'evaluacion' o 'calibracion'")
    parser.add_argument('--casos', nargs='*')
    parser.add_argument('--max', type=int, default=None)
    parser.add_argument('--out', type=Path, default=here)
    parser.add_argument('--no-qc', action='store_true')
    args = parser.parse_args()

    r1 = pd.read_csv(here / 'r1_landmarks.csv').set_index('Caso')
    est = pd.read_csv(here / 'r1_estados.csv').set_index('Caso')
    casos = [c for c in est.index[est['cohorte'] == args.cohorte] if r1.loc[c, 'S1_hallado'] == 'si']
    if args.casos:
        casos = [c for c in casos if any(s in c for s in args.casos)]
    rutas = {p.name.split('.nii')[0]: p for p in (root / 'data').rglob('*.nii.gz')}
    qc_dir = None if args.no_qc else args.out / 'outputs' / 'e9_qc'
    if qc_dir is not None:
        qc_dir.mkdir(parents=True, exist_ok=True)

    campos = ['Caso', 'D_TS_max_mm', 'L_TS_mejor_mm', 'D_IS_izq_max_mm', 'D_IS_der_max_mm',
              'pico_sup_z_rel_mm', 'pico_sup_D_mm', 'pico_inf_z_rel_mm', 'pico_inf_D_mm',
              'z_mejor_rel_mm', 'y_mejor_rel_mm', 'ang_coronal_crestas_deg', 'ang_axial_eips_deg',
              'frac_metal_eje', 'viable_TS_10mm']
    campos += [f'viable_TS_d{d}_c{c:.0f}' for d in CALIBRES for c in HOLGURAS] + ['Error']
    destino = args.out / 'e9_corredor.csv'
    perfiles = args.out / 'e9_perfiles.csv'
    hechos = set(pd.read_csv(destino)['Caso']) if destino.exists() else set()
    nuevos = 0
    with destino.open('a' if hechos else 'w', encoding='utf-8', newline='') as h, \
            perfiles.open('a' if hechos else 'w', encoding='utf-8', newline='') as hp:
        w = csv.DictWriter(h, fieldnames=campos, extrasaction='ignore')
        wp = csv.DictWriter(hp, fieldnames=['Caso', 'z_rel_S1_mm', 'D_TS_mejor_mm'])
        if not hechos:
            w.writeheader()
            wp.writeheader()
        for caso in casos:
            if caso in hechos:
                continue
            if args.max is not None and nuevos >= args.max:
                break
            nuevos += 1
            try:
                fila, perfil = analizar(rutas[caso], r1.loc[caso], qc_dir)
            except Exception as exc:  # noqa: BLE001
                fila, perfil = {'Caso': caso, 'Error': f'{type(exc).__name__}: {exc}'}, []
            w.writerow(fila)
            wp.writerows(perfil)
            h.flush()
            hp.flush()
            gc.collect()
            print(f'{caso}: D_TS {fila.get("D_TS_max_mm")} IS {fila.get("D_IS_izq_max_mm")}/'
                  f'{fila.get("D_IS_der_max_mm")} err={fila.get("Error", "")}', flush=True)


if __name__ == '__main__':
    main()
