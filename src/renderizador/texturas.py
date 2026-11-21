"""Perdidas auxiliares de textura, perceptual-proxy y adversarial (docs/01-decisiones.md 2026-11-21 (18)). EXPLORATORIO, POST-HOC.

No se importa salvo que `entrenar.py` reciba `--aux-tex`, `--aux-per` o `--aux-adv`: sin esas banderas el entrenamiento es el de run04.

- `perdida_textura`: desviacion estandar local del componente de alta frecuencia (canales MW y SW), diferencia cuadratica de logaritmos.
- `perdida_percep`: L1 sobre una piramide laplaciana de 3 niveles. NO es la perdida perceptual de la literatura (sin red preentrenada en CT): es un proxy.
- `PatchD` y `hinge_*`: PatchGAN condicionado a `M` y `G`, con normalizacion espectral.
Todas devuelven un valor por imagen (B,) y trabajan sobre `x0` codificado en [-1, 1] con forma (B, 3, H, W).
"""
from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F


def _caja(x: torch.Tensor, k: int) -> torch.Tensor:
    return F.avg_pool2d(F.pad(x, (k // 2,) * 4, mode='reflect'), k, 1)


def alta_frecuencia(x: torch.Tensor, k: int = 5) -> torch.Tensor:
    return x - _caja(x, k)


def desv_local(h: torch.Tensor, k: int = 9) -> torch.Tensor:
    return torch.sqrt(_caja(h * h, k) + 1e-6)


def perdida_textura(x0p: torch.Tensor, x0: torch.Tensor, valido: torch.Tensor) -> torch.Tensor:
    """(B,) diferencia cuadratica de log-desviaciones estandar locales de alta frecuencia, canales MW (1) y SW (2), en `valido` (B,1,H,W)."""
    tot = x0p.new_zeros(x0p.shape[0])
    for c in (1, 2):
        sp = desv_local(alta_frecuencia(x0p[:, c:c + 1]))
        st = desv_local(alta_frecuencia(x0[:, c:c + 1]))
        d = (torch.log(sp + 1e-3) - torch.log(st + 1e-3)) ** 2
        tot = tot + (d * valido).sum((1, 2, 3)) / valido.sum((1, 2, 3)).clamp(min=1.0)
    return tot / 2.0


def _piramide(x: torch.Tensor, niveles: int = 3) -> list[torch.Tensor]:
    out, cur = [], x
    for _ in range(niveles):
        bajo = F.avg_pool2d(cur, 2)
        out.append(cur - F.interpolate(bajo, scale_factor=2, mode='bilinear', align_corners=False))
        cur = bajo
    out.append(cur)
    return out


def perdida_percep(x0p: torch.Tensor, x0: torch.Tensor, g: torch.Tensor) -> torch.Tensor:
    """(B,) L1 sobre piramide laplaciana (3 niveles + residuo), enmascarada a `g` (B,1,H,W)."""
    pp, pt = _piramide(x0p), _piramide(x0)
    pesos = (1.0, 1.0, 1.0, 0.5)
    tot = x0p.new_zeros(x0p.shape[0])
    for l, (a, b) in enumerate(zip(pp, pt)):
        m = (F.avg_pool2d(g, 2 ** l) > 0.5).to(a.dtype) if l else g
        tot = tot + pesos[l] * ((a - b).abs() * m).sum((1, 2, 3)) / (m.sum((1, 2, 3)) * a.shape[1]).clamp(min=1.0)
    return tot


class PatchD(nn.Module):
    """PatchGAN condicionado: entrada = x (3 canales) + M + G (5 canales); normalizacion espectral; salida (B,1,H/8,W/8)."""

    def __init__(self, cin: int = 5, base: int = 32) -> None:
        super().__init__()
        sn = nn.utils.spectral_norm

        def bloque(i: int, o: int) -> nn.Sequential:
            return nn.Sequential(sn(nn.Conv2d(i, o, 4, 2, 1)), nn.LeakyReLU(0.2, True))

        self.red = nn.Sequential(bloque(cin, base), bloque(base, base * 2), bloque(base * 2, base * 4),
                                 sn(nn.Conv2d(base * 4, 1, 3, 1, 1)))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.red(x)


def mascara_parche(g: torch.Tensor) -> torch.Tensor:
    return (F.avg_pool2d(g, 8) > 0.5).to(g.dtype)


def perdida_d(D: PatchD, real: torch.Tensor, falso: torch.Tensor, M: torch.Tensor, g: torch.Tensor,
              sel: torch.Tensor) -> torch.Tensor:
    """Hinge del discriminador; `sel` (B,) con 1 donde t < tmax."""
    mk = mascara_parche(g)
    dr = D(torch.cat([real, M, g], 1))
    df = D(torch.cat([falso, M, g], 1))
    s = sel.view(-1, 1, 1, 1)
    n = (mk * s).sum().clamp(min=1.0)
    return ((F.relu(1 - dr) + F.relu(1 + df)) * mk * s).sum() / n


def perdida_g_adv(D: PatchD, falso: torch.Tensor, M: torch.Tensor, g: torch.Tensor) -> torch.Tensor:
    """(B,) perdida adversarial del generador (hinge): -media de D(falso) en parches de G."""
    mk = mascara_parche(g)
    df = D(torch.cat([falso, M, g], 1))
    return -(df * mk).sum((1, 2, 3)) / mk.sum((1, 2, 3)).clamp(min=1.0)
