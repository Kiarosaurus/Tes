"""A20 - evaluador comun de `streak amplitude` de E-A2, igual para el difusor y para el brazo fisico de Peters.

DEFINICION (01-decisiones 2026-10-05 (3) y (4); no se reinventa aqui)
--------------------------------------------------------------------
- Campo de desviacion: difusor `Delta = I_sintetica - I_original`; Peters `Delta = recon(con metal) -
  recon(sin metal)`, el par de la simulacion.
- ROIs: anillos completos (360 grados) en **planos perpendiculares a `u`**, desde una guarda de **un voxel en
  plano del propio caso** hasta **12 mm**, excluyendo `M`, en todo el largo de `M` **menos 8 mm por extremo**.
- Estadistico por ROI (Peters, 2.5, p. 5): promedio del 5 % superior menos el del 5 % inferior de `Delta`.
- **Un valor por paciente:** mediana sobre las ROIs.
- Junto al endpoint, para el difusor: fraccion de voxeles de la ROI de la imagen sintetica que quedan exactamente
  en el suelo de -1000 HU (#141).

IMPLEMENTACION (eleccion propia, fijada antes de ver ningun resultado de E-A2)
------------------------------------------------------------------------------
- **Distancia a `M`:** transformada de distancia euclidea 3D con el espaciado del caso. Lejos de los extremos
  de un cilindro recto, coincide con la distancia en el plano perpendicular a `u`. Los extremos quedan fuera por
  el recorte de 8 mm.
- **Planos:** rebanadas perpendiculares a `u` de espesor igual a la guarda (un voxel en plano), con la posicion
  a lo largo del eje `t = p . u`. Una ROI necesita al menos 20 voxeles (el minimo de `a15`).
- **Cortes axiales validos:** solo cuentan los voxeles de cortes que el brazo realmente produjo. Para el
  difusor, los que genero `a15` (hoy, solo los que contienen `M`; #160). Para Peters, los simulados (`k = 2`).
  Para comparar los dos brazos, `--interseccion` usa los cortes comunes.

USO
---
    python experiments/objetivo3/a20_evaluador_ea2.py peters --npz outputs/a19/a19_dataset6_CLINIC_0101_data.npz
    python experiments/objetivo3/a20_evaluador_ea2.py difusor --caso dataset6_CLINIC_0101_data \\
        --dir outputs/a15_nifti --etiqueta mejor_37k --semillas 0 1 2 3 4 [--interseccion outputs/a19/...npz]
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import numpy as np

_AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(_AQUI))

R_MAX_MM = 12.0
RECORTE_EXTREMO_MM = 8.0           # e9_corredor.py, D-O2.3 (a12)
MIN_VOX = 20
SUELO_HU = -1000.0


def amplitud(x: np.ndarray) -> float:
    """Estadistico de Peters: promedio del 5 % superior menos el del 5 % inferior."""
    x = np.sort(np.asarray(x, dtype=np.float64))
    m = max(1, int(round(0.05 * x.size)))
    return float(x[-m:].mean() - x[:m].mean())


def rois(M: np.ndarray, esp3d, u_af: np.ndarray, guarda_mm: float) -> np.ndarray:
    """Etiqueta de ROI (rebanada perpendicular a `u`) por voxel, en orden axial-primero; -1 fuera de las ROIs.

    `M` va en orden (axial, plano0, plano1) y `u_af` es la direccion del eje en ese mismo orden.
    """
    from scipy import ndimage as ndi
    esp = np.asarray(esp3d, dtype=float)
    u = np.asarray(u_af, dtype=float) / np.linalg.norm(u_af)
    idx = np.argwhere(M)
    marg = np.ceil((R_MAX_MM + 1.0) / esp).astype(int)
    lo = np.maximum(idx.min(0) - marg, 0)
    hi = np.minimum(idx.max(0) + marg + 1, M.shape)
    caja = tuple(slice(a, b) for a, b in zip(lo, hi))
    Mc = M[caja]
    dist = ndi.distance_transform_edt(~Mc, sampling=esp)
    g = np.stack(np.meshgrid(*[np.arange(a, b) * e for a, b, e in zip(lo, hi, esp)], indexing='ij'), -1)
    t = g @ u
    t_m = t[Mc]
    t0, t1 = t_m.min() + RECORTE_EXTREMO_MM, t_m.max() - RECORTE_EXTREMO_MM
    sel = (~Mc) & (dist > guarda_mm) & (dist <= R_MAX_MM) & (t >= t0) & (t <= t1)
    lab = np.full(Mc.shape, -1, dtype=np.int32)
    lab[sel] = np.floor((t[sel] - t0) / guarda_mm).astype(np.int32)
    out = np.full(M.shape, -1, dtype=np.int32)
    out[caja] = lab
    return out


def evalua(delta: np.ndarray, lab: np.ndarray, validos: np.ndarray, img: np.ndarray | None = None) -> dict:
    """Mediana sobre ROIs de la amplitud de colas de `delta`; solo voxeles de cortes axiales `validos`."""
    usable = (lab >= 0) & validos[:, None, None]
    ids = np.unique(lab[usable])
    amps, n_vox, suelo = [], [], []
    for i in ids:
        s = usable & (lab == i)
        if s.sum() < MIN_VOX:
            continue
        amps.append(amplitud(delta[s]))
        n_vox.append(int(s.sum()))
        if img is not None:
            suelo.append(float((img[s] <= SUELO_HU + 0.5).mean()))
    if not amps:
        return {'amp_HU': float('nan'), 'n_rois': 0, 'n_vox': 0, 'suelo_frac': float('nan')}
    return {'amp_HU': float(np.median(amps)), 'n_rois': len(amps), 'n_vox': int(np.sum(n_vox)),
            'amp_p25': float(np.percentile(amps, 25)), 'amp_p75': float(np.percentile(amps, 75)),
            'suelo_frac': float(np.median(suelo)) if suelo else float('nan')}


def geometria_af(caso: str, particiones: list[str]):
    """`M` completa, espaciado y `u` en orden axial-primero, con la misma pose que `a15`/`a19`."""
    from a19_peters_completo import geometria
    raiz = _AQUI.parents[1]
    vol, M, G, esp2d, pose = geometria(caso, [raiz / 'data'], _AQUI.parent / 'objetivo1' / 'p1_particion.csv',
                                       particiones, _AQUI.parent / 'objetivo2' / 'outputs' / 'e9ts_ejes_corredor.csv',
                                       'default6mm')
    eje, plano, z = pose['eje_axial'], pose['plano'], pose['zooms']
    orden = [eje] + list(plano)
    esp3d = [z[i] for i in orden]
    u_af = np.array(pose['u'])[orden]
    return vol, M, esp3d, u_af, esp2d[0]


def calcula_delta(ruta: Path, etiqueta: str) -> None:
    """`Delta = max(s, r)` (autora, 2026-10-09; fijada antes de ver los numeros).

    s = rango de la amplitud del difusor entre sus semillas, por paciente, promediado sobre los pacientes.
    r = |amplitud Fe_A - amplitud Fe_B| de Peters, por paciente, promediado sobre los pacientes.
    Solo pacientes con los dos brazos medidos.
    """
    with open(ruta, newline='', encoding='utf-8') as fh:
        filas = list(csv.DictReader(fh))
    dif, fis = {}, {}
    for f in filas:
        if f['brazo'] == 'difusor' and f['condicion'].startswith(etiqueta + '_s'):
            dif.setdefault(f['caso'], []).append(float(f['amp_HU']))
        if f['brazo'] == 'peters' and f['condicion'] in ('Fe_A', 'Fe_B'):
            fis.setdefault(f['caso'], {})[f['condicion']] = float(f['amp_HU'])
    casos = sorted(c for c in dif if c in fis and len(fis[c]) == 2)
    if not casos:
        raise SystemExit('sin pacientes con los dos brazos en %s' % ruta)
    s_p = {c: max(dif[c]) - min(dif[c]) for c in casos}
    r_p = {c: abs(fis[c]['Fe_A'] - fis[c]['Fe_B']) for c in casos}
    s, r = float(np.mean(list(s_p.values()))), float(np.mean(list(r_p.values())))
    delta = max(s, r)
    for c in casos:
        print('%s | difusor: %d semillas, rango %.1f HU | Peters Fe: |A-B| = %.1f HU' % (c, len(dif[c]), s_p[c], r_p[c]))
    print('s = %.1f HU | r = %.1f HU | Delta = max(s, r) = %.1f HU (lo fija %s)'
          % (s, r, delta, 'el difusor' if s >= r else 'Peters'))
    out = ruta.with_name('a20_delta.json')
    out.write_text(json.dumps({'s_HU': s, 'r_HU': r, 'Delta_HU': delta, 'casos': casos, 's_por_caso': s_p,
                               'r_por_caso': r_p, 'formula': 'Delta = max(s, r), 01-decisiones 2026-10-09 (4)'},
                              indent=2), encoding='utf-8')
    print('-> %s' % out)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='brazo', required=True)
    p = sub.add_parser('peters')
    p.add_argument('--npz', type=Path, nargs='+', required=True)
    d = sub.add_parser('difusor')
    d.add_argument('--caso', required=True)
    d.add_argument('--dir', type=Path, required=True, help='salida de a15 con --nifti')
    d.add_argument('--etiqueta', default='mejor_37k')
    d.add_argument('--semillas', type=int, nargs='+', default=[0, 1, 2, 3, 4])
    d.add_argument('--interseccion', type=Path, default=None, help='npz de a19: usar solo sus cortes simulados')
    dl = sub.add_parser('delta', help='calcula Delta = max(s, r) desde el CSV (formula fijada 2026-10-09)')
    dl.add_argument('--csv', type=Path, default=_AQUI / 'outputs' / 'a20' / 'a20_ea2.csv')
    dl.add_argument('--etiqueta', default='mejor_37k')
    for q in (p, d):
        q.add_argument('--corrida-final', action='store_true', help='permite test (tras congelar diseno_A.md)')
        q.add_argument('--out', type=Path, default=_AQUI / 'outputs' / 'a20' / 'a20_ea2.csv')
    args = ap.parse_args()
    if args.brazo == 'delta':
        calcula_delta(args.csv, args.etiqueta)
        return
    parts = ['val', 'test'] if args.corrida_final else ['val']
    args.out.parent.mkdir(parents=True, exist_ok=True)
    filas = []

    if args.brazo == 'peters':
        for ruta in args.npz:
            z = np.load(ruta)
            caso = json.loads(ruta.with_suffix('.json').read_text(encoding='utf-8'))['caso']
            vol, M, esp3d, u_af, guarda = geometria_af(caso, parts)
            lab = rois(M, esp3d, u_af, guarda)
            validos = np.zeros(M.shape[0], bool)
            validos[z['ks']] = True
            full = {}
            for nom in ('limpia_A', 'limpia_B', 'Fe_A', 'Fe_B', 'Ti_A', 'Ti_B'):
                v = np.zeros(M.shape, np.float32)
                v[z['ks']] = z[nom]
                full[nom] = v
            for mat in ('Fe', 'Ti'):
                for r in ('A', 'B'):
                    res = evalua(full['%s_%s' % (mat, r)] - full['limpia_%s' % r], lab, validos)
                    filas.append({'brazo': 'peters', 'caso': caso, 'condicion': '%s_%s' % (mat, r), **res})
                    print('%s peters %s_%s: amp %.0f HU | %d ROIs' % (caso, mat, r, res['amp_HU'], res['n_rois']))
            ruido = evalua(full['limpia_A'] - full['limpia_B'], lab, validos)
            filas.append({'brazo': 'peters', 'caso': caso, 'condicion': 'ruido_A-B', **ruido})
    else:
        import nibabel as nib
        vol, M, esp3d, u_af, guarda = geometria_af(args.caso, parts)
        lab = rois(M, esp3d, u_af, guarda)
        validos = M.reshape(M.shape[0], -1).any(1)          # a15 genera solo los cortes con `M` (#160)
        if args.interseccion:
            ks = np.load(args.interseccion)['ks']
            v2 = np.zeros_like(validos)
            v2[ks] = True
            validos &= v2

        def lee(ruta: Path) -> np.ndarray:
            return np.moveaxis(nib.load(str(ruta)).get_fdata(dtype=np.float32), 2, 0)   # a15 guarda (y, x, axial)
        orig = lee(args.dir / ('a15_%s_original.nii.gz' % args.caso))
        if orig.shape != M.shape:
            raise SystemExit('forma del original de a15 %s != %s' % (orig.shape, M.shape))
        for s in args.semillas:
            sint = lee(args.dir / ('a15_%s_%s_s%d_sintetica.nii.gz' % (args.caso, args.etiqueta, s)))
            res = evalua(sint - orig, lab, validos, img=sint)
            filas.append({'brazo': 'difusor', 'caso': args.caso, 'condicion': '%s_s%d' % (args.etiqueta, s), **res})
            print('%s difusor %s s%d: amp %.0f HU | %d ROIs | suelo %.3f'
                  % (args.caso, args.etiqueta, s, res['amp_HU'], res['n_rois'], res['suelo_frac']))

    nuevo = not args.out.exists()
    claves = ['brazo', 'caso', 'condicion', 'amp_HU', 'amp_p25', 'amp_p75', 'n_rois', 'n_vox', 'suelo_frac']
    with open(args.out, 'a', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=claves, extrasaction='ignore')
        if nuevo:
            w.writeheader()
        w.writerows(filas)
    print('-> %s' % args.out)


if __name__ == '__main__':
    main()
