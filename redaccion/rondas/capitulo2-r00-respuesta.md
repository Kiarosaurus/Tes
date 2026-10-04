# capitulo2 — r00 (redaccion inicial) — respuesta del redactor

Modo: redactar. Archivo: `overleaf/secciones/capitulo2.tex` (estaba en esqueleto, 13 lineas). No hay
reportes de revision en esta etapa; se documenta lo redactado, la fuente de cada cifra, los GAP, las
decisiones de redaccion y los supuestos. Ningun PDF de `papers/` se abrio: todo sale de fichas.

## 1. Resumen de lo redactado

Cinco `\section`, en el orden del esqueleto. Dos titulos cambiaron (ver §5). Etiquetas nuevas:
`cap:estado-arte`, `sec:ea-lesiones`, `sec:ea-simulacion`, `sec:ea-colocacion`,
`sec:ea-representacion`, `sec:ea-brecha`, `tab:comparacion`.

| Seccion | Criterios | Contenido |
|---|---|---|
| Apertura (3 parrafos) | G-B5, G-B9, G-B6, G-T5 | Funcion del capitulo; mapa seccion -> objetivo; disciplina de busqueda con `\GAPDEC` |
| 2.1 Sintesis de lesiones mediante difusion | G-B5, G-B7, P-EA2 | Dos familias (inpainting acotado / corte completo); DiffTumor, Ramzan, LeFusion, LGESynthNet, DiffBoost, Konz; metodos no difusivos que tocan fuera de la mascara (Hu, Jin, Wu); RePaint; cierre por familia (PAT-64) |
| 2.2 Insercion y simulacion fisica | G-B5, G-B7, P-EA2 | Insercion sintetica como practica establecida; difusion ya usada para MAR; Peters (resultados y limites de validacion); colocacion aleatoria o por regla; XCIST como fundamento; Ren (proyeccion, datos de fabricante) |
| 2.3 Planificacion y colocacion | G-B5, G-B7, P-EA2 | Liu 2025; Zhang 2026 (solo resumen); Zwingmann 2009/2013/2010; Herman; Kaiser, McLaren, Ziran, Ramadanov; tres carencias frente a Obj 2 y 4 |
| 2.4 Representacion multiventana y extension | G-B5, G-B7, P-EA2 | Wang 2025 y Li 2024 (ventanas para quitar, no para generar); autoencoders (Rombach, Chen 2026, Guo); imagen frente a proyeccion (De Man, Lin, Li); extension cualitativa (De Man, Park, Glover, Selles 2023, Li) y en mm (Radzi, Cassanego); sin precedente de banda numerica |
| 2.5 Comparacion critica y brecha | G-B8, G-B10, P-EA3 | Tabla `tab:comparacion` (9 trabajos + fila propia); lectura por filas; brecha identica a la tension de la introduccion, con su `\GAPDEC`; aporte en tres elementos; lo que no se reclama; `\GAPDEC` de estrechamiento (#56) |

## 2. Fuente de cada cifra

Cifras propias: **una sola**, el ancho de "unos 12 mm" de `B_delta` (`tesis/main.tex`:79, *"($\sim$12mm)"*;
DEC 2026-09-19). El capitulo no da ningun resultado propio (los veredictos van al cap. 4).
Cifras ajenas: todas con `\cite` y ficha en `docs/literatura/<clave>.md`; la columna da la fila de la ficha.

| Cifra en el texto | Fuente (ficha) |
|---|---|
| Truncado `[-175, 250]` HU | `chen2024tumorsynthesis`: Apendice E.2, p. 21 |
| Dice higado 62.5 -> 66.5 %, media de cinco particiones, una de tres redes | `chen2024tumorsynthesis`: Tabla 4, p. 17 (U-Net; se cita el promedio 5-fold, no fold0) |
| Cuatro radiologos; cerca de la mitad de sinteticos tomada por real | `chen2024tumorsynthesis`: §4.1, pp. 5-6 |
| Dice 58.89 -> 63.53 (mejor configuracion) | `ramzan2026claim`: Tabla 2, p. 11 |
| SSIM de imagen completa 0.587; cicatriz < 1 % de la imagen | `jacob2026lgesynthnet`: Tabla 1, p. 7; Sec. 1, p. 2 |
| Dice 0.72 -> 0.77 con 300 sinteticas | `jacob2026lgesynthnet`: Tabla 2, p. 8 |
| Dice 78.46 -> 84.56; 94.42 -> 94.78; 62.92 -> 71.65 % | `zhang2025diffboost`: Tabla II, p. 3678 |
| `[0, 255]`; Dice 0.8980; 40 pacientes | `konz2024anatomicallycontrollable`: Sec. 3, p. 93; Tabla 1, p. 94; Sec. 2, p. 92 |
| Efecto de masa hasta 1.3 veces el radio | `hu2023`: Tabla 1, p. 7426 |
| Ventanas que no pasan de 600 HU (Hu 189, Jin 600, Wu 250/500) | `hu2023` §4; `jin2021freetumor` Sec. 4.2, p. 12; `wu2025freetumor` Tabla A19 |
| 256 x 256 | `lugmayr2022repaint`: Sec. 5.1, p. 11466 |
| 120 kVp, Poisson, sin dispersion ni volumen parcial, sinogramas reproyectados | `zhang2018` (fila de `_index.md`) |
| 100 mascaras de metal | `lin2019` (fila de `_index.md`) |
| 1090 volumenes; cinco energias; 3071 HU | `wang2019cochlear`: Intro, p. 2; Sec. 2.1, p. 3 |
| 31 % de equipos con difusion | `haneda2025aapm`: Sec. 3.1, p. 11 |
| 14 000 casos; 8 metricas; 29 escenarios; hasta 5 objetos | `peters2025hybrid`: 2.3, p. 4; 2.4, p. 4; 2.5 |
| < 2 % valor medio de TC; ruido < 10 %, hasta 13.3 % en una de cuatro configuraciones | `peters2025hybrid`: 3.1, p. 6; 2.2, p. 3 |
| Solape >= 50 % con region > 200 HU | `karageorgos2024ddpm`: Sec. II-A, p. 4 |
| Varillas Ti 20 mm y Fe 10 mm | `wu2022xcist`: Figura 11, p. 29 |
| > 3.0 cm; 274 de 14 000 | `haneda2025aapm`: Sec. 4, p. 16 |
| Varilla de Ti de 12.7 mm; dos casos de crioablacion | `ren2022metalinsertion`: Sec. 2.1.3; Sec. 2.5 |
| 14 casos; 2.56 mm y 3.31 grados; 86.7 %; tres cirujanos; 10.58 +- 3.84 frente a 4.36 +- 3.83 mm | `liu2025pipeline`: Sec. VI, p. 14; Abstract; IV-B, pp. 16-17; Tabla III, p. 38 |
| 17 segmentos | `ramzan2026claim`: Sec. 2.2, p. 5 |
| Grado 0 en 69 % y 40 %; p = 0.02; cuatro niveles | `zwingmann2009navigated`: Results, pp. 1836-1837; M&M, p. 1835 |
| 2.6 % (1832 tornillos); 0.1 % (262 tornillos); cero eventos de la cohorte 2009 | `zwingmann2013`: Fig. 2, p. 1261; Discusion, p. 1264 |
| 63 y 131 tornillos; 81/11/3/5 %; 42/22/21/13 % + 2 % en grado 4 | `zwingmann2010percutaneous`: Resumen, p. 1501; Tabla 1, p. 1503 |
| 36.5 % S1, 14.8 % S2, p = 0.035; ningun tornillo integramente fuera | `herman2016` (fila de `_index.md`; `tesis/main.tex`:52) |
| 433 TC; 1.53 +- 0.57 y 1.02 +- 0.33 grados; tornillo de 7 mm; 150 mm | `mclaren2021corridor`: M&M, PDF pp. 2-3; Results, PDF p. 4 |
| Diecisiete pelvis; 7 a 25 %; hasta 140 % | `ziran2007fluoroscopic` (`tesis/main.tex`:52; mismo texto que `capitulo3` l. 79) |
| 2500 HU | `wang2025adaptiveweighting` Sec. V-A-2, p. 2413; `li2024` Sec. IV-E, p. 1878 |
| Ventanas `[-1000, 2000]`, `[-320, 480]`, `[-160, 240]` HU | `wang2025adaptiveweighting`: Sec. V-A-1, p. 2412 |
| 26.76 dB frente a 32.67 dB en la ventana estrecha | `wang2025adaptiveweighting`: Sec. V-B, p. 2414 |
| Cinco medicos | `wang2025adaptiveweighting`: Sec. V-C-3, p. 2415 |
| Entrada `[-1000, 2000]` HU; +0.64 dB en el metal mas grande | `li2024`: Sec. III-D, p. 1870; Sec. IV-B.4, p. 1873 (delta enunciado en el texto del articulo) |
| `[-1000, 1000]` HU | `chen2026foundationvae` (fila de `_index.md`; `tesis/main.tex`:77) |
| 31.45 dB frente a 33.51 dB | `lin2019`: Tabla 1, p. 10509 |
| 25 pacientes | `selles2023ai`: Sec. 2.3 |
| 2.0, 2.6, 1.6, 2.0 mm; tornillos de 3.5 a 4.0 mm; un tobillo | `radzi2014metalartifacts`: Resultados, p. 167; M&M, p. 165 |
| 3.1 a 4.2 mm | `cassanego2026evolution`: Tabla 3, p. 7 |
| Sensibilidad 100 %; Dice 82.92 %; 2500 HU | `xie2024implantsegmentation`: Tabla 2, p. 11 (fila de `_index.md`) |

No se calculo ninguna cifra: no hay restas, factores ni porcentajes derivados.

## 3. GAP abiertos en esta etapa

| Tipo | Seccion | Texto de la marca | Origen |
|---|---|---|---|
| `\GAPDEC` | Apertura | protocolo de busqueda de la revision: bases consultadas, cadenas de busqueda, fechas de corte y criterios de inclusion y exclusion, que no constan en el registro del proyecto | G-B6; nuevo |
| `\GAPDEC` | 2.1 | descripcion y atribucion del procedimiento de muestreo de la difusion del sintetizador frente a los de Lugmayr et al. y Zhang et al., pendiente en el registro del proyecto | #106, #117 (ABIERTAS); nuevo |
| `\GAPDEC` | 2.3 | si la distribucion de Zwingmann et al. de 2010 se mantiene fuera de la referencia clinica o entra como analisis de sensibilidad, y con que tratamiento del grado 4 no definido | #113 (ABIERTA); nuevo |
| `\GAPLIT` | 2.4 | fuente primaria del marco multiventana de MAR, que Wang et al. y Li et al. citan y de la que el repositorio no tiene ficha | #24; ya PENDIENTE en `_candidatos.md` (no se duplico la fila) |
| `\GAPDATO` | 2.4 | cifras de la ablacion de Li et al., leidas de una tabla poco nitida y pendientes de verificar contra el articulo antes de citarlas | ficha `li2024.md` (advertencia de transcripcion); nuevo |
| `\GAPDATO` | 2.5 | el sintetizador no ha generado todavia ninguna muestra sintetica, asi que no existe resultado del Objetivo 3 | #116; replica del de `capitulo3` e `introduccion` |
| `\GAPDEC` | 2.5 | por que hace falta un sintetizador aprendido si la simulacion fisica puede ejecutarse sobre las poses del muestreador; la misma pregunta queda abierta en la justificacion de la introduccion | #128.1; replica del de `introduccion` (G-B10) |
| `\GAPDEC` | 2.5 | si el reclamo de novedad del sintetizador se reformula como esa combinacion, propuesta en el registro del proyecto tras las lecturas de Jin et al., Wu et al. y Konz et al., o se mantiene el enunciado de tres elementos | #56, ajuste del 2026-09-21 "no aplicado"; nuevo |

Totales del lint: GAP lit = 1, dato = 2, dec = 5. Ninguno cerrado.

## 4. Decisiones de redaccion

1. Metodos con nombre propio en mayusculas sin expansion en la ficha (CLAIM, SMILE, NMAR, EMIDEC) **no se
   nombran**: se citan por autores. Los de caja mixta si se nombran una vez, junto al autor: DiffTumor,
   DiffBoost, LGESynthNet, LeFusion (E-T4; misma regla que NMAR en capitulo3-r00).
2. Homonimos: "Zhang et al." (DiffBoost, LeFusion, tornillo pedicular), "Wang et al." (implante coclear, MAR
   multiventana), "Chen et al." (DiffTumor, autoencoders de video), "Zwingmann et al." (2009, 2010, 2013) van
   siempre con su `\cite` y, al cambiar de seccion, con el nombre del metodo o un rasgo que los separe (PAT-14).
3. *Scoring benchmark* de Peters et al. = "conjunto de evaluacion"; "referencia" sigue reservada a la
   referencia clinica.
4. *Downstream* = "segmentacion posterior" / "tarea posterior"; la metrica, "coeficiente de Dice" la primera
   vez y "Dice" despues (la sigla DSC no se usa fuera de la introduccion).
5. "Muestreador" solo para el muestreador de colocacion; el *sampler* de la difusion = "muestreo de la
   difusion" / "procedimiento de muestreo" (PAT-14, por #117).
6. MRI = "resonancia magnetica (RM)"; CBCT = "TC de haz conico", sin sigla; PSNR = "relacion senal-ruido de
   pico (PSNR, *peak signal-to-noise ratio*)", definida en 2.4.
7. *Cupping* se deja en ingles y en cursiva, sin traduccion, porque ni el glosario ni las fichas la dan.
8. Preprints se senalan como "prepublicacion" (`wu2025freetumor`, `chen2026foundationvae`) (P-EA1).
9. Fuente con "Profundidad: solo abstract" (`zhang2026pediclescrew`): se dice en el texto que solo se dispuso
   del resumen, se describe la tarea "segun ese resumen" y no se da ninguna cifra.
10. Estado del arte = resultados de los autores con su condicion (en fantoma, en su mejor configuracion, con
    una de tres redes), sin calcular diferencias.
11. La brecha se enuncia con las mismas palabras que la tension de la introduccion (G-B10) y lleva el mismo
    `\GAPDEC` (decision introduccion-r02 sobre GAP replicados).
12. Un ajuste registrado como "no aplicado" en una implicancia se presenta como formulacion posible
    ("seria ...") seguida de `\GAPDEC`; los hechos de las fichas que lo motivan si entran como hechos.

## 5. Cambios de titulos

- "Simulacion fisica de artefactos metalicos" -> "Insercion y simulacion fisica de artefactos metalicos": la
  seccion cubre tambien la insercion analitica y en proyeccion (Zhang y Yu, Wang 2019, Ren), que no es el
  simulador.
- "Representacion multiventana en reduccion de artefactos" -> "Representacion multiventana y extension
  espacial del artefacto": la seccion sostiene tambien `B_delta` y el supuesto de dominio de imagen.

## 6. Supuestos y cosas que conviene revisar

1. **Wang 2025, 26.76 frente a 32.67 dB.** La ficha dice "DICDNet-MW transferido a SW" frente a "MWDICDNet en
   SW". Se redacto como "una red que no se entreno en la ventana estrecha" frente a "la version multiventana
   de esa red". No se afirma en que ventana se entreno.
2. **"La lista de fuentes la definio la autora"** sale de la regla 9 del `CLAUDE.md` raiz, no de un registro
   de busqueda.
3. **Xie et al.**: "cobertura en exceso" se escribio como lectura de este trabajo (la ficha dice que el termino
   no aparece en el articulo); la introduccion lo afirma como reporte de los autores y quedaria mas fuerte
   que la ficha.
4. **Herman et al.**: "este trabajo lee" el dato de ningun tornillo fuera del hueso como cota del muestreador
   (`tesis/main.tex`:52 lo escribe asi).
5. **`ramzan2026claim`**: la ficha se hizo sobre el preprint de arXiv; `refs.bib` lo da como actas de 2026.
   No se senalo como prepublicacion.
6. **Tabla**: `array` no esta cargado en la plantilla, asi que las celdas van justificadas (no se toco el
   preambulo). Cabe en una pagina (p. 32 del PDF de `redaccion/.build/`).
7. `capitulo1.tex` sigue en esqueleto: RM, PSNR y los nombres de metodos se definen aqui por ser su primera
   aparicion en el orden del documento. "U-Net" y "DDPM" se evitaron porque el marco teorico aun no los define.
8. No se usaron `varma2025medvae` (sin entrada en `refs.bib`), `macháček2023` (clave con tilde) ni
   `dorjsembe2024`, `singhrao2024fiducial`, `chen2015lesion`, `ferrero2017technicalnote` (no hacian falta).

## 7. Lint

`python scripts/lint_redaccion.py capitulo2 --compilar`: **PASA**, alta = 0, media = 0, baja = 0;
GAP lit = 1, dato = 2, dec = 5. Compila: 85 paginas, sin citas ni referencias indefinidas.

## Decisiones de redaccion

Las doce del §4.
