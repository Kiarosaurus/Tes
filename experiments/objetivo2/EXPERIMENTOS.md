# Indice de experimentos del Objetivo 2

> **Para que existe.** Este directorio tiene ~55 scripts y ~25 CSV, y hasta el 2026-09-22 no habia forma
> de saber, mirando el arbol, cual de ellos esta vigente, cual quedo superado, quien lo lleno y que lo
> consume. Esa falta de mapa ya produjo un error: el 2026-09-22 el asistente leyo una planilla vacia
> (`r1_revision_itksnap_revisor.csv`, 0 de 61) y concluyo que "el revisor no habia respondido", cuando
> la revision **si** se habia hecho, en otro formato y en otro archivo. Y al inventariar para escribir
> este indice aparecio **una segunda planilla vacia que nadie estaba siguiendo** (ver #123).
>
> **Que NO es.** No sustituye a `docs/ESTADO.md` (por donde voy) ni a `docs/04-implicancias.md`
> (hallazgos que tocan el argumento). Esto es **procedencia de artefactos**: quien produjo cada cosa y
> si se puede usar.
>
> **Regla de mantenimiento:** al anadir un experimento, anadir su fila. Al superar uno, no borrarlo:
> moverlo a *Superados* con el motivo; si ya nadie lo importa, `git mv` a `experiments/obsoletos/objetivo2/`
> y anadir su fila en `experiments/obsoletos/README.md`. Manual del cluster: `experiments/KHIPU.md`.

## Leyenda de `Origen`

| Valor | Significado |
|---|---|
| `script` | lo genera un `.py` de este directorio; reproducible |
| `Khipu` | lo genera un job de Slurm; lleva el numero de job |
| `autora` | lo llena la autora a mano |
| `revisor clinico` | lo llena el revisor clinico externo |
| `agente` | lo llena un agente de Claude |

---

## 1. R1 — marco de referencia de Kaiser y landmarks

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `r1_landmarks.py` / `.csv` | deteccion de los cinco landmarks; 179 filas | script | **VIGENTE** |
| `r1_resumen.py` / `r1_estados.csv` | estado por volumen; 179 filas, 78 col | script | **VIGENTE** |
| `r1_landmarks.md` | nota de la deteccion (la de v2a esta en `../obsoletos/objetivo2/`) | asistente | **VIGENTE** |
| `../obsoletos/objetivo2/r1_mosaico.py` | mosaico sagital de +-60 mm para revisar S1 | script | **ARCHIVADO** (ver 7) |
| `r1_auditoria_s1_agente.csv` | juicio del nivel de S1 sobre el mosaico; 70 filas | agente | **VIGENTE** como contraste |
| `r1_auditoria_s1_clinico.csv` | juicio del nivel de S1; **65 de 65 llenas** | revisor clinico | **VIGENTE — es la referencia que cita `main.tex`** |
| `r1_auditoria_s1.md` | procedencia y acuerdo entre los dos juicios | asistente | **VIGENTE** |
| `r1_cortes_itksnap.py` / `.csv` | posicion del punto de S1 en indices del archivo; 65 filas | script | **VIGENTE**; lo reusa R2 |
| `../obsoletos/objetivo2/r1_revision_itksnap_revisor.csv` / `.md` | 2da vuelta de S1 en ITK-SNAP; **0 de 61 llenas** | revisor clinico | **ARCHIVADO, NO BORRAR** (ver 7) |
| `r1_revision_laminas_revisor.csv` | 2da vuelta de S1 sobre laminas; 61 filas | pendiente | **ABIERTO** |
| `../obsoletos/objetivo2/r1_landmarks.v1-parcial.csv`, `.v2a.csv`, `r1_estados.v2a.csv` | versiones previas | script | **ARCHIVADOS**, se conservan por trazabilidad |

## 2. TS — cohorte de TotalSegmentator

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `ts_piloto.sbatch`, `ts_piloto_qc.py` / `.csv` | piloto de TS y su QC; 16 casos | Khipu 51300 | **VIGENTE** |
| `ts_cohorte.sbatch`, `ts_qc*.py`, `ts_nivel_s1.csv` | cohorte de TS y QC de nivel; 168 filas | Khipu | **VIGENTE** |
| `ts_componentes.py` / `.sbatch` | componentes por estructura | Khipu 51504/51522 | **VIGENTE** |
| `ts_cajas_limpias.py` / `.csv` | cajas tras limpieza; 2 864 filas | Khipu 51527 | **VIGENTE** |
| `ts_analisis.py` / `.md`, `ts_cohorte.md` | analisis de la cohorte | script | **VIGENTE** |

## 3. E8, E9, E9b, E11 — geometria medida

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `e8_censo_implantes.py`, `e8_componentes.csv` / `.md` | censo de implantes reales; 313 componentes | script | **VIGENTE** |
| `e9_corredor.py` | corredor por umbral HU | script | **SUPERADO por E9-TS** (#48: el umbral no representa el esponjoso). **NO BORRAR:** E9-TS, SAP y E12 le importan `tramo`, `evaluar_linea`, `muestrear` y las constantes |
| `e9b_densidad_s1.py` / `.csv` / `.md` | densidad por zona en S1; 121 filas | script | **VIGENTE** — componente 2 de SAP |
| `e11_perfil_axial.py` / `.md`, `e11_componentes.csv` | perfil de diametro de implantes reales; 144 filas | script | **VIGENTE** — de aqui sale el cilindro de 4.91 mm (D3) |

## 4. E9-TS — corredor sobre mascaras de TS

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `e9ts_corredor.py` | medicion del corredor; **modificado el 2026-09-22** para guardar el eje por altura (#121) | script | **VIGENTE** |
| `e9ts_corredor.csv` | 2 352 filas, 152 casos, 0 errores | Khipu 51505 | **VIGENTE — respalda cifras de `main.tex`. No sobrescribir** |
| `e9ts_corredor.sbatch`, `e9ts_3mm.sbatch`, `noche_e9ts.sh` | jobs de la corrida original | — | **VIGENTES** |
| `e9ts_ejes.sbatch` | segunda pasada para el eje por altura; `--out-dir` propio | — | **ABIERTO**: sin lanzar |
| `e9ts_resumen.py` / `.md` | tablas por cohorte | script | **VIGENTE** |
| `e9ts_repetibilidad.py` | repetibilidad | script | **VIGENTE** |
| `e9ts_revision_laminas.md` / `_autora.csv` (`.raw.csv` y `.sin_revisor.csv`: entregas originales) | condicion de reapertura del recorte de 6 mm; 16 de 16 revisadas, **0 `fallo_6mm`** | autora + medico | **CERRADO** (#131, 2026-10-04): no reabre la decision de 6 mm |
| `e9ts_revision_laminas_agente.csv` / `.raw.csv` | veredicto preliminar del agente `revisor-laminas-corredor` | agente | **VIGENTE** como contraste |
| `maintex_cifras.py` / `.md` | cifras que van al documento | script | **VIGENTE** |

## 5. SAP y muestreador — Objetivo 2 propiamente dicho

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `preinscripcion_muestreador.md` | distribucion de poses y metrica, congeladas antes de medir | autora + asistente | **VIGENTE — congelada 2026-09-22** |
| `src/muestreador/sap.py`, `muestreo.py` | la metrica y el muestreador | script | **VIGENTE** |
| `e12_sap_control.py` / `.md` | seis controles de SAP (C1-C6) | script | **VIGENTE** |
| `e13_muestreo_sap.py` / `.sbatch` | muestreo + SAP + Wasserstein-1 | script | **VIGENTE** |
| `e13_poses.csv` / `e13_sap.md` | cohorte primaria, 72 casos, 3 600 poses | Khipu 52175 | **VIGENTE — el resultado del Objetivo 2** |
| `e13_poses_g3.csv` / `e13_sap_g3.md` | sensibilidad, 49 casos | Khipu 52175 | **VIGENTE** |
| `e13_poses_piloto.csv` / `e13_sap_piloto.md` | 2 casos de grupo 1, prueba del camino | script | **NO ES RESULTADO**: fuera de cohorte |
| `e13b_estratificado.py` / `.md` | W1 por viabilidad del corredor | script | **VIGENTE — post hoc declarado** (#122) |
| `e14_relleno_envolvente.py` / `e14_relleno.sbatch` -> `outputs/e14_relleno.csv` | envolvente con cierre frente a cierre + relleno; 152 casos | Khipu | **CERRADO** (#131): 0 casos cambian; cierra #127 pto 13 |
| `e11_componentes.csv` | componentes medidos por E11 | script | **VIGENTE** (ver 3) |
| `verificar_coherencia.py` | 104 comprobaciones (2026-10-08): codigo, preinscripcion, controles y `main.tex` dicen lo mismo | script | **VIGENTE — correr antes de cerrar sesion** |

## 6. R2 — verificacion del nivel del segundo corredor (#121)

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `r2_nivel_pico_itksnap.py` / `.csv` | muestra de 18 casos e indices | script | **ABIERTO** |
| `r2_nivel_pico_laminas.py` | laminas sagitales alargadas, con indices al pie | script | **VIGENTE** |
| `r2_nivel_pico_revisor.md` (la version previa, `.ANTERIOR.md`, en `../obsoletos/objetivo2/`) | instrucciones de la revision de S2 | asistente | **ABIERTO — en pausa**: la linea marca una altura y con el sacro inclinado admite dos respuestas. Esperar al eje por altura |
| `outputs/r2_s1_revalidacion/` | 61 laminas con la cruz de S1 | script | **ABIERTO**: listas para revisar |
| `outputs/r2_nivel_pico/` | 18 laminas con la altura del pico | script | **EN PAUSA** |

## 6 bis. R3 — cribado de fractura (#125)

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `r3_fractura_grupos.csv` | reparto ciego, 15 estrechos + 15 control; **no se entrega al revisor** | script | **VIGENTE** |
| `r3_fractura_revisor.csv` / `.md` (`.raw.csv`: entrega original) | juicio de fractura por caso | revisor clinico | **VIGENTE** — recuento verificado el 2026-10-05 en `04-implicancias.md` |

## 7. Superados y archivados, y por que no se borran

Desde el 2026-10-08 lo superado que **nadie importa** vive en `experiments/obsoletos/objetivo2/` (inventario
y ruta anterior en `../obsoletos/README.md`). Lo superado que **todavia se importa** se queda aqui.

| Artefacto | Donde esta | Motivo |
|---|---|---|
| `e9_corredor.py` | aqui | **lo importan** `e9ts_corredor.py`, `e12_sap_control.py`, `e14_relleno_envolvente.py` y `src/muestreador/sap.py` |
| `ts_piloto_qc.py` / `.csv` | aqui | congelado como evidencia de #49/#50; lo importan `ts_qc.py`, `e9ts_corredor.py`, `e12`, `e14` |
| `e13_poses_piloto.csv` | aqui | lo lee `verificar_coherencia.py` |
| `r1_mosaico.py`, `r1_revision_itksnap_revisor.*`, `r1_landmarks.v*`, `r1_estados.v2a.csv`, `r2_nivel_pico_revisor.ANTERIOR.md` | `../obsoletos/objetivo2/` | ver tabla de abajo |

Detalle historico:

| Artefacto | Por que quedo fuera | Por que se conserva |
|---|---|---|
| `r1_revision_itksnap_revisor.csv` / `.md` | 2da vuelta de S1 en ITK-SNAP que no se persiguio; se resolvio por lamina | **Citado desde `docs/01-decisiones.md`, `docs/04-implicancias.md` y `docs/ESTADO.md`.** Borrarlo dejaria huerfanas esas citas, y `01-decisiones.md` solo lo edita la autora (regla 3). Ademas documenta **por que** existe la lamina alargada: el revisor objeto que el mosaico de +-60 mm no deja contar vertebras |
| `r1_mosaico.py` | recorte de +-60 mm, no permite contar vertebras | produjo `r1_auditoria_s1_clinico.csv`, que es la referencia vigente citada en `main.tex` |
| `e9_corredor.py` | umbral HU invalido para el esponjoso (#48) | **lo importan** `e9ts_corredor.py`, `sap.py` y `e12_sap_control.py` |
| `r1_landmarks.v*`, `r1_estados.v2a.csv` | versiones previas de la deteccion | trazabilidad de las cifras publicadas en cada momento |

**Regla general: en este proyecto no se borra evidencia.** Un artefacto superado se marca, no se elimina.
Un CSV vacio **no significa** que nadie respondio: puede ser una planilla que se preparo y se sustituyo
por otra via. Antes de concluir nada de un archivo vacio, buscar si existe otro que conteste lo mismo.
