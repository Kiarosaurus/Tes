# Auditoria de trazabilidad — capitulo2 — r06

Seccion: `overleaf/secciones/capitulo2.tex` (Cap. II, 139 lineas). Lint r06: PASA 0/0/0, GAP lit=1 dato=2 dec=9
(recontados: dec en l.12, 28, 64, 74, 76 x2, 86, 130, 136; dato en l.92 y 102; lit en l.82). Respuesta previa:
`capitulo2-r05-respuesta.md`. T02 (unidad de los RMSE) esta ESCALADO a la autora y no lo re-reporto: no tengo
argumento nuevo (las fichas siguen sin unidad; DEC 2026-09-15 (2) y `capitulo3.tex`:67, :176 siguen en HU). Tampoco
re-reporto T03 (depende de T02) ni T07 (pendiente 1, fuera de la seccion). Las 45 claves `\cite` existen en
`overleaf/referencias.bib` (45/45; `gardner2010safezones` entra en r05). No abri ningun PDF.

Revise en especial lo que cambio en r05:
- **Wang 2025, condicion simulada (l.82 y celda l.121):** coincide con `wang2025adaptiveweighting.md`:276-277
  (DICDNet-MW transferido a SW 26.76/0.9501; MWDICDNet en SW 32.67/0.9803; Sec. V-B) y :205-208 (test sintetico de
  2000 pares). CLINIC-metal solo con evaluacion visual (:255-258). "Una red no entrenada en la ventana estrecha" =
  DICDNet-MW, correcto. La celda ("sin ella") y el cuerpo dicen lo mismo. PAT-31 y PAT-92 no reinciden.
- **Lin, condicion simulada (l.92):** `lin2019.md`:192-194, 276 ("simulated metal artifacts on real patient CTs");
  31.45 / 33.51 dB de Tabla 1 (:43-44); salvedad de X_LI (:145-148). Correcto.
- **RMSE de 20.2 atribuido a Karageorgos (l.90):** `karageorgos2024ddpm.md`:44 (fila NMAR, Tabla I p. 28);
  `peters2025hybrid.md`:49, 158 (NMAR = 2). La oracion ya tiene sujeto Karageorgos et al. y la cita de Peters
  queda solo para la calibracion. T01 de r05 corregido; PAT-90 no reincide. Nota: DEC 2026-09-15 (2)
  (`01-decisiones.md`:823) llama al 12.3 "difusion en imagen", y la ficha dice que el DDPM de Karageorgos
  opera en el sinograma (:12, :94, :205). El cap. 2 no repite el error ("su modelo de difusion", l.90, y l.36
  "en el dominio del sinograma"). Es una discrepancia interna de la DEC, que conviene avisar a la autora; no es
  hallazgo del texto.
- **Parrafo de Gardner (l.70):** 222 frente a 346 mm2, 50 TC de adultos, lado no lesionado y estudio previo sin
  diferencia coinciden con `gardner2010safezones.md`:72, 308, 323, 382. La consecuencia (medir el corredor en cada
  volumen, sin estratificar) coincide con DEC 2026-09-08 (2) (`01-decisiones.md`:319-332). Hay una baja en la
  oracion de apertura (T02).
- **Marco de Kaiser (l.68):** 104 TC no lesionadas, area, longitud y angulos coinciden con `kaiser2014dysmorphism.md`
  §C, §D y §H; la distribucion propia coincide con DEC (`01-decisiones.md`:211-217). Precision baja (T04).
- **Parrafos partidos en 2.4 (l.84/86, l.90/94):** la oracion movida al cierre de l.94 ("La banda trunca por diseno
  los efectos ... lejos del metal") tiene respaldo en `glover1980nonlinear.md`:35 ("una banda local trunca por diseno
  un efecto potencialmente no local"), `li2024.md`:18, 82 (artefacto "global") y `selles2023ai.md`:29 (lado
  contralateral). La medicion de ida y vuelta sin autoencoder "aunque no entra en su criterio de fallo" coincide con
  `experiments/objetivo1/p1_compuerta.md`:5 (solo `vae regla` decide) y :31-38 (columnas de identidad).
- **"Efectos" en lugar de "rayas" (l.94):** el texto es correcto. Pero el motivo que da la respuesta r05 (ES-04),
  que Selles et al. "no describen rayas", contradice la ficha: `selles2023ai.md`:29 copia "dark and bright streaks
  throughout the images". No cambia nada en el texto. Lo anoto para que esa razon no se reutilice en otra seccion.

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | baja | E-R6, G-T4 | l.94 | "muestran rayas que irradian desde el metal en las direcciones de mayor atenuacion" | `deman1999.md`:196 ("dark streaks in the directions of highest attenuation", Sec. III-B, endurecimiento del haz) y :205 ("streaks ... radiating from the metals", Sec. III-D, efecto de borde exponencial) | La oracion junta en un solo fenomeno dos observaciones que la ficha separa por mecanismo. Las rayas oscuras en la direccion de mayor atenuacion son del endurecimiento del haz. Las rayas que irradian desde el metal son de otro mecanismo (Sec. III-D). Ninguna frase de la ficha dice "irradian en las direcciones de mayor atenuacion" | "De Man et al. muestran rayas oscuras en las direcciones de mayor atenuacion y rayas que irradian desde el metal, en una simulacion bidimensional ..." |
| T02 | baja | G-T4, E-R6 (PAT-85) | l.70, primera oracion | "Las mismas mediciones muestran ... esa variacion no se agrupa de forma consistente por fenotipo" | `gardner2010safezones.md`:72, 346-347 (S1: 222 frente a 346 mm2, P < 0.001), :382 (Carlson, citado por Gardner, sin diferencia); `kaiser2014dysmorphism.md` §F (tres fenotipos, 41 %); DEC 2026-09-08 (2) (`01-decisiones.md`:329-332) | Patron PAT-85 reincide en forma leve. (a) "Las mismas mediciones" apunta a Kaiser y McLaren, del parrafo anterior, pero las cifras que siguen son de Gardner y Ziran. (b) Las mediciones de Gardner muestran una diferencia significativa entre fenotipos. La inconsistencia aparece solo al compararlas con Carlson, a quien Gardner cita, y es la lectura de la DEC (2). La oracion se la atribuye a "las mediciones". El cierre del parrafo ya lo dice bien ("la inconsistencia entre estudios") | "Las mediciones publicadas muestran que el corredor varia entre pelvis, y el efecto del fenotipo sobre su tamano no es consistente entre estudios." |
| T03 | baja | G-T4 (ficha insuficiente) | l.94 | "Selles et al. miden diferencias de HU en hueso y musculo, cerca ... y contralateral" | `selles2023ai.md`:20-26 (solo 461 pacientes, 35 mascaras, 25 pacientes, seis ROI, con pagina); :29 (hueso trabecular, gluteo medio e iliaco, cerca y contralateral: prosa sin frase ni pagina) | La ficha no tiene tabla de "Evidencia textual". La afirmacion sobre las regiones y el lado contralateral solo esta en prosa de la ficha, sin frase original ni pagina. La l.12 del capitulo afirma que cada ficha copia la frase y la pagina de lo que se cita. Aqui no se cita cifra (salvo 25, que si tiene pagina), asi que no hay error de fondo | Relectura de `selles2023ai` con `lector-papers` para completar la Evidencia textual (ROI, lado contralateral, frase de "streaks throughout the images" con pagina). Sin cambio en el texto mientras tanto |
| T04 | baja | E-R6 | l.68 | "reformatean 104 TC ... perpendicularmente al platillo superior de S1 y miden en ellas el area" | `kaiser2014dysmorphism.md`:200-202 (reformateo "along the axis of the sacrum"; el eje es perpendicular al platillo; despues, "Reformats ... perpendicular to the ... osseous corridors"); :226 (area sobre "contiguous slices perpendicular" al corredor) | Hay dos reformateos. El area se mide en cortes perpendiculares al corredor, no en el reformateo definido por el platillo de S1. "Miden en ellas" atribuye la medicion del area al primer reformateo. DEC (`01-decisiones.md`:211-212) da la formula corta y no sostiene el "en ellas" | "Kaiser et al. reformatean 104 TC de pelvis no lesionadas segun el eje del sacro, perpendicular al platillo superior de S1, y sobre cortes perpendiculares al corredor miden el area transversal, la longitud y los angulos axial y coronal." |

## Inventario

| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l.8 | Comparacion por objetivos; tabla con fila propia; brecha | `redaccion/MAPA.md`:18 | si |
| l.10 | Orden real de las secciones y relacion con Obj 1-4 y $B_\delta$ | estructura del capitulo (l.14, 32, 50, 78) | si (PAT-71 no reincide) |
| l.12 | Sin busqueda sistematica; lista de la autora; fichas con frase y pagina; candidatos; busquedas dirigidas fechadas; una sola fuente solo resumen | `CLAUDE.md` raiz reglas 2, 15, 16; `_candidatos.md`; `zhang2026pediclescrew.md` (unica ficha "solo abstract" citada; `wang2025adaptiveweighting` la tiene retirada, :11-14) | si (T03 matiza "frase y pagina") |
| l.12 | \GAPDEC protocolo de busqueda | `MAPA.md`:68 | si (justificado) |
| l.16 | Dos familias; rayas que irradian desde el metal | fichas chen2024, ramzan, jacob, lefusion, diffboost, konz; `deman1999.md`:205 | si |
| l.18 | DiffTumor: latente, mascara + region sana; [-175, 250] HU; Dice 62.5 -> 66.5 % con una de tres redes, cinco particiones; cuatro radiologos, cerca de la mitad | `chen2024tumorsynthesis.md` §3.2 p. 4, Ap. E.2 p. 21, Tabla 4 p. 17, §4.1 | si |
| l.20 | Ramzan: RM, dominio de imagen, perdida en mascara, fondo recompuesto; desde LeFusion; Dice 58.89 -> 63.53; fondo cualitativo | `ramzan2026claim.md`; `zhang2025lefusion.md` | si |
| l.22 | LGESynthNet: latente + ControlNet; bordes + imagen enmascarada; Dice 0.72 -> 0.77 con 300; SSIM 0.587; cicatriz < 1 %; lectura propia | `jacob2026lgesynthnet.md` Sec. 3.1, Tablas 1-2 | si |
| l.24 | DiffBoost: 78.46 -> 84.56, 94.42 -> 94.78, 62.92 -> 71.65 %; parches al azar. Konz: [0, 255], Dice 0.8980, 40 pacientes | `zhang2025diffboost.md` Tabla II p. 3678; `konz2024anatomicallycontrollable.md` | si |
| l.26 | Hu 1.3 r; Jin GAN y region de borde; Wu 2025 prepublicacion conserva el exterior | `hu2023.md` Tabla 1; `jin2021freetumor.md` 3.4.1; `wu2025freetumor.md` Ec. 1 | si |
| l.28 | RePaint sin reentrenar, 256 x 256, sin TC ni metal; \GAPDEC muestreo | `lugmayr2022repaint.md` 5.1; #106/#117 ABIERTAS; `MAPA.md`:69 | si |
| l.30 | Cinco con segmentacion, dos con similitud, uno con radiologos; negacion partida por familia | fichas respectivas | si (PAT-64 no reincide) |
| l.34 | Zhang y Yu 15 formas, 120 kVp, Poisson, "no menciona"; Lin 100 formas + volumen parcial; Wang 2019 tubular, 1090, cinco energias; Karageorgos CatSim/XCIST | `zhang2018.md`; `lin2019.md`:53, 281; `wang2019cochlear.md`; `karageorgos2024ddpm.md`:96, 104 | si |
| l.36 | Haneda 31 %; Karageorgos sinograma, traza, reinsercion por umbral; SSIM 0.964 simulado; 13 de 28 en cuatro TC clinicas | `haneda2025aapm.md` 3.1 p. 11; `karageorgos2024ddpm.md`:39, 48, 117-118, 141 | si |
| l.38 | Yun: proyeccion + LDM; CLINIC-metal por inferencia; metal por umbral; 0.82 HU frente a 3.18-6.30 HU de cuatro metodos | `yun2026simulationdriven.md`:21, 41, 110 (Tabla 4 p. 11) | si |
| l.40 | Peters: CatSim calibrado; 14 000; fractales; ocho metricas; 29 escenarios; < 2 %; < 10 %; 13.3 % en un experimento | `peters2025hybrid.md`:20, 43, 47, 140, 195 | si |
| l.42 | Validacion no cubre paso hibrido, geometria generica, 3D | `peters2025hybrid.md`:101, 211 | si |
| l.44 | Peters al azar / *meaningful locations*; Karageorgos >= 50 % en > 200 HU; Wang 2019 centro; Wang 2025 a mano en cortes dentales | `peters2025hybrid.md`:143, 208, 217; `karageorgos2024ddpm.md`:108; `wang2025adaptiveweighting.md`:209-210, 224 | si (PAT-66 no reincide) |
| l.46 | Wu 2022: primer orden, Ti 20 mm, Fe 10 mm; Haneda > 3.0 cm, 274 de 14 000 | `wu2022xcist.md`; `haneda2025aapm.md` | si |
| l.48 | Ren: sondas, varilla Ti 12.7 mm, dos crioablaciones, datos del fabricante, modal | `ren2022metalinsertion.md` | si |
| l.52 | Orden de 2.3 | l.54-76 | si |
| l.54 | Liu: 14 casos; plan unico; 2.56 mm y 3.31 grados; 86.7 % en 12 casos, tres cirujanos; 10.58 ± 3.84 frente a 4.36 ± 3.83 mm; sin iliosacros; no sacro | `liu2025pipeline.md`:25-28, 85, 90, 96, 98, 112, 116-117 | si |
| l.56 | Zhang 2026 solo resumen; sin cifras | `zhang2026pediclescrew.md` | si |
| l.58 | Ramzan 17 segmentos; Chen elipsoides; Jacob elipsoide al azar | fichas | si |
| l.60 | Zwingmann 2009: cuatro niveles; 69 % y 40 %; p = 0.02 | `zwingmann2009navigated.md` | si |
| l.62 | Metaanalisis 2.6 % (1832), 0.1 % (262); cero de 2009; criterio de revision | `zwingmann2013.md` | si |
| l.64 | Zwingmann 2010: 63 y 131; 81/11/3/5; 42/22/21/13 + 2 %; \GAPDEC | `zwingmann2010percutaneous.md`; #113 ABIERTA; `MAPA.md`:70 | si |
| l.66 | Herman 36.5 % y 14.8 %, p = 0.035; distribucion ordinal clinica bajo S1; S1 asumido | `herman2016.md`; `capitulo3.tex`:164 | si |
| l.68 | Kaiser 104 TC no lesionadas, reformateo, area, longitud, angulos | `kaiser2014dysmorphism.md`:81, 200-206, 226-227 | parcial (T04) |
| l.68 | McLaren 433 / 352; Ramadanov y Zabler cualitativo; marco y criterio en `sec:corredor`; distribucion propia | `mclaren2021corridor.md`; `ramadanov2025safezone.md`; DEC `01-decisiones.md`:211-217 | si |
| l.70 | Gardner: 50 TC de adultos, lado no lesionado, S1 222 frente a 346 mm2; estudio previo sin diferencia | `gardner2010safezones.md`:72, 308, 323, 347, 382 | si |
| l.70 | Ziran: 17 pelvis cadavericas; 7-25 %; 97-140 % en ala superior de S1, plano frontal | `ziran2007fluoroscopic.md`:211, 315, 320 | si |
| l.70 | Consecuencia: no pose canonica; medir en cada volumen sin estratificar | DEC 2026-09-08 (2) `01-decisiones.md`:319-332; `capitulo3.tex`:168 | si (apertura: T02) |
| l.72 | Cuatro carencias frente al Obj 2 | l.44, 54, 58, 60-64 | si |
| l.74 | Zwingmann radiologo; Smith cuatro cadaveres, escala heredada + angular; Herman binaria; Liu margen; \GAPDEC angular | `smith2006iliosacral.md`; #11 ABIERTA; `MAPA.md`:41 | si |
| l.76 | Arand 50 TC *post mortem*; ala sacra baja frente a cuerpo de S1; sin HU; \GAPDEC densidad; tres de ocho metricas; \GAPDEC inversion | `arand2019pelvicring.md` p. 381; #50; #16/#17 ABIERTAS; `MAPA.md`:42 | si |
| l.80 | Saturacion <= 600 HU (Chen, Hu, Jin, Wu 2025); umbral 2500 HU (Wang 2025, Li) | fichas; `wang2025adaptiveweighting.md`:186; `li2024.md`:46 | si (PAT-87 no reincide) |
| l.82 | Wang 2025: tres ventanas, cascada, peso aprendido | `wang2025adaptiveweighting.md`:43-56, 165-175 | si |
| l.82 | \GAPLIT fuente primaria del esquema multiventana | `wang2025adaptiveweighting.md`:175; `li2024.md`:87; sin ficha ni PDF de Niu y Wang; `MAPA.md`:71 | si (justificado) |
| l.82 | 14 volumenes CLINIC-metal por inferencia, sin imagen limpia, cinco medicos, 30 imagenes | `wang2025adaptiveweighting.md`:221, 255-258; `02-datos.md`:157 (14 anotados de 75) | si |
| l.82 | Prueba simulada: 26.76 dB / 0.9501 frente a 32.67 dB / 0.9803; lectura propia | `wang2025adaptiveweighting.md`:205-208, 276-277 | si |
| l.84 | Li: ventanas en perdida y evaluacion; entrada [-1000, 2000] HU; +0.64 dB en artefactos simulados, metal mas grande; techo 2000 < 2500 HU | `li2024.md`:10, 38, 45, 46, 58, 102-104 | si |
| l.86 | No se reclama el esquema; ida y vuelta sin autoencoder medida, fuera del criterio de fallo; \GAPDEC codificacion y precision | `p1_compuerta.md`:5, 31-38; `e6c_techo_lw.md`; `MAPA.md` | si (T07 de r05 sigue fuera de la seccion) |
| l.88 | Rombach (compresion, cuello de botella); Chen 2026 prepublicacion, sin unidades, [-1000, 1000] HU; Guo sin rango; negativo acotado | fichas respectivas | si (PAT-64 no reincide) |
| l.90 | Sin umbral publicado (acotado a las fuentes revisadas) | DEC 2026-09-15 (2) `01-decisiones.md`:818-820 | si |
| l.90 | Karageorgos RMSE 12.3 (difusion), datos simulados | `karageorgos2024ddpm.md`:41 (Tabla I p. 28) | si (unidad: T02 de r05 ESCALADO) |
| l.90 | Karageorgos RMSE 20.2 del algoritmo con que Peters calibra | `karageorgos2024ddpm.md`:44; `peters2025hybrid.md`:49, 158 | si (PAT-90 corregido) |
| l.90 | Yun RMSE 12.74, metodo completo, datos simulados | `yun2026simulationdriven.md`:97, 182, 187 | si |
| l.90 | Orden de magnitud, sin convertir RMSE en ida y vuelta | DEC 2026-09-15 (2) `01-decisiones.md`:827-829 | si |
| l.92 | De Man en proyeccion; dos dominios superior; Lin 31.45 frente a 33.51 dB simulados; X_LI; problema mal planteado | `deman1999.md`:21, 138; `lin2019.md`:43-44, 145-148, 264, 276 | si |
| l.92 | Li rama de solo imagen desde la reconstruccion con artefacto; \GAPDATO cifras de ablacion | `li2024.md`:51, 55, 97, 143; `MAPA.md`:72 | si (justificado: la fila c no esta entre las validadas por los deltas) |
| l.92 | Negativo sobre sintesis solo en imagen; "se asume"; comparacion podria contradecir | `lin2019.md`:319; `li2024.md`:198; #61 ABIERTA (como supuesto) | si (PAT-85 no reincide aqui) |
| l.94 | De Man: rayas, direcciones de mayor atenuacion, 2D, hierro y amalgama | `deman1999.md`:42, 166, 186, 196, 205 | parcial (T01) |
| l.94 | Park: *cupping* dentro y rayas fuera | `park2015ct.md`:9, 27 | si |
| l.94 | Glover y Pelc: volumen parcial no lineal, rayas que conectan estructuras, haz monocromatico, hueso no metal | `glover1980nonlinear.md`:10, 14, 35 | si |
| l.94 | Selles: 25 pacientes, implantes de fusion sacroiliaca, hueso y musculo, cerca y contralateral, sin distancia | `selles2023ai.md`:9, 12, 25, 29, 31 | parcial (T03, ficha sin Evidencia textual) |
| l.94 | Li: artefacto en toda la imagen, sin medirlo | `li2024.md`:18, 82, 98 | si |
| l.94 | La banda trunca por diseno los efectos lejanos; remision a amenazas | `glover1980nonlinear.md`:35; `capitulo3.tex`:176 | si |
| l.96 | Radzi 2.0/2.6/1.6/2.0 mm desde el eje, un tobillo, 3.5-4.0 mm; Cassanego 3.1-4.2 mm, seis miembros caninos; ~12 mm como convencion | `radzi2014metalartifacts.md`; `cassanego2026evolution.md`; TM:79; `capitulo3.tex`:176 | si |
| l.98 | Sin precedente numerico; Hu y Jin; Karageorgos pelvis con dos marcadores de oro virtuales; 7.57; 11.45 (1.4 del area); 54.82 (0.7); lectura propia; no da ancho | `karageorgos2024ddpm.md`:54, 56, 58, 171, 173; `capitulo3.tex`:176 | si (sin unidad: T02 de r05 ESCALADO; PAT-84 no reincide) |
| l.102 | Muestreador y SAP ejecutados; \GAPDATO sin muestras sinteticas | `capitulo3.tex`:38; `p1_compuerta.md`:27; DEC 2026-09-19 (`01-decisiones.md`:1136); `MAPA.md`:30 | si (justificado) |
| l.113-121 | Nueve filas: cifras y condicion | cuerpo y fichas (arriba) | si (PAT-67 no reincide) |
| l.123 | Fila propia: supuesto, convencion, poses preinscritas, $G$, SAP ejecutado, *streak amplitude* contra copia y pegado, protocolo segun el plazo | `capitulo3.tex`:125-134, 172, 217, 223; l.130 | si |
| l.128 | Lectura por columnas; Peters en fantoma y 2D; esquema multiventana para quitar | l.40-44, 82-84 | si |
| l.130 | Brecha con las palabras de la introduccion; comparaciones previstas; \GAPDEC sintetizador aprendido | `introduccion.tex`:54; #128.1; `MAPA.md`:66; `capitulo3.tex`:217, 223 | si |
| l.132 | Tres elementos; perturbacion del eje segun distribucion preinscrita; sin ajuste; dos razones de "ningun objetivo aisla" | `capitulo3.tex`:125-134; `introduccion.tex`:58, 60 | si (T08 de r05 corregido) |
| l.134 | Wang 2019 tubular; Zhang y Yu, Karageorgos, Peters; umbral automatico (Yun, Wang 2025, Li); Xie 2500 HU, sensibilidad 100 %, Dice 82.92 %; salvedad de mascaras umbralizadas | fichas; `xie2024implantsegmentation.md`; `capitulo3.tex`:178, 182 | si (PAT-69 y PAT-87 no reinciden) |
| l.136 | Piezas publicadas; formulacion posible; \GAPDEC novedad | #56 ABIERTA (ajuste no aplicado); `MAPA.md`:73 | si |
| l.138 | Supuesto y convencion; evaluacion por coherencia, no por segmentacion | #61; `docs/00-tesis.md` Fuera de alcance 1 | si |
| global | 45 claves `\cite` | `overleaf/referencias.bib` (45/45) | si |
| global | Apellido = primer autor; dos autores sin "et al." (Zhang y Yu, Ramadanov y Zabler, Glover y Pelc) | `.bib` | si |
| global | Cita como sujeto gramatical (E-F3) | texto completo | si: ninguna |
| global | Contenido retirado (Dice/HD95 como objetivo, latente/ControlNet como metodo vigente, "31-60%", BFC/ISC) | texto completo | si: no aparece; ControlNet y latente solo como trabajos ajenos |
| global | Fuentes de fabricante | ninguna | si |
| global | Prepublicaciones senaladas (`wu2025freetumor`, `chen2026foundationvae`) | l.26, l.88 | si |
| global | Implicancias ABIERTAS afirmadas como hecho (#11, #16/#17, #56, #61, #106/#117, #113, #128) | todas como GAP, supuesto o formulacion posible | si |
| global | Fichas "solo abstract" con cifras del cuerpo | `zhang2026pediclescrew` sin cifras | si |
| global | Patrones VIGENTES: PAT-14 (no: "escala" solo para Peters y Smith, "marco" solo Kaiser), PAT-31 (no), PAT-64 (no), PAT-66 (no), PAT-67 (no), PAT-69 (no), PAT-71 (no), PAT-76 (no), PAT-80 (no), PAT-82 (no), PAT-84 (no), PAT-85 (T02, leve), PAT-86 (no), PAT-87 (no), PAT-88 (T07 de r05, fuera de la seccion), PAT-89 (no), PAT-90 (no: corregido), PAT-91 (T02 de r05 escalado; sin argumento nuevo), PAT-92 (no), PAT-93 (no) | texto completo | ver hallazgos |

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Dos observaciones de una fuente, de mecanismos distintos, se funden en una sola oracion | E-R6, G-T4 | "rayas que irradian desde el metal en las direcciones de mayor atenuacion" | nuevo |
| Se atribuye a "las mediciones" una conclusion que solo sale de comparar estudios (lectura de DEC) | E-R6, E-P3 | "Las mismas mediciones muestran que ... no se agrupa de forma consistente por fenotipo" | PAT-85 (afin) |
| La respuesta del redactor justifica un cambio con un hecho que la ficha contradice | G-T4 | "Selles et al. no describen rayas" (ficha: "dark and bright streaks throughout") | nuevo |
