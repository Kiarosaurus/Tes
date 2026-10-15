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

TRAZABILIDAD EN EL RESUMEN
--------------------------
`docs/SITUACION_ACTUAL.md`, seccion 5.1, apunta a `ParchesMetal` en las filas **Dimension** y
**Entrada principal**: `__getitem__` arma los tres cortes 2.5D, sus ventanas, `M` y `G`.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

import numpy as np
import torch
from scipy import ndimage as ndi
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


def mapa_peso_anillo(metal: np.ndarray, zooms_plano: tuple[float, float],
                     anillo_mm: tuple[float, float], peso: float) -> np.ndarray:
    """Version 2, D-b: `peso` en los pixeles a `anillo_mm` (en el plano, mm) de `M`; 1 en el resto.

    Distancia euclidea en el plano al metal del componente objetivo, con el espaciado fisico del
    corte: la misma definicion de anillo que D1/D2 (`d1_alcance_rayas.py`). Si el corte no tiene
    metal del componente (parche de banda mas alla de la punta, R3), el mapa es 1 en todo el corte:
    la distancia en el plano no esta definida y no se inventa. Se multiplica por `G` en la perdida.
    """
    w = np.ones(metal.shape, dtype=np.float32)
    if not metal.any() or peso == 1.0:
        return w
    d = ndi.distance_transform_edt(~metal, sampling=zooms_plano)
    w[(d >= anillo_mm[0]) & (d <= anillo_mm[1])] = peso
    return w


def lee_componentes_tornillo(ruta: Path) -> dict[str, int]:
    """Tabla versionada de `v2_d_componentes.py`: {serie `caso_cNNN`: 1 si es tamano tornillo}."""
    with open(ruta, newline='', encoding='utf-8') as fh:
        return {f'{r["Caso"]}_c{int(r["comp"]):03d}': int(r['tornillo'])
                for r in csv.DictReader(fh)}


class ParchesMetal(Dataset):
    """Parches 2.5D: 3 cortes x 3 ventanas + `M` + `G`; objetivo, el corte central.

    Cada elemento devuelve:
    - `x0`   (3, H, W)  corte central codificado en ventanas, en [-1, 1].
    - `cond` (8, H, W)  6 canales de los vecinos con `G` borrada, mas `M` y `G`.
    - `g`    (1, H, W)  mascara de generacion en {0, 1}.
    - `w`    (1, H, W)  SOLO con `anillo_mm` (version 2, D-b): peso por distancia a `M`.

    Con `cache_T` (version 2, B) `cond` lleva un canal mas al final (9): la plantilla `T` normalizada
    (`plantilla.normaliza`, `escala_T`), precalculada por `v2_b_cache_T.py` para el corte central.
    """

    def __init__(self, cache: Path, particion: Path,
                 particiones: tuple[str, ...] = ('train',), lado: int = 256,
                 borrar_contexto: bool = False, inclusion: Path | None = None,
                 ratio_banda: float | None = None, semilla: int = 20260921,
                 anillo_mm: tuple[float, float] | None = None,
                 peso_anillo: float = 1.0, cache_T: Path | None = None,
                 escala_T: float | None = None) -> None:
        self.cache = Path(cache)
        if (cache_T is None) != (escala_T is None):
            raise ValueError('cache_T y escala_T van juntos')
        self.cache_T = Path(cache_T) if cache_T is not None else None
        self.escala_T = escala_T
        self.anillo_mm = tuple(anillo_mm) if anillo_mm is not None else None
        self.peso_anillo = float(peso_anillo)
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

    def faltan_T(self) -> list[str]:
        """Parches del indice sin `T` precalculada en `cache_T` (se calcularian al vuelo, lento)."""
        if self.cache_T is None:
            return []
        return [f'{s}_k{k:04d}' for s, k in self.indice if not (self.cache_T / f'{s}_k{k:04d}_T.npy').exists()]

    def _T(self, caso: str, k: int) -> np.ndarray:
        """T cruda del corte; si no esta en `cache_T` se calcula (misma funcion que `v2_b_cache_T.py`) y se guarda."""
        from plantilla import pix_plano, plantilla
        ruta = self.cache_T / f'{caso}_k{k:04d}_T.npy'
        if ruta.exists():
            return np.load(ruta)
        with np.load(self.cache / f'{caso}_k{k:04d}.npz') as z:
            T = plantilla(z['metal'].astype(bool), pix_plano(z['zooms'], int(z['eje'])))
        self.cache_T.mkdir(parents=True, exist_ok=True)
        np.save(ruta, T)
        return T

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
            d = {'hu': self._rellena(z['hu'], -1000.0),
                 'metal': self._rellena(z['metal'], False),
                 'g': self._rellena(z['g'], False)}
            if self.anillo_mm is not None:
                # el parche es `vol[k]` con el eje axial movido al frente (a1b): el plano conserva
                # el orden original de los otros dos ejes
                eje, zooms = int(z['eje']), [float(v) for v in z['zooms']]
                d['zooms_plano'] = tuple(zooms[i] for i in range(3) if i != eje)
            return d

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

        extra = [centro['metal'].astype(np.float32)[None], g[None]]
        if self.cache_T is not None:
            from plantilla import normaliza
            T = self._rellena(self._T(caso, k), 0.0)
            extra.append(normaliza(T, self.escala_T)[None])
        cond = np.concatenate(ctx + extra, axis=0)
        item = {'x0': torch.from_numpy(x0.astype(np.float32)),
                'cond': torch.from_numpy(cond.astype(np.float32)),
                'g': torch.from_numpy(g[None]),
                'caso': caso, 'k': k}
        if self.anillo_mm is not None:
            w = mapa_peso_anillo(centro['metal'], centro['zooms_plano'], self.anillo_mm,
                                 self.peso_anillo)
            item['w'] = torch.from_numpy(w[None])
        return item

    def pesos_sobremuestreo(self, tornillo: dict[str, int],
                            frac_objetivo: float) -> tuple[torch.Tensor, dict[str, float]]:
        """Version 2, D-a: peso por parche para que los de tamano tornillo salgan con `frac_objetivo`.

        Con `n` parches de tornillo entre `N`, peso `f = p (N - n) / ((1 - p) n)` para ellos y 1
        para el resto: la fraccion esperada de tornillos por sorteo es exactamente `p`. Si `p` es
        menor o igual que la fraccion natural `n / N` no se sobremuestrea (`f` = 1). Una serie que
        falta en la tabla aborta: la tabla tiene que cubrir el manifiesto entero.
        """
        faltan = sorted({s for s, _ in self.indice} - set(tornillo))
        if faltan:
            raise RuntimeError(f'{len(faltan)} series del manifiesto sin fila en la tabla de '
                               f'componentes (p. ej. {faltan[:3]}); regenerar v2_d_componentes')
        es = torch.tensor([float(tornillo[s]) for s, _ in self.indice])
        n, total = float(es.sum()), float(len(es))
        if n == 0:
            raise RuntimeError('ningun parche de tamano tornillo en el manifiesto')
        natural = n / total
        f = max(1.0, frac_objetivo * (total - n) / ((1.0 - frac_objetivo) * n))
        pesos = torch.where(es > 0, torch.tensor(f), torch.tensor(1.0)).double()
        series_t = {s for s, _ in self.indice if tornillo[s]}
        return pesos, {'parches_tornillo': n, 'parches': total,
                       'series_tornillo': float(len(series_t)),
                       'frac_natural': round(natural, 4),
                       'frac_objetivo': frac_objetivo, 'factor': round(f, 4)}

    def resumen(self) -> dict[str, float]:
        # `casos` son pacientes (unidad de la particion); `series` son implantes (unidad de entrenamiento).
        return {'parches': float(len(self.indice)), 'casos': float(len(self.casos)),
                'series': float(len(self.por_caso)),
                'borde': float(self.n_borde),
                'frac_borde': round(self.n_borde / len(self.indice), 4)}
