"""Region de generacion `G = M union B_delta` y composicion exacta fuera de ella.

POR QUE ESTE MODULO NO REIMPLEMENTA NADA
----------------------------------------
Mismo criterio que `ventanas.py`: `M` (metal por umbral) y `B_delta` (banda euclidea 3D con el
spacing del header) ya estan implementados y controlados en `experiments/objetivo3/a1_parches.py` y
`experiments/objetivo1/p1_decodificador_sd15.py`. Se reexportan; no se copian.

QUE APORTA DE NUEVO
-------------------
`componer()`, que es la operacion que hace verdadera la promesa central del Diseno A: fuera de `G` el
resultado es el CT de origen, **voxel a voxel**. En el Diseno A eso no es un resultado medido sino una
propiedad de construccion (bloque E-A3 de `diseno_A.md`), y solo es cierta si la composicion se hace
en un unico sitio. Este es ese sitio.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

# Igual que en `ventanas.py`: primero el `sys.path` tal cual (Khipu, `~/metalsynth/qc`), y solo si falla
# se anaden las rutas del repositorio.
_RAIZ = Path(__file__).resolve().parents[2]
try:
    from a1_parches import region_generacion  # noqa: E402
except ModuleNotFoundError:
    for _sub in ('experiments/objetivo3', 'experiments/objetivo1'):
        _p = str(_RAIZ / _sub)
        if _p not in sys.path:
            sys.path.insert(0, _p)
    from a1_parches import region_generacion  # noqa: E402
from p1_decodificador_sd15 import BDELTA_MM  # noqa: E402

__all__ = ['BDELTA_MM', 'region_generacion', 'componer', 'verificar_composicion']


def componer(original: np.ndarray, generado: np.ndarray, g: np.ndarray) -> np.ndarray:
    """Devuelve `generado` dentro de `g` y `original` fuera. No modifica las entradas.

    Es la unica via por la que un HU generado puede llegar al volumen de salida.
    """
    if original.shape != generado.shape or original.shape != g.shape:
        raise ValueError(f'formas distintas: {original.shape}, {generado.shape}, {g.shape}')
    fuera = np.asarray(original)
    salida = fuera.copy()
    salida[g] = np.asarray(generado)[g]
    return salida


def verificar_composicion(original: np.ndarray, salida: np.ndarray, g: np.ndarray) -> None:
    """Control que puede fallar: fuera de `G` la salida es identica bit a bit al original.

    Se llama en cada sintesis. Si falla, la fila E-A3 de la tabla de evaluacion deja de ser
    "cero por construccion" y pasa a ser un error a investigar.
    """
    fuera = ~np.asarray(g)
    if not np.array_equal(np.asarray(salida)[fuera], np.asarray(original)[fuera]):
        n = int((np.asarray(salida)[fuera] != np.asarray(original)[fuera]).sum())
        raise RuntimeError(f'composicion cambia {n} voxeles fuera de G')
