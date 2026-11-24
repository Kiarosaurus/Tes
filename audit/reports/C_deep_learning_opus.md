# Informe C — Auditoría científica prospectiva (rol: Senior Deep Learning Researcher)

**Alcance revisado:** `thesis/secciones/introduccion.tex`, `capitulo3.tex` completo, `capitulo4.tex`, `code/src/renderizador/*.py`, `code/src/common/ventanas.py` y los resultados y scripts de `results/objetivo3/` y `results/objetivo1/` necesarios para verificar cifras. Trabajo en solo lectura. Las cifras marcadas como **cálculo propio** las derivé yo a partir de archivos del material que cito; no aparecen en la tesis.

**Leyenda de clasificación:** INDISPENSABLE (antes del cierre experimental) / RECOMENDABLE (si hay capacidad) / OPCIONAL / TRABAJO FUTURO. Ninguna recomendación pide entrenar ni cambiar configuraciones. Casi todas son análisis de inferencia o de CPU sobre salidas y checkpoints que ya existen, o correcciones de texto.

---

## 1. Resumen ejecutivo

1. El sintetizador **no ve el corte central fuera de $G$**, y en los cortes vecinos $G$ llega borrada. Toda la anatomía dentro de $G$ se genera sin ningún dato del receptor: un tubo de unos 29 mm de diámetro a lo largo de 138 mm. Esto explica, con mucha probabilidad, el piso de ruido de 893 HU y el perfil plano. Además invalida, dentro de $G$, las etiquetas óseas del receptor para cualquier uso como aumento de datos. El texto de la tesis no lo dice con claridad (C-01).
2. Las decisiones de validación (punto de control, material, $\Delta$, versión 2, barrido $\eta$, ajuste fino, criterio visual) descansan en **los mismos dos receptores**. Hay 30 pelvis viables de la partición de entrenamiento que el sintetizador nunca vio y que permitirían ampliar la validación solo con inferencia (C-04).
3. Ningún resultado muestra que el modelo aprendido supere a un baseline no aprendido. El artefacto paramétrico, que no usa aprendizaje, queda más cerca del protocolo físico (−98.9 frente a −301.0 HU), y la pregunta de investigación sigue nombrando como comparador a la copia y pegado, que es degenerada (C-08).
4. Los métodos post hoc en curso tienen defectos de implementación o de diseño que impiden leerlos:
   - la pérdida adversarial compara un *fake* sin componer con un *real* completo, lo que deja al discriminador un atajo;
   - el *perceptual proxy* es un L1 multiescala que favorece el suavizado;
   - el control de ajuste fino ya degrada el modelo;
   - el parámetro "$\eta_{\mathrm{DDIM}}$" no es el $\eta$ de Song et al.

   Ver C-02, C-05, C-06 y C-07.
5. La validación que eligió los candidatos a punto de control usó **256 de los 896 parches, todos de un solo paciente** (C-03).

---

## 2. Hallazgos

### C-01 — El modelo no recibe el corte central: la anatomía dentro de $G$ es alucinada
- **Ubicación:**
  - `code/src/renderizador/datos.py:107`, `:217-230`
  - `results/objetivo3/a15_cadena_completa.py:48`
  - `code/src/renderizador/difusion.py:95`
  - `thesis/secciones/capitulo3.tex:204`, `:214`
- **Evidencia:**
  - `a15_cadena_completa.py:48`: "**El corte central no entra en el condicionamiento.** El modelo solo ve a sus dos vecinos".
  - `datos.py:220`: `hu[v['g']] = -1000.0  # el contexto vecino tambien lleva G borrada`.
  - `difusion.py:95`: `xt = xt * g`.
  - Tesis, cap3:204: "El modelo recibe el parche con $G$ borrada".
- **Descripción:** La entrada consta de $x_t$ (anulado fuera de $G$), los cortes $k\pm1$ con $G$ borrada, $M$ y $G$. Dentro de $G$ la red no recibe ningún píxel del receptor, ni del corte central ni de los vecinos. Para un tornillo de 4.91 mm con banda de 12 mm, $G$ es un tubo de unos 28.9 mm de diámetro (**cálculo propio**: 4.91 + 2×12) a lo largo del corredor (mediana de 138 mm, cap3:182). Ese tubo atraviesa el sacro y las dos articulaciones sacroilíacas. La red tiene que inventar todo ese tramo de anatomía, y fuera de $G$ la composición pega el original.
- **Coherencia con lo medido:**
  - piso de ruido de 893 HU frente a 184 HU (cap4:140);
  - Sørensen-Dice del hueso de 0.677 frente a 0.800 del protocolo físico (cap4:188-189);
  - meseta de 946, 919 y 727 HU entre 6 y 12 mm, del orden del piso (cap4:157-159).
- **Severidad:** alta.
- **Confianza:** alta sobre el diseño (está en el código); media sobre su peso causal en el piso de ruido.
- **Impacto:**
  - El criterio primario mezcla el artefacto con el error de *inpainting* de la anatomía.
  - El texto de la tesis lleva a pensar que el corte central se recibe.
  - Para la motivación declarada (aumento de datos para la segmentación ósea), las máscaras óseas del receptor dejan de corresponder a la imagen dentro de $G$.
- **Acción:**
  - (a) INDISPENSABLE (texto): describir exactamente los 11 canales y declarar que la anatomía de $G$ se regenera sin observarla, con su consecuencia para las etiquetas.
  - (b) INDISPENSABLE (análisis, solo CPU): ver R-1.
- **Dependencias:** C-11, C-12.

### C-02 — "$\eta_{\mathrm{DDIM}}$" no es el $\eta$ de DDIM
- **Ubicación:** `code/src/renderizador/difusion.py:192-195`; `capitulo3.tex:214`, `:309-315`.
- **Evidencia:** `sigma = eta * sb_s`, es decir $\sigma = \eta\sqrt{1-\bar\alpha_{t-1}}$. La tesis cita a Song et al. para el muestreo.
- **Descripción:** En DDIM, $\sigma_t=\eta\sqrt{(1-\bar\alpha_{t-1})/(1-\bar\alpha_t)}\sqrt{1-\bar\alpha_t/\bar\alpha_{t-1}}$. Con el calendario coseno y los 50 pasos del código, la $\sigma$ implementada vale entre 1.0 y 2.9 veces la de DDIM para el mismo $\eta$, con mediana de 2.45 (**cálculo propio** con `betas_coseno`). La variante "100:0.3" inyecta así bastante más ruido que un $\eta=0.3$ estándar. El aumento del percentil 95 (de 1 a 4–5 cáscaras críticas, cap3:315) puede deberse a más varianza estocástica dentro de $G$ y no a más artefacto.
- **Severidad:** media. **Confianza:** alta (fórmula); media (interpretación).
- **Impacto:** la variante 100:0.3, que ya se evalúa en prueba (cap3:333, GAPDATO), puede "mejorar" la cola alta subiendo el piso de ruido.
- **Acción:** INDISPENSABLE si se reportará 100:0.3. Escribir la fórmula real y medir su piso de ruido ($G$ sin $M$) en los dos receptores (R-2).
- **Dependencias:** C-01, C-04.

### C-03 — La pérdida de validación se mide sobre un solo paciente
- **Ubicación:** `entrenar.py:146`, `:270-271`; `results/objetivo3/a7_run04.sbatch:65,70`; `a5_manifiesto_val.csv`; `capitulo3.tex:230`, `:242`, `:297`.
- **Evidencia:**
  - `--lote 16`, `--lotes-val 16` y `shuffle=False` sobre un índice ordenado por nombre.
  - El manifiesto tiene 896 filas: 538 de `metal_0011`, 226 de `metal_0056` y 132 de `metal_0039`. Las primeras 256 son todas de `metal_0011` (**cálculo propio**).
  - La tesis dice "validación de 896 parches de 3 casos".
- **Descripción:** El mínimo de validación en el paso 16 500 (candidato de la versión 1) y el del paso 21 000 (candidatos de la versión 2) se calcularon con parches de un único paciente. Según cap3:254, ese paciente lleva un fijador externo o placas. Sus parches no incluyen los tornillos aislados de `metal_0039`, que sí usa el cotejo. Leer el ascenso posterior de la pérdida como sobreajuste general (cap3:242) no está respaldado.
- **Severidad:** media. **Confianza:** alta.
- **Impacto:** los candidatos del cotejo y la regla de elección de la versión 2 heredan un criterio de un solo paciente.
- **Acción:**
  - INDISPENSABLE (texto): declararlo.
  - OPCIONAL: recalcular la pérdida sobre los 896 parches para los checkpoints guardados.
- **Dependencias:** ninguna.

### C-04 — Selección sobreajustada a los dos receptores de validación
- **Ubicación:** `capitulo3.tex:248`, `:256`, `:301`, `:315`, `:327`, `:504`, `:534`, `:596`; `results/objetivo3/outputs/obj3_pose/a20_val/a20_delta_run04_mejor.json`; `a20_test/a20_ea2_test.csv`.
- **Evidencia:**
  - `"s_por_caso": 0101 → 291.58, 0102 → 100.94`. De ahí sale $\Delta=196.3$ HU, la media de dos valores que difieren casi en un factor 3.
  - En prueba, el rango entre semillas de la *streak amplitude* del modelo evaluado tiene media de 284.7 HU y va de 160.9 a 398.4 HU entre los 13 pacientes (**cálculo propio**, descriptivo, sobre `a20_ea2_test.csv`).
- **Descripción:** Sobre 0101 y 0102 se fijaron al menos ocho decisiones:
  1. el punto de control;
  2. el material;
  3. $\Delta$;
  4. el límite de lectura (0.030);
  5. la elección de la versión 2;
  6. el barrido de $\eta$;
  7. los criterios del ajuste fino;
  8. el criterio visual (c).

  Con $n=2$, cualquier umbral (por ejemplo +0.05 de $\eta^2$, o "4 de 7 cáscaras") queda dentro de la variabilidad entre pacientes. El desenlace confirmatorio de la versión 1 **no cambia**: el límite inferior del IC, −477.0 HU, queda por debajo de −285 HU, así que con un margen del orden del rango observado en prueba la prueba seguiría siendo no concluyente.
- **Severidad:** alta (para las exploraciones post hoc); baja (para el contraste primario). **Confianza:** alta.
- **Acción:** INDISPENSABLE si alguna variante post hoc se va a presentar como mejora. Ver R-3.
- **Dependencias:** C-02, C-06, C-07.

### C-05 — Pérdidas auxiliares (textura, *perceptual proxy*, adversarial): defectos que impiden leerlas
- **Ubicación:** `code/src/renderizador/difusion.py:147-164`; `texturas.py:29-37`, `:50-58`, `:82-97`; `results/objetivo3/pipeline_textura.sbatch:114`, `:147-148`.
- **Evidencia:**
  - `x0p = dif.x0_desde(...)` se pasa entero a `perdida_d(D, _x0, _fake, ...)`. El *real* es el parche verdadero completo y el *fake* no se compone: fuera de $G$ la red nunca se entrena.
  - `PatchD` tiene un campo receptivo de unos 38 px (**cálculo propio**: tres conv 4×4 con stride 2 y una 3×3), mayor que la banda de unos 13–15 px. Las celdas de $G$ ven, por tanto, píxeles de fuera de $G$.
  - `for lote in 16 8` (si hay OOM, el brazo baja a lote 8); el control C toma `lote_T`.
  - La adversarial usa `--aux-adv 0.01` fijo, sin la regla de calibración de λ.
- **Descripción:**
  - **Adversarial.** El discriminador puede separar *real* de *fake* mirando fuera de $G$, de modo que el gradiente útil dentro de $G$ se diluye. Además el discriminador está condicionado solo a $M$ y $G$, no al contexto anatómico, así que premia una textura plausible sin coherencia con la anatomía.
  - **Perceptual proxy.** Un L1 sobre la pirámide laplaciana empuja hacia la mediana condicional, es decir, hacia **más** suavizado, lo contrario del objetivo declarado.
  - **Textura.** Igualar la desviación local de alta frecuencia es igualar momentos: puede producir ruido de textura sin estructura de raya, el mismo defecto de "textura sobrepuesta" que marcó la autora (cap3:542). Sus ventanas de 5 y 9 px también cruzan el borde de $G$.
  - **Comparación con el control.** Si un brazo baja a lote 8 y el control no, la comparación queda confundida.
- **Severidad:** alta (para la validez de esos brazos). **Confianza:** alta (código); media (efecto).
- **Acción:** INDISPENSABLE antes de interpretar cualquier resultado de esos brazos. Si se reportan, declarar el defecto de composición o no interpretarlos, y verificar que brazo y control tienen el mismo lote. Recomiendo no abrir más brazos (R-7).
- **Dependencias:** C-04, C-06.

### C-06 — El control de ajuste fino ya degrada: el comparador está desplazado
- **Ubicación:** `capitulo3.tex:319-331`; `entrenar.py:213-216`, `:268`.
- **Evidencia:**
  - Control: desviación de 585 HU en 0–2 mm, frente a 233 HU del modelo evaluado; pérdida de validación de 0.0647 frente a 0.0540 en el paso 16 500.
  - El ajuste fino carga solo los pesos (`--init-modelo`) y arranca AdamW con momentos nuevos.
- **Descripción:** Seguir entrenando desde un mínimo de validación con el optimizador reiniciado es una explicación más simple de la degradación que el tipo de tarjeta. La regla compara cada brazo con un control que empeora, de modo que un "+" del brazo puede ser solo menos degradación. El efecto de la tarjeta se puede aislar sin entrenar.
- **Severidad:** alta (para las conclusiones de B y del pipeline de texturas). **Confianza:** media.
- **Acción:** INDISPENSABLE antes de reportar cualquier brazo de ajuste fino. Ver R-4.
- **Dependencias:** C-04, C-05.

### C-07 — La métrica angular y el término $L_{\mathrm{ang}}$ miden también anatomía y forma de $M$
- **Ubicación:**
  - `results/objetivo3/c4_anisotropia.py:27` ("el angulo sigue siendo respecto al centroide")
  - `code/src/renderizador/angular.py:137-141`
  - `results/objetivo3/c4_b_resultado.md`
  - `capitulo3.tex:379-389`, `:327`
- **Evidencia:**
  - `control_anatomia` en modo crudo da 0.319 con $K=24$, frente a 0.320 del modelo evaluado en modo crudo.
  - B1000 frente al control por paciente: 0101 da 0.401 frente a 0.332; 0102 da 0.274 frente a 0.266 (+0.069 y +0.008).
- **Descripción:**
  - **Geometría.** En los cortes axiales, un tornillo transilíaco aparece alargado. Sectorizar por ángulo respecto del centroide divide el anillo según la posición a lo largo del tornillo, y eso recoge diferencias anatómicas (hueso o partes blandas a lo largo del trayecto). Es la misma familia de fallo que invalidó la versión 1 de la métrica (cap3:383).
  - **Modo residuo.** Incluye la anatomía regenerada (C-01).
  - **Ruido.** No hay estimación de la variabilidad de $\eta^2_{\mathrm{exc}}$ entre semillas, así que el umbral de +0.05 no tiene escala de ruido.
- **Severidad:** media. **Confianza:** media.
- **Acción:**
  - INDISPENSABLE antes de usar $\eta^2$ en otra decisión: calcular la desviación entre semillas a partir de las 5 semillas ya generadas (R-5).
  - OPCIONAL: estratificar por elongación de $M$ en el corte.
- **Dependencias:** C-01, C-04.

### C-08 — Baselines: el comparador nombrado es degenerado y falta un baseline no aprendido justo
- **Ubicación:** `introduccion.tex:21`; `capitulo3.tex:440`, `:446-448`; `capitulo4.tex:121`, `:170`; `capitulo3.tex:280-293` ($\Gamma_M$).
- **Evidencia:**
  - La pregunta dice "...frente a la inserción por copia y pegado". La misma tesis declara: "Ningún resultado de ese contraste cuenta a favor del sintetizador".
  - Artefacto paramétrico: −98.9 HU [−287.3, +89.4], frente a −301.0 HU del modelo evaluado.
- **Descripción:** La pregunta de investigación pone como comparador un brazo cuya amplitud es nula por construcción. El único baseline no aprendido que se ejecutó (el paramétrico) es un oráculo calibrado con el exceso real y supera al modelo en el criterio primario. Además, en el criterio visual (c) el modelo evaluado tiene la peor puntuación (1.33; cap3:540). Falta el baseline no aprendido natural, que ya está implementado: copia y pegado más $c\cdot\Gamma_M$ (`plantilla.py`), con $c$ ajustado en entrenamiento. Con él se respondería si la difusión aporta algo sobre el *prior* analítico que usa la propia versión 2.
- **Severidad:** alta. **Confianza:** alta.
- **Acción:**
  - INDISPENSABLE (texto): reformular la pregunta, con el protocolo físico como comparador y la copia y pegado como control de cordura.
  - RECOMENDABLE: ejecutar el baseline $\Gamma_M$ (R-6).
- **Dependencias:** R-3.

### C-09 — La compuerta del Objetivo 1 no mide lo que exige el *inpainting* con composición
- **Ubicación:** `introduccion.tex:46`; `capitulo3.tex:74`, `:210`; `capitulo4.tex:29-31`, `:211-213`.
- **Evidencia:**
  - Error del autoencoder en $B_\delta$: 64.62 HU en el mejor caso.
  - Discrepancia del sintetizador elegido en $B_\delta$: 198.0 HU en la reconstrucción de implantes reales.
  - Fuera de $G$ se copia el original (cap3:204).
- **Descripción:** El criterio (error absoluto medio en todo el hueso < 25 HU) es pertinente para una síntesis global. Con composición, en cambio, solo importa la fidelidad dentro de $G$, donde el modelo elegido se equivoca más que la ida y vuelta del autoencoder descartado. Las dos cifras no son estrictamente comparables (una es generación y la otra reconstrucción), pero muestran que el veredicto negativo no establece que la vía latente fuera peor **para esta tarea**. Presentarlo como "hallazgo propio" que obligó al cambio de dominio (intro:46) sobrestima su alcance.
- **Severidad:** media. **Confianza:** alta.
- **Acción:** INDISPENSABLE (texto, coste mínimo): acotar el alcance en intro:46 y en la discusión. La vía latente con composición queda como TRABAJO FUTURO.
- **Dependencias:** ninguna.

### C-10 — El régimen de entrenamiento no permite atribuir diferencias entre versiones
- **Ubicación:** `capitulo3.tex:214`, `:230`, `:242`, `:297`; `entrenar.py:268`; `results/objetivo3/run05/run05a_meta.json`; `results/objetivo3/a1_casos.csv`.
- **Evidencia:**
  - 27 979 587 parámetros (versión 2) y 39 casos.
  - Sin EMA, sin *augmentation* y con tasa de aprendizaje constante. Una búsqueda de EMA, *scheduler* y *augmentation* en `renderizador/` no devuelve nada.
  - Espaciado en el plano de 0.631 a 1.266 mm sin condicionamiento por espaciado (**cálculo propio** sobre `a1_casos.csv`, 74 casos de entrenamiento antes de filtrar).
  - Mínimo de validación a unas 18.6 épocas (**cálculo propio**: 16 500×16/14 182).
  - Una sola semilla de entrenamiento por versión.
- **Descripción:** Las diferencias de la versión 2 (−258.9 y −264.3 frente a −301.0 HU, cap4:226) y del ajuste fino no pueden separarse de la varianza entre corridas, que no se midió. Sin EMA es esperable una alta variabilidad entre checkpoints y semillas (393 frente a 270 HU, cap3:256). Ninguno de los cinco componentes de tornillo revisados es transilíaco (cap3:228, `:632`).
- **Severidad:** media. **Confianza:** alta (hechos); media (consecuencias).
- **Acción:**
  - INDISPENSABLE (texto): declarar que la varianza entre corridas de entrenamiento es desconocida y que ninguna diferencia entre versiones puede atribuirse a la intervención.
  - TRABAJO FUTURO: réplicas de entrenamiento y EMA. No lo recomiendo ahora.
- **Dependencias:** C-04.

### C-11 — Generación corte a corte sin coherencia entre cortes
- **Ubicación:** `results/objetivo3/a15_cadena_completa.py:392-398`; `difusion.py:177-179`; `capitulo3.tex:416`.
- **Evidencia:**
  - Cada corte se muestrea por separado y sus vecinos salen del volumen **original**, no de lo generado.
  - El generador se resiembra con la misma `semilla` en cada corte.
  - Las regiones de medición son "planos perpendiculares al eje del implante", que cruzan muchos cortes axiales.
- **Descripción:** Las discontinuidades entre cortes generados de forma independiente aparecen en los planos de medición como desviaciones extremas y alimentan las colas que mide la *streak amplitude*. Repetir el mismo ruido inicial en cada corte añade además una correlación axial artificial.
- **Severidad:** media. **Confianza:** media. **Magnitud:** NO VERIFICABLE con el material.
- **Acción:** RECOMENDABLE (R-8).
- **Dependencias:** C-01.

### C-12 — Atajo del contexto: en entrenamiento las rayas reales están fuera de $G$
- **Ubicación:** `difusion.py:18-22`; `results/objetivo3/diseno_A.md:337-340`; `datos.py:221`; `capitulo3.tex:238-240`.
- **Evidencia:** "El modelo puede depender de rayas que en uso no existen" (diseno_A.md). La bandera `borrar_contexto` existe y no se entrenó.
- **Descripción:** Los vecinos fuera de $G$ traen el *streaking* real, muy correlacionado con el objetivo. Si la red aprendió a continuar esas rayas, en receptores limpios generará poco artefacto lejos del metal. Eso es lo observado: déficit desde unos 4 mm (cap3:276). Si esta es la causa, ninguna pérdida auxiliar lo corrige, porque el problema está en el condicionamiento y no en la función de pérdida.
- **Severidad:** media–alta. **Confianza:** media.
- **Acción:** RECOMENDABLE con prioridad alta, antes de invertir más GPU en pérdidas auxiliares (R-9).
- **Dependencias:** C-05.

### C-13 — La pérdida en el espacio codificado apenas pondera las colas del artefacto
- **Ubicación:** `results/objetivo1/e6c_techo_lw.py:42-69`; `difusion.py:102-104`.
- **Evidencia:** LW = asinh(h/500) sobre [−1000, 20 000] HU; MW = [−320, 480]; SW = [−160, 240].
- **Descripción (cálculo propio):** En unidades de [−1, 1], la sensibilidad por HU es:
  - LW: 6.9e-4 en 0 HU y 3.1e-4 en ±1000 HU;
  - MW: 2.5e-3;
  - SW: 5e-3.

  Sumando los cuadrados de los tres canales, un error de 1 HU en tejido blando pesa unas 340 veces más en el MSE que el mismo error en valores extremos de raya, donde MW y SW están saturados. La pérdida privilegia la fidelidad cerca de 0 HU y regresa a la media en las colas. Es coherente con el déficit del percentil 95 y con el "halo liso", pero es una hipótesis.
- **Severidad:** media. **Confianza:** media.
- **Acción:**
  - RECOMENDABLE (texto): mencionarlo en la discusión como causa plausible.
  - OPCIONAL: descomponer el error de validación por intervalos de HU.
- **Dependencias:** ninguna.

### C-14 — Criterio visual y "prueba de Turing"
- **Ubicación:** `capitulo3.tex:534-542`, `:628`.
- **Evidencia:** protocolo físico 5.00, real 4.83, modelo evaluado 1.33; una sola lectora (la autora); $P(X\ge4)=0.34$ con $n=6$.
- **Descripción:** Con una lectora que conoce los modelos, el criterio no distingue el protocolo físico de lo real y no es una prueba de Turing. Optimizar pérdidas hacia ese criterio con la misma lectora y los mismos dos receptores sobreajusta el juicio visual. Superar una prueba de Turing no demostraría ni coherencia física ni utilidad diagnóstica o de entrenamiento.
- **Severidad:** media. **Confianza:** alta.
- **Acción:** TRABAJO FUTURO (R-10). No usarlo como criterio de cierre.

---

## 3. Recomendaciones de análisis

Para cada recomendación: la pregunta científica, la evidencia nueva que aporta, el riesgo que resuelve, el coste y lo que pasa si no se hace. Todas son de inferencia o de CPU.

**R-1 — Perfil por anillos del piso de ruido ($G$ sin $M$). INDISPENSABLE**
- **Pregunta:** ¿la meseta de 727–949 HU entre 4 y 12 mm es artefacto o error de *inpainting*?
- **Evidencia nueva:** amplitud y error absoluto medio de la generación sin metal por anillo de 2 mm y por tejido (hueso o partes blandas), en los 13 pacientes y las 5 semillas ya generadas (salidas `--sin-metal` del piso de ruido).
- **Riesgo que resuelve:** validez de constructo del criterio primario y del "perfil plano" (C-01).
- **Coste:** bajo (CPU, sobre volúmenes ya generados; si no se guardaron, inferencia sobre 13 pacientes).
- **Si no se hace:** la discusión del perfil (cap4:168) atribuye al sintetizador una amplitud que puede ser anatomía regenerada.

**R-2 — Piso de ruido de las variantes del barrido de $\eta$ en validación. INDISPENSABLE si se reporta 100:0.3**
- **Pregunta:** ¿el aumento del percentil 95 con $\eta>0$ es artefacto o varianza inyectada?
- **Evidencia nueva:** amplitud con $G$ sin $M$ para 50:0, 50:0.3 y 100:0.3 en 0101 y 0102, más el cociente entre piso y amplitud.
- **Riesgo que resuelve:** C-02.
- **Coste:** bajo (2 pacientes × 5 semillas × 3 variantes).
- **Si no se hace:** el resultado en prueba de 100:0.3 queda sin lectura posible.

**R-3 — "Validación 2": ampliar los receptores de validación sin tocar la partición de prueba. INDISPENSABLE para cualquier afirmación post hoc de mejora**
- **Pregunta:** ¿las decisiones y umbrales tomados sobre $n=2$ se sostienen con más pacientes?
- **Evidencia nueva:** de los 72 pacientes de la cohorte del Objetivo 2, 49 están en la partición de entrenamiento y 30 de ellos tienen un corredor viable con $D\ge9$ mm (**cálculo propio** cruzando `objetivo2/e13_poses.csv` con `objetivo1/p1_particion.csv`). El sintetizador nunca los vio, porque solo entrena con volúmenes con metal. Con 10 a 15 de ellos se pueden reestimar en exploración:
  - $s_{\mathrm{sem}}$ y su dispersión;
  - el ranking entre el modelo evaluado, 100:0.3, B1000, B300 y el control;
  - la variabilidad de $\eta^2_{\mathrm{exc}}$.
- **Riesgo que resuelve:** sobreajuste de selección (C-04) y reutilización de la partición de prueba.
- **Coste:** medio (solo inferencia del sintetizador; el protocolo físico no hace falta para $s_{\mathrm{sem}}$ y su $r_{\mathrm{rep}}$ vale 6.1 HU). Hay que verificar que ninguno sea otra adquisición de un paciente con metal de entrenamiento, porque las auditorías de identidad no cubren a los pacientes sin metal (cap3:600).
- **Si no se hace:** todas las conclusiones post hoc quedan en $n=2$, y cualquier "mejora" es indistinguible de la variabilidad entre pacientes.
- **Nota:** no sustituye el contraste confirmatorio ni redefine $\Delta$.

**R-4 — Aislar el efecto de la tarjeta sin entrenar. INDISPENSABLE antes de reportar el ajuste fino**
- **Pregunta:** ¿la degradación del control se debe a la tarjeta o a seguir entrenando?
- **Evidencia nueva:** inferencia de `run04/mejor.pt` en la tarjeta del ajuste fino (2 receptores, 5 semillas, cotejo de 1 mm), comparada con la referencia del 15 de octubre (diferencia máxima ya fijada de 0.04 HU, cap3:313). Exigir además que cada brazo no sea inferior al modelo evaluado en la desviación de 0–2 mm.
- **Riesgo que resuelve:** C-06.
- **Coste:** bajo.
- **Si no se hace:** "B frente a control" mide cuánto contrarresta un brazo la degradación, y no el efecto del término.

**R-5 — Variabilidad entre semillas de $\eta^2_{\mathrm{exc}}$. INDISPENSABLE antes de usar la métrica para decidir**
- **Pregunta:** ¿qué diferencia de $\eta^2$ supera el ruido de muestreo?
- **Evidencia nueva:** desviación estándar y rango por paciente con las 5 semillas ya generadas, por cada $K$.
- **Riesgo que resuelve:** umbrales sin escala (C-07).
- **Coste:** muy bajo (CPU).
- **Si no se hace:** las condiciones (i) de B y la tabla de cap3:393-408 no tienen escala de ruido.

**R-6 — Baseline no aprendido con $\Gamma_M$. RECOMENDABLE**
- **Pregunta:** ¿la difusión aporta algo sobre el *prior* analítico que ella misma usa?
- **Evidencia nueva:** copia y pegado más $c\cdot\Gamma_M$, con $c$ fijado en entrenamiento por mínimos cuadrados contra el exceso real por anillo. Medirlo en validación 2 y, de forma descriptiva, en los 13 pacientes de prueba, con la misma *streak amplitude*, el perfil por anillos y $\eta^2$.
- **Riesgo que resuelve:** C-08, al aportar un baseline justo que no es un oráculo.
- **Coste:** bajo (CPU; `plantilla.py` ya existe).
- **Si no se hace:** la contribución aprendida sigue sin una comparación que pueda ganar o perder de forma informativa.

**R-7 — Regla de parada de las exploraciones. INDISPENSABLE (decisión escrita, coste nulo)**
- Declarar por escrito:
  1. no se abren más brazos;
  2. cada brazo ya entrenado se evalúa una sola vez en validación 2 y, solo si pasa, una vez en prueba, como exploratorio;
  3. todo se reporta en un apéndice de "exploraciones post hoc".
- **Riesgo que resuelve:** el *garden of forking paths*.
- **Si no se hace:** el capítulo 3 sigue creciendo (cap3:309-333 y 534-544 ya mezclan diseño congelado y exploración).
- Mover este bloque a un apéndice ayuda además a reducir la extensión del documento.

**R-8 — Coherencia entre cortes. RECOMENDABLE**
- **Pregunta:** ¿cuánto de las colas viene de discontinuidades en $z$?
- **Evidencia nueva:** energía del gradiente axial dentro de $G$ (sintético frente a original y frente al protocolo físico), sobre volúmenes ya generados.
- **Coste:** bajo (CPU).
- **Si no se hace:** C-11 queda como hipótesis no medida.

**R-9 — Diagnóstico del atajo del contexto, solo inferencia. RECOMENDABLE (prioridad alta)**
- **Pregunta:** ¿la amplitud generada depende de las rayas del contexto?
- **Evidencia nueva:** en la reconstrucción de implantes reales de validación, generar con el contexto fuera de $G$ original y con ese contexto suavizado (por ejemplo, con un filtro de mediana), y medir el cambio de amplitud dentro de $G$.
- **Riesgo que resuelve:** decide si seguir con pérdidas auxiliares tiene sentido (C-12).
- **Coste:** bajo–medio.
- **Si no se hace:** se puede seguir gastando GPU en pérdidas que no actúan sobre la causa.

**R-10 — Prueba de Turing visual. TRABAJO FUTURO**
- **Requisitos mínimos de diseño:**
  - al menos 2 o 3 lectores distintos de la autora;
  - elección forzada entre dos alternativas, o real/sintético con prevalencia balanceada;
  - parches emparejados por anatomía y ventana;
  - tamaño muestral calculado para un IC de la exactitud;
  - inclusión del protocolo físico como control positivo.
- **Lectura permitida:** indistinguibilidad perceptual. No implica ni coherencia física ni utilidad.

**R-11 — Sensibilidad del muestreador a $\sigma$. RECOMENDABLE**
- **Pregunta:** ¿la lectura $W_1<0.395$ depende de la convención $h=2\sigma$ (cap3:190, `:610`)?
- **Evidencia nueva:** $W_1$ con $\sigma\times\{0.5, 2\}$ y la misma semilla por caso.
- **Coste:** muy bajo (CPU; no es una ablación de componentes).
- **Si no se hace:** no se puede distinguir el acuerdo con la referencia clínica de un efecto de la escala elegida.

**R-12 — Síntesis sobre poses del muestreador en validación 2. RECOMENDABLE**
- **Pregunta:** ¿el sintetizador se comporta de forma estable en poses perturbadas, incluidas las de grado 3, con el tornillo fuera del hueso?
- **Evidencia nueva:** amplitud y *metal integrity* por grado, solo con el sintetizador, sin usar la partición de prueba.
- **Coste:** medio (inferencia).
- **Si no se hace:** la "cadena" sigue sin evaluarse como cadena (cap4:262).

**Correcciones de texto INDISPENSABLES:** C-01a, C-03, C-08 (pregunta de investigación), C-09, C-10, y la fórmula real de $\sigma$ (C-02).

---

## 4. Pertinencia de los métodos post hoc en curso

| Método | Pertinencia científica | Riesgo principal | Veredicto |
|---|---|---|---|
| Barrido de pasos y $\eta$ | Baja–media. No cambia el modelo y puede subir la varianza. | $\sigma$ no estándar; piso de ruido no medido (C-02) | Mantener como descriptivo; R-2 obligatorio |
| Término angular (B1000, B300) | Baja. El término mide en parte la forma de $M$ y la anatomía. | Control que degrada; $n=2$; sin escala de ruido | Cerrado: no cumple la condición (i); no reabrir |
| Textura | Baja. Iguala momentos, no estructura. | Puede producir textura sobrepuesta | Solo exploratorio, tras R-4 |
| *Perceptual proxy* (L1 laplaciano) | Muy baja. Favorece el suavizado. | Efecto contrario al buscado | No justifica GPU adicional |
| Adversarial (PatchGAN) | Baja con 39 casos. Discriminador sin contexto y atajo por falta de composición. | Alucinación; resultado no interpretable | INDISPENSABLE no interpretarlo tal como está implementado |

Mejorar la apariencia visual queda fuera del reclamo del Objetivo 3 (cap3:628). Ninguno de estos métodos responde a la pregunta de investigación, y todos se deciden después de ver la prueba. Lo que sí es científicamente necesario es explicar **por qué** el modelo falla: lo responden R-1, R-8, R-9 y C-13, a coste bajo y sin entrenar. Que hoy se gaste más GPU en pérdidas que en esos diagnósticos es el principal desequilibrio de la estrategia actual.

## 5. Lo que no recomiendo (evitar el *scope creep*)

- Nuevas arquitecturas (3D, latentes con composición, residuales sobre la anatomía conocida, entrenamiento con pares simulados por física): TRABAJO FUTURO. Son la vía correcta para C-01 y C-12, pero exceden el alcance y el cómputo disponible.
- Réplicas de entrenamiento, EMA y ablaciones de banda, codificación o máscara: TRABAJO FUTURO. Lo necesario ahora es declarar que no se hicieron (C-10).
- La evaluación de segmentación posterior: sigue fuera de alcance. Antes de hacerla, debería resolverse que las etiquetas óseas dentro de $G$ ya no son válidas (C-01).
- Una nueva prueba de equivalencia confirmatoria: no tiene sentido, porque la partición de prueba ya se usó.

## 6. Dependencias y orden sugerido

1. R-7, junto con las correcciones de texto (coste nulo).
2. R-5, R-1 y R-2 (CPU o inferencia mínima).
3. R-4 y R-9.
4. R-3, que da el marco para R-6 y R-12.
5. R-8 y R-11 si queda capacidad.

---

**Resumen en 3 líneas**
1. El sintetizador regenera toda la anatomía de $G$ sin verla (sin el corte central y con $G$ borrada en los vecinos). Junto con una pérdida en el espacio codificado que casi no pondera las colas, es la explicación más probable del piso de ruido de 893 HU, del perfil plano y del déficit del percentil 95. Los diagnósticos baratos de esa causa (R-1, R-8, R-9) deberían ir antes que más GPU en pérdidas auxiliares.
2. Las exploraciones post hoc (barrido de $\eta$, ajuste fino, textura, *perceptual proxy*, adversarial) descansan en dos receptores, un control que degrada, un $\eta$ que no es el de DDIM y una pérdida adversarial con un atajo de implementación. Antes de leerlas hacen falta una regla de parada (R-7) y una validación 2 de solo inferencia con las 30 pelvis viables que el modelo nunca vio (R-3).
3. Falta un baseline no aprendido justo ($\Gamma_M$, R-6) y la pregunta de investigación debe dejar de nombrar como comparador a la copia y pegado. La compuerta del Objetivo 1 no demuestra que la vía latente fuera peor para un *inpainting* con composición, y una prueba de Turing con una sola lectora no demostraría ni coherencia física ni utilidad.
