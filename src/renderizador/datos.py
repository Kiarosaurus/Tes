"""Dataset 2.5D sobre el cache de parches de A1.

DE DONDE SALEN LOS DATOS
------------------------
De `experiments/objetivo3/a1b_parches_componente.py --cache <dir>`, que escribe un `.npz` por
(componente, corte): `hu` (parche 2D, float32), `metal`, `g` (bool), `y0`, `x0`, `eje`, `zooms`.
El nombre es `{caso}_c{comp:03d}_k{corte:04d}.npz`.

**La clave de agrupacion incluye el componente** (`dataset7_..._c000`), no solo el caso. Eso es
deliberado: los vecinos 2.5D de un corte tienen que ser del **mismo implante**, no del implante
contralateral que casualmente aparece en el mismo corte. Con la unidad por componente (D2, #102) eso
sale solo, porque cada componente tiene su propia serie de cortes.

Tambien acepta el formato viejo `{caso}_k{corte:04d}.npz` de `a1_parches.py`, que quedo congelado
como evidencia de #102 y **no debe usarse para entrenar**: su `G` es multi-implante.

2.5D, Y EL CASO DE BORDE QUE HAY QUE DECLARAR
---------------------------------------------
Se piden 3 cortes contiguos y se genera el central. A1 **solo cachea cortes con metal**, asi que en
los extremos del implante el vecino no existe. Ahi se repite el corte central y se marca la fila
como `borde`. No se inventa contexto: repetir es la opcion que no introduce informacion falsa, y la
fraccion de parches en borde se reporta, porque si fuera alta el supuesto 2.5D de `diseno_A.md`
seccion 4 se debilita.

PARTICION
---------
Se filtra por caso contra `p1_particion.csv` (semilla 20260917). Es la misma particion por paciente
de P1, por la *Strict Isolation Rule* de `main.tex:111`. **Ningun corte de test entra aqui.**
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import numpy as np
import torch
from torch.utils.data import Dataset

_RAIZ = Path(__file__).resolve().parents[2]
if str(_RAIZ / 'src') not in sys.path:
    sys.path.insert(0, str(_RAIZ / 'src'))

from common.ventanas import canales_diseno_a, codifica_bloque  # noqa: E402

# `serie` = todo lo anterior a `_kNNNN`, es decir caso MAS el sufijo `_cNNN` cuando lo hay. Es la clave
# de agrupacion del 2.5D y la base del nombre de archivo, asi que tiene que incluir el componente.
PATRON = re.compile(r'^(?P<serie>.+)_k(?P<k>\d{4})\.npz$')


def lee_particion(ruta: Path, particiones: tuple[str, ...]) -> set[str]:
    """Casos de `p1_particion.csv` cuya particion esta en `particiones`."""
    import csv
    with open(ruta, newline='', encoding='utf-8') as fh:
        return {f['Caso'] for f in csv.DictReader(fh) if f['particion'] in particiones}


def caso_de(serie: str) -> str:
    """Quita el sufijo `_cNNN` para volver al caso, que es la unidad de la particion."""
    return re.sub(r'_c\d{3}$', '', serie)


def _lee_manifiesto(ruta: Path) -> set[tuple[str, int]]:
    """Parches admitidos, como {(serie, corte)}. Una fila por parche."""
    import csv
    with open(ruta, newline='', encoding='utf-8') as fh:
        return {(f'{r["Caso"]}_c{int(r["comp"]):03d}', int(r['corte']))
                for r in csv.DictReader(fh)}


class ParchesMetal(Dataset):
    """Parches 2.5D: 3 cortes x 3 ventanas + `M` + `G`; objetivo, el corte central.

    Cada elemento devuelve:
    - `x0`   (3, H, W)  corte central codificado en ventanas, en [-1, 1].
    - `cond` (8, H, W)  6 canales de los vecinos con `G` borrada, mas `M` y `G`.
    - `g`    (1, H, W)  mascara de generacion en {0, 1}.
    """

    def __init__(self, cache: Path, particion: Path,
                 particiones: tuple[str, ...] = ('train',), lado: int = 256,
                 borrar_contexto: bool = False, inclusion: Path | None = None,
                 ratio_banda: float | None = None, semilla: int = 20260921) -> None:
        self.cache = Path(cache)
        self.lado = lado
        self.borrar_contexto = borrar_contexto
        self.canales = canales_diseno_a()
        permitidos = lee_particion(Path(particion), particiones)
        # Criterio de inclusion R1-R3, PREINSCRITO el 2026-09-21 (`01-decisiones.md`).
        # `inclusion` es el MANIFIESTO: un CSV con una fila por parche que entra al entrenamiento,
        # generado por `a5_criterio_inclusion.py --manifiesto`. Es un artefacto versionado, no
        # logica que se recalcule aqui: asi el conjunto congelado es auditable y reproducible.
        # Si es None NO se filtra, y el conjunto es el crudo de A1b, que **no** es el de la decision.
        self.manifiesto = _lee_manifiesto(Path(inclusion)) if inclusion else None
        self.ratio_banda = ratio_banda
        self.semilla = semilla

        # `indice` y `por_caso` van por SERIE (caso + componente); el filtro de particion, por CASO.
        self.indice: list[tuple[str, int]] = []
        self.por_caso: dict[str, set[int]] = {}
        self.casos: set[str] = set()
        for f in sorted(self.cache.glob('*.npz')):
            m = PATRON.match(f.name)
            if m is None:
                continue
            serie, k = m.group('serie'), int(m.group('k'))
            caso = caso_de(serie)
            if caso not in permitidos:
                continue
            # el manifiesto decide que parches ENTRENAN; los vecinos 2.5D se cargan igual aunque
            # no esten en el, porque son contexto y no ejemplos.
            self.por_caso.setdefault(serie, set()).add(k)
            if self.manifiesto is not None and (serie, k) not in self.manifiesto:
                continue
            self.indice.append((serie, k))
            self.casos.add(caso)
        if not self.indice:
            raise RuntimeError(f'cache vacio para {particiones} en {self.cache}')
        self.n_borde = sum(1 for c, k in self.indice
                           if not {k - 1, k + 1} <= self.por_caso[c])

    def __len__(self) -> int:
        return len(self.indice)

    def _rellena(self, a: np.ndarray, valor: float) -> np.ndarray:
        """Rellena el parche hasta `lado` x `lado` repitiendo el valor de fondo."""
        h, w = a.shape
        if (h, w) == (self.lado, self.lado):
            return a
        out = np.full((self.lado, self.lado), valor, dtype=a.dtype)
        out[:min(h, self.lado), :min(w, self.lado)] = a[:self.lado, :self.lado]
        return out

    def _carga(self, caso: str, k: int) -> dict[str, np.ndarray]:
        with np.load(self.cache / f'{caso}_k{k:04d}.npz') as z:
            return {'hu': self._rellena(z['hu'], -1000.0),
                    'metal': self._rellena(z['metal'], False),
                    'g': self._rellena(z['g'], False)}

    def __getitem__(self, i: int) -> dict[str, torch.Tensor]:
        caso, k = self.indice[i]
        centro = self._carga(caso, k)
        vecinos = [self._carga(caso, j) if j in self.por_caso[caso] else centro
                   for j in (k - 1, k + 1)]

        g = centro['g'].astype(np.float32)
        x0 = codifica_bloque(centro['hu'], self.canales) * 2.0 - 1.0

        ctx = []
        for v in vecinos:
            hu = v['hu'].copy()
            hu[v['g']] = -1000.0  # el contexto vecino tambien lleva `G` borrada
            if self.borrar_contexto:  # brazo de sensibilidad de #96, apagado por defecto
                hu[~v['g']] = -1000.0
            ctx.append(codifica_bloque(hu, self.canales) * 2.0 - 1.0)

        cond = np.concatenate(ctx + [centro['metal'].astype(np.float32)[None], g[None]], axis=0)
        return {'x0': torch.from_numpy(x0.astype(np.float32)),
                'cond': torch.from_numpy(cond.astype(np.float32)),
                'g': torch.from_numpy(g[None]),
                'caso': caso, 'k': k}

    def resumen(self) -> dict[str, float]:
        # `casos` son pacientes (unidad de la particion); `series` son implantes (unidad de entrenamiento).
        return {'parches': float(len(self.indice)), 'casos': float(len(self.casos)),
                'series': float(len(self.por_caso)),
                'borde': float(self.n_borde),
                'frac_borde': round(self.n_borde / len(self.indice), 4)}
