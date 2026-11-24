"""C2b: evaluacion visual A CIEGAS con puntaje 1-5 (criterio (c), docs/01-decisiones.md 2026-11-20 (9)). Exploratorio.

Paneles: por brazo, 2 pacientes (0101, 0102) x 3 cortes (1/6, 3/6, 5/6 de los cortes con M que tambien tiene Peters), semilla 0;
mas Peters Ti y el real (metal_0039, 2 tornillos x 3 cortes). Recorte 160 px, ventana fija [-500, 1300] HU, sin etiquetas,
orden aleatorio, ids opacos. Clave aparte (NO abrirla antes de puntuar).
Cada panel: puntaje 1-5 "que tan creible es el artefacto" y casilla "borde del tornillo mas brillante que el interior".

Uso: METALSYNTH_REPO=<repo> python -I c2b_ciego.py --arm run04_mejor=<dir> --arm run04_mejor_p100_e0.3=<dir> ...
     (la etiqueta es la parte de nombre de archivo: a15_<caso>_<etiqueta>_s0_sintetica.nii.gz)
"""
from __future__ import annotations
import argparse, base64, csv, io, os, random, secrets
from pathlib import Path
import numpy as np, nibabel as nib
from PIL import Image
from scipy import ndimage as ndi

REPO = Path(os.environ.get('METALSYNTH_REPO', r'D:/UTEC/CICLOX/Salvar-El-Ciclo/PFCII/metalsynth-pelvis'))
OUT3 = REPO / 'experiments/objetivo3/outputs/obj3_pose'
SALIDA = Path(__file__).resolve().parent / 'c2'
CASOS = ['dataset6_CLINIC_0101_data', 'dataset6_CLINIC_0102_data']
LO, HI, LADO = -500.0, 1300.0, 160


def tercios(lista):
    n = len(lista)
    return [lista[min(n - 1, int(n * f))] for f in (1 / 6, 3 / 6, 5 / 6)]


def panel(sl, cy, cx):
    h = LADO // 2
    p = np.pad(sl, h, mode='constant', constant_values=-1000)
    r = p[int(round(cy)):int(round(cy)) + LADO, int(round(cx)):int(round(cx)) + LADO]
    g = np.clip((r - LO) / (HI - LO), 0, 1)
    img = Image.fromarray((g * 255).astype(np.uint8)).resize((320, 320), Image.BICUBIC)
    b = io.BytesIO()
    img.save(b, 'PNG')
    return base64.b64encode(b.getvalue()).decode()


def centro(m2):
    y, x = ndi.center_of_mass(m2)
    return y, x


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--arm', action='append', required=True, help='etiqueta=carpeta con a15_*_sintetica.nii.gz')
    ap.add_argument('--sufijo', default='')
    a = ap.parse_args()
    arms = [x.split('=', 1) for x in a.arm]
    items = []   # (brazo, caso, corte, b64)
    for caso in CASOS:
        z = np.load(OUT3 / f'peters_val/a19_{caso}.npz')
        ks = [int(k) for k in z['ks']]
        cand = [(i, k) for i, k in enumerate(ks) if z['M'][i].any()]
        vols = {}
        for et, d in arms:
            f = Path(d) / f'a15_{caso}_{et}_s0_sintetica.nii.gz'
            vols[et] = nib.load(str(f)).get_fdata(dtype=np.float32)
        for i, k in tercios(cand):
            cy, cx = centro(z['M'][i])
            items.append(('peters_Ti', caso, k, panel(z['Ti_A'][i], cy, cx)))
            for et in vols:
                items.append((et, caso, k, panel(vols[et][:, :, k], cy, cx)))
    import sys
    sys.path.insert(0, str(REPO / 'experiments/objetivo1'))
    from e6b_vae_sd15 import eje_axial
    real = nib.load(str(REPO / 'data/dataset7/dataset7_CLINIC_metal_0039_data.nii.gz'))
    arr = real.get_fdata(dtype=np.float32)
    eje = eje_axial(real)
    vol = np.moveaxis(arr, eje, 0)
    lab, n = ndi.label(vol > 2500)
    zo = np.array(real.header.get_zooms()[:3], float)
    tam = ndi.sum(vol > 2500, lab, index=np.arange(1, n + 1)) * float(np.prod(zo))
    for c in [i + 1 for i in np.argsort(-tam) if tam[i] >= 500.0][:2]:
        m3 = lab == c
        zs = sorted(set(np.nonzero(m3)[0]))
        for k in tercios(zs):
            cy, cx = centro(m3[k])
            items.append(('real', f'metal_0039_c{c}', int(k), panel(vol[k], cy, cx)))
    rng = random.Random(secrets.randbits(64))
    rng.shuffle(items)
    ids = [secrets.token_hex(3) for _ in items]
    SALIDA.mkdir(exist_ok=True)
    nombre = 'b' + a.sufijo
    with open(SALIDA / f'clave_{nombre}_NO_ABRIR.csv', 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['id', 'brazo', 'caso', 'corte_k'])
        for i, it in zip(ids, items):
            w.writerow([i, it[0], it[1], it[2]])
    cards = ''.join(
        f'<div class="c"><img src="data:image/png;base64,{it[3]}"><div class="r">#{n + 1} credibilidad: '
        + ''.join(f'<label><input type="radio" name="s{ids[n]}" value="{j}">{j}</label>' for j in range(1, 6))
        + f'</div><label class="b"><input type="checkbox" name="b{ids[n]}"> borde del tornillo más brillante que el interior</label>'
        f'<input type="hidden" class="id" value="{ids[n]}"></div>' for n, it in enumerate(items))
    html = f'''<!doctype html><meta charset="utf-8"><title>C2b ciego</title>
<style>body{{font:14px sans-serif;background:#111;color:#ddd}}.g{{display:grid;grid-template-columns:repeat(auto-fill,340px);gap:12px}}
.c{{background:#222;padding:8px}}img{{width:320px;height:320px}}label{{margin:0 5px}}.b{{display:block;margin-top:4px;color:#aaa}}</style>
<h3>C2b — {len(items)} paneles, ventana fija [{LO:.0f}, {HI:.0f}] HU. Puntúa de 1 (nada creíble) a 5 (indistinguible de un artefacto real). No abras la clave.</h3>
<button onclick="ex()">Descargar respuestas (CSV)</button><div class="g">{cards}</div>
<script>function ex(){{let r=['id,puntaje,borde_brillante'];document.querySelectorAll('.c').forEach(c=>{{const id=c.querySelector('.id').value;
const s=c.querySelector('input[type=radio]:checked');const b=c.querySelector('input[type=checkbox]').checked;r.push(id+','+(s?s.value:'')+','+(b?1:0))}});
const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([r.join('\\n')]));a.download='c2b_respuestas.csv';a.click()}}</script>'''
    (SALIDA / f'ciego_{nombre}.html').write_text(html, encoding='utf-8')
    print(len(items), 'paneles ->', SALIDA / f'ciego_{nombre}.html')


if __name__ == '__main__':
    main()
