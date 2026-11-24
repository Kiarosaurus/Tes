"""C2: genera el HTML a ciegas (ver c2_protocolo.md) y la clave. Solo lectura sobre el repo.

Uso: python -I c2_ciego.py            (escribe c2/ciego.html y c2/clave_NO_ABRIR.csv)
"""
from __future__ import annotations
import base64, csv, io, secrets, random
from pathlib import Path
import numpy as np, nibabel as nib
from PIL import Image
from scipy import ndimage as ndi

REPO = Path(r'D:/UTEC/CICLOX/Salvar-El-Ciclo/PFCII/metalsynth-pelvis')
OUT3 = REPO / 'experiments/objetivo3/outputs/obj3_pose'
SALIDA = Path(__file__).resolve().parent / 'c2'
CASOS = ['dataset6_CLINIC_0101_data', 'dataset6_CLINIC_0102_data']
BRAZOS_NII = {'run04_mejor': 'run04_mejor', 'run05a': 'run05a_mejor', 'run05b': 'run05b_mejor'}
LO, HI, LADO = -500.0, 1300.0, 160


def tercios(lista):
    n = len(lista)
    return [lista[min(n - 1, int(n * f))] for f in (1/6, 3/6, 5/6)]


def panel(sl, cy, cx):
    h = LADO // 2
    p = np.pad(sl, h, mode='constant', constant_values=-1000)
    r = p[cy:cy + LADO, cx:cx + LADO]  # centro (cy,cx) -> tras pad h
    g = np.clip((r - LO) / (HI - LO), 0, 1)
    img = Image.fromarray((g * 255).astype(np.uint8)).resize((320, 320), Image.BICUBIC)
    b = io.BytesIO(); img.save(b, 'PNG')
    return base64.b64encode(b.getvalue()).decode()


def centroide(m2):
    y, x = ndi.center_of_mass(m2)
    return int(round(y)), int(round(x))


def main():
    SALIDA.mkdir(exist_ok=True)
    items = []  # (brazo, origen, caso, k, b64)
    for caso in CASOS:
        z = np.load(OUT3 / f'peters_val/a19_{caso}.npz')
        ks = [int(k) for k in z['ks']]
        M = z['M']
        cand = [(i, k) for i, k in enumerate(ks) if M[i].any()]
        vols = {}
        for br, d in BRAZOS_NII.items():
            f = OUT3 / f'delta/{d}/a15_{caso}_{d}_s0_sintetica.nii.gz'
            vols[br] = nib.load(str(f)).get_fdata(dtype=np.float32)
        for i, k in tercios(cand):
            cy, cx = centroide(M[i])
            items.append(('peters_Ti', 'sint', caso, k, panel(z['Ti_A'][i], cy, cx)))
            for br, v in vols.items():
                items.append((br, 'sint', caso, k, panel(v[:, :, k], cy, cx)))
    # real: metal_0039
    real = nib.load(str(REPO / 'data/dataset7/dataset7_CLINIC_metal_0039_data.nii.gz'))
    a = real.get_fdata(dtype=np.float32)
    lab, n = ndi.label(a > 2500)  # conectividad 6 por omision en 3D
    vox = float(np.prod(real.header.get_zooms()))
    comps = [(c, (lab == c)) for c in range(1, n + 1) if (lab == c).sum() * vox >= 500]
    comps = sorted(comps, key=lambda t: -t[1].sum())[:2]
    for c, m in comps:
        zs = sorted(set(np.nonzero(m)[2]))
        for k in tercios(zs):
            cy, cx = centroide(m[:, :, k])
            items.append(('real', 'real', f'metal_0039_c{c}', int(k), panel(a[:, :, k], cy, cx)))
    rng = random.Random(secrets.randbits(64))
    rng.shuffle(items)
    ids = [secrets.token_hex(3) for _ in items]
    with open(SALIDA / 'clave_NO_ABRIR.csv', 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(['id', 'brazo', 'caso', 'corte_k'])
        for i, it in zip(ids, items): w.writerow([i, it[0], it[2], it[3]])
    cards = ''.join(
        f'<div class="c"><img src="data:image/png;base64,{it[4]}"><div>#{n+1}'
        f'<label><input type="radio" name="r{ids[n]}" value="real"> real</label>'
        f'<label><input type="radio" name="r{ids[n]}" value="sint"> sintético</label>'
        f'<select name="q{ids[n]}"><option value="">conf.</option>'
        + ''.join(f'<option>{j}</option>' for j in range(1, 6)) +
        f'</select></div><input type="hidden" class="id" value="{ids[n]}"></div>'
        for n, it in enumerate(items))
    html = f'''<!doctype html><meta charset="utf-8"><title>C2 ciego</title>
<style>body{{font:14px sans-serif;background:#111;color:#ddd}}.g{{display:grid;grid-template-columns:repeat(auto-fill,340px);gap:12px}}
.c{{background:#222;padding:8px}}img{{width:320px;height:320px}}label{{margin:0 6px}}</style>
<h3>C2 — {len(items)} paneles, ventana fija [{LO:.0f}, {HI:.0f}] HU. Marca real/sintético y confianza 1-5. No abras clave_NO_ABRIR.csv.</h3>
<button onclick="ex()">Descargar respuestas (CSV)</button><div class="g">{cards}</div>
<script>function ex(){{let r=['id,juicio,confianza'];document.querySelectorAll('.c').forEach(c=>{{const id=c.querySelector('.id').value;
const j=c.querySelector('input[type=radio]:checked');const q=c.querySelector('select').value;r.push(id+','+(j?j.value:'')+','+q)}});
const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([r.join('\n')]));a.download='c2_respuestas.csv';a.click()}}</script>'''
    (SALIDA / 'ciego.html').write_text(html, encoding='utf-8')
    print(len(items), 'paneles')


if __name__ == '__main__':
    main()
