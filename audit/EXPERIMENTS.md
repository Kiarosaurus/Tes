# EXPERIMENTS.md — Fase 1: inventario y triage de experimentos

Snapshot: `review/` (solo lectura). Rutas de resultados relativas a `review/results/`; rutas de tesis relativas a `review/thesis/secciones/`. Abreviaturas: **I**=introduccion.tex, **C3**=capitulo3.tex, **C4**=capitulo4.tex, **CO**=conclusiones.tex, **TF**=trabajosFuturos.tex.

**Alcance y límites de esta fase.**
- Las cifras se copian de los `.md`/`.tex`. No recalculé los CSV.
- `docs/01-decisiones.md`, `04-implicancias.md`, `obsoletos/` y `data/` no están en el snapshot. Las decisiones y las implicancias (#nnn) que citan los scripts son **NO VERIFICABLES CON EL SNAPSHOT**.
- No hay figuras de resultados (`.png`) en `results/` fuera de las láminas de `exploration-3d/outputs/`. La tesis no incluye ninguna figura de resultados (`inventory.md`: 2 `\begin{figure}`, 0 `includegraphics`).
- Objetivos de la tesis (I:37-43): **O1** compuerta Go/No-Go de representación; **O2** muestreador de colocación + SAP + referencia clínica; **O3** sintetizador por difusión en imagen, evaluado contra Peters (physical protocol), copy-paste y E-A1; **O4** definición de SAP y adopción de métricas de Peters (sin evaluación propia).
- Mapa de nombres: v1 = `run04` (`run04_mejor`, paso 16 500; `run04_60k` = sensibilidad de checkpoint). v2 = `run05a` (sobremuestreo + peso, "D") y `run05b` (+ canal T, "B" analítico). "Peters" = protocolo físico XCIST con Ti/Fe.

## 1. Tabla resumen

| # | Familia | Estado | Rol | Tratamiento |
|---|---|---|---|---|
| E1 | Datos y auditoría de cohorte (`exploration-3d`) | ESTABLE | Baseline indispensable | CONSERVAR (cuerpo resumido) + TRASLADAR A ANEXOS el embudo detallado |
| E2 | O1: e6a / e6c (ida y vuelta sin autoencoder; barrido de techo LW) | ESTABLE | Ablación relevante | RESUMIR (cifras clave en cuerpo; tabla e6c a Anexos) |
| E3 | O1: e6b (VAE SD1.5 preentrenado, 178 volúmenes) | ESTABLE | Exploración metodológica | RESUMIR |
| E4 | O1: p1 compuerta Go/No-Go + sensibilidades sin 0053/0072 | ESTABLE | Contribución principal (hallazgo negativo) | CONSERVAR |
| E5 | O1: extensión a MAISI (cota por saturación) | ESTABLE (trazabilidad rota) | Evidencia complementaria | CONSERVAR condicionado a recuperar script/cifra (ver Dudas) |
| E6 | O2: e8 + e11 (censo morfológico, perfil axial) | ESTABLE | Evidencia complementaria (fija 4.91 mm) | RESUMIR |
| E7 | O2: TotalSegmentator QC + e9ts (+3 mm, revisión de láminas) + e14 | ESTABLE | Baseline indispensable | CONSERVAR (e9ts); RESUMIR (3 mm, láminas, e14) |
| E8 | O2: r1 landmarks / r2 nivel / r3 fractura / e9b densidad / e9 por HU | ESTABLE | Evidencia complementaria; e9 = Invalidado | CONSERVAR r1 y r3; RESUMIR r2 y e9b; e9 → CONSOLIDAR en una frase |
| E9 | O2: e12 controles SAP + e13 muestreo/SAP + e13b + e15 | ESTABLE | Contribución principal | CONSERVAR |
| E10 | Registro 2026-10-15/16 (envolvente-canal, techo platillo, Fisher, etc.) | ESTABLE (post hoc) | Evidencia complementaria | RESUMIR / TRASLADAR A ANEXOS |
| E11 | O3 base: conjunto de entrenamiento, run04, calibraciones en validación, cotejo | ESTABLE (base de run04) | Baseline indispensable | CONSERVAR el núcleo; TRASLADAR A ANEXOS calibraciones |
| E12 | O3 base: brazo físico Peters (sonda, a19, material a21) | ESTABLE | Baseline indispensable | CONSERVAR |
| E13 | O3 base: E-A2 en prueba v1 + variantes + paramétrico + piso de ruido + acuerdo | ESTABLE | Contribución principal (resultado no concluyente) | CONSERVAR (primario y paramétrico); RESUMIR (variantes); TRASLADAR A ANEXOS (acuerdo) |
| E14 | O3 base: E-A1 reconstrucción de implantes reales | ESTABLE | Evidencia complementaria | RESUMIR |
| E15 | O3 diagnóstico: D1/D2/D4/a28/a29 | ESTABLE | Evidencia complementaria | CONSERVAR D1/D2/a29 (motivan v2); TRASLADAR A ANEXOS D4 y a28 |
| S1 | Modelos y diseños sustituidos (run01-03, mejor_37k, pose espejada, SD latente + ControlNet) | Sustituido | Modelo sustituido / Invalidado | OMITIR DEL MANUSCRITO los modelos; CONSERVAR la mención del rediseño |
| A1 | v2: run05a / run05b + piloto B + elección + prueba exploratoria | ACTIVO/dependiente | Exploración metodológica | POSPONER DECISIÓN |
| A2 | Barrido pasos:eta, etapa 0 v3, prueba de 100:0.3 | ACTIVO | Exploración metodológica / Pendiente | POSPONER DECISIÓN |
| A3 | C4: métrica angular η²_exc (v1 invalidada, v2) | ACTIVO | Exploración metodológica | POSPONER DECISIÓN |
| A4 | B-mínima angular (control λ=0, B1000, B300) | ACTIVO | Ablación relevante / Pendiente | POSPONER DECISIÓN |
| A5 | Criterio visual (c) + borde_estatica + textura_metricas | ACTIVO | Exploración metodológica | POSPONER DECISIÓN |
| A6 | Pipeline T/P/A (textura / perceptual / adversarial) | ACTIVO, sin resultados en snapshot | Pendiente | POSPONER DECISIÓN |
| P1 | Diseñados y no ejecutados (realismo, QC visual, ciego de 3 modelos, poses en síntesis, semimáximo, 2.º corredor) | Pendiente declarado | Pendiente | CONSERVAR como TF; OMITIR de métodos lo no ejecutado salvo el diseño ya declarado (ver ficha) |

---

## 2. Fichas — material ESTABLE

### E1. Datos y auditoría de cohorte
- **Objetivo (inferido):** inventariar CTPelvic1K local (178 volúmenes), clasificar metal/objetos, agrupar por paciente y definir particiones sin fuga.
- **Método:** `exploration-3d/explorar.py`, `grupos.py`, `grupo_paciente.py`, `duplicados_parciales.py`, `exclusiones.py`, `sensibilidad_hu.py`, `procedencia.py`, `correcciones_autora.py`. Cribado HU>2500; SHA256 de volumen y de cortes; revisión 3D de la autora; clasificación visual asistida por agentes (113 candidatos, "propuesta sin validar").
- **Resultados:** `docs/02-datos.md`. Vigente al 2026-10-11: 166 volúmenes en uso = 159 pacientes (125 train / 8 val / 33 test; test = 20 dataset6 + 13 CLINIC-metal). `exploration-3d/sensibilidad_hu.md`: candidatos 177 (1500 HU), 113 (2500 HU), 104 (3500 HU). `p1_particion.csv`, `grupos.csv`.
- **Validez:** sin ground truth de máscaras (Dice/HD95 no disponible, `02-datos.md`). Mapeo dataset6→CLINIC y dataset7→CLINIC-metal es **inferido**. Las auditorías de identidad no cubren pacientes sin metal. Una revisión de cortes solo consta para 56 pacientes de CLINIC-metal (C3:50). Dos fugas halladas después del entrenamiento (0053=0054; 0003=0072).
- **Objetivos:** transversal (O1-O3). **Dependencias:** todo lo demás depende de `p1_particion.csv`.
- **Uso en tesis:** C3:42-71 (sec:datos, 1435 palabras); C3:119-128; C4:43; I:78, 92-98. Sin tablas ni figuras propias.
- **Vigencia:** vigente. **Rol:** Baseline indispensable.
- **Tratamiento:** CONSERVAR el recuento vigente y la regla de aislamiento. Mover la historia de las auditorías a Anexos con una tabla-embudo (diagrama candidato) reduciría el cuerpo sin ocultar nada.

### E2. O1: e6a / e6c (codificación sin autoencoder)
- **Objetivo (inferido):** cota inferior del error de la codificación multiventana antes de introducir el VAE; elegir el techo de la ventana ancha.
- **Método / config:** `objetivo1/e6a_codificacion.py`, `e6c_techo_lw.py`. Decodificador oráculo (mejor canal por vóxel); ROI hueso HU>150, metal HU>2500; ventanas LW[-1000,2000], MW[-320,480], SW[-160,240]; profundidades float/16/12/8 bits; configs `pub`, `LW3000..LW20000`, `pub+MTW`, `pub+asinh`. e6c submuestrea a 1 000 000 vóxeles por ROI.
- **Resultados:** `e6a_codificacion.md`: oráculo `pub` float, mediana 0.95 HU; falla 25 HU en 50/178 volúmenes. `e6c_techo_lw.md`: `LW20000` y `pub+asinh` float 0.00 HU en hueso; 0/178 fallan. Metal: `pub` 3588.80 HU, `LW20000` 0.00 HU. e6c sirve de control de identidad para p1 (165/165).
- **Validez:** descriptivo; sin VAE, por tanto es una cota inferior ("un VAE real solo puede empeorarla").
- **Objetivos:** O1 (y la representación que adopta O3). **Dependencias:** ninguna aguas arriba; alimenta e6b, p1, run04 (`pub+asinh`).
- **Uso en tesis:** C3:77-85, 206 (representación); C4:41 (0.00 / 21.80 HU en 34 pacientes de prueba), C4:237 (discusión). La cifra de C4:41 viene de p1 (identidad) y no de e6a/e6c directamente.
- **Vigencia:** vigente; sustenta la elección de `pub+asinh` del sintetizador. **Rol:** Ablación relevante.
- **Tratamiento:** RESUMIR. El barrido de techo (tabla e6c) justifica `asinh` y `LW20000`, que son elecciones de diseño del sintetizador; va a Anexos como tabla.

### E3. O1: e6b (VAE SD1.5 preentrenado, 178 volúmenes)
- **Objetivo (inferido):** medir el ida y vuelta con el VAE real de SD1.5 antes de preinscribir la compuerta.
- **Método:** `objetivo1/e6b_vae_sd15.py/.sbatch`; `AutoencoderKL` de `stable-diffusion-v1-5` en float32, cortes axiales 2D, decodificadores `oráculo` y `regla`. Configs `pub`, `LW20000`, `pub+asinh` (`pub+MTW` no entra: 4 canales).
- **Resultados:** `outputs/e6b_vae_sd15.md`: MAE hueso mediana, `vae regla` 152.05 / 212.00 / 162.95 HU (pub / LW20000 / pub+asinh); 178/178 volúmenes fallan en las tres.
- **Validez:** el propio script dice "no decide nada". **Exploración sobre los 178 volúmenes, incluidos los de la futura partición de prueba**; la regla de p1 se fijó después de conocer este resultado desfavorable (la tesis lo declara: C3:74, C3:574).
- **Objetivos:** O1. **Dependencias:** e6c (control `identidad oraculo`). Insumo de p1.
- **Uso en tesis:** solo textual: C3:74 y amenazas (C3:574); sin tabla. Las cifras de C4 salen de p1.
- **Vigencia:** vigente como antecedente. **Rol:** Exploración metodológica.
- **Tratamiento:** RESUMIR (una frase ya presente). No ocultar que la regla se fijó después de ver este resultado.

### E4. O1: p1, compuerta Go/No-Go
- **Objetivo (inferido):** decidir de forma preinscrita si el autoencoder de SD1.5 (preentrenado o con decodificador afinado y encoder congelado) conserva el HU del hueso con MAE < 25 HU; si no, O3 se rediseña.
- **Método / config:** `p1_decodificador_sd15.py`, `p1_entrenar.sbatch`, `p1_evaluar.sbatch`. 2 modelos × 3 configuraciones = 6 combinaciones. Afinado de `post_quant_conv` + `decoder`, 30 000 pasos, L1, lr 1e-4, lote 4; el último estado se usa (la validación no elige). Partición por paciente estratificada (`p1_particion.csv`). Regla: Go si alguna combinación tiene media por paciente < 25 HU, comparación múltiple sin corregir. Controles: 3/3, 3/3, 165/165, 330/330.
- **Resultados:** `p1_compuerta.md`: **NO-GO**. Mejor combinación = afinado `pub+asinh`, media 61.72 HU, IC95 [55.12, 68.99], 34/34 pacientes ≥25 HU. Peor = sd15 `LW20000`, 209.39 HU. Sensibilidades: `p1_sin_0053.md` (n=33, mejor 60.95, IC [54.28, 68.19]) y `p1_sin_0072.md` (n=32, 61.08, IC [54.23, 68.57]); veredicto sin cambio. Todas copiadas en C4 tab:res-compuerta.
- **Validez:** n=34 de prueba (21 con metal en la columna Bδ). Fuga: el afinado se entrenó con `0054`/`0003`, pacientes de test `0053`/`0072`; solo podía favorecer un aprobado, y aun así no pasa. Multiplicidad sin corregir (también solo favorece al Go). Regla escrita tras ver e6b.
- **Objetivos:** O1; fundamenta el cambio de dominio de O3. **Dependencias:** e6b, e6c, `p1_particion.csv`, E1.
- **Uso en tesis:** I:37, 46-48; C3:72-94 (diseño); C4:12-45 (tab:res-compuerta C4:18-33); C4:234-239; CO. Línea Bδ de la tabla viene de las columnas descriptivas de `p1_compuerta.md`.
- **Vigencia:** vigente. **Rol:** Contribución principal (resultado negativo propio, declarado como tal).
- **Tratamiento:** CONSERVAR. Es el motivo del rediseño y la tesis lo reporta con honestidad.

### E5. O1: extensión al autoencoder de MAISI (cota por saturación)
- **Objetivo (inferido):** probar un autoencoder entrenado con TC sin correr el modelo, vía la cota de saturación al rango de salida.
- **Método:** inspección del código del bundle `maisi_ct_generative` (`scripts/sample.py`, rango −1000 a 1000 HU) y saturación de los 34 volúmenes de prueba.
- **Resultados en el snapshot:** **ninguno.** `diseno_A.md:481` solo anota "paso 0 de MAISI" como tarea. No hay script, CSV ni `.md` con 42.24 / 18.24 / [6.96, 231.43] / 11 de 34 (cifras de C4:45).
- **Validez:** NO DETERMINABLE CON EL SNAPSHOT. Es una cota determinista sin modelo, por lo que el riesgo estadístico es bajo; el riesgo es de trazabilidad.
- **Uso en tesis:** C3:93; C4:45; C4:237; I:46; CO.
- **Vigencia:** vigente en el texto. **Rol:** Evidencia complementaria.
- **Tratamiento:** CONSERVAR condicionado a incorporar el script y la salida en el repo (regla G-T4: toda cifra rastreable).

### E6. O2: e8 / e11 (censo morfológico y perfil axial del metal)
- **Objetivo (inferido):** caracterizar el metal real (clase morfológica, diámetros) para fijar la geometría paramétrica del implante y estimar candidatos a tornillo transsacro.
- **Método:** `objetivo2/e8_censo_implantes.py`, `e11_perfil_axial.py`. Filtro geométrico (HU>2500, eje ≥30 mm, anchos ≤12 mm); diámetro local = 2×p95 de distancia al eje en tramos de 2 mm.
- **Resultados:** e8: 17 de 65 volúmenes de evaluación con ≥1 candidato a tornillo iliosacro/transsacro; `d_ext_2500` mediana 4.97 mm, `d_ext_semimax` 5.08 mm. e11: 79 componentes esbeltos en 43 casos (la mediana de 4.91 mm se cita en C3:140).
- **Validez:** el filtro es geométrico, **no identifica el tipo de implante** (lo dice e11). La mediana de 4.91 mm sale de un filtro sin validación clínica.
- **Objetivos:** O2 (viabilidad) y O3 (máscara M). **Dependencias:** E1.
- **Uso en tesis:** C3:129-156 (tab:geometrias, C3:137); C3:119-128 (17 candidatos); C3:240.
- **Vigencia:** vigente. **Rol:** Evidencia complementaria (fija un parámetro).
- **Tratamiento:** RESUMIR; la cifra 4.91 mm va en el cuerpo con su filtro declarado.

### E7. O2: TotalSegmentator QC + e9ts (+3 mm, revisión de láminas) + e14
- **Objetivo (inferido):** medir el corredor óseo transsacro sobre máscaras anatómicas en vez de HU; elegir el recorte de TotalSegmentator.
- **Método:** `ts_*.py/.sbatch` (TotalSegmentator 2.18.0, `total`, 2 recortes ×179 volúmenes), `e9ts_corredor.py` (rejilla 3 mm, 81 direcciones, tramo óseo continuo, envolvente = cierre de 2 mm sin relleno), `e9ts_3mm.sbatch`, `e9ts_repetibilidad.py`, revisión de láminas, `e14_relleno_envolvente.py`.
- **Resultados:** `outputs/e9ts/e9ts_resumen.md`, cohorte O2 (72): D mediana 9.5 mm (p25 7.4, p75 11.7), 65.3 % cumple d6.5/c1, 23.6 % cumple d8.0/c2; con 3 mm: 62.5 % y 20.8 %. Revisión de láminas de 16 casos: la tesis reporta 14 conformes y 2 fallan con ambos recortes (C3:117); no recontado aquí (`e9ts_revision_laminas_autora.csv`).
- **Validez:** revisión por la autora con apoyo de un médico sin especialidad (revisores no independientes; `e9ts_revision_laminas.md`). La etiqueta S1 no tiene exactitud publicada. Las dos fallas son errores de segmentación que se mantienen en la cohorte preinscrita (C3:117). e14: el relleno no cambia D en ninguno de los 72 (C3:107; script y salida en snapshot: `outputs/e14_relleno.csv`, no recontado).
- **Objetivos:** O2. **Dependencias:** E1 (cohorte), r1 (nivel S1). Alimenta e12/e13.
- **Uso en tesis:** C3:99-118; C4:240-247; I:78, 94-98.
- **Vigencia:** vigente. **Rol:** Baseline indispensable de O2.
- **Tratamiento:** CONSERVAR el protocolo y la cifra principal; RESUMIR la sensibilidad de 3 mm y la revisión de láminas (el detalle puede ir a Anexos).

### E8. O2: r1 / r2 / r3, e9b, e9
- **r1 (`r1_landmarks.py`, `r1_auditoria_s1.md`, revisión de láminas):** legibilidad de los landmarks de Kaiser bajo artefacto. Resultado en tesis: 57 de 64 con 5 referencias localizadas; marco computable con S1 correcto en 48; libre de contaminación en 29 (C3:123). Validez: **revisor clínico sin especialidad, luego segunda lectura de la autora (61/61); el segundo lector no es independiente** (C3:127). Las auditorías de agente (Claude) están rotuladas "no es validación de la autora". CONSERVAR (promesa explícita del diseño, responde la brecha del marco de Kaiser).
- **r2 (`r2_nivel_pico_*`):** nivel del segundo corredor, 18 casos, lectura ciega de la autora (S2 en 13, S3 en 4, S4 en 1; C3:196). n pequeño, lectora única. RESUMIR (justifica nombrar "segundo corredor bajo S1" y su exclusión).
- **r3 (`r3_fractura_*`):** cribado ciego de fractura, 30 casos (15 estrechos + 15 control). Resultado en tesis: 20/30 con fractura confirmada, 10/15 y 10/15 (C3:66). Validez: un médico recién egresado, sin especialidad; 12 casos se abrieron en el volumen por sospecha (C3:68). **Resultado que debilita la lectura "variación anatómica"** de los corredores estrechos. CONSERVAR (amenaza central de O2).
- **e9b (`e9b_densidad_s1.*`):** densidad del esponjoso de S1; sondeo que motivó abandonar HU>150 y usar TotalSegmentator. RESUMIR.
- **e9 (`e9_corredor.py`):** cabecera del propio script: "ESTADO: NO VÁLIDO. NO CITAR SUS CIFRAS". Corredores de 1.6–7.8 mm donde hay tornillos de ~7 mm. **Invalidado**, pero su contribución fue justificar la segmentación anatómica; esa contribución ya figura en C3:103 (fracción ≤150 HU 0.42, proveniente de `e13_sap.md`, C3:103).
- **Tratamiento e9:** CONSOLIDAR en una frase (no ocultar que existió y falló); no citar cifras.
- **Uso en tesis:** C3:54-68, 119-128, 196; I:78, 96.

### E9. O2: e12 (controles de SAP), e13 (muestreo + SAP), e13b, e15
- **Objetivo (inferido):** distribución de grados de brecha cortical de poses perturbadas vs. referencia clínica (Zwingmann); resultado propio del Objetivo 2.
- **Método:** `e12_sap_control.py` (6 controles: fantoma, identidad, monotonía, discriminación, coincidencia de tramos), `e13_muestreo_sap.py/.sbatch`, `e13b_estratificado.py`, `e15_w1_sensibilidad.py`; preinscripción `preinscripcion_muestreador.md` (congelada 2026-09-22 antes de calcular W1). σ_t = 2.5 mm, σ_a por caso (2.07° con L=138 mm), truncamiento 3σ, 50 poses/caso, semilla 20260922 por caso; calibre de medición 7.0 mm (sensibilidad 4.91/7.3).
- **Resultados:** `e13_sap.md` (72 casos, 3 600 poses): G0/1/2/3 = 51.5/31.4/11.1/6.0 %, W1 0.206 (navegada), 0.230 (convencional); calibre 4.91: 0.138/0.533; 7.3: 0.247/0.174. `e13_sap_g3.md` (49): 54.9/30.4/9.9/4.8 %, 0.186/0.299. `e13b_estratificado.md` (post hoc): corredor ≥7.0 mm (57): G0 64.2 %, W1 0.183/0.482; <7.0 mm (15): G0 3.3 %, W1 1.122/0.727. `e15_w1_sensibilidad.md`: IC95 por remuestreo de pacientes [0.152, 0.313] y [0.089, 0.364]; sin CLINIC_0022/0024: 0.203/0.237. Referencia entre series: 0.395.
- **Validez:** preinscrito el muestreador y la métrica; **sin regla de decisión; la escala de lectura (0.395) se eligió después de ver las distancias** (C4:62, 244). Referencias de 26 y 35 tornillos (no pacientes independientes), tratadas como fijas. Referencia de pelvis fracturadas vs. cohorte receptora sin osteosíntesis y con 67 % de fractura (r3). Envolvente puede ocupar el hueco medial de S1 en 14 de 71. **Trazabilidad:** `e13_sap.md` conserva un control "56 de 72 pasan" **mal etiquetado** (corregido a mano en el encabezado, #122); la salida regenerada con el control correcto (`D_TS_max`) no está en el snapshot, aunque el código sí (ver Dudas).
- **Objetivos:** O2 y O4 (SAP). **Dependencias:** E1, E7, E8 (cohorte 72/49), e11 (longitud).
- **Uso en tesis:** C3:95-201, 339-366 (tab:preinscripcion C3:174, eq. brecha C3:346, eq. W1 C3:357); C4:47-89 (tab:res-sap, C4:55); C4:240-247; CO.
- **Vigencia:** vigente. **Rol:** Contribución principal de O2 (más O4).
- **Tratamiento:** CONSERVAR, incluyendo el resultado negativo anatómico (15 corredores estrechos). e13b se mantiene rotulado post hoc.

### E10. Registro de cálculos baratos (2026-10-15/16)
- **Contenido:** `registro/r_envolvente_canal.*` (job 57118, 72 casos, reproduce 71/72), `r_techo_platillo.py` (mediana 6.5 mm, RIC [5.7, 7.2], 72/72), `r_fisher_amenazas.py`, `r_integridad_ea2.py`, `r_rango_ea1.py`, `r_razon_banda_run04.py` (razón 0.638), `r_seccion_convexa.py` (relacionado con T, ver A1). Propósito: cerrar `\GAPDATO` de la tesis.
- **Resultados clave:** cierre ocupa el hueco medial de S1 en 14 de 71 casos, extensión máxima 6.4 mm; hueco medial en B con mediana de HU −11.
- **Validez:** descriptivo y posterior, con controles de regresión. `CLINIC_0044` no reproduce (134.0 vs 135.0 mm). El script no mide forámenes ni el efecto sobre la brecha.
- **Uso en tesis:** C3:~574-640 (amenazas, discontinuo), C3:64-66; C4:258-266; CO.
- **Rol:** Evidencia complementaria. **Tratamiento:** RESUMIR en el cuerpo; el detalle de `r_envolvente_canal` a Anexos. (r_seccion_convexa y r_integridad/rango_ea pertenecen a A1/E13/E14.)

### E11. O3 base: entrenamiento de run04 y selección de checkpoint (base de run04)
- **Objetivo (inferido):** entrenar un inpainting 2.5D en espacio de imagen (O3) y elegir checkpoint/parámetros solo con validación.
- **Método:** `a1_parches.py`, `a1b_parches_componente.py`, `a3_laminas_componentes.py`/`a3_revision_componentes.*` (40 componentes revisados por la autora: 5 tornillos), `a5_criterio_inclusion.py` (R1-R3; R4 no filtra), `a7_run04.sbatch`, `a9_suelo_representacion.py`, `a12_roi_parametros.py`, `a13_comparar_ckpt.py`, `a14_curvas.py`, `a16_calibrar_delta.py`, `a17_cotejo.py`, `a22_hu_copiapega.py`. U-Net 64 ch (27 979 587 parámetros), v-prediction, coseno 1000, AdamW lr 1e-4, lote 16, parches 256, DDIM 50, 5 semillas, representación `pub+asinh`; 60 000 pasos, `mejor.pt` en el paso 16 500; entrenamiento 14 182 parches / 39 casos; validación 896 / 3 casos (0101, 0102 como receptores). Manifiesto run04 = sin 7 secundarios (#163), sin `0003` (#166), sin 3 componentes no ortopédicos.
- **Resultados:** cotejo 1 mm: `run04_mejor` 13/24 cáscaras dentro del intervalo real frente a 7 de `run04_60k` (`resultados_validacion_pose.md`); p95 sintético bajo lo real en 7/12 cáscaras. Δ = 196.3 HU (`run04_mejor`), 115.8 (`run04_60k`). Copy-paste 5371 HU. `delta` de lectura 0.030 (calibrado en validación). Regla del suelo de −1000 HU **no aplicada**: 225.0 HU con p95 vs 1.2 HU con mediana, frente a Δ=196.3 (C3:208).
- **Validez:** **el modelo se entrenó antes de congelar el diseño; lo congelado es la evaluación** (`diseno_A.md:24`; los `run05a_meta.json`/`run05b_meta.json` de v2 declaran `"preinscrito": false`; para run04 el snapshot solo trae `curva.csv` y el log, sin meta). Cotejo y calibración con 2 receptores de validación y **un solo paciente real con tornillos aislados (`metal_0039`, 2 tornillos)**: "descarta, no prueba" (C3:254). Δ con 2 pacientes. Solo 39 casos de entrenamiento; 19 de 39 con composición no ortopédica o de otro tipo (C3:620, no recontado). El 60k sale mejor dentro de M (distancia 497 vs 648 HU), no elegido por regla. Una pose espejada se corrigió después de ver generaciones con test (C3:236).
- **Objetivos:** O3. **Dependencias:** E1 (partición), E2 (representación), a5 (criterio), a3 (revisión de la autora); pose correcta #173.
- **Uso en tesis:** C3:202-264 (cotejo C3:246-256); C4:248-257. Sin tablas propias.
- **Vigencia:** vigente (base de run04). **Rol:** Baseline indispensable del sintetizador evaluado.
- **Tratamiento:** CONSERVAR el modelo, la regla del cotejo y sus límites; TRASLADAR A ANEXOS a9/a12/a16/a22 (calibraciones en validación) y a13/a14 (curvas).

### E12. O3 base: brazo físico (Peters/XCIST)
- **Objetivo (inferido):** construir el comparador físico del contraste primario.
- **Método:** `peters/run.py`, `sonda_peters.md` (protocolo de viabilidad preinscrito 2026-10-09), `a18_sonda_peters.py`, `a19_peters_completo.py`, `a19_pose.sbatch`, `a21_cotejo_material.py`. XCIST (revisiones `4cf3544` y `4993e87`), 2D, 900 columnas, 1000 vistas; uno de cada dos cortes; 2 réplicas A/B; materiales Fe y Ti.
- **Resultados:** `resultados_validacion_pose.md` §2: Ti 2/24 cáscaras dentro (M p50 4462), Fe 0/24 (M p50 7036); real M p50 3838/3092. Ganó Ti por regla; "ningún material reproduce lo real". Viable con submuestreo (segunda corrida).
- **Validez:** protocolo reproducido, **no validado contra un fantoma físico**; Fe en lugar de acero (catálogo XCIST); fantoma tomado del repositorio y no del artículo (`diseno_A.md`); la sonda se corrió con la pose equivocada y no se repitió; réplicas con ruido sin semilla. El material se eligió con modelo afectado antes del reentrenamiento y se repitió con la pose corregida. Peters exagera el artefacto frente a lo real (22/24 cáscaras sobre el intervalo).
- **Objetivos:** O3 (comparador); O4 (métricas). **Dependencias:** a11 (rasterización del tornillo), pose corregida, E11.
- **Uso en tesis:** C3:442-489 (tab:desviaciones C3:460); C4:92-133; I:68-72.
- **Vigencia:** vigente. **Rol:** Baseline indispensable. **Tratamiento:** CONSERVAR; es la referencia del contraste primario y sus limitaciones ya se declaran.

### E13. O3 base: E-A2 en prueba (v1) y análisis añadidos
- **Objetivo (inferido):** contraste primario de equivalencia (TOST pareado) de la *streak amplitude* del sintetizador frente a Peters-Ti en 13 pacientes de prueba sin metal; control de cordura frente a copy-paste.
- **Método:** `a15_cadena_pose.sbatch` (final), `a20_evaluador_ea2.py`, `a24_contrastes.py`, `a26_lecturas.py`, `a20_v1_variantes.sh`, `a27_preservacion_peters.py`, `a29_perfil.py`, `a25_html_sintesis.py`. Pose = eje del corredor sin perturbar. Δ = 196.3 HU (medido en 2 pacientes de validación). 5 semillas; Peters 2 réplicas.
- **Resultados** (`resultados_prueba_v1.md`, `resultados_dec_2026-10-15.md`): primario −301.0 HU, IC90 [−477.0, −124.9], p_TOST 0.845: **no concluyente, difusor < Peters**; margen mínimo 477.0 HU. Hierro −3814.2; sin corredores angostos (n=10) −261.1. `run04_60k`, Δ 115.8: −384.0 [−566.5, −201.4] no equivalencia. Wilcoxon p=0.000122 (=2^-13, degenerado). Variantes: inter −295.3, suelo simétrico −238.3, sin cabeza −329.3, anillos 8-10 y 10-12 mm +478.0 y +411.7 (no equivalencia, mayor). Paramétrico: −98.9 [−287.3, +89.4], con suelo simétrico −36.3. Piso de ruido: difusor 893 HU (0.69 de la amplitud con metal) vs Peters 184 HU (0.12). Acuerdo: CV 0.076 vs 0.241; Pearson 0.40; Bland-Altman sesgo −301.0 HU, límites [−999.0, +397.1]; en razón 0.831 [0.533, 1.296]. Perfil por anillos: razón 0-2/6-8 de 1.92 (difusor) vs 6.71 (Peters Ti), 3.16 (paramétrico).
- **Validez:** n=13; **la partición de prueba ya se había visto con un modelo afectado y con la pose espejada**; casi todas las lecturas del 15 de octubre son **posteriores** para v1 (`visto.md`). Δ de 2 pacientes; tres elecciones (checkpoint, material, margen) hechas sobre los mismos 2 receptores y las tres empujan hacia la equivalencia (C3:596-598). Asimetrías de cortes, suelo y piso de ruido (favorecen al sintetizador en el piso). Tres corredores más angostos que el tornillo entran. Desenlace honesto: **no concluyente**; hay una lectura de dos niveles fijada después de ver la prueba de ambas versiones.
- **Objetivos:** O3 (confirmatorio parcial). **Dependencias:** E11, E12, pose #173, Δ de E11.
- **Uso en tesis:** C3:412-525; C4:90-195 (tab:res-tost C4:100, tab:res-anillos C4:148, tab:res-integridad C4:182); I:50-56; CO.
- **Vigencia:** vigente (resultado final de v1). **Rol:** Contribución principal (resultado no concluyente) con baseline paramétrico muy informativo.
- **Tratamiento:** CONSERVAR el primario, el control de cordura y el paramétrico (muestra que el aprendizaje no aporta sobre un modelo analítico). RESUMIR las 8 variantes (una tabla compacta). TRASLADAR A ANEXOS Bland-Altman, Pitman-Morgan y la escala log. No omitir el hecho de que el piso de ruido favorece al sintetizador.

### E14. O3 base: E-A1 reconstrucción de implantes reales
- **Objetivo (inferido):** medir descriptivamente cuánto reconstruye el sintetizador el implante real (comparado con la TC real).
- **Método:** `a23_ea1.py`, `a23_final_run04.sbatch`; `run04_mejor`, límite de lectura 0.030, componentes ≥500 mm³, hasta 24 cortes por componente, 5 semillas.
- **Resultados** (`resultados_prueba_v1.md`, 3840 parches): material ortopédico (n=9) MAE en G 270.9 HU, M 2312.5, Bδ 198.0; hueso Dice 0.717, metal Dice 0.928; costura descontada 6.3 HU. No ortopédicos (n=4): G 199.8, metal Dice 0.753, costura 9.0.
- **Validez:** descriptivo, sin umbral; n=13 (9+4); la discrepancia en M se mide contra una TC cuya reconstrucción es desconocida; corrió en una porción de GPU compartida; diseño original 19 pacientes (11+8), finales 13 (ver Dudas).
- **Uso en tesis:** C3:426-433; C4:196-222 (tab:res-ea1 C4:204); I:41.
- **Rol:** Evidencia complementaria. **Tratamiento:** RESUMIR (una tabla); el rango entre pacientes viene de `r_rango_ea1.py`.

### E15. O3 diagnóstico: D1/D2/D4/a28/a29
- **Objetivo (inferido):** medir el alcance real del artefacto alrededor de piezas del tamaño de un tornillo y compararlo con el sintético para decidir v2.
- **Resultados:** `d1_d2_resultado.md`: exceso real mediano por anillo 1930/1199/765/473/174 HU (0-2…8-10 mm; 18 pacientes de entrenamiento y validación, 500–4000 mm³); el alcance llega a 10 mm. Sintético `run04_mejor` 1697/488/97/−65/−40. D4: semimáximo −0.24 mm (32 componentes, 23 pacientes). a28: p95 con solo LW entra en la envolvente en 1 de 7 cáscaras: "modelo", no lectura.
- **Validez:** referencia real aproximada (otro corte); 2 pacientes sintéticos de validación; piezas de volumen fijado por tamaño, no por tipo. Hecho después de ver la prueba de v1 (motivó v2).
- **Uso en tesis:** C3:272-276; C4:134-195 (tab:res-anillos C4:148); TF.
- **Rol:** Evidencia complementaria. **Tratamiento:** CONSERVAR D1/D2/a29 (soportan el diagnóstico central del defecto); TRASLADAR A ANEXOS D4 y a28.

### S1. Modelos y diseños sustituidos o invalidados
- `run01`-`run03`, `mejor_37k` (run02): entrenados con `metal_0003`, mismo paciente que `0072` (test); "versión con fuga" (`diseno_A.md:~20-24`, enmienda run04); archivados en `obsoletos/` (**fuera del snapshot**). Pose espejada (#173): cotejo, Δ y corrida final rehechos; los `.md` anteriores fueron sustituidos por `resultados_validacion_pose.md`. Diseño original SD1.5 latente + ControlNet: sustituido tras el No-Go de p1.
- **Rol:** Modelo sustituido / Invalidado. **Tratamiento:** OMITIR DEL MANUSCRITO las cifras de esos modelos (la tesis ya declara que ninguna cifra viene de un modelo afectado, C3:236); CONSERVAR (como está) el relato de por qué hubo reentrenamiento, porque afecta a la validez (amenazas). Contribución evaluada: su única función es de procedencia y justifica el control de pose y el reentrenamiento.

---

## 3. Fichas — material ACTIVO / dependiente (POSPONER DECISIÓN)

### A1. v2: run05a, run05b, piloto B, regla de elección, prueba exploratoria
- **Objetivo (inferido):** corregir la atenuación del artefacto desde ~4 mm (D1 vs D2). D: sobremuestreo de componentes de 500–4000 mm³ (FRAC 0.5, factor 3.91) + peso 3 en anillo 2–10 mm. B: canal T analítico de endurecimiento del haz (`b_piloto_plantilla.py`, `v2_b_cache_T.py`).
- **Resultados:** piloto B: e=0.116, p=0.0085 (13 pacientes), pasa C0/C1/C2 (`b_piloto/b_resumen.md`). Elección (`run05/v2_eleccion.md`): E = 532.8 (run04), 418.2 (run05a), 367.0 (run05b); desviación 0-2 mm 233.0, 284.0, 540.0; tope 279.6 → **"no mejora", sin corrida final con v2**. Prueba exploratoria (`resultados_dec_2026-10-15.md`): run05a −258.9 [−456.7, −61.1], run05b −264.3 [−456.8, −71.7], mismo desenlace no concluyente; Pearson con Ti 0.03 y 0.09 (v1 0.40). E-A1 v2: la ventaja de run05a desaparece con 0.03.
- **Validez:** 2 pacientes de validación; v2 se decidió **después de ver la prueba de v1**; evaluación en prueba posterior y exploratoria; reutiliza la partición; entrenada en GPU distinta. La compuerta de B se probó con residuo que incluye anatomía; r_seccion_convexa: en secciones compactas la ganancia neta es 0.012 (8 pacientes) vs 0.148 en alargadas (no establece que T sea nula). El script run05b en snapshot tiene semillas incompletas en C4 (0101 s0–2, 0102 s0).
- **Dependencias:** E11, E15, A3 (C4 usa run05a/b).
- **Uso en tesis:** C3:266-307; C4:224-229; I:56; tab:res-tost filas v2 (C4:~118-123).
- **Vigencia:** vigente pero superada en importancia por A2-A4 (la tesis posterior la trata como "no sustituye al modelo evaluado"). **Rol:** Exploración metodológica.
- **Tratamiento:** POSPONER DECISIÓN hasta cerrar A2-A6. Inclinación provisional, no vinculante: RESUMIR con los resultados negativos visibles (no mejora, desenlace igual, correlación por paciente cae a ~0) y TRASLADAR A ANEXOS el piloto de B. C3:266-334 mezcla v2 con A2-A5 (ver Dudas).

### A2. Barrido pasos:η (DDIM), etapa 0 v3, prueba de 100:0.3
- **Objetivo (inferido):** ver si el muestreo estocástico explica el déficit de amplitud a 4–12 mm sin reentrenar.
- **Método:** `a15_eta_sweep.sbatch`, `a15_val_ckpt.sbatch`, `veredicto_cascaras.py`, `a15_final_eta.sbatch`, `a20_eta_test.sbatch`; variantes 50:0, 50:0.3, 50:0.6, 100:0.3, 200:0 sobre `run04_mejor`.
- **Resultados:** `eta_veredicto_resultado.md`: **control NO REPRODUCE** (|Δp95| máx 48.63 HU, tolerancia 1.00): "el barrido no se interpreta". Aun así, cáscaras críticas dentro (de 7): 50:0 → 1; 50:0.3 → 4; 100:0.3 → 5; 200:0 → 1; 50:0.6 → 3. D2: 100:0.3 y 50:0.3 suben el perfil 2–10 mm. C4 (η² residuo K=48): 0.312 y 0.308 vs 0.274 y Peters 0.476 (`c4_eta_resultado.md`; C3 tab:c4-eta).
- **Validez:** 2 pacientes de validación; un checkpoint; **control de validez fallido**, sustituido post hoc por la comparación con el diagnóstico de octubre (C3:313-315, la tesis lo dice); variante 100:0.3 elegida en validación sobre los mismos receptores; evaluación en prueba **no ejecutada o no leída** (`\GAPDATO` en C3:333; no hay salida en el snapshot).
- **Uso en tesis:** C3:309-317, 333; tab:c4-eta (C3:397); C3:391.
- **Rol:** Exploración metodológica / Pendiente. **Tratamiento:** POSPONER DECISIÓN hasta tener la prueba. Si se reporta, hay que explicitar que el control de validez falló.

### A3. C4: métrica angular η²_exc
- **Objetivo (inferido):** cuantificar la observación de la autora (real = patrón direccional; sintético = halo liso); las métricas radiales no ven ángulos.
- **Método:** `c4_anisotropia.py` (validación 0101/0102 + real `metal_0039`), `c4b_prueba.py` (13 de prueba); anillos 1 mm por distancia a M (2–10 mm), K sectores, corrección por azar; modos crudo y residuo; protocolo `c4_protocolo.md` declarado antes de calcular.
- **Resultados:** prueba (13), residuo K=24: run04−Peters +0.039 [−0.046, 0.082]; K=12 +0.124 [0.060, 0.152]; K=48 −0.178 [−0.206, −0.134]. **El signo cambia con la escala.** Validación K=48 residuo: run04 0.274, run05a 0.328, run05b 0.264, Peters 0.476.
- **Validez:** **la versión 1 se invalidó**: control sin metal 0.49, halo liso con M elíptico 0.805 (mide la forma de M); v2 se eligió después de ver ese fallo. El ruido baja η² (ruido de 150 HU sobre un halo: 0.008; con rayas: 0.240). η² no distingue rayas de bordes anatómicos radiales. Referencia real: 2 tornillos de un paciente (otro escáner). `c4_resumen_v1_centroide.md` citado pero no está en el snapshot. run05a/b no tienen volúmenes de prueba locales. Post hoc, descriptivo, sin p-values.
- **Uso en tesis:** C3:377-410; amenazas C3:616; C3:410 (figura pendiente `\GAPDATO`).
- **Rol:** Exploración metodológica. **Tratamiento:** POSPONER DECISIÓN (depende de A2-A4). Las dos versiones de la métrica deben quedar documentadas por transparencia.

### A4. B-mínima angular
- **Objetivo (inferido):** probar si un término de amplitud angular en el ajuste fino sube η² (K=48).
- **Método:** `a7_b_minima.sbatch`; 3 000 pasos desde `run04_mejor`, lr 5e-5; control λ=0, B1000 (λ=0.8, t=1000), B300 (λ=3, t=300); T4.
- **Resultados** (`c4_bmin_resultado.md`): (i) η² K=48 residuo B1000−control = +0.038 (< 0.05): **B no mejora por la regla fijada**. (ii) cáscaras críticas 3 vs 0 (cumple); (iii) D2 0-2 mm: B 26 HU vs control 585 (cumple). E (2–10 mm): control 582.0, B 274.8. η² K=48 B1000 0.337 vs Peters 0.476.
- **Validez:** 2 pacientes de validación; un checkpoint; un λ; **hardware T4, no comparable con run04**; el control mismo degrada el artefacto (0-2 mm: 585 vs 233 HU). `b_veredicto_resultado.md` indica "Control NO evaluado; sin él el barrido no es interpretable"; si esta advertencia está reflejada en la tesis para B no queda determinado (NO VERIFICADO).
- **Uso en tesis:** C3:319-331; amenazas C3:604.
- **Rol:** Ablación relevante / Pendiente (criterio (c) visual). **Tratamiento:** POSPONER DECISIÓN. El resultado negativo según regla debe mantenerse visible.

### A5. Criterio visual (c), borde_estatica, textura_metricas
- **Objetivo (inferido):** evaluación visual ciega de credibilidad del artefacto (1–5) de 8 brazos × 6 paneles.
- **Resultados:** `c2b_respuestas_2026-11-21.csv` (48 filas, media 2.9583; **sin clave de brazos en el snapshot**: no se puede verificar la asignación por brazo). En C3:540: Peters-Ti 5.00; real 4.83; 50:0.3 3.33; B300 3.00; 100:0.3 2.33; control 2.17; B1000 1.67; modelo evaluado 1.33. `borde_estatica_resultado.md`: M<2500 HU en 18.2 % del modelo evaluado, 15.6 % en 100:0.3 y 50:0.3, 14.0 % en Peters, 40.2 % en el control. `textura_metricas.py` (sin salida en el snapshot).
- **Validez:** **evaluadora única (la autora) que conoce los modelos; ciego nominal**; criterio añadido tras ver datos; 6 paneles por brazo; P(X≥4 de 6)=0.34 por azar (cálculo en C3:536); lo real viene de otro paciente y otro escáner; anclas de la escala pendientes (`\GAPDEC`); marcado con `\REVVISUAL`, es decir, bajo revisión.
- **Uso en tesis:** C3:534-544.
- **Rol:** Exploración metodológica. **Tratamiento:** POSPONER DECISIÓN. Tal como está es descriptivo; no reportarlo como prueba de realismo. Nótese que el orden visual no coincide con el orden de las métricas numéricas.

### A6. Pipeline T/P/A (textura / perceptual / adversarial)
- **Objetivo (inferido):** ensayar pérdidas auxiliares `--aux-tex`, `--aux-per`, `--aux-adv` en el entrenamiento para reducir "estática" y "textura sobrepuesta" (hallazgos del criterio (c)).
- **Material:** `pipeline_textura.sbatch`, `pipeline_lambda.py` (λ = 0.1·L_v/L_término), `pipeline_reporte.py`, `textura_metricas.py`, `evalua_todo_local.sh`. Rama `exp/textura-percep-adv`. Brazos `aux_C`, `aux_T`, `aux_P`, `aux_A`.
- **Resultados en el snapshot:** ninguno (no hay `REPORTE.md`, `estado.tsv` ni `res/`). **NO DETERMINABLE CON EL SNAPSHOT.** La tesis no los menciona.
- **Rol:** Pendiente. **Tratamiento:** POSPONER DECISIÓN. Hasta tener resultados, no corresponde a ninguna sección.

### P1. Diseñados y no ejecutados
- Contraste de realismo (perfil radial + histograma en M contra tornillos aislados de prueba; sin script, la lista de pacientes no se formó), control de calidad visual, comparación ciega de los tres modelos, síntesis con poses del muestreador, modelo entrenado con máscara por semimáximo, muestreo del segundo corredor.
- **Uso en tesis:** C3:526-532, 305, 438; C4:260-261; TF:27 y siguientes; I:44, 56, 68.
- **Rol:** Pendiente. **Tratamiento:** CONSERVAR el diseño declarado como no ejecutado en TF, que ya los lista con honestidad. La regla de referencia de realismo (C3:530, amenazas C3:580) se escribió con 3 de 11 pacientes ya revisados: se declara pero no puede ser auditada. Evaluar si el detalle del diseño del realismo (C3:526-532) debe permanecer en Métodos o pasar a TF (POSPONER DECISIÓN en esta fase).

---

## 4. Dudas que requieren decisión de la autora

1. **Trazabilidad de MAISI (E5).** ¿Dónde están el script y la salida de las cifras 42.24 / 18.24 / [6.96, 231.43] / 11 de 34 (C4:45)? Sin ellas, la afirmación no es rastreable (G-T4).
2. **Control de identidad de SAP (E9).** C4:49 afirma que la pose sin perturbar da brecha nula con el diámetro del propio corredor en los 72. `e13_sap.md` y `e13_sap_g3.md` conservan el control mal etiquetado (56/72) con una corrección manual y declaran que el código se corrigió "para la próxima corrida". ¿Se regeneró la salida? Si es así, falta en el snapshot.
3. **Cohorte de E-A1.** El diseño y C3:428 hablan de 19 pacientes de prueba con metal; los resultados y C4:196 usan 13 (9+4). C3:67 dice 10 con objetos no ortopédicos, de los cuales E-A1 usa 4. ¿Qué excluye a los 6 restantes (umbral de 500 mm³, extracorpóreos)?
4. **Estructura C3/C4 para v2 y exploraciones de noviembre.** Los resultados de A2-A5 están en C3:309-334 y 534-544, el capítulo de métodos; C4:224-229 solo trae v1 vs v2. ¿Dónde irán cuando se decida?
5. **Control de validez de A2 y B (A2/A4).** η-sweep: el control no reproduce (48.63 HU) y se sustituyó después de ver el fallo. B: el control de validez falta según `b_veredicto_resultado.md`. ¿Se mantiene el barrido con esa salvedad, o se re-corre?
6. **Criterio visual (c).** La clave de brazos no está en el snapshot, y la evaluadora es única y no ciega de verdad. ¿Se agrega un segundo lector (idealmente clínico) antes de citar los puntajes? Decisión sobre las anclas de la escala (`\GAPDEC`).
7. **Estatus de T/P/A.** ¿Siguen en curso? Las decisiones que dependen de ellos (tratamiento de v2, A2-A5) quedan abiertas.
8. **Prueba de 100:0.3.** `a15_final_eta.sbatch` y `a20_eta_test.sbatch` existen pero no hay resultado; C3:333 mantiene `\GAPDATO`. ¿Se ejecutó?
9. **η² sobre los 13 de prueba (c4b).** Se calculó con la prueba ya vista. ¿Se mantiene con la etiqueta post hoc o se limita a validación?
10. **e9 y modelos sustituidos.** ¿Mención explícita de que e9 (por HU) fue invalidado, o solo la justificación de las máscaras anatómicas? Propuesta: una frase.
11. **Revisión de láminas (E7, E8).** Las cifras 14/16 y 61/61 vienen de la tesis y no se recontaron en esta fase; confirmar desde los CSV de la autora antes de la Fase 2.
12. **Documentos fuera del snapshot** (`01-decisiones.md`, `04-implicancias.md`, `obsoletos/`): varias lecturas solo se verifican contra ellos; decidir si entran en una fase posterior.
