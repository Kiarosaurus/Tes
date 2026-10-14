"""Version 2, opcion B — canal de condicion `T`: plantilla analitica aproximada de endurecimiento del haz.

`T = -FBP[ h(lambda * R(M)) ]`, `h(u) = ln(sinh u / u)`, con `R` la Radon paralela de la mascara de metal del parche
(longitudes en mm) y FBP con filtro rampa (`park2017characterization` Ec. 1.6/2.10; `park2016MAR` Ec. 15;
`hyung2017ml` Ec. 15 sin `c chi`). Es la MISMA definicion que `experiments/objetivo3/b_piloto_plantilla.py`, que paso la
compuerta el 2026-10-13 (`experiments/objetivo3/b_piloto/b_resumen.md`); `prueba_igual_al_piloto` lo comprueba.

- `LAMBDA_T` = lambda0 del piloto (regla sin HU: 1 / mediana de la longitud maxima de metal, 11.80 mm). No se calibra.
- El parche (256 px) contiene el corte entero del componente, asi que `T` sobre el parche es `T` sobre el corte
  completo restringida al parche (la Radon de `M` no depende del fondo).
- Normalizacion compartida entre entrenamiento e inferencia: `T / escala`, recortado a +-`TOPE`, con `escala` = p99 de
  |T| FUERA de `M` en parches de entrenamiento (`v2_b_cache_T.py`), guardada en `escala.json` y en el checkpoint.
"""
from __future__ import annotations

import numpy as np

LAMBDA_T = 1.0 / 11.80   # por mm; = 0.0847 (b_resumen.md, lambda0)
N_ANG = 360
TOPE = 3.0


def h(u: np.ndarray) -> np.ndarray:
    """ln(sinh u / u), estable: 0 en u = 0 y forma asintotica para u grande."""
    u = np.abs(np.asarray(u, dtype=np.float64))
    out = np.zeros_like(u)
    chico = (u > 0) & (u < 1e-4)
    out[chico] = u[chico] ** 2 / 6.0
    med = (u >= 1e-4) & (u < 20)
    out[med] = np.log(np.sinh(u[med]) / u[med])
    gr = u >= 20
    out[gr] = u[gr] - np.log(2.0 * u[gr])
    return out


def plantilla(mascara: np.ndarray, pix_mm: float, lam: float = LAMBDA_T, n_ang: int = N_ANG) -> np.ndarray:
    """T cruda (sin normalizar) en la grilla de `mascara`. Sin metal, T = 0."""
    if not mascara.any():
        return np.zeros(mascara.shape, dtype=np.float32)
    from skimage.transform import iradon, radon   # perezoso: solo hace falta donde se calcula T
    # iradon devuelve una imagen cuadrada: un parche no cuadrado (borde del corte) se rellena con ceros (sin metal,
    # no cambia R(M)) y se recorta despues
    alto, ancho = mascara.shape
    lado = max(alto, ancho)
    m = np.zeros((lado, lado), dtype=np.float64)
    m[:alto, :ancho] = mascara
    theta = np.linspace(0.0, 180.0, n_ang, endpoint=False)
    L = radon(m, theta=theta, circle=False) * pix_mm
    T = -iradon(h(lam * L), theta=theta, filter_name='ramp', circle=False, output_size=lado)
    return T[:alto, :ancho].astype(np.float32)


def normaliza(T: np.ndarray, escala: float) -> np.ndarray:
    """Canal de entrada: T / escala recortado a +-TOPE."""
    return np.clip(T / escala, -TOPE, TOPE).astype(np.float32)


def pix_plano(zooms: np.ndarray, eje: int) -> float:
    """Espaciado en el plano axial (media de los dos ejes que no son `eje`)."""
    z = [float(zooms[i]) for i in range(3) if i != eje]
    return 0.5 * (z[0] + z[1])


def prueba_igual_al_piloto() -> float:
    """Diferencia maxima frente a `b_piloto_plantilla.plantilla` en un estadio (debe ser ~0)."""
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'experiments' / 'objetivo3'))
    import b_piloto_plantilla as bp
    yy, xx = (np.mgrid[:128, :128] - 64 + 0.5) * 0.8
    m = ((np.abs(xx) <= 20) & (np.abs(yy) <= 3)) | ((np.abs(xx) - 20) ** 2 + yy ** 2 <= 9)
    return float(np.abs(plantilla(m, 0.8) - bp.plantilla(m, 0.8, LAMBDA_T)).max())
