"""SAP — Surgical Admissibility Profile. Unica metrica introducida por esta tesis (`00-tesis.md`).

POR QUE ESTE MODULO NO REIMPLEMENTA NADA DE LA GEOMETRIA DEL CORREDOR
---------------------------------------------------------------------
Mismo criterio que `common/ventanas.py` y `common/region.py`. El tramo oseo de una trayectoria, la
tolerancia a huecos, la exigencia de salida a blando y el recorte de 8 mm por extremo ya estan
implementados, ya corrieron sobre 152 casos con 0 errores y ya tienen control propio en
`experiments/objetivo2/e9_corredor.py`. Se **importan**; no se copian. Si SAP recortara el tramo con su
propio codigo, el grado de brecha y la viabilidad de corredor dejarian de ser comparables entre si, y la
primera vez que discreparan no habria forma de saber cual de las dos implementaciones produjo la cifra.

QUE MIDE SAP, Y CONTRA QUE SE COMPARA
-------------------------------------
Tres componentes, segun la fila *Surgical Admissibility* de la tabla de Expected Results de `main.tex`:

1. **Grado de brecha cortical de cuatro niveles** (escala de `smith2006iliosacral`, tal como la usa
   `zwingmann2009navigated`), con los limites de convencion propia ya escritos en `main.tex`:
   grado **0** sin perforacion, **1** en `(0, 2)`, **2** en `[2, 4]`, **3** en `(4, inf)` mm.
2. **Fraccion por zona de densidad** sobre el eje de la pose.
3. **Viabilidad de corredor** (`mclaren2021corridor`), `Dmax >= d + 2c` (#31).

La comparacion es **Wasserstein-1** contra las dos distribuciones ordinales de
`zwingmann2009navigated`, condicionadas por tecnica y **solo en S1** (#12, #28).

DECISIONES QUE ESTE MODULO IMPLEMENTA (no las toma: estan en `docs/01-decisiones.md`, 2026-09-22)
-------------------------------------------------------------------------------------------------
- **D-O2.3** — la brecha es la profundidad de protrusion fuera de la envolvente osea, medida sobre el
  campo de distancia euclidea **signada** (ver `campo_signado`), con 8 mm recortados por extremo. Ese recorte es
  clinico, no numerico: un tornillo iliosacro entra y sale por la cortical del ilion **por diseno**, y
  sin el recorte toda trayectoria valida puntuaria grado 3 por sus propios puntos de entrada y salida.
- **D-O2.4** — el diametro de SAP es **7.0 mm**, porque es el calibre del benchmark:
  *"the screws using a 7.0-mm cannulated screw"* (`zwingmann2009navigated`, Materials and Methods,
  p. 1835). 4.91 y 7.3 mm son sensibilidad.
- **D-O2.1** — SAP no se calibra contra Zwingmann. Este modulo **mide**; no ajusta nada.

LIMITE QUE VA DECLARADO DONDE SE REPORTE LA CIFRA
-------------------------------------------------
La envolvente `hueso` viene de TotalSegmentator, que segmenta **hueso**, no cortical. Su borde
**aproxima** la superficie cortical externa. SAP mide protrusion fuera de la envolvente osea segmentada.
No se reclama medicion de cortical.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from scipy import ndimage as ndi

_RAIZ = Path(__file__).resolve().parents[2]
try:
    from e9_corredor import (BONE_HU, PASO_MM, RECORTE_EXTREMO_MM, SALIDA_BLANDO_MM,  # noqa: E402
                             muestrear, tramo)
except ModuleNotFoundError:
    _p = str(_RAIZ / 'experiments' / 'objetivo2')
    if _p not in sys.path:
        sys.path.insert(0, _p)
    from e9_corredor import (BONE_HU, PASO_MM, RECORTE_EXTREMO_MM, SALIDA_BLANDO_MM,  # noqa: E402
                             muestrear, tramo)

__all__ = ['BONE_HU', 'D_SAP_MM', 'D_SENSIBILIDAD_MM', 'LIMITES_GRADO', 'ZWINGMANN',
           'campo_signado', 'puntos_eje', 'pose_base', 'brecha_mm', 'grado', 'evaluar_pose', 'fraccion_densidad',
           'distribucion_grados', 'wasserstein1_ordinal', 'sap_pose',
           'verificar_control_corredor', 'verificar_monotonia']

# D-O2.4: el calibre del benchmark. Las otras dos son sensibilidad declarada, no alternativas.
D_SAP_MM = 7.0
D_SENSIBILIDAD_MM = (4.91, 7.3)

# Limites de `main.tex`. El paper no cierra los bordes ("less than 2 mm", "between 2 and 4 mm"),
# asi que el cierre de cada intervalo es convencion propia y esta declarado como tal.
LIMITES_GRADO = (2.0, 4.0)

# Distribuciones de referencia, en porcentaje de tornillos por grado 0/1/2/3. De la ficha de
# `zwingmann2009navigated`, con frase original verificada. `zwingmann2010percutaneous` NO entra (#113).
ZWINGMANN = {
    'navegado': np.array([69.0, 15.0, 8.0, 8.0]),        # 26 tornillos en 24 pacientes
    'convencional': np.array([40.0, 37.0, 11.5, 11.5]),  # 35 tornillos en 32 pacientes
}

_T_EJE = np.arange(-160.0, 160.01, PASO_MM)

# Puntos minimos del tramo ya recortado para que la brecha sea un maximo sobre algo, y no
# sobre dos o tres muestras sueltas. A 1 mm de paso son 10 mm de travesia util.
MIN_PUNTOS_TRAMO = 10


def campo_signado(hueso: np.ndarray, zoom: np.ndarray) -> np.ndarray:
    """Distancia signada en mm: positiva fuera de la envolvente osea, negativa dentro, 0 en el borde.

    POR QUE SIGNADA Y NO SOLO EXTERIOR
    ----------------------------------
    Con un campo solo exterior, la brecha de un cilindro **inscrito** en el corredor no salia 0 sino
    ~1 voxel: los puntos de la superficie del cilindro caen justo sobre el borde de la mascara, el
    redondeo los echa fuera y la distancia al voxel oseo mas proximo ya no es cero. El control de
    `verificar_control_corredor` lo detecto (1.000 mm con `d = D_TS_max`, que por construccion debe dar
    0) y por eso el campo es signado.

    La razon de fondo es de **coherencia**, no de estetica numerica: `D_TS_max` se define en
    `e9_corredor.evaluar_linea` como `2 x min` de **este mismo** `distance_transform_edt` sobre la
    mascara osea. Usando la misma convencion de distancia para medir la brecha, la identidad
    "cilindro de diametro `D_TS_max` sobre el eje del corredor => brecha 0" se cumple por construccion
    y deja de ser una aproximacion.
    """
    m = np.asarray(hueso)
    fuera = ndi.distance_transform_edt(~m, sampling=zoom)
    dentro = ndi.distance_transform_edt(m, sampling=zoom)
    return (fuera - dentro).astype(np.float32)


def _indices(zoom: np.ndarray, origen: np.ndarray, forma, pts: np.ndarray) -> np.ndarray:
    """Coordenadas de voxel (continuas) de `pts`. Lanza si alguna cae fuera del recorte.

    No se tolera el punto fuera: la distancia al hueso no esta definida ahi, y devolver un 0 o un NaN
    silencioso convertiria una brecha real en grado 0. El recorte de `e9_corredor.recortar` es de
    +-130 / 110 mm alrededor de S1; una pose que se salga de el es un error de entrada, no un caso borde.
    """
    idx = (np.asarray(pts, dtype=float) - origen) / zoom
    lim = np.array(forma) - 1
    fuera = ~np.all((idx >= 0) & (idx <= lim), axis=-1)
    if fuera.any():
        raise ValueError(f'{int(fuera.sum())} puntos caen fuera del recorte')
    return idx


def _muestrear_campo(campo: np.ndarray, zoom: np.ndarray, origen: np.ndarray,
                     pts: np.ndarray) -> np.ndarray:
    """Campo continuo por interpolacion TRILINEAL sobre los puntos dados.

    Trilineal y no vecino mas proximo: con vecino mas proximo la brecha se cuantiza al voxel y el error
    de redondeo (hasta media diagonal de voxel) se acumula en un **maximo**, que es justo el estadistico
    mas sensible a ese ruido. Sobre el campo signado la interpolacion es ademas legitima: es una funcion
    continua que cruza 0 en el borde, no una etiqueta.
    """
    idx = _indices(zoom, origen, campo.shape, pts)
    plano = idx.reshape(-1, 3).T
    val = ndi.map_coordinates(np.asarray(campo, dtype=np.float32), plano, order=1, mode='nearest')
    return val.reshape(idx.shape[:-1])


def _muestrear_vecino(campo: np.ndarray, zoom: np.ndarray, origen: np.ndarray,
                      pts: np.ndarray) -> np.ndarray:
    """Vecino mas proximo. Para HU, donde interpolar cruzaria bordes de metal y de aire."""
    idx = np.rint(_indices(zoom, origen, campo.shape, pts)).astype(np.int64)
    return campo[idx[..., 0], idx[..., 1], idx[..., 2]]


def puntos_eje(c: np.ndarray, u: np.ndarray, t: np.ndarray) -> np.ndarray:
    """Puntos del eje `c + t u`, en mm. Forma `(len(t), 3)`."""
    return np.asarray(c, dtype=float)[None, :] + t[:, None] * np.asarray(u, dtype=float)[None, :]


def _span_corredor(hueso: np.ndarray, zoom: np.ndarray, origen: np.ndarray,
                   c: np.ndarray, u: np.ndarray) -> np.ndarray | None:
    """Tramo segun `e9_corredor.tramo`: con salida a tejido blando. Es el tramo del CORREDOR.

    Se conserva **solo** para `verificar_control_corredor`, que comprueba la convencion de distancia
    contra `D_TS_max`, definido sobre este mismo tramo. **No** se usa para calificar poses: ver
    `_span_pose` y #120.
    """
    eje = puntos_eje(c, u, _T_EJE)
    b = muestrear(hueso, zoom, origen, eje)
    tr = tramo(b, len(_T_EJE) // 2)
    if tr is None:
        return None
    iL, iR = tr
    k = int(round(RECORTE_EXTREMO_MM / PASO_MM))
    sel = np.arange(iL + k, iR - k + 1)
    if len(sel) < MIN_PUNTOS_TRAMO:
        return None
    return _T_EJE[sel]


def _span_pose(longitud_mm: float) -> np.ndarray:
    """Tramo que SAP califica: el **propio implante**, de longitud fija, centrado en la pose y recortado
    8 mm por extremo.

    POR QUE NO SE USA `e9_corredor.tramo` (decision #120, opcion (b), 2026-09-22)
    -----------------------------------------------------------------------------
    `tramo` exige que la trayectoria **salga a tejido blando** (40 mm sin hueso) y `evaluar_linea` exige
    ademas que cada salida sea al menos tan lateral como la EIPS. Son correctos para **buscar un
    corredor transsacro valido**, que es para lo que se escribieron. SAP no busca corredor: **califica
    una pose ya puesta**, y un tornillo malposicionado no tiene por que cumplirlos. Con `tramo` de
    puerta, el control C5 de E12 devolvia "no evaluable" a 5-8 grados de inclinacion, y descartar esas
    poses sesgaria a la baja el Wasserstein-1 contra `zwingmann2009navigated`, que califico **todos**
    sus tornillos.

    POR QUE LA LONGITUD ES FIJA Y NO LA DICTA EL HUESO
    --------------------------------------------------
    Las dos versiones anteriores definian el tramo por donde hubiera hueso, y las dos las tumbo un
    control de E12:

    1. *Del primer al ultimo cruce con la envolvente.* En `dataset7_CLINIC_metal_0008_data` el eje
       vuelve a tocar hueso a ~90 mm del centro, el tramo pasaba de 97 a 167 mm incluyendo decenas de
       milimetros de tejido blando, y la brecha salia **10.38 mm sobre el propio eje del corredor**,
       que por construccion debe dar 0. Lo detecto **C6**.
    2. *Igual, pero cortando en el primer hueco de 40 mm.* Arreglaba C6, pero a 20 grados de inclinacion
       la brecha volvia a **0.0**: el tramo se encoge con la pose, se queda en el trocito de hueso que
       la pose aun atraviesa, y **"quedarse dentro del hueso que uno mismo elige atravesar" es
       trivialmente satisfacible**. Lo detecto **C5**.

    Un implante es un objeto fisico de longitud dada: su extension **no puede depender de donde este el
    hueso**, porque entonces la metrica premia justamente a las poses que se salen. La longitud es la
    del corredor **de ese caso** (`L_TS_mejor_mm`), ya medida en E9-TS: un tornillo transsacro es, por
    definicion, el que cruza el corredor. **No introduce ninguna constante nueva** y, sobre el eje del
    corredor, reproduce exactamente su tramo, de modo que C2 y C6 siguen dando 0 por construccion.

    Se conserva el recorte de **8 mm por extremo**: la entrada y la salida por la cortical del ilion
    son **por diseno** y no son perforacion.
    """
    media = float(longitud_mm) / 2.0 - RECORTE_EXTREMO_MM
    if not np.isfinite(media) or media <= 0:
        raise ValueError(f'longitud de implante no utilizable: {longitud_mm}')
    n = int(np.floor(media / PASO_MM))
    return np.arange(-n, n + 1, dtype=float) * PASO_MM


def pose_base(hueso: np.ndarray, zoom: np.ndarray, origen: np.ndarray, c: np.ndarray,
              u: np.ndarray) -> tuple[np.ndarray, float] | None:
    """Pose base del caso: centro anclado al punto medio del corredor y longitud del implante.

    POR QUE HACE FALTA ANCLAR
    -------------------------
    `c_x_mm, c_y_mm, c_z_mm` de `e9ts_corredor.csv` es el punto **desde el que se lanzo la busqueda**
    del corredor, no el punto medio del tramo oseo que encontro. En `dataset6_CLINIC_0002_data`
    coinciden; en `dataset7_CLINIC_metal_0008_data` **no**, y un implante simetrico alrededor de `c`
    queda descentrado respecto del corredor. El control C6 de E12 lo destapo: los dos tramos median casi
    lo mismo (97 y 96 mm) pero la brecha sobre el eje del corredor salia **6.65 mm** en vez de 0, porque
    estaban en sitios distintos.

    Anclar es una operacion **por caso y previa a cualquier perturbacion**: usa solo geometria ya medida
    y no depende de la pose muestreada. Con ella, la identidad "implante sobre el eje del corredor =>
    brecha 0" vuelve a cumplirse por construccion.

    Devuelve `(centro_anclado, longitud_mm)`, o `None` si el caso no tiene corredor valido.
    """
    t = _span_corredor(hueso, zoom, origen, c, u)
    if t is None:
        return None
    t_medio = float(t[0] + t[-1]) / 2.0
    longitud = float(t[-1] - t[0]) + 2 * RECORTE_EXTREMO_MM
    u = np.asarray(u, dtype=float)
    return np.asarray(c, dtype=float) + t_medio * (u / np.linalg.norm(u)), longitud


def brecha_mm(hueso: np.ndarray, zoom: np.ndarray, origen: np.ndarray, c: np.ndarray, u: np.ndarray,
              diametro_mm: float = D_SAP_MM, *, sdf: np.ndarray | None = None,
              span: str = 'pose', longitud_mm: float | None = None) -> float | None:
    """Profundidad maxima de protrusion del cilindro fuera de la envolvente osea, en mm.

    COMO SE MIDE, Y POR QUE ASI
    ---------------------------
    Sobre el **eje**, no sobre la superficie del cilindro:

        brecha = max sobre t de  max(0, radio + sd(c + t u))

    con `sd` la distancia signada (positiva fuera del hueso, negativa dentro). Leida por partes:
    con el eje **dentro** del hueso, `sd = -d_dentro` y la expresion es `radio - d_dentro`, es decir
    cuanto excede el radio del cilindro a la distancia del eje a la cortical mas proxima; con el eje
    **fuera**, `sd = +d_fuera` y la expresion suma la propia desviacion del eje.

    **Por que sobre el eje y no muestreando la superficie.** La primera version muestreaba el cilindro
    solido y la fallaba el control de `verificar_control_corredor`: con `d = D_TS_max` daba 0.616 mm en
    vez de 0. La causa no era un error de codigo sino de **convencion**: `D_TS_max` se define en
    `e9_corredor.evaluar_linea` como `2 x min` del EDT **sobre el eje**, mientras que muestrear la
    superficie pregunta si unos puntos continuos caen dentro de una mascara **voxelizada**, y las dos
    cosas difieren hasta media diagonal de voxel. Midiendo sobre el eje con el mismo EDT, la identidad
    "cilindro de diametro `D_TS_max` sobre el eje del corredor => brecha 0" se cumple **exactamente**, y
    el error del fantasma cae de 0.68 mm a 0.05 mm.

    **Que supone, y va declarado.** El punto de la cortical mas proximo al eje esta a `d_dentro`, y el
    disco de radio `radio` sobresale `radio - d_dentro` por ese punto. Como `d_dentro` es el minimo, esa
    es la protrusion maxima en el sentido de "distancia mas alla de la superficie mas proxima". La
    medida es **radial**, en el plano perpendicular al eje: coincide con la protrusion para una cortical
    localmente plana, y no captura geometrias en las que el hueso envuelve al cilindro.

    Devuelve 0.0 si el cilindro no sobresale (grado 0), y None si la trayectoria no tiene tramo oseo
    valido: sin tramo no hay corredor y la pose no es evaluable, que no es lo mismo que no perforar.
    """
    if span == 'corredor':
        t = _span_corredor(hueso, zoom, origen, c, u)
    elif span == 'pose':
        if longitud_mm is None:
            raise ValueError("span='pose' necesita `longitud_mm` (la del corredor del caso)")
        t = _span_pose(longitud_mm)
    else:
        raise ValueError(f'span desconocido: {span!r}')
    if t is None:
        return None
    if sdf is None:
        sdf = campo_signado(hueso, zoom)
    sd = _muestrear_campo(sdf, zoom, origen, puntos_eje(c, u, t))
    return float(max(0.0, (diametro_mm / 2.0 + sd).max()))


def grado(brecha: float | None) -> int | None:
    """Grado ordinal 0-3 de `smith2006iliosacral` con los limites de `main.tex`. None si no evaluable."""
    if brecha is None:
        return None
    lo, hi = LIMITES_GRADO
    if brecha <= 0.0:
        return 0
    if brecha < lo:
        return 1
    if brecha <= hi:
        return 2
    return 3


def fraccion_densidad(hu: np.ndarray, hueso: np.ndarray, zoom: np.ndarray, origen: np.ndarray,
                      c: np.ndarray, u: np.ndarray, longitud_mm: float) -> float | None:
    """Fraccion del eje, dentro de hueso y ya recortado, que cae en zona de baja densidad (<= 150 HU).

    Componente 2 de SAP. Por D-O2.6 se **reporta**; no condiciona el muestreo.
    """
    eje = puntos_eje(c, u, _span_pose(longitud_mm))
    idx = (np.asarray(eje, dtype=float) - origen) / zoom
    en_recorte = np.all((idx >= 0) & (idx <= np.array(hueso.shape) - 1), axis=-1)
    if not en_recorte.any():
        return None
    eje = eje[en_recorte]
    dentro = muestrear(hueso, zoom, origen, eje)
    if not dentro.any():
        return 0.0   # el implante no atraviesa hueso: no hay fraccion de esponjoso que reportar
    valores = _muestrear_vecino(np.asarray(hu, dtype=np.float32), zoom, origen, eje)[dentro]
    return float((valores <= BONE_HU).mean())


def distribucion_grados(grados, no_evaluables: str = 'error') -> np.ndarray:
    """Proporciones por grado 0/1/2/3, en porcentaje.

    `no_evaluables` decide que hacer con las poses cuyo eje no tiene tramo oseo valido (grado `None`),
    y **no tiene defecto permisivo a proposito**: con `'error'` la funcion lanza. Descartarlas en
    silencio inflaria los grados buenos —una pose que ni siquiera entra en el sacro desapareceria del
    denominador— y el Wasserstein-1 contra `zwingmann2009navigated` saldria artificialmente bajo, que es
    justo el sesgo que D-O2.1 existe para evitar. La serie de Zwingmann grado **todos** sus tornillos,
    porque todos estaban implantados; el denominador tiene que ser comparable.

    - `'error'`   (defecto) lanza si hay alguna. Obliga a decidir caso por caso.
    - `'grado3'`  las cuenta como grado 3. Es lo defendible si la pose sale del hueso: perforar mas de
      4 mm y no tocar hueso no son clinicamente distinguibles en esta escala.
    - `'excluir'` las descarta. Solo con el recuento declarado junto a la cifra.

    Ver #120: cual de las tres se usa en el resultado principal es decision de la autora.
    """
    g = list(grados)
    n_nulos = sum(1 for x in g if x is None)
    if n_nulos and no_evaluables == 'error':
        raise ValueError(f'{n_nulos} poses sin tramo oseo valido; elige `no_evaluables` (ver #120)')
    if no_evaluables == 'grado3':
        g = [3 if x is None else x for x in g]
    elif no_evaluables in ('excluir', 'error'):
        g = [x for x in g if x is not None]
    else:
        raise ValueError(f'no_evaluables desconocido: {no_evaluables!r}')
    arr = np.array(g, dtype=int)
    if arr.size == 0:
        raise ValueError('ninguna pose evaluable')
    return np.bincount(arr, minlength=4)[:4] / arr.size * 100.0


def wasserstein1_ordinal(p: np.ndarray, q: np.ndarray) -> float:
    """Wasserstein-1 entre dos distribuciones sobre los grados 0-3, tratados como equiespaciados.

    Los grados son categorias ordinales de intervalos de milimetros de ancho desigual ((0,2), [2,4],
    (4,inf)); tratarlos como equiespaciados es una **convencion declarada**, no una propiedad medida.
    La unidad del resultado es "grados", no milimetros, y asi debe reportarse.
    """
    p = np.asarray(p, dtype=float)
    q = np.asarray(q, dtype=float)
    if p.shape != (4,) or q.shape != (4,):
        raise ValueError(f'se esperan 4 grados, no {p.shape} y {q.shape}')
    p = p / p.sum()
    q = q / q.sum()
    return float(np.abs(np.cumsum(p)[:-1] - np.cumsum(q)[:-1]).sum())


def evaluar_pose(hueso: np.ndarray, zoom: np.ndarray, origen: np.ndarray, c: np.ndarray,
                 u: np.ndarray, longitud_mm: float, diametro_mm: float = D_SAP_MM, *,
                 sdf: np.ndarray | None = None) -> dict:
    """Grado de brecha de UNA pose. Siempre devuelve grado: ninguna pose se queda sin calificar.

    Es la funcion que alimenta la distribucion que se compara con `zwingmann2009navigated`, y por eso no
    puede devolver `None`: el denominador de Zwingmann incluye **todos** sus tornillos (#120, opcion (b)).

    Los puntos del implante que caen fuera del recorte de +-130 / 110 mm alrededor de S1 estan, por
    construccion del recorte, lejisimos del sacro: se cuentan como **fuera del hueso**, no se descartan.
    Si son tantos que dentro del recorte no queda tramo medible, la pose sale `fuera_de_recorte` y
    **grado 3**, que es donde corresponde a un implante que ni siquiera cae en la region de interes.
    """
    if sdf is None:
        sdf = campo_signado(hueso, zoom)
    t = _span_pose(longitud_mm)
    pts = puntos_eje(c, u, t)
    idx = (np.asarray(pts, dtype=float) - origen) / zoom
    dentro = np.all((idx >= 0) & (idx <= np.array(sdf.shape) - 1), axis=-1)
    if int(dentro.sum()) < MIN_PUNTOS_TRAMO:
        return {'brecha_mm': None, 'grado': 3, 'estado': 'fuera_de_recorte',
                'n_fuera_recorte': int((~dentro).sum()), 'largo_mm': float(t[-1] - t[0])}
    sd = _muestrear_campo(sdf, zoom, origen, pts[dentro])
    b = float(max(0.0, (diametro_mm / 2.0 + sd).max()))
    return {'brecha_mm': b, 'grado': grado(b),
            'estado': 'ok' if dentro.all() else 'recorte_parcial',
            'n_fuera_recorte': int((~dentro).sum()), 'largo_mm': float(t[-1] - t[0])}


def sap_pose(hu: np.ndarray, hueso: np.ndarray, zoom: np.ndarray, origen: np.ndarray,
             c: np.ndarray, u: np.ndarray, d_max_corredor_mm: float, longitud_mm: float,
             diametro_mm: float = D_SAP_MM, *, sdf: np.ndarray | None = None,
             holgura_mm: float = 1.0) -> dict:
    """Los tres componentes de SAP para una pose. No decide nada: mide.

    `d_max_corredor_mm` es el `D_TS_max_mm` del caso, de `e9ts_corredor.csv`.
    """
    if sdf is None:
        sdf = campo_signado(hueso, zoom)
    r = evaluar_pose(hueso, zoom, origen, c, u, longitud_mm, diametro_mm, sdf=sdf)
    return {
        'diametro_mm': diametro_mm,
        'brecha_mm': r['brecha_mm'],
        'grado': r['grado'],
        'estado': r['estado'],
        'frac_baja_densidad': fraccion_densidad(hu, hueso, zoom, origen, c, u, longitud_mm),
        'viable_corredor': bool(d_max_corredor_mm >= diametro_mm + 2 * holgura_mm),
    }


def verificar_control_corredor(hueso: np.ndarray, zoom: np.ndarray, origen: np.ndarray,
                               c: np.ndarray, u: np.ndarray, d_max_corredor_mm: float,
                               *, sdf: np.ndarray | None = None, tol_mm: float = 0.0) -> float:
    """Control que PUEDE FALLAR (D-O2.3): el cilindro de diametro `D_TS_max` sobre el eje del corredor
    tiene que dar brecha 0.

    No es una comprobacion de estilo: `D_TS_max` es, por construccion de `evaluar_linea`, dos veces la
    distancia libre minima a lo largo del eje ya recortado. Un cilindro de ese diametro centrado en ese
    eje esta enteramente dentro del hueso. Si sale > 0, el muestreo del cilindro, el recorte del tramo o
    el campo de distancia estan mal, y la cifra de ese caso no se usa.

    `tol_mm` cubre solo la discretizacion del muestreo por vecino mas proximo; por defecto es 0.
    """
    b = brecha_mm(hueso, zoom, origen, c, u, float(d_max_corredor_mm), sdf=sdf,
                  span='corredor')
    if b is None:
        raise RuntimeError('el eje del corredor no tiene tramo oseo valido: control no aplicable')
    if b > tol_mm:
        raise RuntimeError(f'control del corredor falla: brecha {b:.3f} mm con d = D_TS_max = '
                           f'{d_max_corredor_mm:.3f} mm (deberia ser 0)')
    return b


def verificar_monotonia(hueso: np.ndarray, zoom: np.ndarray, origen: np.ndarray,
                        c: np.ndarray, u: np.ndarray, diametros_mm=(4.91, 7.0, 7.3, 8.0),
                        *, sdf: np.ndarray | None = None,
                        longitud_mm: float | None = None) -> list[float]:
    """Control que PUEDE FALLAR: la brecha no puede decrecer al ensanchar el cilindro."""
    if sdf is None:
        sdf = campo_signado(hueso, zoom)
    ds = sorted(float(d) for d in diametros_mm)
    vals = []
    for d in ds:
        b = brecha_mm(hueso, zoom, origen, c, u, d, sdf=sdf, longitud_mm=longitud_mm)
        if b is None:
            raise RuntimeError('trayectoria sin tramo oseo valido: control no aplicable')
        vals.append(b)
    for d0, d1, b0, b1 in zip(ds, ds[1:], vals, vals[1:]):
        if b1 < b0 - 1e-6:
            raise RuntimeError(f'monotonia falla: d {d0} -> {d1} mm baja la brecha '
                               f'{b0:.3f} -> {b1:.3f} mm')
    return vals
