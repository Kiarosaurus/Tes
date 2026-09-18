# Estado actual

> Lo actualiza Claude al cerrar cada sesion. Fuente de verdad de "por donde voy".

## PUNTO DE RETOMA — leer esto primero (2026-09-17)

> Sustituye como entrada al bloque del 2026-09-15 que sigue abajo (queda como historico; sus pendientes sobre
> #36/#39 y la lectura de Chen ya estan resueltos). Verificado contra disco el 2026-09-17.

**Donde esta el proyecto.**
- `main.tex` compila: **6 paginas**, 64 referencias, 0 errores, 0 citas indefinidas. `src/` sigue **vacio**.
- Literatura: **toda entrada de `refs/raw/` tiene ficha** (ronda 2026-09-16). Implicancias hasta **#76**.
- **Decisiones del 2026-09-17, delegadas al asistente como asesor** (`01-decisiones.md`, entrada 2026-09-17):
  - se mantiene el renderizador (la autora rechazo recortarlo);
  - ablaciones FUERA; brazo fisico de Peters sobre un subconjunto reducido;
  - Chen citado como preprint.
- **Regla preinscrita en `main.tex`:** el Go/No-Go del Objetivo 1 (MAE en hueso < 25 HU, pacientes separados) se
  prueba con el VAE de SD 1.5 preentrenado y con una variante de **decodificador adaptado y encoder congelado**. Si
  ninguno pasa, **no hay Objetivo 3** y el No-Go es el resultado.

**E6b con RMSE — NO SE CORRIO (confirmado en Khipu por la autora, 2026-09-17).** `sacct` desde 2026-09-15 solo
muestra 51539 (prueba), 51540 (cohorte MAE, 08:44:58) y 51591 (prueba RMSE de 1 volumen); `~/metalsynth/data/e6b/` esta
vacio. En la PC: `outputs/e6b_vae_sd15.csv` = cohorte MAE vieja (178 filas, 32 columnas, sin `rmse`), logs en
`outputs/e6b/`. **Decision 2026-09-17 (2):** no se relanza la cohorte RMSE sola; MAE y RMSE se reportan dentro de P1.

**Siguiente, en orden:**
1. **P1 — PREPARADO Y PROBADO EN LOCAL (2026-09-17), falta correr en Khipu.** `experiments/objetivo1/p1_decodificador_sd15.py`
   + `p1_entrenar.sbatch` / `p1_evaluar.sbatch` + `p1_particion.csv` (168 pacientes: 126/8/34, semilla 20260917). Regla
   fijada por la autora antes de correr: Go si **alguna** de {sd15, afinado} x {pub, LW20000, pub+asinh} tiene **media por
   paciente** del MAE en hueso con **`vae regla`** < 25 HU en los 34 de test. Comandos: `KHIPU.md`, seccion P1 (prueba
   corta -> 3 entrenamientos -> evaluacion). Local: controles identidad/eco/hash/`B_delta` OK; VAE real sin probar.
   **#76 DECIDIDA Y APLICADA** (regla completa en `main.tex:77`; desempate a priori pub+asinh > LW20000 > pub, sd15 antes
   que afinado; pase MARGINAL si IC95 superior >= 25 HU). Registrada en `01-decisiones.md` 2026-09-17 (3).
   **Lanzado en Khipu (2026-09-17):** prueba 51667 (entrenar) + 51668 (evaluar, afterok) y cohorte 51669/51670/51671
   (pub+asinh/LW20000/pub) **a la vez, sin esperar la prueba**. Evaluacion rechazada (`QOSMaxSubmitJobPerUserLimit`).
   Estado 00:56: 51667 corre bien en ds001 (paso 0: val hueso regla MAE 156.02 HU, 4.1 GB); 51668 espera dependencia;
   51669-71 en PD (Priority). ~01:05: 51667 COMPLETED (5:40); **51668 FAILED rc=1 (2:38), causa sin leer**; 51669 corre
   en ds001 (arranco antes del hold); 51670-71 retenidos. Causa de 51668: faltaba `qc/e6b_vae_sd15_mae_20260915.csv` (evaluacion
   completa, fallo en el control). Prueba: 1.32 s/paso, 24.6 GB, ~11 h/config. Pendiente: subir CSV + `.py`, `resumen` en
   nodo de acceso (meta sd15 frente a E6b 4 de 4) y `scontrol release 51670 51671`.
   **51669 (`pub+asinh`) COMPLETED en 10:36:07** (estimacion 11 h, acertada). **51670 y 51671 siguen PENDING 20 h
   despues por `scontrol hold`; liberados y 51670 corre en g002, 51671 detras.** Controles de la prueba CERRADOS:
   **sd15 frente a E6b 4 de 4**, identidad 2 de 2, hashes OK. Falta: evaluacion (~3.5-4 h tras el ultimo entrenamiento).
2. **P2:** verificar en el codigo de XCIST si paciente y metal se proyectan juntos (#70).
3. **P3:** muestreador + SAP en `src/muestreador/` (en paralelo a P1).
Autora: laminas `e9ts_revision_laminas_autora.csv` 0/16; plazo de 2 semanas al revisor de #53.

## PUNTO DE RETOMA anterior (2026-09-15, historico)

> Escrito para que una sesion nueva, sin historial, retome sin releer nada mas. Todo lo de
> abajo esta verificado contra archivos en disco. Las decisiones son de la autora: Claude no
> las aplica sin orden explicita (reglas 3, 4 y 14 de `CLAUDE.md`).

### Donde esta el proyecto

- **Literatura cerrada por saturacion; el proyecto esta en fase experimental.** `src/` sigue
  **vacio**: todo lo ejecutable esta en `experiments/`. Segun #23, la entrega queda a unas 12
  semanas.
- **Cohorte por paciente (decision del 2026-09-10):**
  - 178 volumenes = 168 pacientes (`Grupo paciente` en `revision.csv`).
  - Volumenes fuera de uso: `experiments/exploration-3d/exclusiones.csv` (11; ningun archivo
    borrado).
  - Particion por objetivo: `grupos.csv` (grupo 1 con material ortopedico = 65, grupo 2 = 37,
    grupo 3 limpio = 66).
  - `metal_0059` y `metal_0071` estan unidos sin perdida en `data/derivados/`.
- **`tesis/main.tex` compila** (4 paginas, **43** referencias, 0 citas indefinidas). Cambios
  recientes:
  - R1 en 48/29 (`Field limitation`);
  - TS en el Objetivo 2, holgura #31 (1-2 mm) y parrafo `Corridor measurement on the local cohort`;
  - limpieza: "changed neither the transsacral corridor diameter nor its 10~mm viability";
  - `maintex_cifras.py` recalcula ese parrafo desde tablas versionadas: **12 de 12**.

### Lo que se midio (reproducible, en disco)

| Exp | Donde | Resultado vigente |
|---|---|---|
| E1 | `exploration-3d/sensibilidad_hu.py` | 2500 HU criba con 0 falsos negativos (113 candidatos) |
| Dup. | `exploration-3d/duplicados_parciales.py` | 6 grupos por SHA256 + 3 por cortes compartidos; todos resueltos por paciente |
| E6a / E6c | `objetivo1/` | Techo de 2000 HU de LW: 48 de 75 con metal fallan el Go/No-Go. `pub+MTW` (4a ventana) domina (#39) |
| R1 | `objetivo2/r1_*.py` | 65 pacientes: marco computable con S1 confirmado por revisor clinico **48**, sin contaminacion **29** (transcripcion corregida el 2026-09-14; ya en `main.tex`). Revisor: medico ORL, ciego; acuerdo con el agente kappa 0.81. Segundo juicio en ITK-SNAP (#53): planilla de 61 casos lista, **0 de 61 llenos** |
| E8 | `objetivo2/e8_*.py` | >= 17 de 65 con tornillo iliosacro; a 2500 HU los tornillos salen fragmentados (9/57) y con fuste de 5.1 mm (#46). Test-retest `0065`/`0066` |
| E9b | `objetivo2/e9b_*.py` | Alguna esfera de S1 con mediana < 150 HU en **38% con metal y 43% sin metal** (#48). **El brazo sin metal queda cuestionado por #50** |
| E9 | `objetivo2/e9_corredor.py` | **NO VALIDO**, no correr: el umbral HU no captura el esponjoso sacro (#48) |
| TS piloto | `objetivo2/ts_piloto.sbatch`, `ts_piloto_qc.py` | Job 51300, 2 casos x 2 recortes. Sin truncamiento; entre recortes Dice 0.93-0.97 con diferencias en SI/ala (#49). En `CLINIC_0002` las esferas de E9b caen un nivel arriba de la S1 de TS y las alas en tejido blando (#50) |
| TS cohorte | `objetivo2/ts_cohorte.sbatch` -> `ts_qc_cohorte.sbatch` (`ts_qc.py`) | **Completa y traida a la PC** (2026-09-13): jobs 51315 (358/358 ok) y 51316 (179 casos, 0 errores). Integridad verificada. Repetibilidad contra el piloto no exacta: 16 y 8 voxeles en `metal_0008` 6 mm (#49). Entrada: **`objetivo2/ts_cohorte.md`** |
| TS analisis | `objetivo2/ts_analisis.py` -> `ts_analisis.md`, `ts_nivel_s1.csv` | Nivel S1 de TS concuerda con el clinico en 57/57 (tras corregir la transcripcion de `metal_0012`); R1 falla el nivel en 7/60 de calibracion (#50). "Ala < 150 HU dentro de sacro/S1": 8% con metal, 15% sin metal (#48 decia 38/43%). Recorte ~5% de voxeles; 10 casos con cajas desplazadas 14-98 mm (#49). #51 cerrada: era transcripcion. Laminas: 12/197, revisadas por agentes |
| E9-TS | `objetivo2/e9ts_corredor.py` (51505; 3 mm: 51529) | 152 casos, 0 errores. Objetivo 2 (72 tras QC de nivel, #54): `D_TS` mediana 9.5 mm (IQR 7.4-11.7); viables a 10 mm 29/72 (6 mm) y 27/72 (3 mm). Grupo 1 con `ocupado_semimax`: 53.8% -> 40.4% en 52. Tablas versionadas en `objetivo2/` |
| E10 / E10b | `ts_componentes.py` (51522), `ts_cajas_limpias.py` (51527) | F = 0.001: `D_TS` y viabilidad invariantes para F hasta 0.05; quedan 4 cajas desplazadas > 10 mm (1 original, 3 creadas por la limpieza), declaradas (#49) |
| E6b | `objetivo1/e6b_vae_sd15.py` + `.sbatch` | **Cohorte completa y en la PC** (job 51540): 178 volumenes, 0 errores, control de identidad 873/873, 8.74 h. **Las tres configuraciones fallan el Go/No-Go de hueso en 178/178**, tambien con el decodificador oraculo (cota). El VAE de SD 1.5 sin reentrenar agrega 163-212 HU sobre codificaciones cuya identidad es 0.00 HU (#36/#39, ronda (7)) |

### Decisiones tomadas en esta ronda (todas en `01-decisiones.md`)

1. **Unidad = paciente:** duplicados parciales, union, `metal_0068` sin material ortopedico,
   ningun `.nii.gz` se borra.
2. **#20:** indice menor en las copias exactas.
3. **#41 via (c):** geometria parametrica, calibre de 6.5-8.0 mm, cilindro liso. **Contingencia
   abierta:** via (a), extraer de CLINIC-metal, **solo** si a futuro falta por completo
   bibliografia de calibres y longitudes. La falta de rosca o cabeza no la dispara.
4. **#31:** `Dmax >= d_implante + 2c`, `c` = 1-2 mm radiales (operacionalizacion declarada de
   Kaiser).
5. **#22:** 2500 HU solo para cribado; metal integrity con la regla adaptativa de Peters.
6. **#48/#49/#50 (2026-09-14):** TS `total` 2.18.0; recorte de 6 mm principal y 3 mm como sensibilidad (se
   reabre solo si las laminas muestran un fallo de 6 mm); E9b retirado.
7. **#52 (a + c), #35 cerrada, #54 opcion (a):** `ocupado_semimax` principal; F = 0.001 justificada por la
   invarianza de `D_TS` (decision 2026-09-14 (5)).
8. **#53 (2026-09-15):** el revisor clinico juzga los 61 casos con S1 en ITK-SNAP, ciego y en planilla aparte.

### PENDIENTES PARA LA PROXIMA SESION, por urgencia

1. **#36 + #39: VAE y ventanas, juntas. Bloquean el Objetivo 1**, que es obligatorio.
   - **E6b ya corrio y ya se analizo** con el criterio preinscrito: **SD 1.5 sin reentrenar no pasa**. La opcion 1
     de #36/#39 queda descartada por evidencia propia. Ver la ronda (7) de `04-implicancias.md`.
   - **Decision de la autora, pendiente:** opciones 2-5 de #36/#39. La 3 (otro VAE, con requisito de MAE de hueso
     < 25 HU) es la via principal; la 5 (revisar el umbral de 25 HU, solo con fuente) es nueva. Ninguna aplicada.
2. **Objetivo 2, cierre (sin decisiones de metodo pendientes):**
   - mandar al revisor `r1_revision_itksnap_revisor.csv` + `.md` + 61 CT (#53). Al volver: comparar con el
     mosaico y con TS; si cambia algun `ok`/`+1`, cambian 48/29 y 57/57 en `main.tex`;
   - revision de laminas de la autora: `e9ts_revision_laminas_autora.csv`, **0 de 16**. Un `fallo_6mm` reabre
     la decision 2026-09-14 (4).
3. **ABIERTAS de referencia:** #55 (cifras por clase de TS; regla F sin precedente, LiTS/KiTS19 en
   `_candidatos.md`) y #54 (discordancia de nivel sin juicio clinico en grupos 2 y 3; ya decidida la opcion a).
4. **Decisiones pequenas de la autora:** tercera regla de umbral para implantes reales (#22).
5. **Opcional, para blindar R1:** revision clinica de crestas y EIPS (heuristica sin revisar, declarado en
   `main.tex`).
6. **No urgente:**
   - revision de artefactos por la autora (#34, #35, #37; solo Objetivo 3);
   - candidatos PENDIENTE de `_candidatos.md`;
   - deuda: leer a fondo Zwingmann 2009 y Smith 2006 antes de la sustentacion.

### Avisos para quien retome

- **Memoria.** La PC tiene 11.8 GB y suele quedar con ~1.5-2 GB libres. Los scripts pesados
  corren por lotes reanudables (`--max`), en primer plano o con procesos nuevos por lote: dos
  corridas de fondo murieron por RAM. Lo que necesite GPU o modelos grandes va a **Khipu**.
  Host, carpetas, entorno, colas, limites, errores ya vistos y comandos estan en
  `experiments/objetivo2/KHIPU.md`: leerlo antes de escribir cualquier `.sbatch`.
- **Procedencia.**
  - `objetivo2/r1_auditoria_s1_clinico.csv`: medico ORL, **no la autora**.
  - `r1_auditoria_s1_agente.csv`: agente.
  - `revision.csv` solo se toca con scripts que verifican y respaldan (`procedencia.py`,
    `grupo_paciente.py`, `correcciones_autora.py`).
- **Historicos que no se usan:** `r1_landmarks.v1-parcial.csv`, `r1_landmarks.v2a.*`,
  `revision.pre-*.csv`.
- **Bibliografia:** `refs/raw` -> `refs/clean` -> `python scripts/build_refs.py` (regla 9). No
  editar `refs.bib` a mano.
- **Patron a vigilar (visto 6 veces):** un enunciado se vuelve verdad por citarse a si mismo, o
  un control que no puede fallar se toma por verificacion (#25, #37, #40, #45, #47, #50). En #50,
  el control de marco de E9b validaba el CT, no el nivel de S1. Verificar contra el archivo o el
  dato antes de construir encima.
- **TS:** `ts_piloto_qc.py` y sus CSV estan congelados como evidencia de #49/#50; para la cohorte
  se usa `ts_qc.py`, que reutiliza sus funciones. No cambiar `--task` ni `--roi_subset` en
  `ts_cohorte.sbatch` sin decision: el recorte depende de las clases pedidas (#49).
- `04-implicancias.md` es el archivo critico irreemplazable (regla 17). Llega hasta la #75 (ultima ronda:
  2026-09-16 (14), recomendaciones aplicadas y 11 fichas faltantes).

## Ultimo paso completado
2026-09-17 (ronda 15) — **la autora delega las decisiones al asistente en rol de asesor**; rechaza recortar el renderizador.
- Chen citado como preprint (Obj 1). Aplicadas en `main.tex` #57, #69-#75; ablaciones FUERA (`00-tesis.md` punto 10);
  brazo fisico sobre subconjunto reducido; **regla preinscrita**: si el VAE (preentrenado o con decodificador adaptado y
  encoder congelado) no pasa el Obj 1, no hay Obj 3. Compila: **6 paginas** (antes 5), 64 refs, 0 errores.
- Decision completa en `01-decisiones.md` (2026-09-17), incluidos los pendientes previos de este archivo.

**Siguiente (en orden):** P1 = afinar solo el decodificador del VAE de SD 1.5 en Khipu y evaluar con E6b (hueso, metal y
`B_delta`) en pacientes separados; P2 = verificar proyeccion conjunta en el codigo de XCIST; P3 = implementar el
muestreador + SAP en `src/muestreador/` (en paralelo a P1). Autora: laminas 0/16 (~1 h) y plazo de 2 semanas a #53.
**Pendientes que surgieron:** limite de paginas (6 pp.); `src/` sigue vacio.

## Paso anterior
2026-09-16 (ronda 14), **orden de la autora** — recomendaciones adoptadas y 11 fichas faltantes generadas.
- **`main.tex` APLICADAS #64 (a), #66 (a), #67 (limitacion) y #68 (a) + regla de borde SAP** `0 / (0,2) / [2,4] / (4,inf)`.
  Compila: 5 pp., 64 refs, 0 errores, 0 citas indefinidas. Decision 2026-09-16 escrita en `01-decisiones.md`.
- **#65 NO aplicada:** la autora espera el raw de las ACTAS de Chen (el de `refs/raw/` es el preprint arXiv); frase
  preparada en `01-decisiones.md`.
- **Re-verificaciones:** `zwingmann2009navigated` (grosor de corte NO ENCONTRADO; un radiologo; nivel del brazo navegado
  NO ENCONTRADO -> **#69**) y `peters2025hybrid` (proyeccion conjunta NO ENCONTRADO; fantoma no cubre el paso hibrido ->
  **#70**). Secciones "Verificacion 2026-09-16" al final de ambas fichas.
- **11 fichas nuevas** (todo raw sin ficha): abadi2019, dorjsembe2024, hu2023, kazerouni2023diffusionsurvey, li2024,
  rombach2022latentdiffusion, selles2024marreview, singhrao2024fiducial, yu2021, zhang2023controlnet y
  templeman1996proximity (solo abstract). **Ya no queda raw sin ficha.** `ziran2003` tiene PDF pero no raw (cadena del
  10 mm cerrada; no se leyo).
- **ABIERTAS nuevas #69-#75**, ninguna aplicada.

**Siguiente:** decision de la autora sobre #69 (S1 en brazo navegado; toca `main.tex:52` y `:78`), #70 (`main.tex:50`),
#71 (`main.tex:56`), #72 (`main.tex:48`, pocas palabras), #73, #74 (junto con #36/#39) y #75 (citar Rombach en la frase de
#66). Ejecucion pendiente: ROI `B_delta` en `e6b_vae_sd15.py` + Khipu.
**Pendientes que surgieron:** candidatos Szalkowski 2021 y Selles 2023 [140] (posible extension espacial, #57); verificar
cifras de Tabla I de `li2024` (imagen poco nitida); `kazerouni2023` y `zhang2023controlnet` leidos sobre preprint.

## Paso anterior
2026-09-16 (ronda 13) — **4 lecturas mas con `lector-papers`**: `mirza2003`, `fan2022`, `routt1997`, `macháček2023`
(fichas, filas en `_index.md`, `_candidatos.md` actualizado). **#68 NUEVA** (escala de 4 grados literal en Mirza, que la
declara heredada; `main.tex:52` dice "lettered" y omite ese eslabon; SAP sin regla de borde para 4.0 mm). #67
actualizada. `fan2022`, `routt1997` y `macháček2023` sin implicancia ABIERTA (registrado).

**Siguiente:** decision de la autora sobre #64-#68. Vaccaro 1995 Part II sube a N1 en `_candidatos.md` (unico nodo sin
leer de la escala). Verificacion menor: proyeccion conjunta paciente+metal en `peters2025hybrid`.
**Pendientes que surgieron:** quedan 11 PDF sin ficha, ninguno con riesgo alto (surveys, arquitecturas, MAR puros,
DukeSim, Polyp-DDPM, hu2023, singhrao2024).

## Paso anterior
2026-09-16 (ronda 12) — **4 lecturas con `lector-papers`**: `arand2019pelvicring`, `chen2026foundationvae`, `tejwani2014`,
`zhang2018` (fichas, filas en `_index.md`, candidatos en `_candidatos.md`). **#64-#67 NUEVAS** y #63 actualizada.
`main.tex`, `00-tesis.md` y `01-decisiones.md` sin tocar. #64: Arand citado como "bone density maps" sin mapa utilizable.
#65: Chen no refuta E6b. #66: E6b no mide la banda B_delta. #67: grosor de corte del CT vs benchmark Zwingmann.

**Siguiente:** decision de la autora sobre #64 (redaccion `main.tex:78`), #65 (frase en Related Work), #66 (ROI de banda
en E6b) y #67 (verificar protocolo CT de Zwingmann 2009). Mas urgente sigue siendo #36/#39 (VAE); MAISI entra como
candidata N1 para la opcion 3.
**Pendientes que surgieron:** protocolo de CT de `zwingmann2009navigated` no esta en su ficha (releer ese punto);
Wagner 2014 queda condicionada a #64.

## Paso anterior
2026-09-15 (ronda 11) — **2 lecturas mas, correcciones APLICADAS a `main.tex` y bibliografia regenerada**,
todo por orden explicita de la autora en el mismo turno.
- **`zwingmann2013.md` (N2 propuesto) y `lin2019.md` (N1 propuesto).** Fichas y filas en `_index.md`.
- **#62 NUEVA:** `zwingmann2009navigated` **no es independiente** de `zwingmann2013` — es su ref. 10 **y** su
  estudio primario n.o 19, y **entra con cero eventos en ambos brazos**, porque ahi "malposicion" significa
  revision. Prueba limpia de que tasa agregada y grado ordinal son constructos distintos. **Cierra la cadena
  del 2%-15%**, que el propio paper imprime como "2 to 15 %" y "0 to 15 %" con las mismas dos referencias.
- **#63 NUEVA:** `lin2019` (DuDoNet) **no prohibe** el renderizador en dominio imagen — es rendimiento, no
  imposibilidad, y ademas es REMOCION, que el paper llama *ill-posed*. #61 queda como falta de precedente.
- **`main.tex`: #56, #58, #59, #60 y #61 APLICADAS.** Compila: **5 paginas** (antes 4), **64 referencias**,
  0 citas indefinidas, 0 errores.
- **`refs.bib` 43 -> 64.** Se generaron los **21 `refs/clean/` que faltaban** desde su raw; `refs/raw/` intacto.
  Procedencia y decisiones, una por una, en `refs/MAPEO.md`. Ya no queda raw sin clean ni clean sin raw.
- **Correccion:** el reporte previo dijo que `deman1999` no tenia raw. Era falso (filtro `^title` que falla en
  los `.bib` de IEEE). Si es citable, y ya se cito.

**Siguiente:** decision de la autora sobre #62 y #63, y copiar a `01-decisiones.md` las cinco aplicadas si las
da por definitivas. **Lectura siguiente mas rentable: `zhang2018`** — es la fuente del protocolo de simulacion
de metal que `lin2019` reutiliza y omite, y **ya tiene PDF, raw y entrada en `refs.bib`**.
**Pendientes que surgieron:** (1) con `\nocite{*}` en `main.tex:139` las 21 altas entran a la bibliografia sin
citarse — solo 5 de las 21 se citan hoy; si debe listar solo lo citado, hay que quitar `\nocite{*}` (regla 14).
(2) `herman2016` apunta a dos versiones: `refs.bib` a la de revista (2017, 35(7):1478-1484), la ficha al
*Accepted Article*. (3) `tejwani2014` y `gottschling2009` van sin DOI: su raw no lo trae. (4) `macháček2023`
tiene clave no ASCII; compila, pero renombrarla es decision de la autora.

## Paso anterior
2026-09-15 (ronda 10) — **4 lecturas nuevas con `lector-papers`**, elegidas entre los 24 PDF de `papers/`
sin ficha. Fichas: `gertzbein1990.md`, `ramzan2026claim.md`, `herman2016.md`, `deman1999.md`.
Filas anadidas a `_index.md` (N1 Gertzbein; N2 los otros tres) y candidatos de snowballing a `_candidatos.md`.
- **#56 CERRADA EN EVIDENCIA** (sigue ABIERTA en decision): CLAIM era la cuarta fuente sin leer.
  Recuento final de la frase de `main.tex:48`: *"bounded inpainting"* 3/4, *"strictly inside the mask"* 2/4,
  **"implicitly assume non-rigidity" 0/4** — no lo enuncia ninguno de los cuatro PDF.
- **#58 NUEVA:** `gertzbein1990` publica **SEIS** tramos de 2 mm, no cuatro grados; los cortes de 6 y 8 mm no
  tienen justificacion declarada y su referencia anatomica es el pediculo, no el corredor iliosacro.
  Toca la atribucion de la escala del benchmark SAP/BFC en `main.tex:48` y amplia #4.
- **#59 NUEVA:** `herman2016` da 32% de malposicion por tornillo y **S1 36.5% frente a S2 14.8%**; tensiona el
  parrafo S1/S2. **No resuelve #32** (es 2D fluoroscopico, scale-invariant, sin Dmax).
- **#60 y #61 NUEVAS:** `deman1999` **no mide extension espacial del streak**, asi que el reclamo de novedad de
  B_delta sobrevive y **#57 sigue sin fuente externa**; abre el hueco del dominio imagen frente a proyeccion.

**Siguiente:** decision de la autora sobre #56 (opcion a), #58 (b+c), #59 (c), #60 (b o c) y #61 (b).
`main.tex`, `00-tesis.md` y `01-decisiones.md` sin tocar (reglas 4 y 14).
**Pendientes que surgieron:** `gertzbein1990` y `herman2016` tienen `.nbib` en `refs/raw/` pero **no estan en
`refs.bib`**; `deman1999` **no tiene raw** y hoy no es citable (regla 9). `herman2016` es version
"Accepted Article" sin paginacion de revista: elegir version antes de citar paginas (patron `isensee2021`).
Candidata mas fuerte de la ronda para leer: **Zwingmann 2013**, metaanalisis de malposicion por modalidad.

## Paso anterior
2026-09-14 (3):
- **#52 decidida (a + c)** y **#35 cerrada** por la autora. `grupos.py` regenerado: solo cambian `Regla` y
  `Estado regla`. Registradas en `01-decisiones.md` (2026-09-14 (2)) con orden de la autora.
- **E9-TS ahora calcula #52 (c):** politicas `hueso`, `ocupado_2500` (cota) y `ocupado_semimax` (propuesta #22).
  `metal_0008`, 6 mm: 11.3 -> 10.0 mm ocupado; 3 mm: 9.5 sin cambio. El resumen pone primero la cohorte del
  Objetivo 2 (grupos 2 y 3).
- **#53:** `r1_cortes_itksnap.py` -> `r1_cortes_itksnap.csv`, corte exacto del punto de S1 en el archivo original,
  para que el revisor lo abra en ITK-SNAP. Ciego, con comprobacion por HU.

**Lanzados en Khipu (2026-09-14, n006):** E10 = job 51504, E9-TS = 51505 (los dos en `R`), resumen = 51506
(espera a los dos). Cierre: `KHIPU.md`, "Noche automatica", pasos 3-5.
**Revision del cierre (2026-09-14, tarde):** E9-TS integro (152 casos, 0 errores, 2352 filas). **E10 INCOMPLETO:**
42/179 casos (`CLINIC_0001`-`0042`, solo dataset6), `ts_componentes_errores.csv` vacio (0 bytes: proceso matado sin
`finally`). Seccion 6 de `e9ts_resumen.md` NO sirve para fijar F. `sacct`: FAILED, ExitCode `0:9` (SIGKILL externo)
a los 6:47, MaxRSS 908 MB de 32G; no es tiempo ni memoria del job, y `CLINIC_0043` tiene tamano normal. Causa sin
confirmar (sospecha: E9-TS con 16 procesos en el mismo n006). Siguiente: `sacct`/`seff` de 51504 y 51505, cabecera
`Caso,Error` a mano en el CSV de errores, relanzar E10 solo (~10 s/caso) y regenerar el resumen.
**Relanzado:** E10 = 51522 (`R` en n006, sin E9-TS al lado), resumen = 51523 (`afterok`). GPUs revisadas: g002
(RTX A6000 48 GB) libre; `a-tesis` no limita `gres/gpu` (detalle en `KHIPU.md`, Colas y limites).
**2026-09-14 (4): E10 completo** (179 casos, 0 errores, rc=0, 16 min) y **E9-TS + E10 analizados**, traidos a
`outputs/e9ts/` y `outputs/ts_componentes/`. Implicancias: #49, #52 y #48 actualizadas; **#54 nueva** (la QC de nivel
excluye 18/91 del Objetivo 2, desigual entre grupos). Textos de decision y de `main.tex` propuestos en el chat, NO
aplicados. Siguiente: la autora decide F, politica de ocupacion principal y #54; luego, aplicar con orden explicita.
**2026-09-14 (5), con orden explicita de la autora:** decision 2026-09-14 (3) escrita en `01-decisiones.md` (F = 0.001,
`ocupado_semimax` principal, #54 opcion a). `main.tex`: TS en el Objetivo 2 y parrafo `Corridor measurement on the local
cohort`; compila, 4 paginas, 41 referencias, 0 indefinidas. `wasserthal2023` dado de alta (raw -> clean -> refs.bib,
MAPEO, `_index.md` N2 propuesto, ficha por `lector-papers`). **#55 nueva:** el paper no valida S1 ni metal. E10b listo
(`ts_cajas_limpias.py` + `.sbatch`, probado en local: control 8/8); comandos en `KHIPU.md`, seccion E10b.
Siguiente: correr E10b en Khipu y confirmar que F = 0.001 elimina los 10 desplazamientos; revisar laminas (36
componentes >= 1%, `CLINIC_0091`/`0078`); despues, Objetivo 1 (#36/#39, E6b en g002).
**2026-09-14 (6):** #55 actualizada con el README del repositorio TS que pego la autora: el paper es de la v1 (literal de
los autores); `vertebrae_S1` existe en `total`; Apache-2.0; piden citar nnU-Net; el recorte robusto es "better" segun
ellos (toca #49) y reconocen confusion de vertebras vecinas (toca #54). Opciones (a)-(d) en #55, sin aplicar.
**2026-09-14 (7), orden de la autora:** `main.tex` con los cuatro pendientes (post hoc, cota 2500 HU, desfase de la
publicacion de TS, cita nnU-Net `isensee2021`); compila, 4 paginas, 42 referencias. **La autora prefiere 3 mm como
recorte principal: PENDIENTE** (#49, ronda (6)); las cifras con 3 mm ya existen. Preparado y probado en local
`e9ts_3mm.sbatch` (laminas 3 mm + repetibilidad + resumen); comandos en `KHIPU.md`, "E9-TS con 3 mm". Falta: fila de
`isensee2021` en `_index.md` (ficha en curso), fuentes de la autora sobre 3 mm, correr E10b y E9-TS 3 mm en Khipu.
**Ficha de `isensee2021` hecha:** el PDF local es el **preprint arXiv 2020**, no el Nature Methods 2021 del raw (#55,
actualizacion). La cita de `main.tex` no depende de su contenido; falta el PDF publicado o decidir (#55 opciones a-c).
nnU-Net usa "componente mayor", no fraccion: la regla F no tiene respaldo bibliografico (se declara como propia).
**Detenido (2026-09-14):** la autora subio `falk2019` como el nnU-Net de Nature Methods 2021, pero el raw es Falk et al.
2019, "U-Net: deep learning for cell counting..." (otro articulo). No se proceso ni se corrigio nada; esperando el PDF
correcto como `papers/isensee2021.pdf` (#55, seguimiento).
**Resuelto:** la autora subio el PDF de Nature Methods y retiro `falk2019`. Ficha de `isensee2021` rehecha y verificada;
se mantiene que nnU-Net solo usa "componente mayor" (sin fraccion) y no tiene CT oseo ni metal. `main.tex` sin cambios.
LiTS y KiTS19 en `_candidatos.md` como posibles precedentes de F.
**E9-TS 3 mm corrido (51529):** repetibilidad IDENTICO frente a 51505 (2352 x 43); 152 laminas con 3 mm en
`outputs/e9ts_3mm/`. Objetivo 2 con 3 mm y F = 0.001: 9.35 mm (IQR 7.75-11.7), 27/72 viables. **E10b no llego a la PC**
(sin `outputs/ts_cajas_limpias/`). Siguiente: traer o correr E10b; la autora revisa laminas 3 mm y aporta la fuente
citable del recorte; luego, con orden, decision y `main.tex` a 3 mm.
**2026-09-14 (8): `ebraheim1993` leido** con `lector-papers`. Por decision de la autora, solo ficha: el raw queda sin
`clean/` y `refs.bib` sigue con 42 entradas. Es un reporte de un caso sin tasa, asi que no es fuente del 2%-15%; su
pitfall es la superposicion en la AP y no afecta SAP. Registrado en `_index.md` (N3 propuesto), `_candidatos.md` y #12,
sin implicancia nueva. De las 4 refs. de Hinsche faltan Routt 1997 y Templeman 1996, que no hacen falta para el alcance.
**2026-09-14 (9):** comandos de E10b entregados a la autora (sin cambios en `KHIPU.md`; meta de filas 2865 verificada
contra el script). La autora confirma que eligio 3 mm solo por el README: #49 actualizada, porque cambiar el principal
ahora seria post hoc. Recomendacion: mantener 6 mm y reabrir solo si E10b o las laminas muestran un fallo del recorte de 6 mm. Siguiente: correr
E10b, la autora decide #49 y despues el Objetivo 1.
**2026-09-14 (10):** decision 2026-09-14 (4) escrita en `01-decisiones.md` por orden de la autora: 6 mm principal y
3 mm como sensibilidad; `main.tex` sin cambios. **E10b analizado** (job 51527, rc=0, control 715/716 por la S1 vacia de
`metal_0053`). Con F = 0.001 quedan 4 desplazamientos: 1 original y 3 nuevos creados por la limpieza. Ningun cambio en
`D_TS`. Cae la justificacion escrita de F en la decision (3); #49 actualizada con opciones y recomendacion (a). Siguiente:
la autora decide la justificacion de F; revision de laminas; Objetivo 1.
**2026-09-14 (11):** decision 2026-09-14 (5) escrita por orden de la autora: se mantiene F = 0.001 y su justificacion
queda en la invarianza de `D_TS`; la seccion E10b de #49 queda CERRADA. Objetivo 2 sin decisiones pendientes de metodo.
Siguiente propuesto: cierre corto del Objetivo 2 (versionar tablas citadas, revision dirigida de laminas, #53) y despues
el Objetivo 1: E6b sin reentrenar (VAE de SD 1.5 sobre configuraciones de 3 canales) para decidir #36 + #39 juntas.
**2026-09-15:** por orden de la autora:
- **Tablas versionadas** en `experiments/objetivo2/` (e9ts_corredor, e9ts_resumen, ts_cajas_limpias y su control; hash
  identico). `maintex_cifras.py` las recalcula: **11 de 12** cifras de `main.tex` coinciden. La que no es "changed no
  measurement": en `CLINIC_0012` el corredor iliosacro izquierdo cambia 0.2 mm; texto propuesto en #49, sin aplicar.
- **Plantilla de revision de laminas** (16 casos) y su guia, `e9ts_revision_laminas.md`.
- **E6b preparado y probado en local sin modelo** (identidad 12/12 frente a E6c; con E6c alterado da 11/12; eco 12/12).
  Comandos en `KHIPU.md`, seccion E6b.

Siguiente: prueba corta y cohorte de E6b en Khipu; revision de laminas (autora); tabla de ITK-SNAP al revisor (#53);
decidir el texto de #49.
**2026-09-15 (2), orden de la autora:**
- **`main.tex`**: la limpieza "changed neither the transsacral corridor diameter nor its 10~mm viability"; compila, 4
  paginas, 42 referencias, 0 indefinidas. `maintex_cifras.py` da **12 de 12**.
- **#53**: el revisor mira los 61 casos; planilla ciega `r1_revision_itksnap_revisor.csv` (61 filas) e instrucciones
  en `.md`. La decision falta escribirla en `01-decisiones.md` (texto propuesto en el chat).

Siguiente: mandar la planilla, los .md y los 61 CT al revisor; E6b en Khipu; revision de laminas.
**2026-09-15 (3):**
- **Decision de #53 (61 casos)** escrita en `01-decisiones.md` por orden de la autora.
- **Prueba corta de E6b OK:** job 51539, ds001 (A6000), control 6/6, 182.8 s por volumen; cohorte estimada en ~8.8 h.
  Unica cifra vista, sin interpretar (n = 1): `pub`, hueso, `metal_0000`: identidad 156.6, VAE oraculo 222.7, regla 291.2 HU.

Siguiente: lanzar la cohorte de E6b (`KHIPU.md`, E6b, paso 4) y traerla; despues, analizar #36/#39.
**2026-09-15 (4):** `ESTADO.md` consolidado. PUNTO DE RETOMA puesto al dia (tabla con E9-TS, E10/E10b y E6b;
decisiones 6-8; pendientes rehechos) y borrado un "Siguiente" obsoleto de 51504-51506. Verificado en disco: sin
salidas de E6b en la PC, laminas 0/16 y planilla del revisor 0/61. Sin trabajo experimental nuevo.
`01-decisiones.md` sin cambios (no hubo decision nueva). **La autora decide esperar ITK-SNAP** para la frase
"confirmed the S1 level on every patient" de `Field limitation` (#53): se reescribe una sola vez, con el juicio
nuevo. `main.tex` sin cambios. Commit bloqueado por `ESTADO.md` sin stage: `git add docs/ESTADO.md`.

Siguiente: cohorte de E6b (lanzar o traer) y analisis de #36/#39; enviar la planilla al revisor; laminas. Al volver
la planilla: 48/29, 57/57 y la frase "confirmed" de `main.tex`.
**2026-09-15 (5):**
- **Fichas nuevas** (`lector-papers`) de `zhang2025diffboost` y `jacob2026lgesynthnet`. DiffBoost se **releyo sobre
  la version IEEE TMI** que subio la autora (raw `.nbib` -> `.bib` de IEEE; `clean/` y `refs.bib` sin cambios;
  `MAPEO.md` actualizado). Las otras 5 pedidas ya tenian ficha y no se releyeron. `_index.md` al dia (N2 propuesto);
  2 candidatos N3 en `_candidatos.md`.
- **#56 nueva:** la frase de `main.tex:48` ("bounded inpainting... non-rigidity... strictly inside the mask") no es fiel
  para DiffBoost y solo en parte para LGESynthNet; `ramzan2026claim`, citado en la misma frase, no tiene ficha.
  `main.tex` sin cambios.

**2026-09-15 (6):** candidatos de DiffBoost: Med-DDPM [35] agregado (N3); DiffuseExpand [36] a descartados. #56 con
recomendacion de asesor (leer CLAIM, afirmacion causal y no espacial, conservar DiffBoost, bajar "structurally fail") y
correccion: `main.tex:54` no reclama ControlNet. **#57 nueva:** "globally far beyond" frente a B_delta ~12 mm y titulo
"local". Pendiente de la autora: verificar las citas de DiffBoost y LGESynthNet contra el PDF (#56).

Siguiente: la autora decide #56 y #57 (recomendado: leer `ramzan2026claim`, luego una sola reescritura de `main.tex:48/54`);
prioridad por debajo de E6b.

**2026-09-15 (7): cohorte de E6b traida y analizada.** Job 51540: 178 volumenes, 0 errores, rc = 0, control de identidad
frente a E6c **873 de 873**, mediana 180 s/volumen, 8.74 h. Integridad completa. Contra el criterio fijado antes de ver
resultados, el VAE de SD 1.5 sin reentrenar **falla el Go/No-Go de hueso (25 HU) en 178/178 con las tres
configuraciones**, y tambien con el decodificador `oraculo`, que es cota inferior: el mejor volumen de la mejor
combinacion da 52.85 HU. Hallazgo de fondo: `LW20000` y `pub+asinh` tienen identidad **0.00 HU** y el VAE les agrega
**212.00** y **162.95** HU de mediana, dos ordenes de magnitud por encima del error de ventana de E6c (1-6 HU a 8 bits).
Elegir ventana no arregla el Objetivo 1 mientras el VAE sea este. **#36/#39 actualizada** (ronda (7)) con el efecto sobre
las cuatro opciones y una quinta nueva (revisar el umbral de 25 HU, solo si se justifica con bibliografia).
`main.tex`, `00-tesis.md` y `01-decisiones.md` sin cambios (reglas 3 y 14).

**Busqueda de respaldo para #36/#39, solo sobre fichas ya escritas (sin PDFs nuevos, sin buscar fuera):** el umbral de
25 HU **si tiene con que anclarse**. `peters2025hybrid` (2.5, p.5) y `haneda2025aapm` (Sec. 2.3, p.6) definen *CT number
accuracy* como RMSE contra ground truth, con el mismo umbral de hueso de 150 HU; NMAR, el ancla de la escala AAPM, da
RMSE 20.2 (karageorgos, Tabla I, p.28) y el mejor latente publicado 12.74 (yun, Tabla 1, p.10). 25 HU queda justo encima
de NMAR: se justifica, no hace falta bajarlo (desactiva en gran parte la opcion 5). **Problema nuevo: E6b reporta MAE y el
campo publica RMSE**; no son comparables de frente, y el CSV solo guarda MAE. Candidato de VAE con cifra de HU: uno,
indirecto, el **CVQ-VAE x4 de MLD-MAR** (`yun2026simulationdriven`, ref. 23 = Zheng y Vedaldi 2023). Registrado en
`04-implicancias.md` (#36/#39, hallazgos 1-6) y en `_candidatos.md`, seccion "Candidatos de AUTOENCODER" (3 filas; Esser
VQGAN rehabilitado tras estar descartado).

**2026-09-15 (8), orden explicita de la autora:**
- **Umbral de 25 HU anclado y citado.** Decision escrita en `01-decisiones.md` (2026-09-15 (2)): se **mantiene** 25 HU y
  se cita. `main.tex` editado en los dos sitios donde vivia la cifra (Objetivo 1 y fila `Representation Viability`):
  ROI de hueso sobre el umbral de 150 HU del protocolo adoptado, declaracion de que **no existe umbral publicado de
  pasa/no-pasa**, y ancla en NMAR 20.2 HU / imagen 12.3 HU (`karageorgos2024ddpm`) / latente 12.74 HU
  (`yun2026simulationdriven`). **La discrepancia RMSE vs MAE se declara en el texto.** Compila: 4 paginas, 42
  referencias, 0 citas indefinidas. `refs.bib` SIN CAMBIOS (las 4 claves ya estaban; regla 9 respetada).
- **Busqueda web autorizada** (excepcion declarada al flujo de bibliografia; nada entro a `refs.bib`). Resultado:
  el hueco se **confirma** desde fuera (DM4CT no separa la primera etapa y no usa HU), y aparece
  **`Foundation VAEs for 3D CT` (ICML 2026, arXiv:2605.30893)**, que hace la pregunta de E6b y da la respuesta
  contraria con siete VAE de video congelados. Diferencia probable: recortan a **[-1000, 1000] HU**, fuera del rango
  de hueso denso y metal. **Sin verificar.** Es la lectura de prioridad 1. Tres filas en `_candidatos.md`.
- **Opcion 5 de #36/#39 cerrada en la practica**: el umbral no se baja, se justifica.

**2026-09-15 (9), orden de la autora:**
- **`papers/chen2023foundation.pdf` VERIFICADO: es el correcto.** Es *Foundation VAEs for 3D CT...* (arXiv:2605.30893v1,
  ICML 2026), **no** *Towards Generalizable Tumor Synthesis* (que es `chen2024tumorsynthesis`, CVPR 2024). Comparten
  autores (Qi Chen, Yuille, Zhou), de ahi la confusion. **Lo que si esta mal es la clave: dice 2023 y el paper es 2026**,
  y no hay `refs/raw/` para el. Pendiente de la autora: renombrar y pegar el raw (sugerencia `chen2026foundationvae`).
- **E6b reporta ahora MAE y RMSE** (`e6b_vae_sd15.py`). Columna de MAE sin sufijo (no rompe el control ni las corridas
  viejas); RMSE con sufijo ` rmse`; CSV de 32 a **56 columnas**; informe con tablas de las dos metricas y Go/No-Go por
  metrica. Probado en local con `--vae identidad`: control **12/12**, RMSE >= MAE en 24 de 24 pares, y el informe de la
  cohorte vieja se regenera con control **873/873** y MAE identico. Sin regresion. `KHIPU.md` actualizado; comandos sin
  cambio.
- **Hallazgo:** para `pub`, MAE y RMSE no dan lo mismo (2 volumenes de prueba: MAE 2.02 frente a RMSE 53.30 en hueso).
  El techo de 2000 HU satura pocos voxeles con error enorme y MAE lo diluye. `LW20000` y `pub+asinh` dan 0.00 en las
  dos. La metrica **no es neutral: penaliza a la configuracion con techo**, que es el tema de #39. Solo 2 volumenes,
  sin VAE: no se interpreta mas.

**2026-09-15 (10), orden de la autora:** `chen2026foundationvae` **dado de alta y cerrado**. `refs/clean/` +
`build_refs.py` -> **43 entradas**; `MAPEO.md` con fila de procedencia y nota. Decision 2026-09-15 (3) escrita en
`01-decisiones.md`: se cita **el preprint de arXiv** con dos excepciones declaradas (se conservan `eprint`,
`archivePrefix` y `primaryClass` contra la regla 7 de MAPEO, porque son el unico localizador; y se cita como
preprint un trabajo aceptado en ICML 2026). Se reabre solo si el paper llega a citarse en `main.tex`. **`PMLR 306`
no se usa en ninguna parte:** sale solo del pie del PDF y no se confirmo contra el editor. `main.tex` **sin editar**
(no lo cita); el PDF pasa de 42 a 43 referencias por `
ocite{*}`. **E6b RMSE corriendo en Khipu** (prueba corta
51591; el `tail` fallaba solo porque el job estaba en cola, ya documentado en `KHIPU.md`).

Siguiente: **rehacer la cohorte de E6b en Khipu** (~8.8 h; el CSV viejo no tiene las columnas `rmse` y no se pueden
reconstruir). Leer `Foundation VAEs` con `lector-papers` para confirmar el recorte a [-1000, 1000] HU: si se confirma,
es el mejor argumento a favor del encuadre de la tesis; si no, contradice a E6b y hay que responderlo. Despues, probar
el CVQ-VAE reusando E6b. En paralelo, sin bloqueo: planilla de ITK-SNAP al revisor (#53), revision de laminas (0/16),
y #56/#57.

## Paso anterior
2026-09-14 (2):
- **`main.tex` pasa a 48/29** por orden de la autora; compila, 4 paginas.
- **E9-TS listo para la noche:** `e9ts_corredor.py` + `.sbatch`, `e9ts_resumen.py` y `noche_e9ts.sh`, que lanza
  E10, E9-TS y el resumen con dependencias. Calcula recorte x limpieza para los 152 casos con S1 y no decide nada.
  Probado en `metal_0008`: 35 s; D_TS 11.3 (6 mm) / 9.5 (3 mm).
- Recomendaciones registradas en #52 (opcion a, con #35) y #53 (texto de "confirmed").

Siguiente: la autora sube y lanza (`KHIPU.md`, "Noche automatica"). Por la manana, `data/e9ts/e9ts_resumen.md`; luego
decidir F, #52/#35 y el texto de #53.

## Paso anterior
2026-09-14: **#48, #49 y #50 decididas y registradas** en `01-decisiones.md` (asesoria del 2026-09-13, literal, por
orden de la autora). **Transcripcion de R1 corregida:** `metal_0012` = `+1` (lo corrigio la autora) y `metal_0015` = `?`.
Con eso R1 queda en **48/29** (`main.tex` sigue diciendo 49/30, sin aplicar), TS/clinico 57/57 y **#51 cerrada**. La
lista del segundo revisor tiene 15 casos (#53). **E10 preparado y probado en local** (`ts_componentes.py` + `.sbatch`,
manual en `KHIPU.md`).
Siguiente: lanzar E10 en Khipu; la autora decide #52 y la orden para 48/29 en `main.tex`; despues, E9 sobre TS.

## Paso anterior
2026-09-13 (2): **cohorte TS analizada** con `experiments/objetivo2/ts_analisis.py`, que genera `ts_analisis.md` y
`ts_nivel_s1.csv`. TS como detector de nivel: concuerda con el clinico en 56 de 57; R1 falla el nivel en 7 de 60 de
calibracion. Tabla de #50 rehecha: "ala < 150 HU dentro de sacro/S1" da 8% con metal y 15% sin metal (antes 38/43%).
Recorte: ~5% de voxeles y 10 casos con fragmentos desplazados. #48, #49 y #50 actualizadas; **#51 nueva**
(`metal_0012` contradice la cifra 49/30 de `main.tex`). Laminas: 12 de 197, revisadas por agentes.
Siguiente: decisiones de la autora (#48, #49, #50, #51), luego rehacer E9 sobre las mascaras de TS con limpieza de componentes.

## Paso anterior
2026-09-13: **cohorte de TotalSegmentator completa, en la PC y verificada; sin analizar.** 358/358 corridas TS y
QC de 179 casos sin errores; la QC reproduce el piloto. Repetibilidad no exacta (#49, actualizada).
Entrega para el analisis en `experiments/objetivo2/ts_cohorte.md`.
Pendiente que surgio: 32 filas de `sacrum` sin techo (resuelto en parte el 2026-09-13 (2): 12 de 16 casos explicados).

## Paso anterior
2026-09-12 (cierre): **piloto de TotalSegmentator ejecutado y analizado; scripts de la cohorte listos.**
- Piloto: job 51300 (ag001, MIG A100 `3g.20gb`; TS 2.18.0; torch 2.14.0+cu130), 2 casos x {3 mm, 6 mm},
  59-76 s por corrida. Antes fallaron 3 jobs, por la cola y por un bug del script; los dos
  problemas estan documentados en `KHIPU.md`.
- QC (`ts_piloto_qc.py`, `ts_piloto_qc*.csv`, laminas en `outputs/ts_piloto_qc/`): #49 ampliada con
  evidencia; **#50 nueva** (error de nivel de S1 -> "ala < 150 HU" en tejido blando; 6 de 6 casos +1).
- Cohorte: `ts_cohorte.sbatch` (179 volumenes x 2 recortes, reanudable, control de repetibilidad
  contra el piloto) y `ts_qc_cohorte.sbatch` + `ts_qc.py`. Manual en `experiments/objetivo2/KHIPU.md`.
  **Lanzados el 2026-09-12:** TS = job 51315 (ag001, `R`); QC = job 51316 (`big-mem`, espera a 51315).
Siguiente: cierre de 51315/51316 (KHIPU.md, pasos 5-6). Luego, sesion manual de QC y decisiones #48/#49/#50
(PENDIENTE 1).

## Paso anterior
2026-09-12: preparados (no ejecutados) los comandos para correr TotalSegmentator 2.18.0 en Khipu
(`khipu.utec.edu.pe`, particiones `debug-gpu`/`gpu`, `--gres=shard:1`; pesos en el nodo de acceso,
porque los nodos GPU no tienen internet). Solo falta subir `data/derivados/...union.nii.gz`: los 178
originales ya estan en Khipu. #49 nueva (version, `total_v3`, modelo de recorte).
Siguiente: la autora corre el piloto (`metal_0008` + `CLINIC_0002`), valida y decide #48/#49.

## Paso anterior
2026-09-11 (cierre): #31 y #22 decididas y registradas; cifra de R1 escrita en `main.tex`; E9
(corredor) pilotado y **declarado no valido** por segmentacion (#48); E9b mide esponjoso de S1 bajo
150 HU en ~40% de los pacientes, con o sin metal; con y sin los 7 de FOV da lo mismo en densidad.
Siguiente: decidir la via de segmentacion (#48/#29, Khipu) y #36+#39. Detalle en PUNTO DE RETOMA.

## Paso anterior (2026-09-10 / 11, detalle)
2026-09-10: **R1 y E8 ejecutados enteros, y barrido de duplicados parciales.** #26 con cifra
provisional (52/69 marco computable con S1 correcto, 33 sin contaminacion; FOV y heuristica
pesan mas que el metal). #45 nueva: `metal_0059`/`0071` son el mismo estudio (contradice la
decision del 2026-09-07), mas `0011`/`0034` y `CLINIC_0038`/`0090`. #46 nueva: la via (a) de
#41 no produce geometria por umbral. #21: `metal_0068` sin osteosintesis densa.
Cierre del 2026-09-10: la autora **confirma** mismo paciente en los tres pares de #45, que
`0065`/`0066` son la misma persona y que `metal_0068` no tiene material ortopedico. Queda en
#45 una propuesta por par: contenedor, union sin perdida o par de reproducibilidad. Con
ella, dataset7 con osteosintesis pasa a 71 volumenes y 65 pacientes. Tambien hay texto
propuesto para `01-decisiones.md`, sin aplicar.
**Aplicado por orden de la autora:** union sin perdida de `0059`/`0071` en `data/derivados/`
y `Grupo paciente` lleno: 178 volumenes, 168 pacientes; dataset7 con osteosintesis 71/65,
dataset6 sin objeto 70/69.
**Cierre final del 2026-09-10 (orden de la autora):** decision por paciente escrita en
`01-decisiones.md`; `exclusiones.csv` creado (11 volumenes, ningun archivo borrado);
`metal_0068` corregido; `grupos.csv` regenerado (65/37/66); R1 y E8 recontados por paciente:
marco computable con S1 correcto 51/65, sin contaminacion 32/65; >= 17 con tornillo
iliosacro; fuste 5.08 mm.
#20 CERRADA por la autora (indice menor). Mosaicos regenerados sobre 65 pacientes y
plantilla ciega `experiments/objetivo2/r1_auditoria_s1_clinico.csv`.
2026-09-11: la plantilla de S1 la lleno un **medico cirujano ORL** (revisor clinico externo,
no la autora). Con el como referencia: **49/65** marco computable con S1 correcto, **30/65**
ademas sin contaminacion; acuerdo con el agente kappa 0.80. #20 escrita en `01-decisiones.md`.
2026-09-11 (2): **#41 via (c) APLICADA** en `01-decisiones.md` y `main.tex` (Objetivo 2,
regla de aislamiento, parrafo `Implant geometry source`; compila). **Contingencia (a)
ABIERTA:** extraer geometrias de CLINIC-metal si a futuro falta por completo bibliografia
con calibres y longitudes (no la disparan rosca, canulacion ni cabeza). Plantilla renombrada
por la autora a `r1_auditoria_s1_clinico.csv`. Lectura de `xie2024` (#47) lanzada.
Xie leido (#47): cita de C1 PARCIALMENTE respaldada (sobrecobertura solo en cortes simulados;
direccion dependiente del umbral); redaccion alternativa de C1 propuesta, sin aplicar.
Por orden de la autora: `grass2016`, `lee2014`, `wagner2017` y `zhao2012` anadidas a `refs.bib`
(36 -> 40, MAPEO actualizado; tesis compila: 4 paginas, 0 citas indefinidas, 2 avisos ya
conocidos) y `00-tesis.md:114` pasa de 'CAD propia' a geometria parametrica.
C1 reescrita en `main.tex:54` por orden de la autora; **#47 CERRADA**.
Siguiente: FOV del Obj 2 (7 pacientes sin crestas); cifra de R1 (49/65, revisor clinico) en
`main.tex:115`.

## Paso anterior
2026-09-09 (cierre real): **#40 RESUELTA y #41 abierta, y es lo mas grave de la sesion.**
La autora identifico el origen del "banco de 61": es la cita de `liu2021ctpelvic1k`,
Data annotation p. 3, *"The remaining 61 metal-affected CTs ... left unannotated"*.
Confirmado contra la ficha ya verificada y contra la Tabla 1 (`0(61)/0/14`), y contra el
disco: **61 + 14 = 75 = dataset7**. `CLAUDE.md:23` encadena dos errores de categoria:
CT de pacientes leidos como geometrias de implante, y dataset publico de terceros leido
como "insumo propio". **#41: C1 se queda sin insumo.** No existe ninguna fuente de
geometrias de implante en el repositorio, y con eso el Objetivo 2 (unico aporte propio del
minimo viable) no tiene que colocar, **#31 colapsa** (`d_implante` no existe), `main.tex:111`
regula un banco inexistente y `00-tesis.md:114` habla de un CAD propio que no hay.
Opciones ejecutables con lo que hay en disco: (a) extraer geometrias de los implantes de
los 75 CLINIC-metal, con la tension de aislamiento que eso implica, o (c) geometrias
parametricas con los rangos publicados de #30 y #31. Propuesta de correccion de
`CLAUDE.md:23` redactada en #40, sin aplicar.
Precision: 1184 y 75 son cifras del propio paper de 2021 (Introduction p. 2 y Tabla 1
p. 3), no una actualizacion posterior. **#40 CERRADA el 2026-09-09**: la autora retira su
observacion sobre el dataset y confirma que el estado de ANOTACION de los 61 no ha
cambiado y que la lectura de la evidencia textual era correcta. Sin efecto sobre #13
(siguen 14 de 75 anotados) ni sobre #41, que sigue ABIERTA.
Siguiente: la autora decide #41 (de donde salen las geometrias) — es ahora el bloqueo
numero uno del alcance minimo, por delante de #37, #39 y #36.

## Paso anterior
2026-09-09 (cierre): **E6a ejecutado** y **bloqueo declarado por pedido de la autora**.
E6a mide el tramo `HU -> ventana -> HU` del Objetivo 1 (sin VAE, cota inferior de
cualquier decodificador). Dos hallazgos: **#38**, las tres ventanas publicadas son
**redundantes en reconstruccion** (`max |LW - oraculo|` en hueso a float = **0.0 exacto**;
la unica ganancia es 1.679 HU a 8 bits, o sea cuantizacion, no rango) — no refuta C3, pero
si refuta que la multi-ventana **preserve mejor los HU**; y **#39**, el Go/No-Go
**no puede fallar** en pelvis limpia (mediana **0.00 HU**) y **falla en 48 de 75** con
metal (mediana 46.36, max 274.49), antes del VAE, solo por el techo de 2000 HU de LW.
En ROI de metal el MAE es **3588.80 HU** de mediana, con HU maximo mediano de 18 822 y
pico 24 970 contra un techo de 2000: **la representacion no puede codificar lo que la
tesis debe generar.** `main.tex` no declara sobre que cohorte se evalua el Objetivo 1.
**Bloqueo declarado:** #15, #22, #34 y #35 detenidas hasta que la autora marque artefactos.
Afecta solo la cohorte del Objetivo 3; Obj 1 y Obj 2 siguen libres.
Antes tambien: **#34 corregida por procedencia** (la columna `Artefactos` la llenaron los
agentes desde laminas, no la autora; sus 20 `no` son afirmaciones de ausencia fragiles),
**#35** (una cohorte para tres consumidores), **#36** (el VAE del Obj 1 no esta
especificado en ningun documento) y **#37** (`revision.csv` no declara procedencia por
campo).
Siguiente: la autora decide **#37 primero** (procedencia por campo) y luego hace la
revision visual de estriacion sobre los 33 volumenes de dataset6 con objeto. En paralelo,
decidir #38/#39 (que hacer con el techo de 2000 HU) y #36 (que VAE). Sigue sin ubicarse el
banco de 61 geometrias.

## Paso anterior
2026-09-09: **primer experimento del giro a benchmarks (E1)**. Corrido
`experiments/exploration-3d/sensibilidad_hu.py` sobre los 178 volumenes locales (solo
lectura; `revision.csv` intacto). **#22 EJECUTADA**: 1500 HU deja 177 de 178 como
candidatos y **queda descartado** (entra hueso cortical); 2500 HU da 113 candidatos, 65
limpios y **cero falsos negativos** contra la revision 3D de la autora; 3500 HU da 104
candidatos y 74 limpios pero **pierde 5 metales reales**. Cambios de clase: 64 de 1500 a
2500, 9 de 2500 a 3500. Las 178 clasificaciones a 2500 reproducen exactamente
`revision.csv`. **#34 nueva**: los 5 que pierde el 3500 son los cinco `accesorio`
extracorporeos de dataset6, asi que el umbral y la definicion de `Objeto extraño` son la
misma decision (2500 -> 65 limpios; 3500 -> 74 limpios). Ademas, analisis de prioridad de
las 34 implicancias y cola de experimentos E1-E6 propuesta.
Siguiente: **E6, el Go/No-Go del Objetivo 1** (MAE < 25 HU en hueso del round-trip
multi-ventana), que no tiene ningun bloqueo. Antes de E2 y E3 hacen falta tres decisiones
de la autora: adoptar o no TotalSegmentator (#29), donde esta el banco de 61 geometrias
(NO esta en `data/`, que solo tiene dataset6 y dataset7), y si se adopta la formulacion
parametrica `Dmax >= d_implante + holgura` (#31).
Aviso de estado del repo: `docs/04-implicancias.md`, `refs.bib` y `tesis/main.pdf` siguen
modificados sin commitear desde el 2026-09-08, mas 15 `refs/raw/*` sin trackear.

## Paso anterior
2026-09-08: cerrada la seccion "la geometria que McLaren NO publica" con 7 lecturas
(`grass2016`, `wagner2017`, `lee2014`, `hasenboehler2011`, `zhao2012`, `mendel2011`,
`gottschling2009`). La geometria SI existe pero en marcos que no componen (#30); Gras y
Wagner se invierten el orden S1/S2 por definicion distinta de diametro (#30b, corrobora
#12 y #27); el umbral es siempre calibre de tornillo mas holgura en 7 fuentes, lo que
habilita expresarlo como `Dmax >= d_implante + holgura` sobre el banco de 61 (#31);
Gottschling es de femur y tibia (#32); el "hasta 50%" de dismorfismo no lo sostiene
ninguna de las tres fuentes citadas (#33). Busqueda de corredor: **cerrada por saturacion**.
Decision de la autora: cerrar **tras** dos lecturas finales (`carlson2000`, `ebraheim1997`),
y cierre **reversible** si los experimentos revelan que falta geometria. **Ebraheim leido**
(pediculo S1 en mm, entrada a 3-3.5 cm del borde posterior del ilion, margen 4-6 mm entre
dos tornillos; sin angulos, sin S2; septimo marco incompatible, #30 ampliada).
**Carlson BLOQUEADO: falta el PDF y el raw.** Unica candidata de reapertura anotada:
Morse 1994, angulos para tornillo sacro sobre TC preoperatoria.
Siguiente (decidido por la autora): cerrar los tres pendientes de datos — cifra de R1 (#26),
tabla de sensibilidad HU 1500/2500/3500 (#22) y representante de los 3 grupos duplicados
(#20, que bloquea el split). Todo sobre datos ya en disco.

## Paso anterior
2026-09-08: evaluado TotalSegmentator para el Objetivo 2 (#29 ABIERTA). Es util como
ROI/mascara anatomica inicial (`sacrum`, S1, caderas), no entrega S2, cortical, landmarks
ni corredor y no esta validado aqui bajo metal. Recomendado piloto 1.5 mm + QC local;
pendiente decision de adopcion. No cambia SAP ni downstream.

## Paso anterior
2026-09-08: Keating 1999 leido con `lector-papers` desde DOCX completo sin paginacion.
SI publica malposicion en 5/38 pacientes (13%): fuente indirecta via Hinsche y punto
interior, no origen del rango 2%-15% ni de sus extremos. Binario, radiografico, sin
S1/S2 ni escala SAP; #12 no se reabre. `refs.bib` = 36; tesis recompilada sin citas
indefinidas. Siguiente: sensibilidad HU y #26.

## Paso anterior
2026-09-08: Gardner incorporado como respaldo anatomico S1/S2 en `00-tesis.md`,
`01-decisiones.md` y `main.tex` (Problem Statement y Objetivo 2), por encargo de la autora.
Se mantiene geometria individual sin fenotipos y benchmark ordinal SAP solo en S1.
PDF recompilado: 4 paginas, sin citas indefinidas. Siguiente: sensibilidad HU y landmarks (#26).

## Paso anterior
2026-09-08: auditada consistencia de Gardner contra su ficha ya leida. Corregidos
candidatos, indice, ficha e implicancias: LEIDO; areas S1/S2 similares en dismorficos,
no inversion ni prior ordinal. Sin cambio de alcance: geometria individual sin fenotipos;
SAP clinico solo S1. Siguiente: sensibilidad HU y landmarks (#26).

## Paso anterior
2026-09-08: van den Bosch leido con `lector-papers`; 6/31 vs 1/49 son pacientes con
quejas neurologicas, no malposicion por nivel. #28 resuelta; #12 cerrada delimitando
SAP ordinal a S1 por tecnica, S2 descriptivo. Aplicado en tesis y alcance; 35 referencias.
Siguiente: sensibilidad HU y landmarks (#26). Prior ordinal clinico S2 sigue no disponible.
Validacion: PDF recompilado, 35 entradas y ninguna cita indefinida; dos avisos BibTeX
ya documentados por revistas sin volumen (Hinsche y Templeman).

## Paso anterior
2026-09-08 (cierre): auditada entera la cadena de citas del umbral de 10 mm con tres
lecturas mas (`ziran2007fluoroscopic`, `moed2006s2screw`, `gardner2010safezones`).
**Cuatro eslabones, ninguno lo mide**: Ziran no contiene el umbral, el "1 cm" de Moed es
separacion interforaminal (otra magnitud), Kaiser lo elige y Gardner lo declara como
consenso por calibre de tornillo. Conclusion: **nunca fue una medicion, es una convencion
profesional**, y la tesis lo afirma con frases literales. Cadena declarada agotada.
Decisiones de la autora aplicadas: **no estratificar por fenotipo** (#27 CERRADA, y con eso
la objecion de Carlson 2000 deja de aplicar); la geometria en pelvis intactas se reescribe
como **limitacion del campo** en `main.tex`; se anade el respaldo **anatomico** de C2 con
los coeficientes de variacion de Ziran (hasta 97-140%); se adopta la **tabla de
sensibilidad** de cribado a 1500/2500/3500 HU; Ziran queda N2 y Moed baja a **N2
provisional**. `refs.bib` = 34. 16 decisiones fechadas en `01-decisiones.md`.
**#28 nueva**: van den Bosch preparado con el encargo completo redactado y SIN ejecutar.
Siguiente: conseguir el PDF de van den Bosch (decide el eje S1/S2 y puede cerrar #12),
correr la tabla de sensibilidad y la cifra de R1 (#26). Ambas sobre datos ya en disco.

## Paso anterior
2026-09-08 (tarde/noche): la autora adopto las opciones recomendadas y autorizo
aplicarlas. **APLICADO** en `tesis/main.tex` (RQ e hipotesis sin downstream, Obj 5
eliminado con parrafo `Explicitly out of scope`, Obj 4 con SAP como unica metrica propia
y metricas de Peters con sus nombres, C3 reescrita, el rango 31-60% sustituido por las dos
distribuciones ordinales de Zwingmann condicionadas por tecnica y nivel sacro, zona segura
via McLaren con el umbral declarado heredado), en `docs/00-tesis.md` (`Fuera de alcance`
escrito con seis puntos) y en `docs/03-glosario.md` (escrito entero). Compila limpio, 31
entradas. **#14 y #16 CERRADAS**; #13 y #18 degradadas a limitacion declarada.
Alta y lectura de `kaiser2014dysmorphism`: **no** establece el 10 mm (tercer salto de
cita, hacia Gardner 2010 / Ziran 2007 / Moed 2006), pero aporta el marco de referencia
calculable (reformateo perpendicular al platillo de S1, angulo coronal vs crestas iliacas,
angulo axial vs espinas iliacas posteriores, margen cortical de 5 mm, tres fenotipos).
**#26 nueva**: Kaiser midio en pelvis SIN implante y excluye los CT con metal.
Siguiente: la autora decide sobre las cinco propuestas de Kaiser (a-e), y falta que
recoja en `01-decisiones.md` las seis decisiones ya aplicadas.

## Paso anterior
2026-09-08: alta de 3 fuentes (`mclaren2021corridor`, `hinsche2002fluoroscopy`,
`templeman1996proximity`) y llegada del PDF de `wang2025adaptiveweighting`. `refs.bib`
regenerado a 30 entradas. Tres lecturas con `lector-papers`. Resultado: **#1 CERRADA**;
**#2 confirmada** contra el cuerpo; **#7 pasa a PARCIALMENTE CUBIERTA** (McLaren da
umbral y procedimiento, no geometria parametrizada); **#12 agravada** (el 2-15% es cita
de tercera mano y Hinsche es banco sobre plastico); **#13** con tres datos cruzados;
**#24 nueva** (el respaldo de C3 es fuente secundaria y el mecanismo es cascada, no
codificacion de entrada); **#25 nueva** (patron sistemico: tres anclas cuantitativas son
citas heredadas). Decision de la autora tomada: adoptar metricas de Peters, Obj 5 fuera
de alcance, Obj 4 modificado; falta registrarla en `01-decisiones.md` y aplicarla.
Siguiente: que la autora elija opciones en #7, #12, #24 y #25, y decida el nivel de
McLaren (ficha dice N2, `_index.md` dice N1).

## Paso anterior
2026-09-07: cerrados tres pendientes abiertos por orden de la autora.
(1) **LNCS: se ignoran.** La tabla con los volumenes retirados salio de `refs/MAPEO.md`;
en su lugar queda la decision de no perseguirlos, sin los valores, para que nadie los
reintroduzca sin respaldo en `refs/raw/`. (2) **`.gitignore` limpio**: se quitaron el
`@'` inicial y la linea `'@ | Set-Content ...` final; las reglas se verificaron con
`git check-ignore` (`papers/`, `data/`, `*.nii.gz`, `*.bbl`). (3) **`main.tex` migrado a
BibTeX**: `natbib` con `abbrvnat`, `\bibliography{../refs}` y las 19 citas del cuerpo
convertidas a `\citep`/`\citet`/`\citealp`. La lista en texto plano (27 entradas a mano)
desaparecio; ahora sale de `refs.bib`. Compila limpio, 0 citas indefinidas, 27 entradas
en el `.bbl`, y las citas del cuerpo se imprimen igual que antes.
Siguiente: cerrar el representante de los 3 grupos internos de dataset7.

## Paso anterior
2026-09-07: montado el pipeline bibliografico `refs/raw` -> `refs/clean` -> `refs.bib`
por encargo de la autora. 27 fuentes del editor (16 nbib de PubMed, 10 bib, 1 txt),
27 entradas normalizadas en `refs/clean/`, procedencia y reglas en `refs/MAPEO.md`,
regeneracion con `scripts/build_refs.py`. Los 27 DOIs y las 27 claves quedaron
identicos; se corrigio `issue`->`number` en tres entradas (fasciculo que BibTeX
descartaba), se desambiguo `CORR`, se completaron autores y el volumen de SPIE.
`main.tex`: 15 correcciones en la lista de referencias, sin migrar a BibTeX.
Cerrado con los 5 .bib oficiales que pego la autora: `wu2022xcist` confirmado por IOP,
`ramadanov2025safezone` por MDPI, y los tres volumenes LNCS retirados porque el
exportador de Springer no los trae. `refs.bib` sin ningun `% VERIFICAR`. Decision de
precedencia registrada en `01-decisiones.md` con orden explicita.
Regla 9 de `CLAUDE.md` reescrita y marcas eliminadas de `refs.bib`.
Siguiente: cerrar el representante de los 3 grupos internos de dataset7.

## Paso anterior
2026-09-07: la autora reviso en 3D los 178 volumenes; fusionadas sus tres reglas de
clasificacion con la investigacion de los agentes en `revision.csv` (178 filas,
`3D completa`). Cifras: dataset7 con material ortopedico 72 de 75 (69 de contenido
unico); dataset6 con objeto 33, de ellos 27 solo extracorporeo; 70 candidatos a
entrenamiento limpio. #20 y #21 resueltas en criterio, #22 cuantificada (27 volumenes
en juego). #19 estrechada: `CLINIC_0074` resuelto (hay lazo, no es metal) y regla nueva
"autora sin objeto + agente incierto = sin objeto". `metal_0059`/`metal_0071` descartado
como par. Textos "preliminar" borrados de metal_0002 y metal_0003.
Siguiente: que la autora copie sus reglas a `01-decisiones.md` y elija representante en
los 3 grupos duplicados internos de dataset7.

## Paso anterior
2026-09-07: corridos 12 agentes `clasificador-metal` sobre los 113 candidatos HU.
113 filas en `propuesta_clasificacion.csv`, todas `propuesta sin validar`; `revision.csv`
intacto (sigue con 3 filas parciales). Metal: 65 `si (propuesto)`, 42 `incierto`, 1 `no`,
5 mixtos. Cuatro implicancias nuevas #19-22: el umbral HU no detecta (objeto bajo 1500 HU
en CLINIC_0074), duplicados CRUZADOS entre sub-datasets (fuga train/test), CLINIC-metal
con material extracorpóreo, y `Objeto extraño` sin definicion operativa.
Siguiente: decidir #19 (revisar los 178) y #22 (definicion), resolver duplicados.

## Paso anterior
2026-09-07: auditado `experiments/exploration-3d` contra el encargo de Victor.
Descripcion de datos cubierta para lo local; metal y split instrumentados pero SIN
ejecutar (0 de 178 confirmadas, 166 pendiente + 12 duplicado). Nuevo: solo 178 de los
1184 volumenes de CTPelvic1K estan en disco -> implicancia #18. Construido (no corrido)
el subagente `clasificador-metal` con `laminas.py` y `propuesta_clasificacion.csv`.
Siguiente: correr el agente sobre los 113 candidatos y los 65 no candidatos de dataset6.

## Paso anterior
2026-09-07: adopción de Peters registrada en `01-decisiones.md` con autorización.
Índice y fichas armonizados: Peters N1, Wu/XCIST N2; N4 de descartes creado y vacío.
Siguiente: concretar adaptación/validación del protocolo (#16–17) y armonizar `00-tesis.md`.
Continúan pendientes revisión 3D completa, pacientes/duplicados y máscaras.

## Paso anterior — exploración 3D
2026-09-07 (cierre del encargo del 06): flujo 3D con un script y un CSV listo;
178 CT, 113 candidatos HU, 6 grupos duplicados, 3 revisiones parciales. Peters en main.tex.
Siguiente: completar revisión 3D+cortes, resolver duplicados/pacientes y máscaras.
Nuevas implicancias #15–17; #8 aplicada a redacción, validación técnica pendiente.

## Paso anterior — verificación bibliográfica
P4: verificacion de niveles con 10 subagentes `lector-papers`, uno por PDF. **6 de mis
7 movimientos verificados estaban mal.** Reparto corregido a 8/12/7, con 10 fichas
nuevas. Salieron 4 implicancias (#7 a #10) y se actualizaron #5 y #6 con evidencia
textual. `_candidatos.md` poblado con 21 candidatos de snowballing.

## Paso anterior
P3: niveles de `_index.md` reasignados por el criterio nuevo de la autora (riesgo
sobre el argumento central o el benchmark).

## Paso anterior
P2: `docs/literatura/_index.md` completado. Las 27 entradas de `refs.bib` tienen fila,
con estado del PDF y acceso. Inventario: 25 de 27 PDFs presentes; faltan
`wang2025adaptiveweighting` y `zhang2026pediclescrew`.

## Paso anterior
P1: `refs.bib` generado desde la seccion References de `tesis/main.tex`. 27 entradas,
claves `apellidoANIOpalabraclave`. Las 27 quedaron marcadas `% VERIFICAR`.

Ademas: `scripts/renombrar_papers.sh` generado (NO ejecutado). Los 25 PDFs
emparejados, ninguno pendiente. Conflicto de claves resuelto: manda `refs.bib`,
se corrigio `_index.md`. Ficha de `wang2025adaptiveweighting` creada desde abstract.

## Pendientes bibliográficos anteriores
Decidir sobre la implicancia #9 (reenunciar el gap) y la #7 (el muestreador sin fuente
operacional de zona segura). Las dos tocan el alcance minimo viable y ninguna se puede
resolver leyendo mas: son decision de la autora. En paralelo, conseguir McLaren 2021,
que es la posible solucion de #7.

## Pendientes abiertos
- La bibliografia crecio de 2 a 3 paginas al migrar a BibTeX. No es un error: la lista
  a mano llevaba `et al.` y omitia DOI, editores e ISBN; la generada los imprime todos.
  Se probo `plainnat`, `abbrvnat` y `biblatex` con `maxbibnames=1`: las tres dan
  3 paginas. Si hay limite de dos, la decision es de la autora y las palancas son
  quitar los DOI del impreso o bajar el cuerpo de letra de la lista.
- 11 de las 27 entradas no se citan en el cuerpo (`karageorgos2024ddpm`,
  `kazerouni2023diffusionsurvey`, `ren2022metalinsertion`, `rombach2022latentdiffusion`,
  `selles2024marreview`, `singhrao2024fiducial`, `vanbosse2011pelvicpositioning`,
  `wang2019cochlear`, `yun2026simulationdriven`, `zhang2023controlnet`,
  `zhang2026pediclescrew`). Las sostiene `\nocite{*}`, puesto para que la lista siga
  siendo exactamente la que definio la autora. Citarlas en el cuerpo o retirarlas es
  decision suya; sin `\nocite{*}` la lista bajaria a 16 entradas.
- Implicancia #1 ABIERTA: `wang2025adaptiveweighting` es nivel 1 y solo hay abstract.
  Al llegar el PDF, releer con `lector-papers` y regenerar la ficha completa.
- Implicancia #2 ABIERTA (GAP): el multi-ventana publicado es todo de remocion, no
  de sintesis. Verificar el reclamo de novedad antes de escribirlo.
- Implicancias #3 y #4 ABIERTAS, ambas de `zhang2026pediclescrew`: colision de
  encuadre con mi novedad, y una segunda escala de brecha cortical con umbral de
  2 mm que toca la definicion de BFC.
- Implicancia #5 ABIERTA, ACTUALIZADA: `liu2025pipeline` no compite en metodo (plan
  optimo determinista), pero define CSV y QID sobre CTPelvic1K, vecinas de SAP y BFC.
- Implicancia #6 ABIERTA (GAP), ACTUALIZADA: `ren2022` aporta la frase que fundamenta
  el gap pero no sirve de brazo de comparacion (exige raw data de fabricante).
- Implicancia #7 ABIERTA (RIESGO): el muestreador se queda SIN fuente operacional de
  zona segura. Toca el alcance minimo viable. La mas urgente.
- Implicancia #9 ABIERTA (GAP): insertar metal sintetico ya es practica establecida en
  4 trabajos, y la difusion latente ya compitio en MAR. Hay que reenunciar la novedad.
- Implicancia #10 ABIERTA (REDACCION): `chen2024tumorsynthesis` no modela nada fuera de
  la mascara y trunca HU a [-175,250]: respaldo citable de B_delta y de C3.
- `karageorgos2024ddpm`: el subagente propuso N1, se mantuvo en N2 por consistencia.
  Disenso registrado en `_index.md`; decision de la autora.
- `chen2024tumorsynthesis`: candidato a subir a N1, sin decidir.
- Implicancia #11 ABIERTA: SAP ignora la segunda escala (angular) de `smith2006iliosacral`,
  y las tasas de ese paper son cadavericas n=4: no sirven de prior clinico.
- Implicancia #12 ABIERTA (RIESGO, la mas grave): el rango 31-60% NO aparece en
  `zwingmann2009navigated`. Son dos complementos derivados de dos brazos distintos.
- Implicancia #13 ABIERTA (RIESGO): CLINIC-metal tiene solo 14 de 75 volumenes anotados,
  el paper no dice que metal contiene, y no da cifra de degradacion.
- Implicancias #19-22 ABIERTAS, todas de la clasificacion asistida, pero
  estrechadas por la revision 3D del 2026-09-07:
  - #19 estrechada: `CLINIC_0074` resuelto (no es metal). Siguen vivas dos patas,
    el artefacto que fabrica componentes y la mesa del escaner como componente.
    Opcion 1 (correr laminas sobre los 65 no candidatos, ~25 min) sigue abierta.
  - #20: criterio cruzado ya dictado por la autora; falta elegir representante en
    los 3 grupos internos de dataset7 (`0012`/`0021`, `0013`/`0043`, `0046`/`0074`).
    Hasta eso, sigue bloqueando el split.
  - #21 CONFIRMADA con cifra: 3 de 75 de CLINIC-metal no tienen osteosintesis.
    El test es 72, de contenido unico 69. Falta fijar esa cifra.
  - #22 sin decidir, y es la mas barata: define 70 vs 97 volumenes de entrenamiento.
- Implicancia #18 ABIERTA (DATOS): en disco hay 178 de los 1184 volumenes de
  CTPelvic1K; faltan ABDOMEN, COLONOG, MSD_T10, KITS19 y CERVIX. Decidir si se
  descargan o si el alcance de datos se declara como CLINIC + CLINIC-metal.
- Encargo de Victor a medias: `experiments/exploration-3d/cumplimiento-encargo.md`
  detalla que sub-tarea esta cubierta. `clasificador-metal` ya corrio y la revision
  3D esta completa; falta representante en los 3 grupos internos de dataset7 y
  `Grupo paciente`, vacio en las 178 filas, antes de cualquier split.
- Implicancia #14 ABIERTA (GAP): `peters2025hybrid` da la base operacional de BFC e ISC y
  sostiene por escrito la novedad del muestreador. La lectura mas productiva de todas.
- Falta armonizar el alcance completo de `00-tesis.md` con la adopcion de Peters
  (su frase sobre reimplementacion independiente de XCIST).
- Verificacion de #13 pendiente y no bibliografica: mirar los volumenes para saber que
  metal contienen. (La otra —si CLINIC-metal amplio su anotacion desde 2021— quedo
  CERRADA el 2026-09-09 con el cierre de #40: no se amplio.)
- `wang2025adaptiveweighting`: unico N1 SIN VERIFICAR, tercera ronda bloqueado por el PDF.
- Faltan por verificar tambien:
  `arand2019pelvicring` y `xie2024implantsegmentation`.
- `SAP`, `BFC` e `ISC` siguen sin definir en `docs/03-glosario.md`. El nivel de
  `xie2024implantsegmentation` y el de `liu2025pipeline` dependen de esas definiciones.

## Pendientes cerrados
> Lo que ya no requiere accion. Se conserva para no reabrirlo por olvido.

- **Implicancia #8 — APLICADA (redaccion).** La autora adopto el protocolo de
  `peters2025hybrid` como brazo de comparacion en lugar de la reimplementacion de
  XCIST; `wu2022xcist` no valida metal. Decision registrada en `01-decisiones.md`
  con autorizacion el 2026-09-07 y escrita en `main.tex`. Lo que sigue vivo es #17
  (ejecucion, configuracion y validacion) y armonizar `00-tesis.md`.
- **`zhang2026pediclescrew`: nivel resuelto.** Queda en nivel 1 por el criterio de
  riesgo, al ser origen de las implicancias #3 y #4.
- **Mapeo difftumor = `chen2024tumorsynthesis`: RESUELTO** contra el PDF.
- **Par `metal_0059` / `metal_0071`: DESCARTADO.** La autora confirmo el 2026-09-07,
  tras revision 3D, que no son el mismo paciente: comparten spacing y HU minimo, nada
  mas. Sin `Grupo paciente` comun. Registrado en `01-decisiones.md`.
- **#20, criterio cruzado: DICTADO.** En un grupo duplicado que cruza sub-datasets
  prevalece el volumen de dataset7 como representante, y ese volumen queda marcado
  sin material ortopedico. Afecta a `metal_0061`=`CLINIC_0037`,
  `metal_0036`=`CLINIC_0048`, `metal_0064`=`CLINIC_0070`.
- **#19, conflictos autora/agente: RESUELTOS.** `CLINIC_0074` tiene una estructura en
  lazo pero no es metal, asi que sigue siendo candidato limpio. Regla general dictada:
  autora «sin objeto» + agente `incierto` = sin objeto. Cierra los cinco desacuerdos
  menores.
- **Revision 3D de los 178 volumenes: COMPLETA** (`3D completa`, no recorrido de
  cortes). Fusionada con la investigacion de los agentes en `revision.csv`.
- **Textos «preliminar»** borrados de `metal_0002` y `metal_0003`.
- **`refs.bib`: los 27 DOIs, PUESTOS y VERIFICADOS contra el raw del editor.**
  Ninguno cambio al reconstruir el archivo, ni se anadio ni se quito ninguna entrada.
- **Pipeline bibliografico `raw` -> `clean` -> `refs.bib`: MONTADO** el 2026-09-07 por
  encargo de la autora. `refs/raw/` (27 fuentes del editor, intactas), `refs/clean/`
  (27 entradas normalizadas a mano), `refs/MAPEO.md` (procedencia y reglas) y
  `scripts/build_refs.py`, que regenera `refs.bib`. Los `% VERIFICAR` obsoletos
  desaparecieron; quedan 4 nuevos, reales.
- **Bug de compilacion corregido: `issue` -> `number`** en `liu2021ctpelvic1k` (16(5)),
  `xie2024implantsegmentation` (24(1)) y `zhang2026pediclescrew` (34(4)). BibTeX
  clasico descarta `issue` sin avisar: esos tres fasciculos no se habrian impreso.
- **`CORR` desambiguado** a *Clinical Orthopaedics and Related Research* en
  `vanbosse2011pelvicpositioning` y `zwingmann2009navigated`. Se confundia con el
  repositorio de preprints *CoRR* de arXiv. Igual `IEEE TMI` e `Int J CARS`.
- **`deman2007catsim` volume 6510**, que faltaba, confirmado por el raw de SPIE.
- **Autores completos en las 27.** Antes 25 decian `and others`.
- **Precedencia dictada por la autora (2026-09-07): manda `refs/raw/`,** y en su
  defecto `refs/clean/`. Un campo que el raw no confirme no se conserva por costumbre.
  Pendiente que la autora lo copie a `01-decisiones.md`.
- **`ramadanov2025safezone`: raw RESUELTO** el 2026-09-07. La autora sustituyo el .txt
  degradado por el .bib real de MDPI y borro el .txt. Confirma 14(10):3567, el DOI que
  ya estaba, y que el titulo si lleva los dos puntos. Es la fuente de la implicancia #7.
- **Los 4 campos sin respaldo: CERRADOS** el 2026-09-07 con los .bib oficiales.
  `wu2022xcist` CONFIRMADO por IOP (`pages = {194002}`, 67(19)). Los tres volumenes
  LNCS RETIRADOS de `refs.bib` y de `main.tex`: el exportador de Springer no los da.
  `refs.bib` ya no tiene ningun `% VERIFICAR`.
- **Decision de precedencia REGISTRADA** en `01-decisiones.md` el 2026-09-07 con orden
  explicita de la autora.
- **Regla 9 de `CLAUDE.md` REESCRITA** el 2026-09-07 con orden explicita: describe el
  flujo `raw` -> `clean` -> `refs.bib` generado, prohibe cualquier campo sin respaldo
  en el raw y mantiene que la lista de entradas la define la autora.
- **Marcas eliminadas de `refs.bib`.** Ni `% VERIFICAR` ni `% NOTA`: lo que esta en el
  archivo tiene respaldo en el raw. Lo retirado queda solo en `refs/MAPEO.md`.
- **`main.tex`, MIGRADO A BIBTEX** el 2026-09-07 con orden explicita de la autora.
  `\usepackage[round,authoryear]{natbib}`, `\bibliographystyle{abbrvnat}` y
  `\bibliography{../refs}` dentro del `multicols`, con `\renewcommand{\bibsection}{}`
  para no duplicar el encabezado `\section{References}`. Las 17 citas del cuerpo pasaron
  de texto a `\citep` (parentesis), `\citet` (autor + anio en linea) y `\citealp`
  (dentro del parentesis de C1). La lista a mano se borro entera. Compila con
  `pdflatex; bibtex; pdflatex; pdflatex` desde `tesis/`: 0 citas indefinidas, 27
  `\bibitem` en el `.bbl` y las citas del cuerpo impresas igual que antes. Lo que
  cambia de aspecto es la lista: 3 paginas en vez de 2, y 11 entradas la sostiene
  `\nocite{*}`. Las dos cosas estan en Pendientes abiertos.
- **`.gitignore`: LIMPIADO** el 2026-09-07. Se quitaron el `@'` de la primera linea y
  el `'@ | Set-Content -Encoding utf8 .gitignore` de la ultima, restos de un here-string
  de PowerShell que se escribio en vez de ejecutarse. Reglas verificadas con
  `git check-ignore -v`: `papers/`, `data/`, `*.nii.gz` y `*.bbl` se ignoran;
  `refs/raw/*.bib` no.
- **LNCS: IGNORADOS por decision de la autora** el 2026-09-07. Los tres volumenes
  (`jacob2026lgesynthnet`, `ramzan2026claim`, `wang2019cochlear`) no se persiguen en
  otra fuente. Sus valores salieron de `refs/MAPEO.md` para que nadie los reintroduzca
  sin respaldo en `refs/raw/`; ahi queda solo la decision y el motivo (el exportador de
  Springer no trae `series` ni `volume`).
- **`main.tex`, lista de referencias actualizada** el 2026-09-07 con autorizacion
  explicita: 15 correcciones (revistas completas, fasciculos, paginas de las tres
  actas, volumen de SPIE). Sigue en texto plano; no se migro a BibTeX.


## Deudas asumidas
- Leer a fondo Zwingmann 2009 y Smith 2006 antes de la sustentacion:
  la metrica SAP depende de la definicion de grados de brecha cortical.
