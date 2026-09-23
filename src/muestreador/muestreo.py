"""Muestreador de poses: perturba el eje del corredor ya medido. Implementa la preinscripcion.

QUE HACE, EN UNA FRASE
----------------------
Toma el eje del corredor medido por caso en `e9ts_corredor.csv` (centro `c`, direccion `u`) y le aplica
una perturbacion aleatoria **declarada de antemano**, produciendo poses 3D cuyo grado de brecha mide
despues `sap.evaluar_pose`.

DE DONDE SALEN LOS PARAMETROS, Y POR QUE IMPORTA
------------------------------------------------
D-O2.1 (decision del 2026-09-22) prohibe que los parametros salgan de `zwingmann2009navigated` o se
ajusten mirando el Wasserstein-1: si salieran de ahi, la comparacion posterior seria circular y SAP
dejaria de validar nada. Aqui **toda la escala viene de una sola constante independiente**: la holgura
cortical de **5 mm** de `kaiser2014dysmorphism`, que `00-tesis.md` ya adopta como margen operativo del
marco de referencia. La regla que la convierte en dispersion —"5 mm es 2 sigma"— es **convencion propia
declarada**, no un dato medido, y esta escrita como tal en la preinscripcion.

- Desviacion lateral del centro: `sigma_t = 5 / 2 = 2.5 mm`.
- Desviacion angular: `sigma_a = atan(5 / (L/2)) / 2`, con `L` la longitud del corredor **de ese caso**
  (`L_TS_mejor_mm`). Es decir: la misma holgura de 5 mm, expresada como angulo que la produce en la
  punta. Depende del caso y no introduce ninguna constante nueva.

Ninguno de los dos numeros se ha elegido mirando un resultado. Si alguno cambiara despues de ver el
Wasserstein-1, deja de ser preinscripcion y hay que declararlo como desviacion.

LO QUE ESTE MODULO NO HACE
--------------------------
No calibra, no ajusta y no mira los grados que produce. Genera poses y se detiene.
"""
from __future__ import annotations

import hashlib

import numpy as np

__all__ = ['HOLGURA_KAISER_MM', 'FACTOR_SIGMA', 'TRUNCAMIENTO_SIGMA', 'SEMILLA',
           'rng_de_caso', 'sigma_angular_rad', 'base_perpendicular', 'muestrear_poses']

# Unica constante de escala, de `kaiser2014dysmorphism`, ya adoptada en `00-tesis.md`.
HOLGURA_KAISER_MM = 5.0
# Convencion declarada: la holgura es 2 sigma. No es un dato medido.
FACTOR_SIGMA = 2.0
# Truncamiento de la magnitud, para que la cola no genere poses absurdas que dominen la distribucion.
TRUNCAMIENTO_SIGMA = 3.0
# Semilla fija: la corrida es reproducible y no se re-tira hasta que salga bonita.
SEMILLA = 20260922


def rng_de_caso(caso: str, semilla: int = SEMILLA) -> np.random.Generator:
    """Generador propio de cada caso, derivado de la semilla global y del nombre del caso.

    POR QUE NO UN GENERADOR GLOBAL QUE AVANCE CASO A CASO
    -----------------------------------------------------
    La cohorte de sensibilidad (49 casos, grupo 3) es un **subconjunto** de la primaria (72 casos,
    grupos 2 y 3). Con un generador global, el mismo paciente recibiria poses distintas en las dos
    corridas, porque le tocaria otro tramo de la secuencia. La diferencia entre las dos cifras mezclaria
    entonces **efecto de cohorte con ruido de muestreo**, y no habria forma de separarlos.

    Derivando la semilla del nombre del caso, cada paciente recibe **exactamente las mismas poses** en
    cualquier corrida que lo incluya, y la comparacion 72 frente a 49 aisla el efecto de cohorte. El
    hash es `blake2b` y no `hash()`, que en Python varia entre procesos.
    """
    h = hashlib.blake2b(caso.encode('utf-8'), digest_size=8).digest()
    return np.random.default_rng([int(semilla), int.from_bytes(h, 'big')])


def sigma_angular_rad(longitud_corredor_mm: float) -> float:
    """Dispersion angular que produce la holgura de Kaiser en la punta del corredor de ESE caso."""
    semilongitud = float(longitud_corredor_mm) / 2.0
    if not np.isfinite(semilongitud) or semilongitud <= 0:
        raise ValueError(f'longitud de corredor no utilizable: {longitud_corredor_mm}')
    return float(np.arctan(HOLGURA_KAISER_MM / semilongitud) / FACTOR_SIGMA)


def base_perpendicular(u: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Dos vectores unitarios perpendiculares a `u` (mismo criterio que `e9_corredor`)."""
    u = np.asarray(u, dtype=float)
    a = np.array([0.0, 0.0, 1.0]) if abs(u[2]) < 0.9 else np.array([0.0, 1.0, 0.0])
    e1 = np.cross(u, a)
    e1 /= np.linalg.norm(e1)
    return e1, np.cross(u, e1)


def _magnitud(rng: np.random.Generator, sigma: float, n: int) -> np.ndarray:
    """Media normal truncada a `TRUNCAMIENTO_SIGMA`, por rechazo. Magnitud >= 0."""
    out = np.abs(rng.normal(0.0, sigma, size=n))
    tope = TRUNCAMIENTO_SIGMA * sigma
    malos = out > tope
    while malos.any():
        out[malos] = np.abs(rng.normal(0.0, sigma, size=int(malos.sum())))
        malos = out > tope
    return out


def muestrear_poses(c: np.ndarray, u: np.ndarray, longitud_corredor_mm: float, n: int,
                    rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """`n` poses perturbadas alrededor de `(c, u)`. Devuelve `(centros, direcciones)`.

    Perturbacion, con direccion **isotropa** en el plano perpendicular al eje y magnitud media-normal:

    1. desplazamiento del centro de magnitud `~ |N(0, sigma_t)|` en una direccion uniforme de ese plano;
    2. inclinacion del eje de magnitud `~ |N(0, sigma_a)|` alrededor de un eje uniforme de ese plano.

    Isotropa a proposito: no se privilegia ninguna direccion anatomica de error. Privilegiar una
    (anterior, craneal) exigiria un dato de direccionalidad clinica que esta tesis no tiene, y meterlo
    a ojo seria el mismo pecado que calibrar contra Zwingmann.
    """
    c = np.asarray(c, dtype=float)
    u = np.asarray(u, dtype=float)
    u = u / np.linalg.norm(u)
    e1, e2 = base_perpendicular(u)

    sigma_t = HOLGURA_KAISER_MM / FACTOR_SIGMA
    sigma_a = sigma_angular_rad(longitud_corredor_mm)

    fi_t = rng.uniform(0.0, 2 * np.pi, size=n)
    dir_t = np.cos(fi_t)[:, None] * e1[None, :] + np.sin(fi_t)[:, None] * e2[None, :]
    centros = c[None, :] + _magnitud(rng, sigma_t, n)[:, None] * dir_t

    fi_a = rng.uniform(0.0, 2 * np.pi, size=n)
    dir_a = np.cos(fi_a)[:, None] * e1[None, :] + np.sin(fi_a)[:, None] * e2[None, :]
    ang = _magnitud(rng, sigma_a, n)
    direcciones = np.cos(ang)[:, None] * u[None, :] + np.sin(ang)[:, None] * dir_a
    direcciones /= np.linalg.norm(direcciones, axis=1, keepdims=True)
    return centros, direcciones
