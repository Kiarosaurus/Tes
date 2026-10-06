"""A6 — primera muestra sintetica del proyecto (#116). Minimo viable, en local y sin GPU.

POR QUE EXISTE
--------------
`muestrea_ddim` esta definida en `src/renderizador/difusion.py` desde que se escribio el Diseno A y
**ningun archivo la llama**. El resultado es que **nunca se genero una muestra** en este proyecto, y que
**#95, #96, #112 y #57 son predicciones sobre imagenes que nadie ha visto**. Este script existe para
convertir esas cuatro discusiones en observacion, no para producir un resultado de tesis.

Deliberadamente minimo: una muestra, un parche, una lamina. **Si sale mal, tambien sirve.**

NO ES UN RESULTADO Y NO DEBE CITARSE COMO TAL
---------------------------------------------
El `ckpt.pt` disponible es el del **piloto de 200 pasos** (job 52074), que se corrio para medir el coste
(#89), **no para converger**. Lo que salga de aqui dice si la cadena funciona de punta a punta; **no**
dice nada sobre la calidad del renderizador. Cualquier cifra de este script es de diagnostico.

QUE HACE
--------
1. Carga el `ckpt.pt` y reconstruye la U-Net con el `base` guardado en su `meta`.
2. Toma un parche del conjunto de **validacion** (el que el modelo no vio).
3. Llama a `muestrea_ddim` con semilla fija.
4. Decodifica de la representacion multi-ventana a HU con la **misma** `regla` del Objetivo 1.
5. **Compone** con `common/region.componer` y **verifica** que fuera de `G` no cambio ni un voxel.
6. Escribe una lamina de cuatro paneles y un resumen en texto.

CONTROLES QUE PUEDEN FALLAR
---------------------------
- `verificar_composicion`: fuera de `G` la salida es identica bit a bit al original. Si falla, la
  promesa central del Diseno A (preservacion por construccion, bloque E-A3) deja de ser cierta.
- La salida generada tiene que ser **cero exacto fuera de `G`** antes de componer, porque
  `muestrea_ddim` multiplica por `g` en cada paso.
- El HU decodificado dentro de `G` tiene que caer en un rango fisico; si sale todo pegado a un extremo,
  el modelo no aprendio nada y hay que decirlo.

USO
---
    python a6_muestra_minima.py                      # primer parche de val
    python a6_muestra_minima.py --indice 7 --pasos 50
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import torch

_RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_RAIZ / 'src' / 'renderizador'))
sys.path.insert(0, str(_RAIZ / 'src' / 'common'))

from datos import ParchesMetal  # noqa: E402
from difusion import Difusion, muestrea_ddim  # noqa: E402
from modelo import UNetDifusion  # noqa: E402
from region import componer, verificar_composicion  # noqa: E402
from ventanas import decodifica_bloque  # noqa: E402


def a_hu(bloque: torch.Tensor) -> np.ndarray:
    """De la representacion multi-ventana en [-1, 1] a HU.

    Reusa `ventanas.decodifica_bloque`, que aplica la `regla` congelada del Objetivo 1 sobre los tres
    canales apilados en el orden LW, MW, SW. No se reimplementa aqui: una segunda ruta numerica que
    nadie controla es justo lo que `common/ventanas.py` existe para evitar.
    """
    u = (bloque.detach().cpu().numpy()[0] + 1.0) / 2.0        # [-1,1] -> [0,1], (canal, H, W)
    return decodifica_bloque(u)


def escribe_nifti(out_dir: Path, cache: Path, serie: str, k: int,
                  hu_real: np.ndarray, hu_sal: np.ndarray) -> None:
    """Escribe original y compuesta como `.nii.gz` en HU, con el espaciado real del caso.

    POR QUE EXISTE: un clinico no puede juzgar un PNG. La lamina sale recortada a `vmin/vmax` fijos y
    sin unidades, de modo que el metal y el hueso se saturan igual. En ITK-SNAP, con los HU de verdad,
    se ventanea y se distingue. El espaciado en plano sale de `zooms` del propio `.npz`, no se asume.
    """
    try:
        import nibabel as nib
    except ModuleNotFoundError:
        print('AVISO: falta nibabel, no se escribe el .nii.gz')
        return
    npz = Path(cache) / f'{serie}_k{k:04d}.npz'
    if not npz.exists():
        print(f'AVISO: no se hallo {npz.name}, no se escribe el .nii.gz')
        return
    z = np.load(npz)
    zooms = np.asarray(z['zooms'], dtype=float)
    eje = int(z['eje'])
    plano = [i for i in range(3) if i != eje]          # los dos ejes que quedan en el corte
    esp = (zooms[plano[0]], zooms[plano[1]], zooms[eje])
    afin = np.diag([esp[0], esp[1], esp[2], 1.0])
    for nombre, vol in (('original', hu_real), ('compuesta', hu_sal)):
        ruta = out_dir / f'a6_{serie}_k{k:04d}_{nombre}.nii.gz'
        nib.save(nib.Nifti1Image(vol[:, :, None].astype(np.float32), afin), ruta)
        print(f'nifti: {ruta}')
    print(f'  espaciado en plano {esp[0]:.3f} x {esp[1]:.3f} mm, grosor {esp[2]:.3f} mm '
          f'(de `zooms` del caso, eje de corte {eje})')


def indice_mas_metal(ds, manifiesto: Path) -> int:
    """Posicion en `ds` del parche con mas voxeles de metal, segun la columna `n_metal`.

    Se resuelve sobre `ds.indice`, que es la lista de `(serie, corte)` ya filtrada, y no cargando los
    896 `.npz` para mirar el canal `M`. La clave `serie` se arma igual que en `datos._lee_manifiesto`:
    el caso mas el sufijo `_cNNN` del componente.
    """
    import csv
    with open(manifiesto, newline='', encoding='utf-8') as fh:
        filas = [r for r in csv.DictReader(fh) if int(r['n_metal']) > 0]
    if not filas:
        raise SystemExit(f'{manifiesto.name} no tiene ningun parche con metal')
    mejor = max(filas, key=lambda r: int(r['n_metal']))
    clave = (f'{mejor["Caso"]}_c{int(mejor["comp"]):03d}', int(mejor['corte']))
    try:
        i = ds.indice.index(clave)
    except ValueError:
        raise SystemExit(f'el parche con mas metal {clave} no esta en el conjunto cargado')
    print(f'--mas-metal: {clave[0]} corte {clave[1]} | n_metal={mejor["n_metal"]} '
          f'n_G={mejor["n_G"]} -> indice {i}')
    return i


def main() -> None:
    aqui = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--ckpt', type=Path,
                    default=aqui / 'outputs' / 'a2' / 'pasos200_20260921_074236' / 'ckpt.pt')
    ap.add_argument('--cache', type=Path, default=aqui / 'outputs' / 'a1b_cache')
    ap.add_argument('--particion', type=Path,
                    default=aqui.parent / 'objetivo1' / 'p1_particion.csv')
    ap.add_argument('--manifiesto', type=Path, default=aqui / 'a5_manifiesto_val.csv')
    ap.add_argument('--indice', type=int, default=0)
    ap.add_argument('--nifti', action='store_true',
                    help='escribe tambien el original y la salida compuesta como .nii.gz en HU, para abrirlos en ITK-SNAP y ventanear. El PNG no sirve para juicio clinico.')
    ap.add_argument('--mas-metal', action='store_true',
                    help='ignora --indice y toma el parche de val con mas voxeles de metal, que es '
                         'el que muestra el artefacto. Util para una lamina de demostracion.')
    ap.add_argument('--pasos', type=int, default=50)
    ap.add_argument('--semilla', type=int, default=0)
    ap.add_argument('--out-dir', type=Path, default=aqui / 'outputs' / 'a6')
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    ck = torch.load(args.ckpt, map_location='cpu', weights_only=False)
    meta = ck.get('meta', {})
    base = int(meta.get('base', 64))
    # `meta['pasos']` es el objetivo configurado, NO los pasos alcanzados. Lo que importa es `ck['paso']`,
    # que es donde quedo el modelo: un ckpt cortado en la pared de la cola lleva muchos menos.
    paso_ck = ck.get('paso')
    print(f'ckpt: {args.ckpt.name} | base={base} | paso alcanzado: {paso_ck} '
          f'| objetivo configurado: {meta.get("pasos")}')

    modelo = UNetDifusion(base=base)
    modelo.load_state_dict(ck['modelo'])
    modelo.eval()
    n_par = sum(p.numel() for p in modelo.parameters())
    print(f'parametros: {n_par/1e6:.1f} M | dispositivo: cpu')

    ds = ParchesMetal(args.cache, args.particion, particiones=('val',), inclusion=args.manifiesto)
    print(f'conjunto de validacion: { {k: int(v) for k, v in ds.resumen().items()} }')
    if args.mas_metal:
        args.indice = indice_mas_metal(ds, args.manifiesto)
    if args.indice >= len(ds):
        raise SystemExit(f'--indice {args.indice} fuera de rango ({len(ds)} parches)')
    m = ds[args.indice]
    print(f'parche: {m["caso"]} corte {m["k"]}')

    cond = m['cond'][None]
    g = m['g'][None]
    frac_g = float(g.mean())
    print(f'fraccion de la region G en el parche: {100*frac_g:.1f} %')

    dif = Difusion()
    import time
    t0 = time.time()
    with torch.no_grad():
        gen = muestrea_ddim(modelo, cond, g, dif, pasos=args.pasos, semilla=args.semilla)
    seg = time.time() - t0
    print(f'muestreo: {args.pasos} pasos DDIM en {seg:.1f} s ({seg/args.pasos:.2f} s/paso, CPU)')

    gmask = g.numpy()[0, 0].astype(bool)
    fuera = float(np.abs(gen.numpy()[0][:, ~gmask]).max()) if (~gmask).any() else 0.0
    print(f'CONTROL: maximo |valor generado| FUERA de G = {fuera:.3e} (debe ser 0)')

    hu_real = a_hu(m['x0'][None])
    hu_gen = a_hu(gen)
    hu_sal = componer(hu_real, hu_gen, gmask)
    verificar_composicion(hu_real, hu_sal, gmask)
    print('CONTROL: composicion exacta fuera de G -> PASA')

    dentro = hu_gen[gmask]
    print(f'HU generado dentro de G: min {dentro.min():.0f} | p50 {np.median(dentro):.0f} | '
          f'max {dentro.max():.0f}')
    print(f'HU real    dentro de G: min {hu_real[gmask].min():.0f} | '
          f'p50 {np.median(hu_real[gmask]):.0f} | max {hu_real[gmask].max():.0f}')
    mae = float(np.abs(hu_gen[gmask] - hu_real[gmask]).mean())
    print(f'MAE dentro de G: {mae:.1f} HU  (DIAGNOSTICO, NO resultado de tesis)')
    print(f'  El MAE absoluto en HU lo dominan los voxeles de metal, que llegan a miles de HU: un error '
          f'relativo pequeno sobre el metal pesa mas que el hueso entero. No es una metrica de calidad.')
    if paso_ck is not None:
        print(f'  Este ckpt quedo en el paso {paso_ck}. Si viene de `run01`, esta PASADO de su optimo '
              f'(minimo de validacion en ~25 000, ver #134): no es el mejor modelo, es el ultimo.')

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    borrado = hu_real.copy()
    borrado[gmask] = -1000.0
    paneles = [('CT original', hu_real), ('entrada: G borrada', borrado),
               ('salida compuesta', hu_sal), ('solo lo generado en G', np.where(gmask, hu_gen, -1000.0))]
    fig, ax = plt.subplots(1, 4, figsize=(17, 4.6))
    for a, (tit, img) in zip(ax, paneles):
        a.imshow(img, cmap='gray', vmin=-200, vmax=1300)
        a.set_title(tit, fontsize=10)
        a.set_xticks([]); a.set_yticks([])
    fig.suptitle(f'{m["caso"]} corte {m["k"]} — ckpt en el paso {paso_ck}, DIAGNOSTICO, NO es un resultado de tesis '
                 f'(MAE en G: {mae:.0f} HU)', fontsize=10)
    fig.tight_layout()
    salida = args.out_dir / f'a6_{m["caso"]}_k{m["k"]:04d}.png'
    fig.savefig(salida, dpi=130)
    plt.close(fig)
    print(f'lamina: {salida}')

    if args.nifti:
        escribe_nifti(args.out_dir, args.cache, m['caso'], m['k'], hu_real, hu_sal)


if __name__ == '__main__':
    main()
