"""R1 / implicancia #26 — legibilidad de los tres landmarks de Kaiser bajo artefacto.

`tesis/main.tex` (Datasets, "Field limitation") promete por escrito esta cifra:
*"whether those landmarks remain locatable in metal-bearing volumes is not answered by any
published source. It will therefore be quantified on the local cohort."*

Los tres landmarks del marco de `kaiser2014dysmorphism` (decision del 2026-09-08) son:
platillo superior de S1, crestas iliacas y espinas iliacas posterosuperiores (EIPS).

QUE MIDE ESTE SCRIPT, EXACTAMENTE
---------------------------------
No es un detector de landmarks validado: no existe anotacion experta en este repositorio
contra la cual validarlo. Lo que se mide es una condicion **necesaria**: si la evidencia de
imagen en el sitio del landmark sigue siendo legible bajo el artefacto. Se trabaja por
**region** (esfera de 12 mm) y no por punto, y el criterio de "legible" se **calibra** sobre
los volumenes sin objeto de la propia cohorte (ver `r1_resumen.py`).

Lectura correcta del resultado: **cota superior** de localizabilidad, condicionada a que la
heuristica haya caido en el sitio correcto. Por eso cada volumen genera una lamina de QC
(`outputs/r1_qc/`) con los cinco puntos dibujados: sin revisar esas laminas, ninguna cifra
de este script debe escribirse como hallazgo.

V2 (2026-09-10) — CAMBIOS RESPECTO A LA V1
------------------------------------------
La v1 murio por memoria (17 de 178 filas; `r1_landmarks.v1-parcial.csv`). Cambios:
1. **Deteccion sobre rejilla reducida a ~1.5 mm** (max-pooling de la mascara osea). Las
   metricas de region se siguen midiendo a resolucion completa. Pico de memoria ~1/8.
2. **El metal se excluye de la mascara osea antes de localizar** (HU > 2500 dilatado 3 mm).
   En la v1 un pin de fijador externo que sale por la cresta podia ser "el punto mas alto de
   la cresta", y un tornillo que sobresale por detras, "la EIPS".
3. **S1 exige persistencia y transicion observada**: el ancho >= 100 mm debe sostenerse
   10 mm en z (la v1 pedia dos cortes seguidos, ~3 mm), y por encima tiene que haberse visto
   al menos 5 mm de nivel estrecho (L5 o disco). Sin eso el volumen empieza ya dentro del
   sacro (FOV cortado) y la v1 declaraba S1 en el borde superior (`CLINIC_0011`).
4. **Banda de la EIPS**: de la cresta hasta 40 mm por debajo de S1 (la EIPS esta a la altura
   de S2); la v1 cortaba a 70 mm bajo la cresta sin mirar S1.
5. **Crestas sobre el ilion, no sobre la banda lateral** (v2b, tras la primera corrida
   completa): en CT que llegan al torax las costillas eran el punto mas alto (`metal_0063`).
6. **Dos detectores de S1** (sagital primario, ala de control); ninguno es fiable solo. Los
   dos fallan por un nivel vertebral (~30 mm) en casos distintos; la lamina dibuja ambos.

HEURISTICA DE LOCALIZACION (auditable)
--------------------------------------
Todo en RAS+ (`as_closest_canonical`), en mm. Mascara osea = HU > 150 (umbral de bone
integrity de `peters2025hybrid`, #14, ya usado en E6a).

1. Componente conexa osea mas grande que no sea plana en y (descarta rieles de mesa).
2. `x_mid` = mediana de x de esa componente.
3. **Crestas**: banda lateral |x - x_mid| > 60 mm de cada lado, percentil 99.9 de z.
4. **S1**: de la cresta hacia abajo (maximo 130 mm), ancho en x de la componente 2D que
   contiene la linea media. Primer nivel con ancho >= 100 mm sostenido 10 mm, precedido de
   al menos 5 mm de nivel estrecho = platillo.
5. **EIPS**: en cada lado, z en [z_S1 - 40, z_cresta], banda 25 < |x - x_mid| < 100 mm,
   percentil 0.1 de y (lo mas posterior). Sin S1, se usa [z_cresta - 70, z_cresta].

METRICAS POR REGION (esfera de 12 mm, restringida a la mascara de cuerpo)
------------------------------------------------------------------------
- `oscuro`    fraccion de voxeles con HU < -200 dentro del cuerpo: estria oscura.
- `brillante` fraccion con HU > 2500: metal o estria brillante.
- `hueso`     fraccion con HU > 150: control de que la region cae sobre hueso.
- `dist_metal_mm` distancia al voxel de metal (HU > 2500) mas cercano del volumen.
- `fov_ok`    el punto esta a mas de 5 mm de las seis caras del volumen.

Solo lee `data/`. Escribe `r1_landmarks.csv` y laminas PNG en `outputs/r1_qc/` (ignorado
por git; las laminas derivan de `data/` y no se versionan, regla 6).
"""
from __future__ import annotations

import argparse
import csv
import gc
from pathlib import Path

import nibabel as nib
import numpy as np
from scipy import ndimage as ndi
from scipy.spatial import cKDTree

BONE_HU = 150.0
METAL_HU = 2500.0
DARK_HU = -200.0
BODY_HU = -400.0
RADIO_MM = 12.0
BANDA_LATERAL_MM = 60.0
ALA_MIN_MM = 100.0
ALA_PERSISTE_MM = 10.0
ESTRECHO_PREVIO_MM = 5.0
S1_PROFUNDIDAD_MM = 35.0
REJILLA_MM = 1.5
LANDMARKS = ('S1', 'cresta_der', 'cresta_izq', 'eips_der', 'eips_izq')


def cargar(path: Path) -> tuple[np.ndarray, np.ndarray]:
    """Carga el CT a RAS+ como int16 (vista reorientada, sin copia contigua)."""
    img = nib.load(path)
    if img.get_data_dtype() == np.int16:
        arr = np.asanyarray(img.dataobj)
    else:
        # 21 volumenes vienen en int32; el rango de la cohorte (-6671 a 24970) cabe en int16.
        # Se leen por trozos en z para no tener vivas a la vez la copia int32 y la int16.
        forma = img.shape[:3]
        arr = np.empty(forma, dtype=np.int16)
        for k0 in range(0, forma[2], 64):
            trozo = np.asarray(img.dataobj[:, :, k0:k0 + 64])
            arr[:, :, k0:k0 + 64] = np.clip(np.rint(trozo), -32768, 32767)
            del trozo
    ornt = nib.orientations.io_orientation(img.affine)
    arr = nib.orientations.apply_orientation(arr, ornt)
    perm = np.argsort(ornt[:, 0]).astype(int)
    zoom = np.array(img.header.get_zooms()[:3], dtype=np.float32)[perm]
    return arr, zoom


def maxpool(mask: np.ndarray, f: np.ndarray) -> np.ndarray:
    """Reduce una mascara booleana por bloques f, con `any` (conserva estructuras finas)."""
    n = np.array(mask.shape) // f
    m = mask[:n[0] * f[0], :n[1] * f[1], :n[2] * f[2]]
    return m.reshape(n[0], f[0], n[1], f[1], n[2], f[2]).any(axis=(1, 3, 5))


def maxpool_hu(arr: np.ndarray, f: np.ndarray, zoom: np.ndarray,
               bloque: int = 16) -> tuple[np.ndarray, np.ndarray | None, int]:
    """HU maximo por bloque f, por trozos en z; y coordenadas mm del metal a resolucion completa.

    Equivale a `maxpool(arr > umbral)` para cualquier umbral, sin crear ninguna mascara
    booleana del tamano del volumen (la v2 inicial murio por memoria en 51/178 al hacerlo).
    """
    n = np.array(arr.shape) // f
    out = np.empty(tuple(n), dtype=np.int16)
    metal: list[np.ndarray] = []
    total = 0
    for k0 in range(0, n[2], bloque):
        k1 = min(k0 + bloque, n[2])
        blk = np.asarray(arr[:n[0] * f[0], :n[1] * f[1], k0 * f[2]:k1 * f[2]])
        out[:, :, k0:k1] = blk.reshape(n[0], f[0], n[1], f[1], k1 - k0, f[2]).max(
            axis=(1, 3, 5))
        idx = np.argwhere(blk > METAL_HU)
        del blk
        if len(idx):
            idx[:, 2] += k0 * f[2]
            total += len(idx)
            metal.append(idx[::max(1, len(idx) // 20_000)].astype(np.float32) * zoom)
    # Metal fuera del recorte de bloques (bordes < f voxeles): se ignora, es despreciable.
    return out, (np.concatenate(metal) if metal else None), total


def pelvis(bone: np.ndarray, zoom: np.ndarray) -> np.ndarray | None:
    """Componente osea mas grande que no sea plana en y (descarta rieles de mesa)."""
    lab, n = ndi.label(bone, output=np.int32)
    if n == 0:
        return None
    sizes = ndi.sum(bone, lab, range(1, n + 1))
    for i in np.argsort(sizes)[::-1][:6]:
        m = lab == (i + 1)
        idx = np.argwhere(m)
        if ((idx.max(0) - idx.min(0)) * zoom)[1] >= 50.0:
            return m
    return None


def cuerpo(crudo: np.ndarray) -> np.ndarray:
    """Componente mas grande sobre -400 HU, con huecos llenos corte a corte.

    El relleno no es cosmetico: la estria oscura cae bajo -400 HU y sin rellenar la propia
    mascara borraria la senal a medir. El gas intestinal tambien queda dentro, pero esta
    igual en la cohorte sin objeto, que es la que calibra el criterio.
    """
    lab, n = ndi.label(crudo, output=np.int32)
    if n == 0:
        return np.ones_like(crudo, dtype=bool)
    sizes = ndi.sum(crudo, lab, range(1, n + 1))
    body = lab == (int(np.argmax(sizes)) + 1)
    for k in range(body.shape[2]):
        if body[:, :, k].any():
            body[:, :, k] = ndi.binary_fill_holes(body[:, :, k])
    return body


def platillo_s1(mask: np.ndarray, zr: np.ndarray, x_mid: float,
                z_cresta: float) -> float | None:
    """z (mm) del platillo superior de S1 por ensanchamiento sostenido del ala sacra."""
    i_mid = x_mid / zr[0]
    medial = 25.0 / zr[0]
    k_top = min(int(z_cresta / zr[2]), mask.shape[2] - 1)
    necesarios = max(2, int(np.ceil(ALA_PERSISTE_MM / zr[2])))
    estrechos_min = max(2, int(np.ceil(ESTRECHO_PREVIO_MM / zr[2])))
    seguidos, k_inicio, estrechos = 0, None, 0
    for k in range(k_top, -1, -1):
        if (z_cresta - k * zr[2]) > 130.0:
            break
        sl = mask[:, :, k]
        ancho = 0.0
        if sl.any():
            lab, n = ndi.label(sl)
            cerca = np.unique(lab[max(0, int(i_mid - medial)):int(i_mid + medial) + 1, :])
            for c in cerca[cerca > 0]:
                ii = np.nonzero((lab == c).any(axis=1))[0]
                ancho = max(ancho, float(ii.max() - ii.min()) * zr[0])
        if ancho >= ALA_MIN_MM:
            if estrechos < estrechos_min:
                # Sin nivel estrecho por encima no hay transicion observada: el volumen
                # empieza dentro del sacro. Seguir bajando encontraria otro ensanchamiento
                # (pubis), asi que se aborta en vez de adivinar.
                return None
            if seguidos == 0:
                k_inicio = k
            seguidos += 1
            if seguidos >= necesarios:
                return float(k_inicio * zr[2])
        else:
            seguidos = 0
            estrechos += 1
    return None


def s1_sagital(mask: np.ndarray, zr: np.ndarray, x_mid: float,
               z_cresta: float) -> np.ndarray | None:
    """Punto (mm) en el promontorio de S1, sobre el bloque sacro en sagital medio.

    En una losa sagital fina (+-1.5 mm), los cuerpos lumbares son componentes 2D separadas
    por los discos (tejido blando, < 150 HU) y el sacro fusionado es una componente alargada
    unica. Se elige la componente mas grande con extension en z >= 50 mm y tope a menos de
    130 mm bajo la cresta. Se localiza el promontorio (maximo de y + z) y el punto es la media
    de la superficie superior de la componente en los 35 mm por detras de el: el centro del
    platillo, sobre su superficie. El tope en z a secas cae a veces en el arco posterior de
    S1, no en el cuerpo (`CLINIC_0015`). Si el tope toca el borde superior del FOV se devuelve
    None. Una vertebra transicional o un puente osteofitico L5-S1 fusionan L5 con el sacro:
    el metodo lo confunde y lo delata la discrepancia con el metodo del ala.

    Piloto del 2026-09-10: la losa de +-5 mm con cierre morfologico fusionaba L5 con el sacro
    (`CLINIC_0003`); la losa fina los separa en los 8 volumenes inspeccionados.
    """
    r = max(1, int(round(1.5 / zr[0])))
    i_mid = int(round(x_mid / zr[0]))
    losa = ndi.binary_fill_holes(mask[max(0, i_mid - r):i_mid + r + 1, :, :].any(axis=0))
    lab, n = ndi.label(losa)
    mejor, area = None, 0
    for c, sl in enumerate(ndi.find_objects(lab), start=1):
        if sl is None:
            continue
        top_k, bot_k = sl[1].stop - 1, sl[1].start
        if (top_k - bot_k) * zr[2] < 50.0:
            continue
        if not (z_cresta - 130.0 <= top_k * zr[2] <= z_cresta + 40.0):
            continue
        a = int((lab[sl] == c).sum())
        if a > area:
            mejor, area = (c, sl), a
    if mejor is None:
        return None
    c, sl = mejor
    top_k = sl[1].stop - 1
    if top_k >= mask.shape[2] - 1 - int(np.ceil(5.0 / zr[2])):
        return None
    jj, kk = np.nonzero(lab == c)
    y, z = jj * zr[1], kk * zr[2]
    y_prom = y[int(np.argmax(y + z))]  # promontorio: extremo antero-superior
    tops_y, tops_z = [], []
    for j in np.unique(jj[(y >= y_prom - S1_PROFUNDIDAD_MM) & (y <= y_prom)]):
        tops_y.append(j * zr[1])
        tops_z.append(z[jj == j].max())
    return np.array([i_mid * zr[0], np.mean(tops_y), np.mean(tops_z)], dtype=np.float32)


def iliacos(mask: np.ndarray, zr: np.ndarray, x_mid: float) -> dict[str, np.ndarray | None]:
    """Coordenadas mm del hueso iliaco de cada lado: la componente lateral mas grande.

    Se borra la banda |x - x_mid| <= 40 mm y se etiqueta lo que queda. Las costillas se
    unian a la pelvis a traves de la columna y, en CT que suben hasta el torax, el punto mas
    alto de la banda lateral era una costilla, no la cresta (`metal_0063`). Sin la banda
    media cada costilla queda como componente pequena y el ilion (con sacro lateral, pubis y
    femur si estan en contacto) es la mayor de su lado.
    """
    i_lo = max(0, int(np.floor((x_mid - 40.0) / zr[0])))
    i_hi = min(mask.shape[0], int(np.ceil((x_mid + 40.0) / zr[0])) + 1)
    out: dict[str, np.ndarray | None] = {}
    for lado, sl in (('izq', slice(0, i_lo)), ('der', slice(i_hi, mask.shape[0]))):
        sub = mask[sl]
        lab, n = ndi.label(sub, output=np.int32)
        if n == 0:
            out[lado] = None
            continue
        mayor = int(np.argmax(ndi.sum(sub, lab, range(1, n + 1)))) + 1
        pts = np.argwhere(lab == mayor).astype(np.float32)
        pts[:, 0] += sl.start
        out[lado] = pts * zr
    return out


def puntos(mask: np.ndarray, zr: np.ndarray) -> tuple[dict[str, np.ndarray], dict]:
    """Cinco puntos en mm (rejilla reducida) y diccionario de control geometrico."""
    mm = np.argwhere(mask).astype(np.float32) * zr
    x_mid = float(np.median(mm[:, 0]))
    out: dict[str, np.ndarray] = {}
    ctrl: dict[str, float] = {'x_mid': x_mid}

    lados = (('der', mm[:, 0] > x_mid + BANDA_LATERAL_MM),
             ('izq', mm[:, 0] < x_mid - BANDA_LATERAL_MM))
    ilion = iliacos(mask, zr, x_mid)
    z_cresta: list[float] = []
    for lado, _ in lados:
        if ilion.get(lado) is None:
            continue
        s = ilion[lado]
        s = s[np.abs(s[:, 0] - x_mid) > BANDA_LATERAL_MM]
        if s.size == 0:
            continue
        z_top = float(np.percentile(s[:, 2], 99.9))
        out[f'cresta_{lado}'] = s[s[:, 2] >= z_top].mean(0)
        z_cresta.append(z_top)
    if 'cresta_der' in out and 'cresta_izq' in out:
        ctrl['ancho_crestas_mm'] = float(abs(out['cresta_der'][0] - out['cresta_izq'][0]))
    if not z_cresta:
        return out, ctrl

    zc = float(np.mean(z_cresta))
    ctrl['z_cresta_mm'] = zc
    # Dos metodos independientes. Primario: tope del sacro en sagital. Control: ala.
    z_ala = platillo_s1(mask, zr, x_mid, zc)
    p_sag = s1_sagital(mask, zr, x_mid, zc)
    if z_ala is not None:
        ctrl['z_s1_ala_mm'] = z_ala
    z_s1 = None
    if p_sag is not None:
        out['S1'] = p_sag
        z_s1 = float(p_sag[2])
        ctrl['z_s1_sagital_mm'] = z_s1
        ctrl['s1_bajo_cresta_mm'] = zc - z_s1
        if z_ala is not None:
            ctrl['s1_discrepancia_mm'] = z_ala - z_s1

    z_lo = (z_s1 - 40.0) if z_s1 is not None else (zc - 70.0)
    for lado, _ in lados:
        signo = 1.0 if lado == 'der' else -1.0
        dx = (mm[:, 0] - x_mid) * signo
        banda = mm[(dx > 25.0) & (dx < 100.0) & (mm[:, 2] >= z_lo) & (mm[:, 2] <= zc)]
        if banda.size:
            y_post = float(np.percentile(banda[:, 1], 0.1))
            out[f'eips_{lado}'] = banda[banda[:, 1] <= y_post].mean(0)
    return out, ctrl


def contaminacion(arr: np.ndarray, body: np.ndarray, f: np.ndarray, zoom: np.ndarray,
                  punto: np.ndarray, arbol: cKDTree | None) -> dict[str, float]:
    """Metricas de legibilidad en la esfera de 12 mm, a resolucion completa."""
    centro = punto / zoom
    radios = np.ceil(RADIO_MM / zoom).astype(int)
    lo = np.maximum(np.floor(centro - radios).astype(int), 0)
    hi = np.minimum(np.ceil(centro + radios).astype(int) + 1, arr.shape)
    sub = np.asarray(arr[lo[0]:hi[0], lo[1]:hi[1], lo[2]:hi[2]])
    ii, jj, kk = np.ogrid[lo[0]:hi[0], lo[1]:hi[1], lo[2]:hi[2]]
    d2 = ((ii - centro[0]) * zoom[0]) ** 2 + ((jj - centro[1]) * zoom[1]) ** 2 \
        + ((kk - centro[2]) * zoom[2]) ** 2
    bi = np.minimum(ii // f[0], body.shape[0] - 1)
    bj = np.minimum(jj // f[1], body.shape[1] - 1)
    bk = np.minimum(kk // f[2], body.shape[2] - 1)
    esfera = (d2 <= RADIO_MM ** 2) & body[bi, bj, bk]
    vox = sub[esfera]
    fov = float(min(np.min(punto), *(np.array(arr.shape) * zoom - punto)))
    fila: dict[str, float] = {'n_vox': int(vox.size), 'fov_margen_mm': round(fov, 1),
                              'fov_ok': 'si' if fov >= 5.0 else 'no'}
    if vox.size:
        fila['oscuro'] = round(float((vox < DARK_HU).mean()), 5)
        fila['brillante'] = round(float((vox > METAL_HU).mean()), 5)
        fila['hueso'] = round(float((vox > BONE_HU).mean()), 5)
    if arbol is not None:
        fila['dist_metal_mm'] = round(float(arbol.query(punto)[0]), 1)
    return fila


def lamina_qc(arr: np.ndarray, zoom: np.ndarray, pts: dict[str, np.ndarray],
              ctrl: dict, destino: Path, titulo: str) -> None:
    """Tres cortes (sagital medio, coronal de crestas, axial de EIPS) con los puntos."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    def idx(v: float, eje: int) -> int:
        return int(np.clip(round(v / zoom[eje]), 0, arr.shape[eje] - 1))

    colores = {'S1': 'red', 'cresta_der': 'lime', 'cresta_izq': 'cyan',
               'eips_der': 'orange', 'eips_izq': 'magenta'}
    x_mid = ctrl.get('x_mid', arr.shape[0] * zoom[0] / 2)
    ycr = np.mean([pts[k][1] for k in ('cresta_der', 'cresta_izq') if k in pts] or
                  [arr.shape[1] * zoom[1] / 2])
    zei = np.mean([pts[k][2] for k in ('eips_der', 'eips_izq') if k in pts] or
                  [arr.shape[2] * zoom[2] / 2])
    s1 = pts.get('S1')
    cortes = (
        ('sagital x_mid', np.asarray(arr[idx(x_mid, 0), :, :]).T, zoom[1], zoom[2], (1, 2),
         None),
        ('sagital x_mid, zoom S1 (+-60 mm)', np.asarray(arr[idx(x_mid, 0), :, :]).T,
         zoom[1], zoom[2], (1, 2), s1),
        ('coronal crestas', np.asarray(arr[:, idx(ycr, 1), :]).T, zoom[0], zoom[2], (0, 2),
         None),
        ('axial EIPS', np.asarray(arr[:, :, idx(zei, 2)]).T, zoom[0], zoom[1], (0, 1), None),
    )
    fig, ejes = plt.subplots(1, 4, figsize=(20, 5.5))
    for ax, (nombre, img, sh, sv, (eh, ev), foco) in zip(ejes, cortes):
        ax.imshow(np.clip(img, -200, 1200), cmap='gray', origin='lower',
                  extent=(0, img.shape[1] * sh, 0, img.shape[0] * sv), aspect='equal')
        for k, p in pts.items():
            ax.plot(p[eh], p[ev], 'o', ms=9, mfc='none', mec=colores[k], mew=2)
            ax.add_patch(plt.Circle((p[eh], p[ev]), RADIO_MM, fill=False,
                                    ec=colores[k], lw=0.8, ls='--'))
        if ev == 2 and 'z_cresta_mm' in ctrl:
            ax.axhline(ctrl['z_cresta_mm'], color='lime', lw=0.6, ls=':')
        if ev == 2 and 'z_s1_ala_mm' in ctrl:
            ax.axhline(ctrl['z_s1_ala_mm'], color='yellow', lw=0.8, ls='--')
        if foco is not None:
            ax.set_xlim(foco[eh] - 60, foco[eh] + 60)
            ax.set_ylim(foco[ev] - 60, foco[ev] + 60)
        ax.set_title(nombre, fontsize=9)
        ax.tick_params(labelsize=7)
    fig.suptitle(titulo + '  (rojo = S1 sagital; linea amarilla = z de S1 por ala; circulo'
                 ' discontinuo = esfera de 12 mm proyectada)', fontsize=9)
    fig.tight_layout()
    fig.savefig(destino, dpi=80)
    plt.close(fig)


def analizar(path: Path, qc_dir: Path | None) -> dict[str, object]:
    """Una fila por volumen, con las metricas de los cinco puntos."""
    arr, zoom = cargar(path)
    caso = path.name.split('.nii')[0]
    fila: dict[str, object] = {'Caso': caso, 'Dataset': path.name.split('_')[0]}
    f = np.maximum(1, np.rint(REJILLA_MM / zoom)).astype(int)
    zr = (zoom * f).astype(np.float32)
    fila['rejilla_mm'] = '/'.join(f'{v:.2f}' for v in zr)

    hu_ds, metal_mm, n_metal = maxpool_hu(arr, f, zoom)
    fila['n_metal'] = n_metal
    # Submuestreo del metal (~20 000 puntos por trozo): solo se usa para distancia minima,
    # con error acotado por la separacion entre puntos retenidos de un mismo objeto.
    arbol = cKDTree(metal_mm) if metal_mm is not None else None
    del metal_mm
    metal_ds = hu_ds > METAL_HU
    bone_ds = hu_ds > BONE_HU
    if metal_ds.any():
        it = max(1, int(round(3.0 / float(zr.min()))))
        bone_ds &= ~ndi.binary_dilation(metal_ds, iterations=it)
    del metal_ds
    body_ds = cuerpo(hu_ds > BODY_HU)
    del hu_ds

    mask = pelvis(bone_ds, zr)
    del bone_ds
    if mask is None:
        fila['Error'] = 'sin componente osea'
        return fila
    pts, ctrl = puntos(mask, zr)
    del mask
    # centro de bloque de la rejilla reducida -> mm del voxel completo
    desplaz = (f - 1) / 2.0 * zoom
    pts = {k: v + desplaz for k, v in pts.items()}
    ctrl['x_mid'] = ctrl['x_mid'] + float(desplaz[0])
    for clave in [k for k in ctrl if k.startswith('z_')]:
        ctrl[clave] = ctrl[clave] + float(desplaz[2])
    for clave, valor in ctrl.items():
        fila[clave] = round(float(valor), 1)
    for nombre in LANDMARKS:
        if nombre not in pts:
            fila[f'{nombre}_hallado'] = 'no'
            continue
        fila[f'{nombre}_hallado'] = 'si'
        for k in range(3):
            fila[f'{nombre}_{"xyz"[k]}_mm'] = round(float(pts[nombre][k]), 1)
        for clave, valor in contaminacion(arr, body_ds, f, zoom, pts[nombre], arbol).items():
            fila[f'{nombre}_{clave}'] = valor
    if qc_dir is not None:
        lamina_qc(arr, zoom, pts, ctrl, qc_dir / f'{caso}.png',
                  f'{caso}  S1 bajo cresta = {fila.get("s1_bajo_cresta_mm", "-")} mm;'
                  f' ala - sagital = {fila.get("s1_discrepancia_mm", "-")} mm')
    return fila


def escanear(data: Path, out: Path, casos: list[str] | None, qc: bool,
             nombre_csv: str, maximo: int | None = None,
             patron: str = '*_data.nii*') -> None:
    """Recorre los CT y escribe la tabla por volumen, fila a fila y reanudable."""
    paths = sorted(data.rglob(patron))
    if casos:
        paths = [p for p in paths if any(c in p.name for c in casos)]
    if not paths:
        raise SystemExit('No se encontraron CT *_data.nii[.gz]. No se escribio nada.')
    qc_dir = None
    if qc:
        qc_dir = out / 'outputs' / 'r1_qc'
        qc_dir.mkdir(parents=True, exist_ok=True)

    campos: list[str] = ['Caso', 'Dataset', 'rejilla_mm', 'n_metal', 'x_mid',
                         'ancho_crestas_mm', 'z_cresta_mm', 'z_s1_sagital_mm', 'z_s1_ala_mm',
                         's1_discrepancia_mm', 's1_bajo_cresta_mm']
    for nombre in LANDMARKS:
        campos += [f'{nombre}_hallado', f'{nombre}_x_mm', f'{nombre}_y_mm', f'{nombre}_z_mm',
                   f'{nombre}_n_vox', f'{nombre}_oscuro', f'{nombre}_brillante',
                   f'{nombre}_hueso', f'{nombre}_dist_metal_mm', f'{nombre}_fov_margen_mm',
                   f'{nombre}_fov_ok']
    campos.append('Error')

    destino = out / nombre_csv
    hechos: set[str] = set()
    if destino.exists():
        with destino.open(encoding='utf-8', newline='') as handle:
            hechos = {r['Caso'] for r in csv.DictReader(handle) if r.get('Caso')}
        print(f'Reanudando: {len(hechos)} volumenes ya en {destino.name}.')

    with destino.open('a' if hechos else 'w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=campos, extrasaction='ignore')
        if not hechos:
            writer.writeheader()
            handle.flush()
        nuevos = 0
        for i, path in enumerate(paths):
            caso = path.name.split('.nii')[0]
            if caso in hechos:
                continue
            if maximo is not None and nuevos >= maximo:
                break
            nuevos += 1
            try:
                fila = analizar(path, qc_dir)
            except Exception as exc:  # noqa: BLE001 - se registra y se sigue
                fila = {'Caso': caso, 'Dataset': path.name.split('_')[0],
                        'Error': f'{type(exc).__name__}: {exc}'}
            writer.writerow(fila)
            handle.flush()
            gc.collect()
            print(f'{i + 1}/{len(paths)} {caso}: S1={fila.get("S1_hallado", "ERR")} '
                  f's1_bajo_cresta={fila.get("s1_bajo_cresta_mm", "-")} '
                  f'err={fila.get("Error", "")}', flush=True)
    print(f'\nEscrito {destino}.')


def main() -> None:
    """Punto de entrada de linea de comandos."""
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--data', type=Path, default=root / 'data')
    parser.add_argument('--out', type=Path, default=Path(__file__).parent)
    parser.add_argument('--casos', nargs='*', help='subcadenas de nombre (piloto)')
    parser.add_argument('--patron', default='*_data.nii*',
                        help="glob de archivos; p. ej. '*_union.nii.gz' con --data data/derivados")
    parser.add_argument('--no-qc', action='store_true', help='no generar laminas')
    parser.add_argument('--csv', default='r1_landmarks.csv')
    parser.add_argument('--max', type=int, default=None,
                        help='procesar como maximo N volumenes nuevos (lotes reanudables)')
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    escanear(args.data, args.out, args.casos, not args.no_qc, args.csv, args.max,
             args.patron)


if __name__ == '__main__':
    main()
