"""Proceso de difusion: planificador, perdida enmascarada a `G` y muestreo DDIM.

DECISIONES DE ESTE ARCHIVO (todas `[SUPUESTO]` de `diseno_A.md` seccion 5)
-------------------------------------------------------------------------
- Planificador coseno (Nichol y Dhariwal), 1000 pasos de entrenamiento.
- Objetivo `v` por defecto, con `eps` disponible. `v` es mas estable cuando la senal cubre un rango
  dinamico grande, que es el caso aqui: el metal satura las ventanas estrechas.
- **La perdida se calcula SOLO dentro de `G`.** Fuera de `G` el CT se copia, asi que penalizar ahi
  gastaria capacidad en reproducir un contexto que ya se conoce. Esta es la pieza que hace que el
  Diseno A sea inpainting y no generacion libre.
- Muestreo DDIM determinista (eta = 0), 50 pasos, semilla fija.

LO QUE NO RESUELVE
------------------
El riesgo #96: en entrenamiento el contexto fuera de `G` trae el streaking del implante real, y en
sintesis el paciente limpio no. Eso no es un problema del muestreador sino de que datos entran, y
se declara en `diseno_A.md` seccion 8.1.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import torch

OBJETIVOS = ('v', 'eps')


def betas_coseno(n: int, s: float = 0.008, tope: float = 0.999) -> torch.Tensor:
    """Planificador coseno de Nichol y Dhariwal."""
    t = torch.linspace(0, n, n + 1, dtype=torch.float64) / n
    alfa = torch.cos((t + s) / (1 + s) * math.pi / 2) ** 2
    alfa = alfa / alfa[0]
    return torch.clip(1 - alfa[1:] / alfa[:-1], 0, tope).float()


@dataclass
class Difusion:
    """Planificador y operaciones de ruido. `pasos` es el numero de pasos de entrenamiento."""

    pasos: int = 1000
    objetivo: str = 'v'

    def __post_init__(self) -> None:
        if self.objetivo not in OBJETIVOS:
            raise ValueError(f'objetivo {self.objetivo!r} no esta en {OBJETIVOS}')
        self.betas = betas_coseno(self.pasos)
        self.alfas_acum = torch.cumprod(1.0 - self.betas, dim=0)

    def a(self, t: torch.Tensor, dispositivo: torch.device) -> tuple[torch.Tensor, torch.Tensor]:
        """`sqrt(alfa_acum)` y `sqrt(1 - alfa_acum)` en `t`, con forma de difusion (B,1,1,1)."""
        ac = self.alfas_acum.to(dispositivo)[t].view(-1, 1, 1, 1)
        return ac.sqrt(), (1.0 - ac).sqrt()

    def ruidoso(self, x0: torch.Tensor, t: torch.Tensor,
                ruido: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        """Devuelve `x_t` y el objetivo de regresion (`v` o `eps`) para ese `t`."""
        sa, sb = self.a(t, x0.device)
        xt = sa * x0 + sb * ruido
        objetivo = sa * ruido - sb * x0 if self.objetivo == 'v' else ruido
        return xt, objetivo

    def x0_desde(self, xt: torch.Tensor, salida: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        """Reconstruye `x0` a partir de la prediccion de la red."""
        sa, sb = self.a(t, xt.device)
        return sa * xt - sb * salida if self.objetivo == 'v' else (xt - sb * salida) / sa


def perdida(modelo, x0: torch.Tensor, cond: torch.Tensor, g: torch.Tensor,
            dif: Difusion, generador: torch.Generator | None = None) -> torch.Tensor:
    """MSE del objetivo de difusion, promediada **solo sobre los pixeles de `G`**.

    `x0`   (B, 3, H, W)  corte central verdadero, ya codificado en ventanas y en [-1, 1].
    `cond` (B, 8, H, W)  contexto: 6 canales de los dos cortes vecinos + `M` + `G`.
    `g`    (B, 1, H, W)  mascara de la region de generacion, en {0, 1}.

    El promedio se hace por imagen y luego entre imagenes, de modo que un parche con `G` pequena
    pesa lo mismo que uno con `G` grande: si no, el lote lo dominarian las protesis (riesgo 3 de
    `diseno_A.md`).
    """
    b = x0.shape[0]
    t = torch.randint(0, dif.pasos, (b,), device=x0.device, generator=generador)
    ruido = torch.randn(x0.shape, device=x0.device, generator=generador)
    xt, objetivo = dif.ruidoso(x0, t, ruido)
    xt = xt * g  # fuera de G la entrada ruidosa no aporta: el contexto limpio va en `cond`
    salida = modelo(torch.cat([xt, cond], dim=1), t)
    err = (salida - objetivo) ** 2 * g
    n = g.sum(dim=(1, 2, 3)).clamp(min=1.0)
    return (err.sum(dim=(1, 2, 3)) / (n * x0.shape[1])).mean()


@torch.no_grad()
def muestrea_ddim(modelo, cond: torch.Tensor, g: torch.Tensor, dif: Difusion,
                  pasos: int = 50, semilla: int = 0, eta: float = 0.0) -> torch.Tensor:
    """DDIM determinista. Devuelve el corte central generado, en [-1, 1], ya enmascarado a `G`.

    `semilla` se fija siempre: la variabilidad entre semillas es el insumo del margen `Delta` del
    criterio de exito (`diseno_A.md` seccion 8 bis, D4), asi que tiene que ser reproducible.
    """
    dispositivo = cond.device
    gen = torch.Generator(device=dispositivo).manual_seed(semilla)
    forma = (cond.shape[0], 3, cond.shape[2], cond.shape[3])
    x = torch.randn(forma, device=dispositivo, generator=gen) * g
    ts = torch.linspace(dif.pasos - 1, 0, pasos, dtype=torch.long, device=dispositivo)
    for i, t in enumerate(ts):
        tb = t.repeat(cond.shape[0])
        salida = modelo(torch.cat([x * g, cond], dim=1), tb)
        x0 = dif.x0_desde(x, salida, tb).clamp(-1.0, 1.0)
        if i == len(ts) - 1:
            x = x0
            break
        t_sig = ts[i + 1].repeat(cond.shape[0])
        sa_s, sb_s = dif.a(t_sig, dispositivo)
        _, sb = dif.a(tb, dispositivo)
        eps = (x - dif.a(tb, dispositivo)[0] * x0) / sb.clamp(min=1e-8)
        sigma = eta * sb_s
        x = sa_s * x0 + (sb_s ** 2 - sigma ** 2).clamp(min=0).sqrt() * eps
        if eta > 0:
            x = x + sigma * torch.randn(forma, device=dispositivo, generator=gen)
        x = x * g
    return x * g
