"""Entrenamiento del renderizador del Diseno A (difusion en espacio de imagen).

ESTADO: EL DISENO NO ESTA PREINSCRITO
-------------------------------------
`experiments/objetivo3/diseno_A.md` sigue en BORRADOR y tiene cuatro `[DECIDIR]` de la autora. Este
script **existe para poder medir** (prueba corta de 200 pasos en Khipu: s/paso y memoria, #89), que
es el paso 3 de la semana 1. Correrlo entero antes de la preinscripcion contradiria el propio
diseno, asi que `--pasos` no tiene valor por defecto grande y la bandera `--preinscrito` deja
constancia de si la corrida es piloto de medicion o corrida definitiva.

CONTROLES QUE PUEDEN FALLAR (se corren al arrancar, antes de gastar GPU)
------------------------------------------------------------------------
1. Identidad multi-ventana (`common.ventanas.verificar`): ida y vuelta < 1e-6 HU.
2. Aislamiento: ningun caso de test en el cargador. Se comprueba contra `p1_particion.csv`.
3. Enmascarado: con `G` toda a cero la perdida es exactamente 0 (la perdida vive solo en `G`).
4. (version 2, D-b) Con peso uniforme 1 la perdida ponderada es identica a la de la version 1.
5. (version 2, D-a) La fraccion de parches tamano tornillo sorteada por el muestreador queda a
   menos de 0.02 de la fraccion objetivo (20 000 sorteos con la semilla de la corrida).
Si alguno falla, el script aborta.

VERSION 2, OPCION D (`experiments/objetivo3/v2_plan.md`)
--------------------------------------------------------
Sin `--componentes` ni `--anillo-mm` el entrenamiento es exactamente el de la version 1 (run04).
- D-a `--componentes v2_d_componentes_run04.csv --frac-tornillo p`: sobremuestreo con reemplazo de
  los parches de componentes tamano tornillo hasta que salgan con fraccion `p` por sorteo.
- D-b `--anillo-mm a b --peso-anillo w`: dentro de `G`, peso `w` a `a`-`b` mm en el plano de `M`.
  La validacion mide las DOS perdidas: `perdida_val` (sin ponderar, comparable con run04; elige
  `mejor.pt`) y `perdida_val_pond` (la que se optimiza; elige `mejor_pond.pt`).
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from pathlib import Path

import torch

_RAIZ = Path(__file__).resolve().parents[2]
for _p in (str(_RAIZ / 'src'), str(Path(__file__).resolve().parent)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from common.ventanas import verificar as verificar_ventanas  # noqa: E402
from datos import ParchesMetal, lee_componentes_tornillo, lee_particion  # noqa: E402
from difusion import Difusion, perdida  # noqa: E402
from modelo import CANALES_ENTRADA, UNetDifusion  # noqa: E402

# Semilla del sorteo de `t` y del ruido en la validacion. Fija y distinta de `--semilla` para que la
# medicion no quede correlacionada con el estado del entrenamiento. Cambiarla rompe la comparabilidad
# de `perdida_val` con lo ya medido, asi que no se expone como argumento.
SEMILLA_VAL = 20261004


def controles(ds: ParchesMetal, particion: Path, modelo, dif: Difusion,
              dispositivo: str, pesos_muestreo: torch.Tensor | None = None,
              tornillo: dict[str, int] | None = None, frac_objetivo: float | None = None,
              semilla: int = 0) -> dict[str, str]:
    """Los tres controles de la cabecera. Lanza si alguno no cierra."""
    res: dict[str, str] = {}

    v = verificar_ventanas()
    res['identidad_ventanas'] = f"peor {v['peor']:.3g} HU"

    test = lee_particion(particion, ('test',))
    fuga = sorted(set(ds.por_caso) & test)
    if fuga:
        raise RuntimeError(f'FUGA DE TEST: {len(fuga)} casos en el cargador: {fuga[:5]}')
    res['aislamiento'] = f'0 de {len(test)} casos de test en el cargador'

    lote = next(iter(torch.utils.data.DataLoader(ds, batch_size=2)))
    g0 = torch.zeros_like(lote['g']).to(dispositivo)
    with torch.no_grad():
        p = perdida(modelo, lote['x0'].to(dispositivo), lote['cond'].to(dispositivo), g0, dif)
    if float(p) != 0.0:
        raise RuntimeError(f'la perdida no vive solo en G: con G vacia da {float(p)!r}')
    res['perdida_solo_en_G'] = 'G vacia -> 0.0'

    if 'w' in lote:
        x0, cond, g = (lote[k].to(dispositivo) for k in ('x0', 'cond', 'g'))
        with torch.no_grad():
            gen = torch.Generator(device=dispositivo)
            a = perdida(modelo, x0, cond, g, dif, generador=gen.manual_seed(1))
            b = perdida(modelo, x0, cond, g, dif, generador=gen.manual_seed(1),
                        peso=torch.ones_like(g))
        if not torch.allclose(a, b, rtol=1e-6, atol=0.0):
            raise RuntimeError(f'peso uniforme cambia la perdida: {float(a)!r} vs {float(b)!r}')
        en_anillo = float(((lote['w'] != 1.0) & (lote['g'] > 0)).float().mean())
        res['peso_uniforme_identico'] = f'{float(a):.6g} = {float(b):.6g}'
        res['frac_pixeles_anillo_lote'] = f'{en_anillo:.4f}'

    if pesos_muestreo is not None:
        gen = torch.Generator().manual_seed(semilla)
        idx = torch.multinomial(pesos_muestreo, 20_000, replacement=True, generator=gen)
        es = torch.tensor([tornillo[ds.indice[i][0]] for i in idx.tolist()], dtype=torch.float64)
        frac = float(es.mean())
        if abs(frac - max(frac_objetivo, ds_frac_natural(ds, tornillo))) > 0.02:
            raise RuntimeError(f'sobremuestreo: fraccion sorteada {frac:.4f} frente a objetivo '
                               f'{frac_objetivo}')
        res['sobremuestreo'] = f'fraccion tornillo sorteada {frac:.4f} (objetivo {frac_objetivo})'
    return res


def ds_frac_natural(ds: ParchesMetal, tornillo: dict[str, int]) -> float:
    """Fraccion de parches tamano tornillo en el manifiesto, sin sobremuestreo."""
    return sum(tornillo[s] for s, _ in ds.indice) / len(ds.indice)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--cache', type=Path, required=True, help='cache de A1 (.npz por corte)')
    p.add_argument('--particion', type=Path,
                   default=_RAIZ / 'experiments/objetivo1/p1_particion.csv')
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--pasos', type=int, default=200, help='200 = prueba corta de medicion (#89)')
    p.add_argument('--lote', type=int, default=4)
    p.add_argument('--lado', type=int, default=256)
    p.add_argument('--base', type=int, default=64)
    p.add_argument('--lr', type=float, default=1e-4)
    p.add_argument('--objetivo', choices=('v', 'eps'), default='v')
    p.add_argument('--semilla', type=int, default=20260920)
    p.add_argument('--dispositivo', default='cuda' if torch.cuda.is_available() else 'cpu')
    p.add_argument('--trabajadores', type=int, default=2)
    p.add_argument('--cada', type=int, default=25, help='cada cuantos pasos se registra')
    p.add_argument('--borrar-contexto', action='store_true',
                   help='brazo de sensibilidad de #96; NO es el piloto')
    p.add_argument('--preinscrito', action='store_true',
                   help='marcar la corrida como posterior a la preinscripcion de diseno_A.md')
    p.add_argument('--manifiesto', type=Path,
                   default=_RAIZ / 'experiments/objetivo3/a5_manifiesto_train.csv',
                   help='conjunto congelado por la decision 2026-09-21 (R1-R3). '
                        '`--manifiesto ""` entrena con el crudo de A1b, que NO es el de la decision')
    p.add_argument('--manifiesto-val', type=Path,
                   default=_RAIZ / 'experiments/objetivo3/a5_manifiesto_val.csv',
                   help='conjunto de validacion (#105, R2 aplicado tambien a val: 896 parches, '
                        '3 casos). `--manifiesto-val ""` apaga la validacion')
    p.add_argument('--lotes-val', type=int, default=16,
                   help='lotes de validacion por medicion; fijo para que la cifra sea comparable '
                        'entre pasos')
    p.add_argument('--cada-ckpt', type=int, default=2000,
                   help='cada cuantos pasos se guarda ckpt reanudable. El limite de cola de Khipu es '
                        'de 24 h: sin esto, un corte pierde toda la corrida')
    p.add_argument('--reanudar', action='store_true',
                   help='continua desde `ckpt.pt` en --out si existe (modelo, optimizador y paso)')
    v2 = p.add_argument_group('version 2, opcion D (v2_plan.md); sin estas banderas = run04')
    v2.add_argument('--componentes', type=Path, default=None,
                    help='D-a: tabla versionada de v2_d_componentes.py (Caso, comp, tornillo)')
    v2.add_argument('--frac-tornillo', type=float, default=None,
                    help='D-a: fraccion objetivo de parches tamano tornillo por sorteo')
    v2.add_argument('--anillo-mm', type=float, nargs=2, default=None, metavar=('A', 'B'),
                    help='D-b: anillo (mm, en el plano) alrededor de M que recibe --peso-anillo')
    v2.add_argument('--peso-anillo', type=float, default=1.0,
                    help='D-b: peso del anillo dentro de G (1 = sin efecto)')
    v2.add_argument('--cache-T', type=Path, default=None,
                    help='B: carpeta de v2_b_cache_T.py (T por parche + escala.json); anade el canal T (12 entradas)')
    args = p.parse_args()
    if (args.componentes is None) != (args.frac_tornillo is None):
        p.error('--componentes y --frac-tornillo van juntos')
    if args.frac_tornillo is not None and not 0.0 < args.frac_tornillo < 1.0:
        p.error('--frac-tornillo tiene que estar en (0, 1)')
    if args.anillo_mm is not None and (args.peso_anillo <= 0 or
                                       not 0 <= args.anillo_mm[0] < args.anillo_mm[1]):
        p.error('--anillo-mm A B con 0 <= A < B y --peso-anillo > 0')

    torch.manual_seed(args.semilla)
    args.out.mkdir(parents=True, exist_ok=True)

    man = args.manifiesto if (args.manifiesto and str(args.manifiesto)) else None
    if man and not Path(man).exists():
        raise SystemExit(f'ABORTA: falta el manifiesto {man}. Es el conjunto congelado (R1-R3, '
                         f'decision 2026-09-21). Para entrenar sin el, pasa --manifiesto ""')
    escala_T = None
    if args.cache_T is not None:
        escala_T = float(json.loads((args.cache_T / 'escala.json').read_text(encoding='utf-8'))['escala'])
    kw_T = dict(cache_T=args.cache_T, escala_T=escala_T)
    ds = ParchesMetal(args.cache, args.particion, ('train',), args.lado, args.borrar_contexto,
                      inclusion=man, anillo_mm=args.anillo_mm, peso_anillo=args.peso_anillo, **kw_T)
    man_val = args.manifiesto_val if (args.manifiesto_val and str(args.manifiesto_val)) else None
    if man_val and not Path(man_val).exists():
        raise SystemExit(f'ABORTA: falta el manifiesto de validacion {man_val}. '
                         f'Para entrenar sin validacion, pasa --manifiesto-val ""')
    ds_val = (ParchesMetal(args.cache, args.particion, ('val',), args.lado, args.borrar_contexto,
                           inclusion=man_val, anillo_mm=args.anillo_mm,
                           peso_anillo=args.peso_anillo, **kw_T) if man_val else None)
    pesos_muestreo, tornillo, info_muestreo = None, None, None
    if args.componentes is not None:
        tornillo = lee_componentes_tornillo(args.componentes)
        pesos_muestreo, info_muestreo = ds.pesos_sobremuestreo(tornillo, args.frac_tornillo)
    dif = Difusion(objetivo=args.objetivo)
    entrada = CANALES_ENTRADA + (1 if args.cache_T is not None else 0)
    modelo = UNetDifusion(base=args.base, entrada=entrada).to(args.dispositivo)

    chk = controles(ds, args.particion, modelo, dif, args.dispositivo, pesos_muestreo,
                    tornillo, args.frac_tornillo, args.semilla)
    meta = {'pasos': args.pasos, 'lote': args.lote, 'lado': args.lado, 'base': args.base,
            'objetivo': args.objetivo, 'semilla': args.semilla, 'dispositivo': args.dispositivo,
            'parametros': modelo.n_parametros(), 'preinscrito': bool(args.preinscrito),
            'borrar_contexto': bool(args.borrar_contexto),
            'manifiesto': str(man) if man else None,
            'datos': ds.resumen(), 'controles': chk,
            'datos_val': ds_val.resumen() if ds_val is not None else None,
            'manifiesto_val': str(man_val) if man_val else None,
            'cada_ckpt': args.cada_ckpt,
            'v2_D': {'componentes': str(args.componentes) if args.componentes else None,
                     'sobremuestreo': info_muestreo,
                     'anillo_mm': args.anillo_mm, 'peso_anillo': args.peso_anillo},
            'entrada': entrada,
            'v2_B': ({'cache_T': str(args.cache_T), 'escala_T': escala_T,
                      'lambda_por_mm': json.loads((args.cache_T / 'escala.json').read_text(encoding='utf-8'))
                      ['lambda_por_mm']} if args.cache_T is not None else None)}
    (args.out / 'entrenar_meta.json').write_text(json.dumps(meta, indent=2), encoding='utf-8')
    for k, v in chk.items():
        print(f'control {k}: {v}')
    print(f"datos: {ds.resumen()}  parametros: {modelo.n_parametros() / 1e6:.1f} M")
    if ds_val is not None:
        print(f'validacion: {ds_val.resumen()}')
    else:
        print('AVISO: sin validacion. No se podra ver si converge ni medir el margen Delta (D4).')
    if info_muestreo is not None:
        print(f'D-a sobremuestreo: {info_muestreo}')
    if args.cache_T is not None:
        faltan = ds.faltan_T() + (ds_val.faltan_T() if ds_val is not None else [])
        if faltan:
            raise SystemExit(f'ABORTA: {len(faltan)} parches sin T precalculada en {args.cache_T} '
                             f'(p. ej. {faltan[:3]}); correr v2_b_cache_T.py antes de entrenar')
        print(f'B canal T: escala {escala_T:.6g} (cond con {entrada - 3} canales, modelo con {entrada} entradas)')
    if args.anillo_mm is not None:
        print(f'D-b peso {args.peso_anillo} en {args.anillo_mm[0]}-{args.anillo_mm[1]} mm de M')
    if not args.preinscrito:
        print('AVISO: corrida NO preinscrita. Es piloto de medicion (#89), no resultado de tesis.')

    muestreador = None
    if pesos_muestreo is not None:
        # con reemplazo y `len(ds)` sorteos por "epoca": misma longitud de epoca que run04, otra
        # composicion. Generador propio para que la secuencia dependa solo de `--semilla`.
        muestreador = torch.utils.data.WeightedRandomSampler(
            pesos_muestreo, num_samples=len(ds), replacement=True,
            generator=torch.Generator().manual_seed(args.semilla))
    cargador = torch.utils.data.DataLoader(
        ds, batch_size=args.lote, shuffle=muestreador is None, sampler=muestreador,
        num_workers=args.trabajadores, drop_last=True, pin_memory=args.dispositivo == 'cuda')
    ponderada = args.anillo_mm is not None
    opt = torch.optim.AdamW(modelo.parameters(), lr=args.lr)

    cargador_val = (torch.utils.data.DataLoader(
        ds_val, batch_size=args.lote, shuffle=False, num_workers=0, drop_last=True)
        if ds_val is not None else None)

    def mide_val() -> tuple[float, float]:
        """Perdida media sobre `--lotes-val` lotes fijos de validacion.

        Fijos y sin barajar a proposito: la cifra tiene que ser comparable entre pasos. Con lotes
        distintos cada vez, la curva mezclaria convergencia con que parches tocaron.

        **El generador tambien se fija, y no es un detalle.** `perdida` sortea el nivel de ruido `t`
        y el ruido mismo; la MSE de difusion depende fuertemente de `t`. Con `generador=None` cada
        medicion cae en niveles distintos y la columna oscila por COMO se midio, no por lo que
        aprendio el modelo: en el job 54367 eso dio saltos de +-15% entre pasos consecutivos
        (0.0547 -> 0.0718 -> 0.0643 en 4 000 pasos), suficiente para tapar la tendencia que la
        columna existe para mostrar. Con la semilla fija, dos pasos distintos se comparan sobre el
        MISMO conjunto de (parche, t, ruido) y la diferencia es atribuible al modelo.
        """
        nan = float('nan')
        if cargador_val is None:
            return nan, nan
        modelo.eval()
        gen = torch.Generator(device=args.dispositivo)
        gen.manual_seed(SEMILLA_VAL)
        gen_p = torch.Generator(device=args.dispositivo)
        gen_p.manual_seed(SEMILLA_VAL)  # mismos (t, ruido) para la ponderada: solo cambia el peso
        total, total_p, n = 0.0, 0.0, 0
        with torch.no_grad():
            for i, lv in enumerate(cargador_val):
                if i >= args.lotes_val:
                    break
                x0, cond, g = (lv[k].to(args.dispositivo) for k in ('x0', 'cond', 'g'))
                total += float(perdida(modelo, x0, cond, g, dif, generador=gen).detach())
                if ponderada:
                    total_p += float(perdida(modelo, x0, cond, g, dif, generador=gen_p,
                                             peso=lv['w'].to(args.dispositivo)).detach())
                n += 1
        modelo.train()
        return total / max(n, 1), (total_p / max(n, 1) if ponderada else nan)

    def guarda(ruta: Path, paso_actual: int) -> None:
        """Checkpoint REANUDABLE: modelo, optimizador y paso. Sin el optimizador, reanudar reinicia
        los momentos de AdamW y la curva da un salto artificial."""
        torch.save({'modelo': modelo.state_dict(), 'opt': opt.state_dict(),
                    'paso': paso_actual, 'meta': meta}, ruta)

    # [minimo de validacion, paso en que ocurrio]. Lista y no dos escalares para poder asignarla
    # desde el cuerpo del bucle sin `nonlocal`.
    mejor = [float('inf'), -1]
    mejor_p = [float('inf'), -1]
    paso = 0
    modo = 'w'
    ck_previo = args.out / 'ckpt.pt'
    if args.reanudar and ck_previo.exists():
        prev = torch.load(ck_previo, map_location=args.dispositivo, weights_only=False)
        modelo.load_state_dict(prev['modelo'])
        if 'opt' in prev:
            opt.load_state_dict(prev['opt'])
        paso = int(prev.get('paso', 0))
        modo = 'a'
        print(f'REANUDADO desde {ck_previo} en el paso {paso}')
        # El minimo de validacion tambien se reanuda: sin esto, la primera validacion tras reanudar
        # sobrescribiria `mejor.pt` aunque fuera peor que el minimo ya guardado antes del corte.
        for ruta, clave, reg in ((args.out / 'mejor.pt', 'perdida_val', mejor),
                                 (args.out / 'mejor_pond.pt', 'perdida_val_pond', mejor_p)):
            if ruta.exists():
                m = torch.load(ruta, map_location='cpu', weights_only=False)
                reg[0], reg[1] = float(m[clave]), int(m['paso'])
                print(f'  minimo previo en {ruta.name}: {reg[0]:.5f} en el paso {reg[1]}')
        if 'opt' not in prev:
            print('AVISO: el ckpt no traia estado del optimizador; AdamW arranca con momentos a cero.')

    curva = open(args.out / 'curva.csv', modo, newline='', encoding='utf-8')
    w = csv.writer(curva)
    if modo == 'w':
        # `s_por_paso` es el promedio ACUMULADO y se conserva por comparabilidad con el piloto;
        # `s_tramo` es el ritmo del ultimo tramo, que es lo que #114 pedia y no se podia leer.
        w.writerow(['paso', 'perdida', 'perdida_val', 's_por_paso', 's_tramo', 'gb_max']
                   + (['perdida_val_pond'] if ponderada else []))

    modelo.train()
    t0, it = time.time(), iter(cargador)
    paso0, t_tramo, paso_tramo = paso, time.time(), paso
    while paso < args.pasos:
        try:
            lote = next(it)
        except StopIteration:
            it = iter(cargador)
            continue
        l = perdida(modelo, lote['x0'].to(args.dispositivo), lote['cond'].to(args.dispositivo),
                    lote['g'].to(args.dispositivo), dif,
                    peso=lote['w'].to(args.dispositivo) if ponderada else None)
        opt.zero_grad(set_to_none=True)
        l.backward()
        torch.nn.utils.clip_grad_norm_(modelo.parameters(), 1.0)
        opt.step()
        paso += 1
        if paso % args.cada == 0 or paso == args.pasos:
            gb = (torch.cuda.max_memory_allocated() / 1e9
                  if args.dispositivo == 'cuda' else 0.0)
            ahora = time.time()
            sp = (ahora - t0) / max(paso - paso0, 1)
            st = (ahora - t_tramo) / max(paso - paso_tramo, 1)
            t_tramo, paso_tramo = ahora, paso
            val = float(l.detach())
            pv, pvp = mide_val()
            w.writerow([paso, round(val, 6), ('' if pv != pv else round(pv, 6)),
                        round(sp, 4), round(st, 4), round(gb, 2)]
                       + ([('' if pvp != pvp else round(pvp, 6))] if ponderada else []))
            curva.flush()
            txt_val = 'sin val' if pv != pv else f'val {pv:.5f}'
            print(f'paso {paso}/{args.pasos} perdida {val:.5f} {txt_val} '
                  f'{st:.3f} s/paso (tramo) {gb:.1f} GB', flush=True)
            # El ultimo paso NO es el mejor modelo. En el job 54367 la validacion toco su minimo
            # alrededor del paso 44 000 y al 144 500 estaba al DOBLE, mientras `ckpt.pt` se
            # sobrescribia cada 5 000 pasos: las pesas buenas se perdieron. `mejor.pt` guarda el
            # minimo de validacion y se escribe SIN el optimizador, porque es para inferencia.
            if pv == pv and pv < mejor[0]:
                mejor[0], mejor[1] = pv, paso
                torch.save({'modelo': modelo.state_dict(), 'paso': paso, 'perdida_val': pv,
                            'meta': meta}, args.out / 'mejor.pt')
                print(f'  nuevo minimo de validacion: {pv:.5f} en el paso {paso} -> mejor.pt',
                      flush=True)
            if ponderada and pvp == pvp and pvp < mejor_p[0]:
                mejor_p[0], mejor_p[1] = pvp, paso
                torch.save({'modelo': modelo.state_dict(), 'paso': paso,
                            'perdida_val_pond': pvp, 'meta': meta}, args.out / 'mejor_pond.pt')
                print(f'  nuevo minimo de validacion ponderada: {pvp:.5f} en el paso {paso} '
                      f'-> mejor_pond.pt', flush=True)
        if args.cada_ckpt > 0 and paso % args.cada_ckpt == 0:
            guarda(args.out / 'ckpt.pt', paso)
            print(f'ckpt guardado en el paso {paso}', flush=True)
    curva.close()

    guarda(args.out / 'ckpt.pt', paso)
    if mejor[1] >= 0:
        print(f'MEJOR VALIDACION: {mejor[0]:.5f} en el paso {mejor[1]} (mejor.pt). '
              f'Ultimo paso: {paso}. Si la distancia entre ambos es grande, el modelo paso de largo '
              f'el minimo y el `ckpt.pt` final NO es el que hay que usar.', flush=True)
    if mejor_p[1] >= 0:
        print(f'MEJOR VALIDACION PONDERADA: {mejor_p[0]:.5f} en el paso {mejor_p[1]} '
              f'(mejor_pond.pt).', flush=True)
    sp = (time.time() - t0) / max(paso - paso0, 1)
    print(f'LISTO. {paso} pasos, {sp:.3f} s/paso. '
          f'Extrapolacion a 30 000 pasos: {sp * 30_000 / 3600:.1f} h')


if __name__ == '__main__':
    main()
