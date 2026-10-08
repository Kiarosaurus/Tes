"""Estadisticos del cotejo de checkpoint, comunes a lo real y a lo sintetico (01-decisiones.md 2026-10-07 (2)).

Una sola implementacion para los dos lados: #150 nacio de que el perfil real (`a12`) y el sintetico
(`a15`) se calculaban distinto y no eran comparables.

- **Perfil radial:** distancia 2D a `M` en el plano del corte, cascaras de 0.5 mm de 0 a 12 mm. En cada
  cascara, mediana y p95 de HU expresados como **elevacion** sobre la mediana del anillo de 12-15 mm del
  mismo corte. Agregacion: corte -> (semilla) -> paciente o componente -> entre ellos.
- **Histograma dentro de `M`:** p50, p75 y p95 sobre los voxeles > 2500 HU. La fraccion > 2500 es solo
  control: en lo real la mascara se define con ese umbral y vale 1 por construccion.
"""
from __future__ import annotations

import warnings

import numpy as np
from scipy import ndimage as ndi

METAL_HU = 2500.0
PASO_MM = 0.5
R_MAX_MM = 12.0
ANILLO_MM = (12.0, 15.0)
MIN_VOX = 10

__all__ = ['METAL_HU', 'PASO_MM', 'R_MAX_MM', 'ANILLO_MM', 'bordes', 'perfil_corte', 'agrega',
           'histograma_m']


def bordes(paso: float = PASO_MM, r_max: float = R_MAX_MM) -> np.ndarray:
    """Bordes de las cascaras, de 0 a `r_max` mm."""
    return np.round(np.arange(0.0, r_max + paso / 2, paso), 4)


def perfil_corte(hu: np.ndarray, m: np.ndarray, esp2d, excluir: np.ndarray | None = None,
                 paso: float = PASO_MM, r_max: float = R_MAX_MM,
                 anillo: tuple[float, float] = ANILLO_MM) -> np.ndarray:
    """Elevacion de la mediana y del p95 por cascara en un corte; NaN donde hay menos de `MIN_VOX`.

    `excluir` marca voxeles que no entran en ninguna cascara (p. ej. metal de otro componente).
    Devuelve un arreglo (n_cascaras, 2): columna 0 = elevacion p50, columna 1 = elevacion p95.
    """
    b = bordes(paso, r_max)
    out = np.full((len(b) - 1, 2), np.nan)
    if not m.any():
        return out
    dist = ndi.distance_transform_edt(~m, sampling=esp2d)
    valido = ~m if excluir is None else (~m & ~excluir)
    ref = valido & (dist > anillo[0]) & (dist <= anillo[1])
    if ref.sum() < MIN_VOX:
        return out
    nivel = float(np.median(hu[ref]))
    for i in range(len(b) - 1):
        sel = valido & (dist > b[i]) & (dist <= b[i + 1])
        if sel.sum() < MIN_VOX:
            continue
        v = hu[sel]
        out[i, 0] = float(np.median(v)) - nivel
        out[i, 1] = float(np.percentile(v, 95)) - nivel
    return out


def agrega(perfiles: list[np.ndarray]) -> np.ndarray:
    """Mediana elemento a elemento, ignorando NaN (corte -> semilla -> paciente)."""
    if not perfiles:
        raise ValueError('sin perfiles que agregar')
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', RuntimeWarning)   # cascara vacia en todos -> NaN, es lo esperado
        return np.nanmedian(np.stack(perfiles), axis=0)


def histograma_m(valores: np.ndarray) -> dict:
    """p50/p75/p95 sobre los voxeles de `M` > 2500 HU, y la fraccion > 2500 como control."""
    v = np.asarray(valores, dtype=np.float64)
    sobre = v[v > METAL_HU]
    d = {'n_M': int(v.size), 'frac_sobre_2500': round(float((v > METAL_HU).mean()), 4) if v.size else np.nan,
         'n_sobre': int(sobre.size)}
    for q in (50, 75, 95):
        d['hu_p%d' % q] = round(float(np.percentile(sobre, q)), 1) if sobre.size else np.nan
    return d
