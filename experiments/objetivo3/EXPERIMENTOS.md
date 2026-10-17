# Indice de experimentos del Objetivo 3

> **Para que existe.** Procedencia de artefactos: quien produjo cada cosa y si se puede usar. Mismo
> formato que `experiments/objetivo2/EXPERIMENTOS.md` (leyenda de `Origen` alli). No sustituye a
> `docs/ESTADO.md` (por donde voy) ni a `docs/04-implicancias.md`. El diseno del renderizador esta en
> `diseno_A.md`. Manual del cluster: `experiments/KHIPU.md`.
>
> **Regla de mantenimiento:** al anadir un experimento, anadir su fila. Si queda superado y nadie lo
> importa, `git mv` a `experiments/obsoletos/objetivo3/` y anadir su fila en `experiments/obsoletos/README.md`.
>
> **Modelo vigente: run04** (sin fuga, #166). Todo lo generado o medido con run01/run02 (`mejor_37k`) o run03 esta
> archivado en `experiments/obsoletos/objetivo3/outputs/` y **no es citable** (#166, #171). Resultados citables del
> Objetivo 3: solo los de la corrida final con run04 y la pose corregida (#173: `a15_cadena_pose`, `a19_pose`,
> `a23_final_run04`, `a24`), cuando existan.
> Las salidas (`outputs/`) no estan versionadas. Actualizado el 2026-10-15 (DEC 2026-10-15: lecturas del TOST,
> variantes posteriores y comparador parametrico; seccion 6c).

## 1. Diseno y datos de entrenamiento

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `diseno_A.md` | diseno del renderizador y de la evaluacion | autora + asistente | **CONGELADO** el 2026-10-09 (seccion 0) + **ENMIENDA 2026-10-11 (run04)**, antes de tocar test con run04 |
| `a1_parches.py`, `a1_casos.csv` | parches 2.5D **por corte** | script | **SUPERADO por A1b** (#102), congelado como evidencia de #102. **NO MOVER:** lo importan `a1b` y `src/common/region.py` |
| `a1b_parches_componente.py` | parches 2.5D **por componente** (decision D2) | script | **VIGENTE**. Lo importan `a3`, `a4`, `a15`, `a23` y `src/renderizador/datos.py` |
| `a3_laminas_componentes.py`, `a3_revision_componentes.csv` / `.md` | laminas de 40 componentes para fijar el criterio de implante (#104) | script + autora | **CERRADO**: 40 de 40 con veredicto; 3 no ortopedicos quitados del manifiesto de run04 (#167) |
| `a4_html_componentes.py` | vista 3D interactiva de componentes | script | **VIGENTE**. **NO MOVER:** `a5` importa `CUERPO_HU`, `mascara_cuerpo` |
| `a5_criterio_inclusion.py`, `a5_conjunto.csv` | criterio R1-R3 | script | **VIGENTE** (`01-decisiones.md`, 2026-09-21) |
| `a5_manifiesto_train_run04.csv` | entrenamiento de run04: **14 182 parches, 39 casos** | script + autora | **VIGENTE** (`01-decisiones.md` 2026-10-11) |
| `a5_manifiesto_val.csv` | validacion: 896 parches, 3 casos | script | **VIGENTE** |
| `a5_manifiesto_train.csv`, `_sin163.csv`, `_sin166.csv` | manifiestos de run01/run02, run03 y paso intermedio | script | **SUPERADOS** por `_run04` (#163, #166, #167). Se conservan por procedencia |

## 2. Entrenamiento

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `a7_run04.sbatch` | entrenamiento de run04 (60 000 pasos, mismos hiperparametros que run02) | Khipu 55706 | **VIGENTE**. Salida en `outputs/a7/run04/`; minimo de validacion en el paso 16 500 (#168) |
| `v2_d_componentes.py` -> `v2_d_componentes_run04.csv` / `.md` | version 2, D-a: componentes del manifiesto de run04 marcados tamano tornillo (500-4000 mm3) | script (local, necesita `outputs/a1b/a1b_componentes.csv`) | **ESCRITO 2026-10-13, POR CORRER** (la tabla no existe aun) |
| `a7_cache_T.sbatch`, `v2_b_cache_T.py`, `a7_run05b.sbatch` | version 2, B: cache del canal T y run05b (D + B) | Khipu | **CORRIDOS** 2026-10-14 (cache 56650; run05b 56721-56724) |
| `a16_v2.sbatch`, `a15_cadena_v2.sbatch`, `v2_eleccion.sbatch` + `v2_eleccion.py` | version 2: calibracion de `delta`, cadena en validacion y regla de eleccion aprobada | Khipu 56777-56781 | **CORRIDOS 2026-10-14**: "no mejora" (#182); resultado en `run05/v2_eleccion.md` |
| `a15_cadena_v2.sbatch` (`ETAPAS=final EXPLORATORIO=1`), `a23_v2.sbatch` | version 2 en prueba, EXPLORATORIO y POSTERIOR (declarado en `v2_plan.md`) | Khipu 56791-56794 | **CORRIDO 2026-10-14**; E-A1 de v2 visto (#184). `a23_v2.sbatch` con `SUF=_d003` (DEC 2026-10-15 pto 19): **CORRIDO** 56868/56869; #190 |
| `a20_v2.sbatch` | version 2: `a20` en validacion (Delta propio) y prueba + `a24`, en Khipu (CPU), sin bajar NIfTI | Khipu | Job 56847 abortado (doble envio). Ampliado 2026-10-15 (`ETAPA`, `VARIANTE`, candado). **CORRIDO** 56857-56865 (rc=0) -> `outputs/khipu_2026-10-15/v2_prueba/`; #190. El brazo parametrico se agrego despues; no depende del modelo y vale el de v1 |
| `a7_run05a.sbatch` | version 2, run05a = run04 + D (sobremuestreo + peso 2-10 mm), `FRAC=0.5`, `PESO=3` | Khipu 56570-56573 + 56704 | **CORRIDO 2026-10-14**: `mejor.pt` en 21 000 (val 0.0597); curva en `run05/run05a_curva.csv` |
| `../obsoletos/objetivo3/a7_entrenar.sbatch`, `a7_run03.sbatch` | run01/run02 y run03 | Khipu | **ARCHIVADOS** 2026-10-12 (fuga, #166) |
| `a14_curvas.py` | grafico de curvas de entrenamiento | script | **VIGENTE** (herramienta) |
| `a13_comparar_ckpt.py` | dos checkpoints pareados sobre validacion | script | herramienta; sus salidas con run01/run02 estan archivadas |

## 3. Mediciones sin modelo y muestras

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `a8_muestra_serie.py` | serie completa de cortes, HTML, `.nii.gz`, montaje | script | **VIGENTE** (herramienta); muestras con run01/run02 archivadas |
| `a9_suelo_representacion.py` | recorte del suelo de -1000 HU, sin modelo (#141) | script | **CORRIDO** sobre 23 058 parches; no usa el difusor |
| `a10_costura.py` | salto de HU en el borde de `G` (#139) | script | **VIGENTE** (herramienta) |
| `a12_roi_parametros.py` | perfil radial del artefacto real y parametros de las ROIs, sobre validacion | script | **CORRIDO**; no usa el difusor |
| `a16_calibrar_delta.py` | fija `delta` de `regla_suave` (v2, #152) | script (local) | **CORRIDO con run04 (2026-10-11, #172)**: `run04_mejor` **0.030**, `run04_60k` **0.050** -> `outputs/a16_run04/`, log `outputs/a16_run04.log`. Lo medido con el modelo archivado (0.05) esta en `../obsoletos/objetivo3/outputs/a16/`. Como aplicarlo: pendiente de la autora (#172) |
| `a22_hu_copiapega.py` | HU de la copia y pegado (mediana del metal de entrenamiento) | script | **CORRIDO con run04: 5371 HU** (`outputs/a22_run04/`) |

## 4. Cadena completa, cotejo y `Delta`

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `a11_rasterizar_tornillo.py` | pose -> `M`, `B_delta`, `G`; `pose_a_marco_crudo` (RAS+ del Obj 2 -> array crudo) y `control_pose` (#173) | script | **VIGENTE, CORREGIDO 2026-10-12**; lo importan `a15`, `a18`, `a19` |
| `a15_cadena_completa.py` | pelvis limpia -> pose -> `M` -> generacion; **no reanudable** | script | **VIGENTE** |
| `a15_cadena_pose.sbatch` + `a17_cotejo.py` + `a20_evaluador_ea2.py` | con la pose corregida (#173), un job por punto de control: cotejo (0101/0102) -> `s` de `Delta` -> corrida final de E-A2 (13 de test); cada uno con su limite calibrado (#172 (A)) | Khipu 56243/56244 + local | **CORRIDO** (2026-10-12, rtxa6000 g002, rc=0). Cotejo: `run04_mejor` 13 frente a 7 (#174); `Delta` 196.3 / 115.8 HU (#175). Salidas en `outputs/obj3_pose/`; resumen versionado `resultados_validacion_pose.md` |
| `../obsoletos/objetivo3/outputs/pose_espejada/` | todo lo generado con la pose espejada: cotejo, `Delta`, control shard (identico bit a bit, #170: la conclusion sobre la GPU sigue valiendo), corrida final, Peters, material | Khipu | **ARCHIVADO** 2026-10-12 (#173) |
| `../obsoletos/objetivo3/a15_cadena.sbatch`, `a15_cotejo.sbatch`, `a15_delta.sbatch` | versiones con `mejor_37k`/`run01` | Khipu | **ARCHIVADOS** 2026-10-12 |
| `../obsoletos/objetivo3/a17_cotejo_resultado.md`, `a20_resultados.md` | resultados con `mejor_37k` | local | **ARCHIVADOS** 2026-10-12 (Peters, repetido en `a20_resultados_run04.md`) |

## 5. Brazo fisico (Peters / XCIST)

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `peters/` | configuracion y parche del script publicado de XCIST, fuera del clon (#146) | script | **VIGENTE** |
| `sonda_peters.md`, `a18_sonda_peters.py` | sonda de viabilidad preinscrita (2026-10-09 (2)) | script | **CORRIDA CON POSE ESPEJADA** (#173); `a18` corregido, no se repite (la viabilidad la cubre `a19_pose`) |
| `a19_peters_completo.py`, `a19_pose.sbatch` | brazo fisico con la pose corregida: validacion (0101/0102, `r` y material) -> 13 de test | Khipu 56245 | **CORRIDO** (2026-10-12, n006, rc=0; `r` = 6.1 HU). `a19_peters.sbatch`, `a19_final.sbatch`: pose espejada |
| `a21_cotejo_material.py` | material primario frente a tornillos reales (regla 2026-10-09 (5)) | script (local) | **REHECHO** 2026-10-12 sobre `peters_val` (`--dir-a19`): Ti 2 frente a 0 de 24 (#174, DECIDIDA: ningun material reproduce lo real; Ti el menos alejado) |

## 6. Corrida final (test, diseno congelado + enmienda)

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `casos_ea2_test.txt` | los 13 pacientes de test sin metal de E-A2 | script | **VIGENTE** |
| (corrida final del difusor) | ahora es la etapa `final` de `a15_cadena_pose.sbatch` | — | ver seccion 4 |
| `a23_ea1.py`, `a23_final_run04.sbatch` | E-A1: reconstruccion del implante real en test con metal (no usa la pose sintetica: #173 no lo toca) | Khipu 56355 | **CORRIDO** 2026-10-12 (`run04_mejor`, 0.030, shard rtxa6000, rc=0, 13 pacientes) -> `outputs/obj3_pose/a23_final_run04_d003/`; resumen en `resultados_prueba_v1.md` |
| `a24_contrastes.py` | TOST primario y sensibilidades; dos lecturas de `Delta` para `run04_60k` | script | **CORRIDO** sobre v1 (`resultados_prueba_v1.md`). Analisis congelado; las lecturas de DEC 2026-10-15 van en `a26` |
| `a25_html_sintesis.py` | HTML de inspeccion visual (3D y cortes original/sintetica/diferencia) desde los `.nii.gz` de `a15` -> `<carpeta>/html/<etiqueta>/` | script | **VIGENTE** (herramienta; no mide). Corrido 2026-10-12 sobre `obj3_pose/{final,delta}` (60 HTML) |
| `../obsoletos/objetivo3/a15_final.sbatch`, `a23_final.sbatch` | corrida final con `mejor_37k` | Khipu 55454, 55455 | **ARCHIVADOS** 2026-10-12 (fuga); no citables (#164, #171) |

## 6b. Diagnostico de la version 1 y version 2 (#176, 2026-10-13)

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `resultados_prueba_v1.md` | evaluacion de prueba de la version 1 (E-A2 `a24`, E-A1 `a23`) | local | **HECHO** (#177) |
| `d1_alcance_rayas.py`, `d1_resultado.md` | D1: alcance del artefacto real por anillo (todas las piezas y `--vol-max 4000`) | local | **HECHO**: tornillos ~10 mm |
| `d2_perfil_sintetico.py`, `d1_d2_resultado.md` | D2: perfil del artefacto sintetico con la misma metrica | local | **HECHO**: sintetico se apaga ~6 mm |
| `v2_plan.md` | plan de la version 2 = B + D (run05a, run05b), compuerta, regla de eleccion y analisis exploratorio declarado | autora + asistente | **EN CURSO**: entrenados; regla = "no mejora" (#182); evaluacion exploratoria en prueba **CORRIDA** (Khipu 56857-56865; #190) (`01-decisiones.md` 2026-10-13, 2026-10-14, 2026-10-14 (2)) |

## 6c. Decisiones del 2026-10-15 (cierre de `\GAPDEC`, lecturas del TOST; posteriores para v1, previas para v2)

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `visto.md` | inventario fechado de que resultados se vieron (D-extra 4) | asistente | **VIGENTE**: se agrega una fila por cada resultado nuevo visto |
| `a20_evaluador_ea2.py` (ampliado) | `suelo_frac` de Peters, `exceso_costura` en todos los brazos (D5), `--suelo-simetrico` (D1), `--excluir-cabeza-mm` (D2), `--r-min-mm/--r-max-mm` (anillos 8-16 mm), brazo `parametrico` (D12, DEC 2026-10-15 (2)) | script | **VIGENTE**; regresion exacta en `0012` |
| `a20_v1_variantes.sh` | las 8 variantes de `a20` sobre run04_mejor (v1), en local | local | **CORRIDO** 2026-10-15 (01:25-04:15) -> `outputs/obj3_pose/a20_variantes/` |
| `a26_lecturas.py` | desenlaces (D15), IC90 por permutacion (D14), margen minimo y comun (D16), Bland-Altman y Pitman-Morgan (pto 22) | script | **CORRIDO** sobre v1 (`outputs/a26/v1_*`); resultados en `resultados_prueba_v1.md` y `resultados_dec_2026-10-15.md`; #187 |
| `a27_preservacion_peters.py` | D8: RMSE y SSIM de Peters sin metal frente a la TC, fuera de `G` | script | **CORRIDO**: RMSE 31.4 HU, SSIM 0.907 (mediana) |
| `a15_cadena_completa.py` (`--sin-metal`, `--guardar-u-g`), `a15_diag.sbatch` | D-extra 2 (piso de ruido del difusor, `MODO=nulo`) y D7 (p95, `MODO=p95`) | Khipu 56867 / 56866 | **CORRIDOS** 2026-10-15 (rc=0) -> `outputs/khipu_2026-10-15/obj3_pose/`; #188 |
| `../registro/r_razon_banda_run04.py`, `../registro/registro_metodos_2026-10-15.md` | razon de parches de solo banda de run04 y registro de metodos que solo constaban en el codigo (decodificador P1, asinh, eje del corredor, landmarks, IC90 por anillo, Fisher) | local | **HECHO** 2026-10-15: razon 0.638 (5 526 / 8 656) |
| `a29_perfil.py`, `a20_pareado.sbatch` | perfil 0-12 mm por brazo y contraste pareado del difusor (#187, #188) | local + Khipu 56968 | **CORRIDO** 2026-10-15 |
| `a28_diag_p95.py` | D7: decodificacion regla_suave frente a solo LW del `u` de `G`, control real en `metal_0039` | local | **CORRIDO** 2026-10-15: veredicto "modelo" (#191) |
| `resultados_dec_2026-10-15.md` | resultados de D4, D8, variantes de v1, comparador parametrico, v2, D7, acuerdo en log, perfil (`a29`) y pareado | asistente | **EN CURSO**: falta D9 |
| (sin script) | D9 (poses del muestreador), D3 a ciegas, realismo (H5) | — | **POR ESCRIBIR** (el control con imagenes reales de D7 se corrio en `a28`) |
| `../registro/r_seccion_convexa.py`, `../registro/registro_2026-10-16.md` §3 | prueba de admision de `T` (B) estratificada por forma de la seccion del tornillo (#178); control: reproduce los 228 cortes y `n_pix` de `b_piloto/b_por_corte.csv` | local (asesor, capitulo3-r27), ~8 min | **CORRIDO** 2026-10-16, descriptivo y posterior: seccion compacta (elong <= 1.5, 1 comp.) d 0.079, e 0.012 (8 pac.) frente a alargada d 0.201, e 0.148 (13 pac.) |
| `../registro/r_integridad_ea2.py`, `../registro/registro_2026-10-16.md` §5 | medianas por brazo de SDC y dVol de hueso y metal en E-A2 (v1, prueba; resume columnas ya calculadas por `a20`, sin analisis nuevo); control: reproduce -301.0 HU y ruido de Peters 183.5 HU de `resultados_prueba_v1.md` | local (asesor, capitulo4-r01), segundos | **CORRIDO** 2026-10-16, descriptivo y posterior (n = 13): `run04_mejor` hueso SDC 0.677, dVol 0.098, metal SDC 0.862, dVol -0.190; Peters Ti 0.800, 0.121, 0.856, 0.283 |

## 7. Archivados

Inventario completo en `experiments/obsoletos/README.md`.

| Artefacto | Donde | Motivo |
|---|---|---|
| `a2_entrenar.sbatch` | `../obsoletos/objetivo3/` | piloto de 200 pasos (job 52074, #89 medida); lo sustituye `a7_entrenar.sbatch` |
| `a6_muestra_minima.py` | `../obsoletos/objetivo3/` | primera muestra de un solo corte (#116); la sustituyen `a8` y `a15` |
| salidas de run01/run02/run03 y todo lo medido con ellas | `../obsoletos/objetivo3/outputs/` | modelo con fuga (#166) |
