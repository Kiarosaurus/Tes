"""Termino auxiliar de AMPLITUD ANGULAR para la prueba minima de B (docs/01-decisiones.md 2026-11-20 (3), punto 7).

POST-HOC y EXPLORATORIO. No se importa salvo que `entrenar.py` reciba `--ang-lambda`: sin esa bandera el
entrenamiento es identico al de run04.

Idea: la perdida MSE promedia y suaviza; un artefacto real tiene estructura angular (rayas) que el MSE tiende a
apagar. Este termino compara, por imagen, la AMPLITUD de la modulacion angular de `x0` predicho con la de `x0`
verdadero, en anillos por distancia a `M` (2-11 px) y K sectores (K = 48 en la prueba), solo dentro de `G`, solo para `t < tmax`
(donde `x0` predicho es fiable):

    A = sqrt(media de (media por sector del residuo respecto al anillo)^2)   por canal
    L_ang = media sobre canales de (A_pred / (A_verdad + EPS_A) - 1)^2   (cociente acotado a 5)

Es una aproximacion en pixeles (no en mm) de la metrica C4 v2 (c4_anisotropia.py): anillos por distancia a `M`,
sectores respecto al centroide de `M`; los residuos se agrupan por sector (todos los anillos). No es la metrica de evaluacion; la evaluacion se hace con C4 sobre HU.
"""
from __future__ import annotations

import numpy as np
import torch
from scipy import ndimage as ndi

R_LO, R_HI = 2, 11      # px
EPS_A = 0.02            # en unidades codificadas [-1, 1]
MIN_PIX_BIN = 3
RATIO_MAX = 5.0


def claves(M: torch.Tensor, g: torch.Tensor, K: int = 24) -> torch.Tensor:
    """(B, H, W) long con `anillo * K + sector`, o -1 donde el pixel no cuenta. `M`, `g` (B, 1, H, W) en {0, 1}."""
    mm = (M[:, 0].detach().cpu().numpy() > 0.5)
    gg = (g[:, 0].detach().cpu().numpy() > 0.5)
    B, H, W = mm.shape
    out = np.full((B, H, W), -1, dtype=np.int64)
    yy, xx = np.indices((H, W))
    for b in range(B):
        if not mm[b].any():
            continue
        d = ndi.distance_transform_edt(~mm[b])
        cy, cx = ndi.center_of_mass(mm[b])
        th = np.arctan2(yy - cy, xx - cx)
        sec = np.minimum(((th + np.pi) / (2 * np.pi) * K).astype(np.int64), K - 1)
        ring = np.floor(d).astype(np.int64) - R_LO
        ok = gg[b] & ~mm[b] & (d >= R_LO) & (d < R_HI)
        out[b][ok] = (ring * K + sec)[ok]
    return torch.from_numpy(out).to(M.device)


def amplitud(X: torch.Tensor, clave: torch.Tensor, K: int = 24) -> tuple[torch.Tensor, torch.Tensor]:
    """Amplitud angular por imagen y canal: (B, C) y `valido` (B,) bool.

    Igual que la metrica C4 v2: se resta la media de cada anillo y los residuos se agrupan por SECTOR (agrupando todos
    los anillos), de modo que cada sector tiene ~N/K pixeles aun con K = 48.
    """
    B, C = X.shape[:2]
    R = R_HI - R_LO
    amp = X.new_zeros((B, C))
    valido = torch.zeros(B, dtype=torch.bool, device=X.device)
    for b in range(B):
        k = clave[b]
        m = k >= 0
        if int(m.sum()) < K * MIN_PIX_BIN:
            continue
        kk = k[m]
        v = X[b][:, m]                                           # (C, n)
        ring, sec = kk // K, kk % K
        rs = X.new_zeros((C, R)).index_add_(1, ring, v)
        rc = torch.bincount(ring, minlength=R).to(X.dtype)
        d = v - (rs / rc.clamp(min=1))[:, ring]                  # residuo respecto al anillo
        ss = X.new_zeros((C, K)).index_add_(1, sec, d)
        sc = torch.bincount(sec, minlength=K).to(X.dtype)
        w = (sc >= MIN_PIX_BIN).to(X.dtype)[None]
        if float(w.sum()) < K // 2:
            continue
        amp[b] = torch.sqrt((((ss / sc.clamp(min=1)) ** 2) * w).sum(1) / w.sum().clamp(min=1) + 1e-8)
        valido[b] = True
    return amp, valido


def perdida_amplitud(x0_pred: torch.Tensor, x0: torch.Tensor, clave: torch.Tensor, t: torch.Tensor,
                     tmax: int, K: int = 24) -> torch.Tensor:
    """Media por imagen de L_ang, solo con `t < tmax` y anillo valido; dividida entre el tamano del lote."""
    Ap, vp = amplitud(x0_pred.clamp(-1.0, 1.0), clave, K)
    with torch.no_grad():
        At, vt = amplitud(x0, clave, K)
    ratio = (Ap / (At + EPS_A)).clamp(max=RATIO_MAX)
    li = ((ratio - 1.0) ** 2).mean(1)
    cuenta = (vp & vt & (t < tmax)).to(li.dtype)
    return (li * cuenta).sum() / x0.shape[0]
