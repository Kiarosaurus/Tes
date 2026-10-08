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
- `regla()`            `u` -> HU sin usar la verdad (canal mas estrecho no saturado). v1, congelada.
- `regla_suave()`      v2 del Objetivo 3 (#152): mezcla con LW como ancla. Nueva aqui, no viene del Objetivo 1:
                       solo la usa el Objetivo 3 y el Objetivo 1 no la conoce.
- `BONE_HU`, `METAL_HU`, `EPS`  umbrales, con el mismo valor que en los experimentos.

La eleccion de `pub+asinh` es un `[SUPUESTO]` de `diseno_A.md`. La lectura del Objetivo 3 SI esta decidida:
`regla_suave` con `DELTA_OBJ3 = 0.05` (`docs/01-decisiones.md`, entrada 2026-10-07).
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
# Rampa de `regla_suave` decidida para el Objetivo 3 (01-decisiones.md, 2026-10-07; #152, adenda 5).
# `decodifica_bloque` sigue en v1 por omision para reproducir lo ya corrido: pasar este valor.
DELTA_OBJ3 = 0.05

__all__ = ['BONE_HU', 'METAL_HU', 'EPS', 'CONFIG_DISENO_A', 'DELTA_OBJ3', 'configuraciones', 'regla',
           'canales_diseno_a', 'codifica_bloque', 'decodifica_bloque', 'peso_borde', 'regla_suave',
           'verificar']


def canales_diseno_a() -> dict[str, tuple]:
    """Los canales de `pub+asinh`: LW asinh [-1000, 20000], MW y SW lineales."""
    return configuraciones()[CONFIG_DISENO_A]


def codifica_bloque(hu: np.ndarray, canales: dict[str, tuple] | None = None) -> np.ndarray:
    """HU -> `u` en [0, 1], apilado como `(canal, ...)` en el orden LW, MW, SW.

    El orden es fijo y explicito porque `regla()` depende de el: LW es el canal ancho de respaldo.
    """
    canales = canales_diseno_a() if canales is None else canales
    return np.stack([canales[n][0](hu) for n in ('LW', 'MW', 'SW')], axis=0)


def peso_borde(u: np.ndarray, delta: float) -> np.ndarray:
    """Confianza en un canal estrecho segun su distancia al borde: 0 hasta `EPS`, 1 desde `delta`.

    Rampa lineal entre `EPS` y `delta` en la distancia `min(u, 1 - u)`. Con `delta = EPS` es el
    escalon de la `regla` v1.
    """
    d = np.minimum(u, 1.0 - u)
    if delta <= EPS:
        return (d >= EPS).astype(np.float64)
    return np.clip((d - EPS) / (delta - EPS), 0.0, 1.0)


def regla_suave(us: dict[str, np.ndarray], canales: dict, delta: float) -> np.ndarray:
    """`regla` v2 del Objetivo 3 (#152): mezcla suave con LW como ancla.

    Parte de LW y refina primero con MW y luego con SW, cada uno pesado por `peso_borde`. Un canal
    estrecho casi saturado (p.ej. `u = 0.989`) ya no sustituye a LW por su techo: pesa poco. Con
    codificacion exacta todos los canales no saturados dan el mismo HU y la mezcla lo conserva, asi que
    la identidad de `verificar()` no depende de `delta`. **No toca la `regla` del Objetivo 1.**
    """
    hu = np.asarray(canales['LW'][1](us['LW']), dtype=np.float64)
    for nombre in ('MW', 'SW'):
        w = peso_borde(us[nombre], delta)
        hu = w * np.asarray(canales[nombre][1](us[nombre]), dtype=np.float64) + (1.0 - w) * hu
    return hu


def decodifica_bloque(u: np.ndarray, canales: dict[str, tuple] | None = None,
                      delta: float | None = None) -> np.ndarray:
    """`u` apilado (canal, ...) -> HU sin usar la verdad.

    `delta=None` aplica la `regla` congelada de P1 (v1, por omision: reproduce todo lo ya corrido).
    Un `delta` aplica `regla_suave` (v2, #152).
    """
    canales = canales_diseno_a() if canales is None else canales
    us = {n: u[i] for i, n in enumerate(('LW', 'MW', 'SW'))}
    return regla(us, canales) if delta is None else regla_suave(us, canales, delta)


def verificar(n: int = 100_000, semilla: int = 0, tol: float = 1e-6,
              delta: float | None = None) -> dict[str, float]:
    """Control: ida y vuelta sin modelo debe devolver los HU de entrada dentro de `tol`.

    Es el analogo del control de identidad de E6b/P1, sobre valores sinteticos que cubren el rango
    util (aire, tejido, hueso y metal). **Lanza** `AssertionError` si no cierra: si esto falla, nada
    de lo que produzca el sintetizador (renderizador) es comparable con las cifras del Objetivo 1.
    """
    rng = np.random.default_rng(semilla)
    hu = np.concatenate([
        rng.uniform(-1000.0, 3000.0, n // 2),
        rng.uniform(3000.0, 20000.0, n // 4),
        np.array([-1000.0, 0.0, BONE_HU, 1000.0, METAL_HU, 20000.0]),
        rng.uniform(-1000.0, 20000.0, n - n // 2 - n // 4 - 6),
    ])
    vuelta = decodifica_bloque(codifica_bloque(hu), delta=delta)
    err = np.abs(vuelta - hu)
    peor = float(err.max())
    assert peor <= tol, f'identidad multi-ventana rota: peor error {peor:.6g} HU > {tol:g}'
    return {'n': float(hu.size), 'mae': float(err.mean()), 'peor': peor}


if __name__ == '__main__':
    print(verificar())
