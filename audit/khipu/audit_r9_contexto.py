"""R-9 (auditoria, C_deep_learning): diagnostico del atajo del contexto, SOLO INFERENCIA.
Envuelve a15_cadena_completa.py sin modificarlo: sustituye `cond_de` por una version que, ademas de borrar G en los cortes
vecinos, suaviza con mediana 2D (lado MEDIANA, por omision 5 px) el contexto FUERA de G. Se compara la amplitud generada dentro
de G con la del contexto original (misma semilla/modelo). Uso: python audit_r9_contexto.py <argumentos de a15> """
import os, sys
from pathlib import Path
import numpy as np
from scipy.ndimage import median_filter
A15_DIR = Path(os.environ.get('A15_DIR', Path.home() / 'metalsynth' / 'experiments' / 'objetivo3'))
sys.path.insert(0, str(A15_DIR))
import a15_cadena_completa as a15  # noqa: E402
MEDIANA = int(os.environ.get('MEDIANA', '5'))

def suaviza_fuera_de_g(hu: np.ndarray, g: np.ndarray, lado: int = MEDIANA) -> np.ndarray:
    """Mediana 2D en todo el parche; los pixeles de G se dejan como estaban (ya vienen en -1000)."""
    f = median_filter(hu, size=lado, mode='nearest')
    return np.where(g, hu, f).astype(hu.dtype)

def cond_de_suave(vol, M, G, k, y0, x0, canales, canal_T=None):
    _, m_c, g_c = a15.parche(vol, M, G, k, y0, x0)
    ctx = []
    for j in (k - 1, k + 1):
        jj = j if 0 <= j < vol.shape[0] else k
        hu_v, _, g_v = a15.parche(vol, M, G, jj, y0, x0)
        hu_v = hu_v.copy(); hu_v[g_v] = -1000.0
        hu_v = suaviza_fuera_de_g(hu_v, g_v)
        ctx.append(a15.codifica_bloque(hu_v, canales) * 2.0 - 1.0)
    extra = [m_c.astype(np.float32)[None], g_c.astype(np.float32)[None]]
    if canal_T is not None:
        from plantilla import normaliza, plantilla
        extra.append(normaliza(plantilla(m_c.astype(bool), canal_T[0]), canal_T[1])[None])
    return np.concatenate(ctx + extra, axis=0).astype(np.float32), g_c, m_c

if __name__ == '__main__':
    if os.environ.get('R9_SUAVE', '1') == '1':
        a15.cond_de = cond_de_suave
        print('R9: contexto suavizado (mediana %d) fuera de G' % MEDIANA, flush=True)
    a15.main()
