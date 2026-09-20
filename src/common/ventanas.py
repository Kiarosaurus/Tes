"""Codificacion multi-ventana en HU y lectura de vuelta, para el Objetivo 3 (Diseno A).

POR QUE ESTE MODULO NO REIMPLEMENTA NADA
----------------------------------------
La codificacion multi-ventana y la `regla` de lectura ya existen, ya corrieron sobre la cohorte y ya
tienen control propio: `experiments/objetivo1/e6c_techo_lw.py` (identidad 0.00 HU a float) y
`experiments/objetivo1/e6b_vae_sd15.py` (identidad frente a E6c, 873/873 en la cohorte y 165/165 en
P1). Volver a escribir esas formulas aqui crearia una **segunda** implementacion numerica que nadie
controlo, y la primera vez que las dos discrepasen en un decimal no habria forma de saber cual de las
dos produjo las cifras de la tesis.

Asi que este modulo **reexporta** la implementacion congelada y anade `verificar()`, que compara las
dos rutas sobre valores sinteticos y **lanza** si no coinciden. Los modulos de `experiments/` quedan
como estan: son evidencia de experimentos ya corridos y no se tocan.

QUE EXPONE
----------
- `configuraciones()`  las nueve configuraciones de canales (cada canal: `(codifica, decodifica)`).
- `CONFIG_DISENO_A`    la que usa el Diseno A: `pub+asinh` (seccion 4 de `diseno_A.md`, `[SUPUESTO]`).
- `codifica_bloque()`  HU -> `u` en [0, 1], un canal por plano.
- `regla()`            `u` -> HU sin usar la verdad (canal mas estrecho no saturado).
- `BONE_HU`, `METAL_HU`, `EPS`  umbrales, con el mismo valor que en los experimentos.

Nada de este archivo decide nada: la eleccion de `pub+asinh` es un `[SUPUESTO]` de `diseno_A.md`.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

# En el repositorio los modulos estan en `experiments/objetivo1/`; en Khipu, planos en `~/metalsynth/qc`
# (convencion de `KHIPU.md`). Se prueba primero el `sys.path` tal cual y solo si falla se anade la ruta
# del repositorio, para que el mismo codigo sirva en los dos sitios sin condicionales por maquina.
_OBJ1 = Path(__file__).resolve().parents[2] / 'experiments' / 'objetivo1'
try:
    from e6c_techo_lw import BONE_HU, METAL_HU, configuraciones  # noqa: E402
except ModuleNotFoundError:
    sys.path.insert(0, str(_OBJ1))
    from e6c_techo_lw import BONE_HU, METAL_HU, configuraciones  # noqa: E402
from e6b_vae_sd15 import EPS, regla  # noqa: E402

CONFIG_DISENO_A = 'pub+asinh'

__all__ = ['BONE_HU', 'METAL_HU', 'EPS', 'CONFIG_DISENO_A', 'configuraciones', 'regla',
           'canales_diseno_a', 'codifica_bloque', 'verificar']


def canales_diseno_a() -> dict[str, tuple]:
    """Los canales de `pub+asinh`: LW asinh [-1000, 20000], MW y SW lineales."""
    return configuraciones()[CONFIG_DISENO_A]


def codifica_bloque(hu: np.ndarray, canales: dict[str, tuple] | None = None) -> np.ndarray:
    """HU -> `u` en [0, 1], apilado como `(canal, ...)` en el orden LW, MW, SW.

    El orden es fijo y explicito porque `regla()` depende de el: LW es el canal ancho de respaldo.
    """
    canales = canales_diseno_a() if canales is None else canales
    return np.stack([canales[n][0](hu) for n in ('LW', 'MW', 'SW')], axis=0)


def decodifica_bloque(u: np.ndarray, canales: dict[str, tuple] | None = None) -> np.ndarray:
    """`u` apilado (canal, ...) -> HU por la `regla` de P1 (sin usar la verdad)."""
    canales = canales_diseno_a() if canales is None else canales
    us = {n: u[i] for i, n in enumerate(('LW', 'MW', 'SW'))}
    return regla(us, canales)


def verificar(n: int = 100_000, semilla: int = 0, tol: float = 1e-6) -> dict[str, float]:
    """Control: ida y vuelta sin modelo debe devolver los HU de entrada dentro de `tol`.

    Es el analogo del control de identidad de E6b/P1, sobre valores sinteticos que cubren el rango
    util (aire, tejido, hueso y metal). **Lanza** `AssertionError` si no cierra: si esto falla, nada
    de lo que produzca el renderizador es comparable con las cifras del Objetivo 1.
    """
    rng = np.random.default_rng(semilla)
    hu = np.concatenate([
        rng.uniform(-1000.0, 3000.0, n // 2),
        rng.uniform(3000.0, 20000.0, n // 4),
        np.array([-1000.0, 0.0, BONE_HU, 1000.0, METAL_HU, 20000.0]),
        rng.uniform(-1000.0, 20000.0, n - n // 2 - n // 4 - 6),
    ])
    vuelta = decodifica_bloque(codifica_bloque(hu))
    err = np.abs(vuelta - hu)
    peor = float(err.max())
    assert peor <= tol, f'identidad multi-ventana rota: peor error {peor:.6g} HU > {tol:g}'
    return {'n': float(hu.size), 'mae': float(err.mean()), 'peor': peor}


if __name__ == '__main__':
    print(verificar())
