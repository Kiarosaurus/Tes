"""U-Net de difusion en el ESPACIO DE LA IMAGEN, condicionada por concatenacion (Diseno A).

QUE ES Y QUE NO ES
------------------
Es la red del Objetivo 3 tras el No-Go de P1 (#91): sin autoencoder, sin ControlNet y sin base
preentrenada. Todo lo de este archivo es `[SUPUESTO]` de `diseno_A.md` seccion 5 (U-Net tipo
DDPM/ADM, float32), no una decision de la tesis.

ENTRADA (11 canales, seccion 4 de `diseno_A.md`)
------------------------------------------------
- 3 canales: el corte central **con ruido** (`x_t`), en sus 3 ventanas (LW asinh, MW, SW) de
  `pub+asinh`, multiplicado por `G` (fuera de `G` vale 0).
- 6 canales de contexto: los 2 cortes axiales vecinos x 3 ventanas, con la region `G` borrada.
- 2 canales de mascara: `M` (metal) y `G` (metal mas banda).
El ensamblado esta en `difusion.perdida` y `difusion.muestrea_ddim` (`cat([x_t, cond])`).
Se genera **solo el corte central**, en sus 3 ventanas -> 3 canales de salida (el objetivo `v`).

POR QUE SIN BASE PREENTRENADA
-----------------------------
No existe una base preentrenada en pixeles de CT que congelar; esa es justamente la razon por la que
#74 se cierra por reemplazo (`diseno_A.md` seccion 1). Entrenar desde cero es una consecuencia
declarada del No-Go, no una preferencia.
"""
from __future__ import annotations

import math

import torch
from torch import nn

CANALES_ENTRADA = 11
CANALES_SALIDA = 3


def embedding_paso(t: torch.Tensor, dim: int) -> torch.Tensor:
    """Embedding sinusoidal del paso de ruido, como en DDPM."""
    mitad = dim // 2
    frec = torch.exp(-math.log(10_000.0) * torch.arange(mitad, device=t.device) / (mitad - 1))
    ang = t.float()[:, None] * frec[None, :]
    return torch.cat([torch.sin(ang), torch.cos(ang)], dim=1)


class Bloque(nn.Module):
    """Bloque residual con GroupNorm, SiLU y condicionamiento aditivo por el paso."""

    def __init__(self, dentro: int, fuera: int, dim_t: int, grupos: int = 8) -> None:
        super().__init__()
        self.norm1 = nn.GroupNorm(min(grupos, dentro), dentro)
        self.conv1 = nn.Conv2d(dentro, fuera, 3, padding=1)
        self.proy_t = nn.Linear(dim_t, fuera)
        self.norm2 = nn.GroupNorm(min(grupos, fuera), fuera)
        self.conv2 = nn.Conv2d(fuera, fuera, 3, padding=1)
        self.salto = nn.Conv2d(dentro, fuera, 1) if dentro != fuera else nn.Identity()
        self.act = nn.SiLU()

    def forward(self, x: torch.Tensor, emb: torch.Tensor) -> torch.Tensor:
        h = self.conv1(self.act(self.norm1(x)))
        h = h + self.proy_t(self.act(emb))[:, :, None, None]
        h = self.conv2(self.act(self.norm2(h)))
        return h + self.salto(x)


class Atencion(nn.Module):
    """Auto-atencion espacial en la resolucion mas baja (donde el coste es tolerable)."""

    def __init__(self, canales: int, grupos: int = 8) -> None:
        super().__init__()
        self.norm = nn.GroupNorm(min(grupos, canales), canales)
        self.qkv = nn.Conv2d(canales, canales * 3, 1)
        self.salida = nn.Conv2d(canales, canales, 1)
        self.canales = canales

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        b, c, h, w = x.shape
        q, k, v = self.qkv(self.norm(x)).reshape(b, 3, c, h * w).unbind(1)
        att = torch.softmax(q.transpose(1, 2) @ k / math.sqrt(c), dim=-1)
        return x + self.salida((v @ att.transpose(1, 2)).reshape(b, c, h, w))


class UNetDifusion(nn.Module):
    """U-Net de 4 escalas. `base=64` es el punto de partida; el ancho real lo fija la prueba corta.

    `forward` predice el objetivo de difusion (ruido o `v`, segun `difusion.py`) para el corte
    central, en las 3 ventanas.
    """

    def __init__(self, base: int = 64, mult: tuple[int, ...] = (1, 2, 4, 8),
                 entrada: int = CANALES_ENTRADA, salida: int = CANALES_SALIDA) -> None:
        super().__init__()
        dim_t = base * 4
        self.tiempo = nn.Sequential(nn.Linear(base, dim_t), nn.SiLU(), nn.Linear(dim_t, dim_t))
        self.base = base
        self.entrada = nn.Conv2d(entrada, base, 3, padding=1)

        anchos = [base * m for m in mult]
        self.bajada = nn.ModuleList()
        self.reduce = nn.ModuleList()
        prev = base
        for i, an in enumerate(anchos):
            self.bajada.append(Bloque(prev, an, dim_t))
            self.reduce.append(nn.Conv2d(an, an, 3, stride=2, padding=1)
                               if i < len(anchos) - 1 else nn.Identity())
            prev = an

        self.medio1 = Bloque(prev, prev, dim_t)
        self.atencion = Atencion(prev)
        self.medio2 = Bloque(prev, prev, dim_t)

        self.subida = nn.ModuleList()
        self.amplia = nn.ModuleList()
        for i, an in enumerate(reversed(anchos)):
            self.amplia.append(nn.Upsample(scale_factor=2, mode='nearest')
                               if i > 0 else nn.Identity())
            self.subida.append(Bloque(prev + an, an, dim_t))
            prev = an

        self.salida = nn.Sequential(nn.GroupNorm(8, prev), nn.SiLU(),
                                    nn.Conv2d(prev, salida, 3, padding=1))
        nn.init.zeros_(self.salida[-1].weight)
        nn.init.zeros_(self.salida[-1].bias)

    def forward(self, x: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        emb = self.tiempo(embedding_paso(t, self.base))
        h = self.entrada(x)
        saltos = []
        for bloque, reduce in zip(self.bajada, self.reduce):
            h = bloque(h, emb)
            saltos.append(h)
            h = reduce(h)
        h = self.medio2(self.atencion(self.medio1(h, emb)), emb)
        for amplia, bloque, salto in zip(self.amplia, self.subida, reversed(saltos)):
            h = amplia(h)
            if h.shape[-2:] != salto.shape[-2:]:  # lados impares tras la reduccion
                h = torch.nn.functional.interpolate(h, size=salto.shape[-2:], mode='nearest')
            h = bloque(torch.cat([h, salto], dim=1), emb)
        return self.salida(h)

    def n_parametros(self) -> int:
        return sum(p.numel() for p in self.parameters())
