"""Duplicados PARCIALES (implicancia #20): volumenes que comparten cortes axiales identicos.

`Grupo duplicado` de `revision.csv` usa SHA256 sobre forma + voxeles: solo detecta copias
EXACTAS. Un volumen que es otro truncado en z (mismo estudio, distinto numero de cortes)
tiene otro hash y pasa como contenido unico. Este script hashea cada corte axial (blake2b
sobre los bytes int16) y reporta los pares que comparten cortes no triviales (se descartan
cortes constantes, p. ej. relleno de FOV).

Solo lee `data/`. Escribe `duplicados_parciales.csv`.
"""
from __future__ import annotations

import csv
import hashlib
from collections import defaultdict
from pathlib import Path

import nibabel as nib
import numpy as np


def main() -> None:
    """Hashea cortes de los 178 CT y lista pares con cortes compartidos."""
    root = Path(__file__).resolve().parents[2]
    paths = sorted((root / 'data').rglob('*_data.nii*'))
    dueno: dict[bytes, set[str]] = defaultdict(set)
    n_cortes: dict[str, int] = {}
    for i, p in enumerate(paths):
        caso = p.name.split('.nii')[0]
        img = nib.load(p)
        arr = np.asanyarray(img.dataobj)
        n_cortes[caso] = arr.shape[2]
        for k in range(arr.shape[2]):
            sl = np.ascontiguousarray(arr[:, :, k])
            if sl.min() == sl.max():
                continue
            h = hashlib.blake2b(str(sl.dtype).encode() + str(sl.shape).encode()
                                + sl.tobytes(), digest_size=16).digest()
            dueno[h].add(caso)
        del arr
        print(f'{i + 1}/{len(paths)} {caso}', flush=True)
    pares: dict[tuple[str, str], int] = defaultdict(int)
    for casos in dueno.values():
        if len(casos) > 1:
            cs = sorted(casos)
            for a in range(len(cs)):
                for b in range(a + 1, len(cs)):
                    pares[(cs[a], cs[b])] += 1
    out = Path(__file__).with_name('duplicados_parciales.csv')
    with out.open('w', encoding='utf-8', newline='') as h:
        w = csv.writer(h)
        w.writerow(['Caso A', 'Cortes A', 'Caso B', 'Cortes B', 'Cortes identicos compartidos'])
        for (a, b), n in sorted(pares.items(), key=lambda t: -t[1]):
            w.writerow([a, n_cortes[a], b, n_cortes[b], n])
            print(a, n_cortes[a], b, n_cortes[b], n)
    print(f'Escrito {out}.')


if __name__ == '__main__':
    main()
