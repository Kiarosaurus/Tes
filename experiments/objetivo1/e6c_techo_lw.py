"""E6c / implicancia #39 — barrido del techo de la ventana ancha (LW).

E6a dejo el diagnostico: con LW [-1000, 2000], el ida y vuelta `HU -> ventana -> HU` da
MAE mediana de 3588.80 HU en ROI de metal, con HU maximo mediano de 18 822 y pico 24 970
contra un techo de 2000. La representacion no puede codificar lo que la tesis debe generar.

E6a NO dice que hacer. Este script convierte esa decision en medicion: mide el mismo ida y
vuelta bajo cada salida candidata, sobre los mismos volumenes y el mismo ROI, para que la
autora elija con una tabla delante y no por argumento.

CONFIGURACIONES COMPARADAS
--------------------------
- `pub`         las tres ventanas publicadas. Es la baseline: LW [-1000, 2000],
                MW [-320, 480], SW [-160, 240] (`wang2025adaptiveweighting`, Sec. V-A-1).
- `LW<techo>`   las mismas tres, moviendo solo el techo de LW a 3000/4000/6000/10000/20000.
- `pub+MTW`     las tres publicadas mas una CUARTA ventana de metal [2000, 20000].
- `pub+asinh`   LW sustituida por compresion no lineal asinh sobre [-1000, 20000], que da
                resolucion fina cerca de 0 HU y gruesa en el rango alto.

QUE MIDE Y QUE NO MIDE (leer antes de citar cualquier numero)
-------------------------------------------------------------
Mide **solo** la perdida por recorte de ventana y por cuantizacion. No incluye el VAE, que
sigue sin especificar (#36). La cota que produce es inferior: ningun decodificador puede
recuperar lo que el recorte ya destruyo.

La profundidad de bits NO es un detalle de implementacion aqui: es el **sustituto medible**
de la precision efectiva del VAE. A float, ampliar el techo es gratis y siempre mejora; el
costo de ampliarlo solo aparece cuando la representacion tiene precision finita, que es el
caso real. Por eso la tabla se lee por columna de bits, no por la fila de float.

Solo lee `data/`. Escribe `e6c_techo_lw.csv` y `e6c_techo_lw.md`.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

import nibabel as nib
import numpy as np

MW = (-320.0, 480.0)
SW = (-160.0, 240.0)
BITS: tuple[int | None, ...] = (None, 16, 12, 8)
BONE_HU = 150.0
METAL_HU = 2500.0
ASINH_ESCALA = 500.0
MAX_VOX = 1_000_000  # submuestreo determinista por paso fijo


def lineal(low: float, high: float):
    """Canal de ventana lineal: recorta a [low, high] y normaliza a [0, 1]."""
    def ida(h: np.ndarray) -> np.ndarray:
        return (np.clip(h, low, high) - low) / (high - low)

    def vuelta(u: np.ndarray) -> np.ndarray:
        return u * (high - low) + low
    return ida, vuelta


def asinh_canal(low: float, high: float, escala: float = ASINH_ESCALA):
    """Canal no lineal asinh: fino cerca de 0 HU, grueso en el rango alto."""
    a, b = np.arcsinh(low / escala), np.arcsinh(high / escala)

    def ida(h: np.ndarray) -> np.ndarray:
        return (np.arcsinh(np.clip(h, low, high) / escala) - a) / (b - a)

    def vuelta(u: np.ndarray) -> np.ndarray:
        return np.sinh(u * (b - a) + a) * escala
    return ida, vuelta


def configuraciones() -> dict[str, dict[str, tuple]]:
    """Las nueve configuraciones candidatas, como diccionarios de canales."""
    base = {'MW': lineal(*MW), 'SW': lineal(*SW)}
    cfgs: dict[str, dict[str, tuple]] = {'pub': {'LW': lineal(-1000.0, 2000.0), **base}}
    for techo in (3000.0, 4000.0, 6000.0, 10000.0, 20000.0):
        cfgs[f'LW{int(techo)}'] = {'LW': lineal(-1000.0, techo), **base}
    cfgs['pub+MTW'] = {'LW': lineal(-1000.0, 2000.0), **base,
                       'MTW': lineal(2000.0, 20000.0)}
    cfgs['pub+asinh'] = {'LW': asinh_canal(-1000.0, 20000.0), **base}
    return cfgs


def cuantiza(u: np.ndarray, bits: int | None) -> np.ndarray:
    """Cuantiza el codigo normalizado a la profundidad dada."""
    if bits is None:
        return u
    niveles = 2 ** bits - 1
    return np.rint(u * niveles) / niveles


def mae_oraculo(valores: np.ndarray, canales: dict[str, tuple],
                bits: int | None) -> float:
    """MAE del decodificador oraculo: por voxel, el mejor de los canales disponibles."""
    errores = None
    for ida, vuelta in canales.values():
        err = np.abs(vuelta(cuantiza(ida(valores), bits)) - valores)
        errores = err if errores is None else np.minimum(errores, err)
    return float(errores.mean()) if errores is not None else float('nan')


def submuestrea(valores: np.ndarray) -> np.ndarray:
    """Paso fijo hasta MAX_VOX. Determinista y reproducible, sin semilla."""
    if valores.size <= MAX_VOX:
        return valores
    return valores[::int(np.ceil(valores.size / MAX_VOX))]


def analizar(path: Path, cfgs: dict[str, dict[str, tuple]]) -> dict[str, object]:
    """Una fila por volumen, con el MAE oraculo de cada configuracion y profundidad."""
    arr = nib.load(path).get_fdata(dtype=np.float32)
    fila: dict[str, object] = {'Caso': path.name.split('.nii')[0],
                               'Dataset': path.name.split('_')[0],
                               'HU máximo': round(float(arr.max()), 1)}
    hueso = submuestrea(arr[arr > BONE_HU])
    metal = submuestrea(arr[arr > METAL_HU])
    fila['n hueso'] = int(hueso.size)
    fila['n metal'] = int(metal.size)
    for nombre, canales in cfgs.items():
        for bits in BITS:
            etiqueta = 'float' if bits is None else f'{bits}b'
            if hueso.size:
                fila[f'{nombre} {etiqueta} hueso'] = round(
                    mae_oraculo(hueso, canales, bits), 4)
            if metal.size:
                fila[f'{nombre} {etiqueta} metal'] = round(
                    mae_oraculo(metal, canales, bits), 4)
    return fila


def informe(filas: list[dict], cfgs: dict, out: Path) -> None:
    """Resumen en Markdown: mediana sobre la cohorte, por configuracion y profundidad."""
    ok = [f for f in filas if not f.get('Error')]
    etiquetas = ['float' if b is None else f'{b}b' for b in BITS]
    lineas = ['# E6c — barrido del techo de LW (implicancia #39)', '',
              f'Volumenes leidos: {len(filas)}; con error: {len(filas) - len(ok)}.',
              f'ROI oseo HU > {BONE_HU:.0f}; ROI de metal HU > {METAL_HU:.0f}.',
              f'Submuestreo determinista a {MAX_VOX:,} voxeles por ROI.',
              'MAE del decodificador oraculo (mejor canal por voxel): **cota inferior**.',
              'Sin VAE (#36 sigue abierta). La columna de bits es el sustituto medible de',
              'la precision efectiva de la representacion latente.', '']
    for roi in ('hueso', 'metal'):
        lineas += [f'## MAE oraculo en ROI de {roi} — mediana sobre la cohorte (HU)', '',
                   '| Configuracion | ' + ' | '.join(etiquetas) + ' |',
                   '|---|' + '---|' * len(etiquetas)]
        for nombre in cfgs:
            celdas = []
            for etiqueta in etiquetas:
                clave = f'{nombre} {etiqueta} {roi}'
                vals = [f[clave] for f in ok if clave in f]
                celdas.append(f'{np.median(vals):.2f}' if vals else 'sin datos')
            lineas.append(f'| `{nombre}` | ' + ' | '.join(celdas) + ' |')
        lineas.append('')
    lineas += ['## Go/No-Go del Objetivo 1 (MAE < 25 HU en hueso)', '',
               '| Configuracion | ' + ' | '.join(etiquetas) + ' |',
               '|---|' + '---|' * len(etiquetas)]
    for nombre in cfgs:
        celdas = []
        for etiqueta in etiquetas:
            clave = f'{nombre} {etiqueta} hueso'
            vals = [f[clave] for f in ok if clave in f]
            celdas.append(f'{sum(v >= 25.0 for v in vals)}/{len(vals)}' if vals else '-')
        lineas.append(f'| `{nombre}` | ' + ' | '.join(celdas) + ' |')
    lineas += ['', 'Celda = volumenes que FALLAN el umbral de 25 HU, sobre el total.', '']
    (out / 'e6c_techo_lw.md').write_text('\n'.join(lineas) + '\n', encoding='utf-8')


def escanear(data: Path, out: Path) -> None:
    """Recorre los CT y escribe la tabla por volumen."""
    paths = sorted(data.rglob('*_data.nii*'))
    if not paths:
        raise SystemExit('No se encontraron CT *_data.nii[.gz]. No se escribio nada.')
    cfgs = configuraciones()
    filas: list[dict] = []
    for i, path in enumerate(paths):
        try:
            fila = analizar(path, cfgs)
        except Exception as exc:  # noqa: BLE001 - se registra y se sigue
            fila = {'Caso': path.name.split('.nii')[0],
                    'Dataset': path.name.split('_')[0], 'Error': str(exc)}
        filas.append(fila)
        print(f'{i + 1}/{len(paths)} {fila["Caso"]}: '
              f'pub 8b hueso={fila.get("pub 8b hueso", "ERR")} '
              f'LW20000 8b hueso={fila.get("LW20000 8b hueso", "-")} '
              f'pub float metal={fila.get("pub float metal", "-")}', flush=True)

    campos = ['Caso', 'Dataset', 'HU máximo', 'n hueso', 'n metal']
    for nombre in cfgs:
        for bits in BITS:
            etiqueta = 'float' if bits is None else f'{bits}b'
            campos += [f'{nombre} {etiqueta} hueso', f'{nombre} {etiqueta} metal']
    campos.append('Error')
    with (out / 'e6c_techo_lw.csv').open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=campos, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(filas)
    informe(filas, cfgs, out)
    print(f'\nEscrito {out / "e6c_techo_lw.csv"} y el informe .md')


def main() -> None:
    """Punto de entrada de linea de comandos."""
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=root / 'data')
    parser.add_argument('--out', type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    escanear(args.data, args.out)


if __name__ == '__main__':
    main()
