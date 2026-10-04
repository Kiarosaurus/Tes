# capitulo1 — r00 (redaccion inicial) — respuesta del redactor

Modo: redactar. Archivo: `overleaf/secciones/capitulo1.tex` (era esqueleto). Lint
`python scripts/lint_redaccion.py capitulo1 --compilar`: **PASA**, alta 0 / media 0 / baja 0;
compila sin errores ni citas o referencias indefinidas (104 paginas). GAP del capitulo: lit 3 / dato 0 / dec 4.

## Que se redacto

Se mantuvieron los cinco `\section` del esqueleto, con sus titulos, y se anadieron `\label`
(`cap:marco`, `sec:mt-tc`, `sec:mt-artefactos`, `sec:mt-iliosacra`, `sec:mt-difusion`,
`sec:mt-estadistica`). Sin cambio de titulos.

- **Apertura** (2 parrafos): funcion del capitulo, que no hace (no compara trabajos ni describe el
  diseno) y orden de las secciones (G-T5). **Figura 1.1** (`fig:mt-conceptos`, P-MT2): cada grupo de
  conceptos con la pieza de la cadena que lo usa.
- **1.1 TC y HU** (5 parrafos, Ec. `eq:ventana`): sinograma, modelo de adquisicion, retroproyeccion
  filtrada y su modelo monocromatico, dominio de proyeccion frente a dominio de imagen, HU, umbrales de
  150 y 2500 HU como definiciones operativas, ventana y saturacion, codificacion multiventana, ida y vuelta.
- **1.2 Artefactos** (7 parrafos): definicion por contraste, mecanismos (endurecimiento del haz con
  *cupping*, inanicion de fotones, dispersion, efecto exponencial de gradiente de borde, volumen parcial
  no lineal), dos consecuencias (artefacto fuera del implante -> `B_delta`; mecanismos definidos en
  proyeccion -> supuesto del dominio de imagen) y MAR frente a simulacion fisica (CatSim).
- **1.3 Fijacion iliosacra** (9 parrafos): indicacion (Tile B y C), tornillo iliosacro frente a
  transiliosacro, colocacion percutanea (fluoroscopia, navegacion), zona segura, corredor y diametro
  maximo, umbral de 10 mm como no establecido, marco de Kaiser, posicion ideal, escala de brecha y su
  origen, definiciones binarias no intercambiables, caracter ordinal de la escala.
- **1.4 Difusion** (7 parrafos, Ecs. `eq:difusion-directa`, `eq:perdida-difusion`): procesos directo
  e inverso, calendario de ruido, objetivo de prediccion del ruido, U-Net, muestreo determinista
  abreviado, condicionamiento (concatenacion, atencion cruzada, ControlNet), difusion latente,
  *inpainting* (RePaint frente a modelo condicionado) y definicion de 2.5D (la introduccion la remite aqui).
- **1.5 Marco estadistico** (6 parrafos): tipos de resultado y unidad de analisis por objetivo,
  Wasserstein-1 con dos ejemplos calculados de la propia formula, superioridad frente a equivalencia,
  Wilcoxon y TOST, intervalo por remuestreo, multiplicidad, que se fijo antes de ver los datos, MAE
  frente a raiz del error cuadratico medio.

Lo que **no** se duplico: estado del arte del cap. 2 (resultados de los autores, tabla, brecha) y
metodo del cap. 3 (criterio de viabilidad `D >= d + 2e`, preinscripcion, SAP, parametros). Se remite con
`\ref` a `sec:ea-representacion`, `sec:datos`, `sec:obj1`, `sec:corredor`, `sec:marco-metal`,
`sec:poses`, `sec:sap`, `sec:sintetizador`, `sec:apariencia`, `sec:amenazas`, `eq:mae`, `eq:w1`,
`fig:pipeline`.

## Fuentes por cifra y afirmacion

Todas las claves existen en `refs.bib` y tienen ficha; ninguna ficha usada dice "Profundidad: solo abstract".

| Seccion | Afirmacion o cifra | Fuente (ficha: lugar) |
|---|---|---|
| 1.1 | Senal por indice del sinograma; suma sobre energias; longitud de interseccion; coeficiente de atenuacion lineal por material y energia | `deman2007catsim`: Sec. 2.1, p. 1 (definiciones de y_i, A_ik, l_iso, mu_ok) |
| 1.1 | Beer-Lambert energia por energia | `abadi2019`: Sec. II-B, p. 1458; `wang2019cochlear`: "discretized on 5 different energies", Introduccion, p. 2 |
| 1.1 | Reconstruccion por retroproyeccion filtrada | `deman1999`: Sec. II-C, p. 692; `deman2007catsim`: Sec. 3.1, p. 5; `karageorgos2024ddpm`: Sec. II-F, p. 10 |
| 1.1 | FBP supone el modelo monocromatico de Radon; discrepancia no lineal policromatica | `park2015ct`: Que hace (Sec. 2) |
| 1.1 | Agua 0 HU, aire -1000 HU por definicion | `wu2022xcist`: Discussion Exp. 1, p. 13 |
| 1.1 | Conversion HU-mu con el coeficiente del agua por energia | `wang2019cochlear`: Sec. 2.1, p. 4 |
| 1.1 | Hueso = voxeles sobre 150 HU | `peters2025hybrid` (ya citado asi en cap. 3); glosario |
| 1.1 | Metal clinico segmentado con 2500 HU; uso local solo de cribado | `wang2025adaptiveweighting`: Sec. V-A-2, p. 2413; `li2024` (como en cap. 2); DEC 2026-09-11 (#22) via cap. 3 §Datos |
| 1.1 | Parte del sacro bajo 150 HU en la cohorte | cap. 3 §Corredor (mediana 0.42), con `\ref` |
| 1.1 | Ventana: saturar a [L, H] y escalar a [0, 1] (Ec. `eq:ventana`) | `wang2025adaptiveweighting`: Eq. (2), Sec. III, p. 2410 |
| 1.1 | Fraccion del rango inversamente proporcional al ancho | Consecuencia directa de la Ec. `eq:ventana` (demostracion, G-T4) |
| 1.1 | Tres ventanas LW/MW/SW; cascada, no canales de entrada | `wang2025adaptiveweighting`: Sec. V-A-1, p. 2412; ficha "Restriccion" |
| 1.1 | Techo 2000 < 2500 HU: el metal satura | cap. 2 §Representacion (misma lectura) |
| 1.2 | Rayas claras y oscuras que ocultan anatomia; severidad por tamano, forma y aleacion; osteosintesis "Medium" cualitativa | `selles2024marreview`: Sec. 1, p. 1; Tabla 1, p. 6 |
| 1.2 | Cuatro mecanismos principales segun Selles | `selles2024marreview`: Sec. 1, p. 1 |
| 1.2 | Cuatro causas mas importantes segun De Man; todas producen rayas; sin peso numerico; ruido no lineal | `deman1999`: Conclusiones, p. 695; Sec. III-E, p. 694; ficha "Respuestas" punto 1 |
| 1.2 | Endurecimiento: absorcion preferente de baja energia, desplazamiento del espectro | `selles2024marreview`: Sec. 1, p. 1 |
| 1.2 | *Cupping* dentro, rayas fuera | `park2015ct`: Introduccion, p. 2 |
| 1.2 | Rayas oscuras en direcciones de mayor atenuacion; rayas que conectan metales | `deman1999`: Sec. III-B, p. 693 |
| 1.2 | Inanicion: muy pocos fotones; faltan datos de proyeccion | `selles2024marreview`: Sec. 1, p. 1 |
| 1.2 | Ruido: lineas finas alternas; depende de la atenuacion integrada | `deman1999`: Sec. III-E, p. 694 |
| 1.2 | Dispersion por densidad electronica; razon pequena basta | `selles2024marreview`: Sec. 1, p. 1; `deman1999`: Sec. III-C, p. 694 |
| 1.2 | EEGE: rayas tangentes a bordes rectos; rayas que irradian del metal; efectos de borde alineados | `deman1999`: Sec. III-D, p. 694; `selles2024marreview`: Sec. 1, p. 1 |
| 1.2 | De Man no mide extension | `deman1999`: ficha, pregunta 2 (NO ENCONTRADO) |
| 1.2 | Volumen parcial no lineal: variacion axial, una discontinuidad local, dos o mas rayas de largo alcance; hueso, fuente monocromatica, sin metal | `glover1980nonlinear`: Que hace; Restriccion; Sec. II, pp. 240-243 |
| 1.2 | De Man simula en 2D y excluye el volumen parcial axial | `deman1999`: Sec. II-A, p. 691 |
| 1.2 | De Man aisla causas modificando el sinograma | `deman1999`: Sec. II-D, p. 693; ficha "Restriccion" |
| 1.2 | CatSim modela espectro, ruido cuantico y electronico, volumen parcial no lineal, dispersion; reconstruye con FBP | `deman2007catsim`: Abstract, p. 1; Sec. 3.1, p. 5. CatSim en XCIST: `wu2022xcist` |
| 1.3 | Fracturas inestables del anillo posterior; Tile B (rotacion) y C (rotacion y vertical); percutanea; navegacion Iso-C3D que rota 190 grados; TC posoperatoria | `zwingmann2009navigated`: Que hace; M&M, p. 1834; Discussion, p. 1837 |
| 1.3 | Iliosacro: entra por el ilion y termina en el sacro | `kaiser2014dysmorphism`: ficha, "Distincion transsacro vs iliosacro" |
| 1.3 | Tres corticales (dos del ilion, una del ala) | `smith2006iliosacral`: M&M, p. 235 |
| 1.3 | Transiliosacro: cruza ambas articulaciones y sale por la tabla externa opuesta; cifras de McLaren transiliosacras | `mclaren2021corridor`: M&M, PDF p. 2 |
| 1.3 | Decubito supino, fluoroscopia en tres planos | `routt1997`: Introduccion, p. 206 |
| 1.3 | Zona segura alar y sus limites; raiz L5, canal, vasos iliacos | `routt1997`: Fig. 2, p. 207; pp. 207, 212-213 |
| 1.3 | Dos conos unidos por la punta; seccion minima ortogonal al eje | `gardner2010safezones`: M&M, p. 623 |
| 1.3 | Recta expandida hasta atravesar la cortical en al menos tres puntos; diametro maximo | `mclaren2021corridor`: M&M, PDF p. 2 |
| 1.3 | 10 mm en las tres fuentes; atribuido a terceros (Gardner, Kaiser); "no establecido" (McLaren) | `gardner2010safezones`: p. 624; `kaiser2014dysmorphism`: p. e120(2), e120(7); `mclaren2021corridor`: Introduccion, PDF p. 2 |
| 1.3 | Reformateo por el eje sacro perpendicular al platillo de S1; lineas de crestas y de espinas | `kaiser2014dysmorphism`: p. e120(2) |
| 1.3 | Posicion ideal; tres tipos de perforacion; grados 0 a 3 con 2 y 4 mm; escala tomada de tornillos pediculares; escala angular | `smith2006iliosacral`: Screw Position, p. 236 |
| 1.3 | Zwingmann aplica la escala sobre TC posoperatoria | `zwingmann2009navigated`: M&M, p. 1835 |
| 1.3 | Definicion binaria de Hinsche | `hinsche2002fluoroscopy`: Measurements, p. 138; glosario (no intercambiable, #12) |
| 1.3 | Grados 1 y 2 de 2 mm; grado 3 abierto | Consecuencia de los limites de Smith et al. (demostracion) |
| 1.4 | Difusion en imagen medica | `kazerouni2023diffusionsurvey` (como en la introduccion) |
| 1.4 | Cadena de Markov que invierte un proceso gaussiano; T = 1000; prediccion del ruido con objetivo simplificado; U-Net | `ho2020denoising`: Que hace; Sec. 4, p. 5 |
| 1.4 | Proposito del proceso directo: borrar la estructura | `dorjsembe2024`: Sec. II, p. 2 |
| 1.4 | Forma cerrada de x_t (Ec. `eq:difusion-directa`) | `zhang2025diffboost`: Ec. 3, Sec. III-A, p. 3672; `dorjsembe2024`: Ec. (1), p. 2 |
| 1.4 | beta_t en (0, 1) | `zhang2025diffboost`: Sec. III-A, p. 3672 |
| 1.4 | Calendario coseno; beta de cocientes sucesivos | `nichol2021improved`: Sec. 3.2, p. 8165 |
| 1.4 | Objetivo de entrenamiento (Ec. `eq:perdida-difusion`), t uniforme | `rombach2022latentdiffusion`: Ec. 1, Sec. 3.2, p. 4 |
| 1.4 | U-Net: ruta contractiva y expansiva simetrica | `ronnenberger2015unet`: Que hace; `song2021ddim`: Apendice D.1 |
| 1.4 | Procesos no markovianos, mismo objetivo, deterministas, menos pasos sin reentrenar; 10 a 50 veces mas rapido | `song2021ddim`: Que hace; Resumen, p. 1 |
| 1.4 | Las tres fuentes en imagenes naturales | fichas de `ho2020denoising`, `song2021ddim`, `nichol2021improved` (Restriccion) |
| 1.4 | Concatenacion para condicion alineada; atencion cruzada | `rombach2022latentdiffusion`: Sec. 4.3.2, p. 7; Fig. 3, p. 4 |
| 1.4 | Mascara concatenada por canal en cada paso | `dorjsembe2024`: Sec. II, p. 2 |
| 1.4 | ControlNet: base congelada, copia del codificador, convoluciones en cero | `zhang2023controlnet`: Que hace; Fig. 2, p. 3 |
| 1.4 | Autoencoder perceptual + adversarial; compresion elimina alta frecuencia; cuello de botella en exactitud por pixel; decodificacion en una pasada | `rombach2022latentdiffusion`: Sec. 3.1, p. 3; Sec. 1, p. 2; Sec. 5, p. 9; Sec. 3.2, p. 4 |
| 1.4 | RePaint: modelo incondicional, region conocida muestreada de la entrada, avance y retroceso | `lugmayr2022repaint`: Que hace; Introduccion, p. 11462 |
| 1.4 | Inpainting de Rombach por concatenacion | `rombach2022latentdiffusion`: Tabla 15, p. 25 |
| 1.4 | El sintetizador recibe el parche con G borrada y las mascaras y copia el resto | cap. 3 §Sintetizador (TM Objective 3; DEC 2026-09-19) |
| 1.4 | 2.5D: tres cortes, se genera el central | `experiments/objetivo3/diseno_A.md` §4 (borrador, `[SUPUESTO]`) -> `\GAPDEC` |
| 1.4 | Lectura de Glover sobre 2.5D | ficha `glover1980nonlinear`, "Donde entra" (lectura del extractor), redactada como "este trabajo lee" |
| 1.5 | Unidad de analisis por objetivo; poses agregadas en el Obj 2; la referencia cuenta tornillos | cap. 3 §Obj1, §Apariencia, §Amenazas (validez de la conclusion) |
| 1.5 | W1 en grados; valores 1 y 3; misma fraccion de grado 0 con distancia distinta | Consecuencia de la Ec. `eq:w1` del cap. 3 (demostracion) |
| 1.5 | Equivalencia solo dentro de un margen fijado de antemano; nunca de una diferencia no significativa; resultado no concluyente posible | TM, Expected Results (Appearance); cap. 3 §Apariencia |
| 1.5 | Wilcoxon pareada de una cola; TOST; margen por variabilidad del metodo | TM, Expected Results; cap. 3 §Apariencia |
| 1.5 | IC 95 % por remuestreo de pacientes; multiplicidad solo favorece el aprobado | TM, Objective 1; cap. 3 §Obj1 y §Amenazas |
| 1.5 | Regla de la compuerta fijada antes de la prueba que decide; distribucion y metrica del muestreador antes de cualquier distancia | cap. 3 §Obj1 y §Poses (PAT-13 respetado) |
| 1.5 | RMSE nunca menor que MAE para los mismos residuos | TM, Objective 1; cap. 3 §Obj1 |

Ninguna cifra propia nueva: las unicas cifras del capitulo son ajenas (con cita) o de la propia
formula (1, 3; demostracion). No se uso ninguna cifra de `experiments/`.

## GAP abiertos (por tipo)

**`\GAPLIT` (3, nuevos; candidatos PENDIENTE en `docs/literatura/_candidatos.md`, ronda 2026-10-03):**
1. §1.1: "fuente de referencia de física de TC que dé la definición de la escala Hounsfield como transformación del coeficiente de atenuación lineal y los fundamentos de la reconstrucción por retroproyección filtrada".
2. §1.5: "fuente de referencia de la distancia de Wasserstein-1 y de su forma para distribuciones sobre una recta".
3. §1.5: "fuentes de referencia de la prueba de rangos con signo de Wilcoxon, de las dos pruebas unilaterales de equivalencia y del intervalo de confianza por remuestreo".

**`\GAPDATO` (0).**

**`\GAPDEC` (4; 1 nuevo, 3 replicados con el mismo texto que otra seccion, PAT-31):**
1. Nuevo, §1.4: "número de cortes contiguos de la entrada 2.5D del sintetizador, que solo propone el borrador de su diseño, pendiente de preinscripción". Fila nueva en MAPA; concreta la de "congelar la preinscripción".
2. Replicado de cap. 2, §1.4: "descripción y atribución del procedimiento de muestreo de la difusión del sintetizador frente a los de Lugmayr et al. y de LeFusion, pendiente en el registro del proyecto" (#106, #117 ABIERTAS).
3. Replicado de cap. 2, §1.3: "si SAP incorpora la dimensión angular de la escala de Smith et al. o declara que usa solo la de perforación, y con qué justificación" (#11 ABIERTA).
4. Replicado de la introduccion, §1.5: "si la comparación de equivalencia frente al protocolo físico se mantiene o pasa a trabajo futuro, contingencia de plazo registrada por la autora" (#90).

Implicancias ABIERTAS tocadas y como se trataron (regla 3): #61/#63 (dominio de imagen) como supuesto
con remision a `sec:amenazas`; #57 (artefacto global frente a banda local) sin cuantificar, ancho como
convencion; #106/#117 (metodo de difusion y muestreo) sin afirmar que el sintetizador usa DDIM, coseno o
RePaint; #11 con `\GAPDEC`. Ninguna se redacta como hecho.

## Decisiones de redaccion (para BITACORA §2)

| Decision | Motivo |
|---|---|
| Notacion de difusion propia para no chocar con el cap. 3 (G-T3, PAT-14): paso `n`, total `n_max`, ruido `xi`, red `xi_theta`, coeficiente `bar-gamma_n` (las fuentes escriben `bar-alpha_t`), varianzas `beta_n`, normal `\mathcal{N}`; el cambio de simbolo se declara en el texto | En el cap. 3, `epsilon` es la holgura radial, `T` el tramo, `t` el parametro del eje, `alpha` el angulo y `N` la normal de las perturbaciones |
| Ventana = `[w_min, w_max]`, no `[L, H]` del glosario | `L` es la longitud del corredor en el cap. 3 |
| *Filtered back-projection* = "retroproyeccion filtrada", sin sigla FBP | Evita una sigla nueva que solo usaria este capitulo |
| "Dominio de proyeccion" (sinograma) frente a "dominio de imagen"; ambos se definen en negrita en §1.1 | Extiende la decision de capitulo3-r05 ("dominio de imagen" unico nombre) |
| *Photon starvation* = "inanicion de fotones"; *scatter* = "dispersion"; *exponential edge-gradient effect* = "efecto exponencial de gradiente de borde"; nonlinear partial volume = "volumen parcial no lineal" | Terminos fijos de `overleaf/CLAUDE.md` y forma ya usada en la introduccion; el parrafo desfasado de la introduccion dice "escasez de fotones" y deberia alinearse al reescribirlo |
| *Noise schedule* = "calendario de ruido"; *sampler* de la difusion = "procedimiento de muestreo" (ya decidido en capitulo2-r00) | Termino nuevo; "muestreador" sigue reservado al de colocacion |
| Siglas RMSE, PSNR, TOST, IC, DDPM, DDIM no se usan en el cap. 1: se escribe el nombre completo ("raiz del error cuadratico medio", "dos pruebas unilaterales de equivalencia", "intervalo de confianza") | Sus definiciones estan en los caps. 2 y 3; usarlas antes obligaria a mover esas definiciones (decision de capitulo2-r04) |
| 2.5D = modelo que opera sobre cortes axiales y recibe cortes contiguos como contexto, sin ser 3D completo; el numero de cortes va con `\GAPDEC` | La introduccion remite aqui la definicion; el numero solo consta en un borrador |
| Generalizaciones sobre "las fuentes revisadas" se sustituyen por los autores concretos cuando la afirmacion solo consta en sus fichas (Beer-Lambert, retroproyeccion filtrada) | PAT-87, PAT-64 |
| Autor de `selles2024marreview` escrito "Selles et al." (como en `refs.bib` y en el cap. 2); el cap. 3 escribe "Sellés" | Inconsistencia a resolver en el cap. 3 por la autora o en su siguiente ronda |

## Observaciones para la autora (no son cambios de este capitulo)

- La introduccion remite a este capitulo la definicion de 2.5D (`introduccion.tex`:41); ya existe en
  §1.4 y podria llevar `\ref{sec:mt-difusion}`.
- El corredor que mide el cap. 3 se llama "transsacro" en `tesis/main.tex` (*maximum transsacral
  corridor diameter*), mientras el implante es un tornillo iliosacro. Este capitulo define ambos tipos y
  no afirma cual mide el cap. 3; conviene revisarlo en la siguiente ronda del cap. 3 (posible E-T1).
- Evaluacion de impacto (regla 13 raiz): la redaccion no cambio alcance ni supuestos; los tres `\GAPLIT`
  son huecos de autocontencion del marco teorico, ya registrados en MAPA y `_candidatos.md`. La
  observacion transsacro/iliosacro podria merecer una entrada en `docs/04-implicancias.md`; no se
  registra aqui porque ese archivo esta fuera de la lista editable del redactor.
