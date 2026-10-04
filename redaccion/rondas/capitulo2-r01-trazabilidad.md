# Auditoria de trazabilidad — capitulo2 — r01

Seccion: `overleaf/secciones/capitulo2.tex` (Cap. II, 114 lineas). Etapa previa: r00 (redaccion inicial,
sin revisores); no hay RECHAZADOS que respetar. Lint r01: PASA 0/0/0, GAP lit=1 dato=2 dec=5.
Fichas rastreadas: las 42 claves citadas. Todas existen en `overleaf/referencias.bib`. Ningun PDF abierto.

Nota sobre la respuesta r00 (§2): seis cifras declaran como fuente una fila de `_index.md` o `tesis/main.tex`
(`zhang2018`, `lin2019`, `herman2016`, `ziran2007fluoroscopic`, `chen2026foundationvae`,
`xie2024implantsegmentation`). Las seis tienen ficha propia en `docs/literatura/` y la ficha sostiene la cifra
(ver inventario); el hallazgo sobre `zhang2018` es de redaccion, no de fuente ausente.

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | G-T4, E-R6 (regla 4) | l.26 | "ese paso se usa en su prueba visual y no en el entrenamiento" | `hu2023.md`, Evidencia textual: filas "Pasos solo para Turing Test" y "Cuales son los cuatro pasos" | La ficha trae la frase de la Fig. 3 (*"Four steps, in light green, are only used for Visual Turing Test"*), pero para **cuales** son esos cuatro pasos dice "NO ENCONTRADO EN EL PDF en texto (solo codificado por color en la figura)", y en "Donde entra" pide verificarlo. La atribucion del efecto de masa a ese grupo sale de una lectura de colores, no de texto. La seccion "Restriccion" de la misma ficha lo afirma sin cita: ficha internamente inconsistente | Quitar la subordinada ("ese paso se usa en su prueba visual...") o dejarla como lectura de la figura: "segun el codigo de colores de su Fig. 3, ese paso se usaria solo en la prueba visual". Proponer relectura de la Fig. 3 de `hu2023` con `lector-papers` para cerrar la fila |
| T02 | media | E-R6 | l.34 | "su simulacion no incluye dispersion ni volumen parcial" / "Lin et al. reutilizan ese protocolo" | `zhang2018.md`, Evidencia: "Simulacion de scatter" y "Efecto de volumen parcial del metal" = NO ENCONTRADO EN EL PDF; `lin2019.md`: *"Metal partial volume effect is also considered"* y *"We adopt similar procedures as in [33]"* | La ficha registra que el PDF **no menciona** dispersion ni volumen parcial; el texto lo convierte en que la simulacion **no los incluye**. Ademas la oracion siguiente dice que Lin et al. "reutilizan ese protocolo", y Lin declara volumen parcial: el parrafo se contradice. `zhang2018.md` anota esa discrepancia ("discrepancia con `lin2019`, que si lo declara") | "su articulo declara simular el endurecimiento del haz y el ruido de Poisson, y no menciona dispersion ni volumen parcial". Para Lin: "adoptan un procedimiento similar, y declaran tambien el volumen parcial del metal" |
| T03 | media | G-T4, E-P3 (PAT-31) | l.38 | "el ruido menos del 10 %, salvo en una de las cuatro configuraciones, 13.3 %" | `peters2025hybrid.md`, Evidencia 3.1 p. 6 y Verificacion 2026-09-16 filas 4e-4f | Patron PAT-31 reincide. La fuente separa por **region**, no por configuracion: <10 % *"in regions without obvious metal artifacts"*; *"in regions with obvious metal artifacts ... up to 13.3% in Exp 4"*. El texto sustituye la condicion y sugiere que en tres configuraciones el ruido queda <10 % tambien en las regiones con artefacto, lo que la fuente no dice | "y el ruido menos del 10 % en las regiones sin artefacto evidente; en las regiones con artefacto la discrepancia fue mayor, de hasta 13.3 % en uno de los experimentos" |
| T04 | media | G-T4, E-P3 (PAT-31, PAT-65) | l.56 | "de 7 a 25 % en la mayoria de ellas y de hasta 140 % en el ala superior de S1" | `ziran2007fluoroscopic.md`, Variabilidad: "7%-25%" general; "Ala superior de S1 en plano frontal sacro, 97%-140%"; "Menor varianza: cortical superior del ala S1, 8%-9%"; `tesis/main.tex`:52 | Patrones PAT-31 y PAT-65 reinciden. Se pierde la condicion "orientacion ... en el plano frontal sacro": la misma superficie (cortical superior del ala de S1) tiene la **menor** variacion (8-9 %) en otra medida, asi que "hasta 140 % en el ala superior de S1" sin plano es engañoso. TM:52 trae la forma precisa ("for most surfaces ... for the orientation of the superior S1 ala in the sacral frontal plane, 97--140%"). "En la mayoria de ellas" tiene como antecedente gramatical "pelvis" y la fuente habla de superficies | "coeficientes de variacion de 7 a 25 % en la mayoria de las superficies medidas, que suben hasta 97-140 % en la orientacion del ala superior de S1 en el plano frontal sacro" |
| T05 | media | E-R6 (PAT-6) | l.52 | "porque, segun los propios autores, la mayoria ... solo llama malposicion a la revisada" | `zwingmann2013.md`, Evidencia: *"Most authors use the term 'malposition' only when a screw revision was performed."* (Discusion, p. 1264); Fig. 2: cohorte 2009 con 0/35 y 0/26 | Patron PAT-6 reincide. Los autores enuncian el criterio general; el enlace causal con el cero de la cohorte de 2009 ("porque") lo hace la ficha (l. 25-28), no el articulo. El texto se lo atribuye a los autores | "La cohorte de 2009 entra en ese agregado con cero malposiciones en sus dos series. Los autores advierten que la mayoria de los estudios solo llama malposicion a la que acabo en revision del tornillo, y este trabajo lee ese cero como efecto de ese criterio" |
| T06 | media | G-T4 | l.68 | "Una prepublicacion de otro grupo, Chen et al." | `chen2026foundationvae.md`; `overleaf/referencias.bib` (entradas `chen2026foundationvae` y `chen2024tumorsynthesis`); TM:77 (*"A concurrent preprint"*) | "De otro grupo" no tiene fuente. TM dice "concurrent", no "de otro grupo". En el `.bib`, `chen2026foundationvae` comparte primer autor (Chen, Qi), Yuille y Zhou con `chen2024tumorsynthesis`, citado en el mismo capitulo: si "otro" se lee frente al capitulo, es falso | "Una prepublicacion concurrente, de Chen et al. \cite{chen2026foundationvae}, reporta..." (sin afirmar pertenencia a grupo) |
| T07 | media | OC-3, G-T4 (decision §2 "GAP replicados") | l.110 | "geometria de implante rigida y parametrica ... en lugar de una mascara ... con umbral fijo" | `docs/04-implicancias.md` #128.4 (ABIERTA: "la geometria parametrica evita el umbral, pero el sintetizador se entrena con mascaras umbralizadas"); `introduccion.tex`:58; TM:79 | La introduccion enuncia este mismo aporte **con** la salvedad de #128.4 ("El entrenamiento del sintetizador si usa mascaras umbralizadas de metal real ... desplazamiento de dominio"). El capitulo 2 lo enuncia sin ella, como aporte limpio, y la tension sigue ABIERTA | Añadir tras la cifra de Xie: "El sintetizador, en cambio, se entrena con mascaras umbralizadas de metal real, y esa diferencia es un desplazamiento de dominio (Seccion~\ref{sec:sintetizador})", como en la introduccion |
| T08 | media | E-F3 | l.56 | "como la de Ramadanov et al.~\cite{ramadanov2025safezone}" | `overleaf/referencias.bib`: `author = {Ramadanov, Nikolai and Zabler, Simon}`; BITACORA §2 (2026-09-29): "Entrada con dos autores: 'Zhu y Liao', no 'et al.'" | La entrada tiene dos autores; la regla fijada es nombrar a ambos | "como la de Ramadanov y Zabler~\cite{ramadanov2025safezone}" |
| T09 | media | E-R6 | l.42 | "lo validan con una varilla de titanio de 12.7 mm y dos casos de crioablacion" | `ren2022metalinsertion.md`, Evidencia: varilla de 12.7 mm (Sec. 2.1.3) como validacion de ruido y endurecimiento; *"Two percutaneous cryoablation cases were used for demonstration."* (Sec. 2.5) | La validacion es con la varilla; los dos casos clinicos son de demostracion. El texto da a los casos el papel de validacion | "lo validan con una varilla de titanio de 12.7 mm y lo demuestran en dos casos de crioablacion" |
| T10 | baja | G-T4 | l.12 | "Cada fuente leida tiene una ficha que copia, para cada cifra o criterio, la frase original" | `_plantilla.md`; fichas `park2015ct`, `glover1980nonlinear`, `selles2023ai`, `zhang2025lefusion`, `konz2024anatomicallycontrollable`, `jin2021freetumor`, `wu2025freetumor`, `lugmayr2022repaint`, `zwingmann2010percutaneous` | Esas nueve fichas no tienen tabla "Evidencia textual": solo "Numeros que cito". Algun criterio citado en el capitulo solo consta en prosa sin frase original (p. ej., `selles2023ai`: "hueso y musculo, cerca del implante y contralateral", l.72). La generalizacion "cada ... cada" no se cumple | "Cada fuente leida tiene una ficha que copia la frase original y la pagina de cada cifra que se cita" |
| T11 | baja | G-T4 (GAP) | l.12 | \GAPDEC{... bases consultadas, cadenas ..., fechas de corte ... que no constan en el registro} | `docs/literatura/_candidatos.md` l. 539-553 (busqueda web 2026-09-15, por orden de la autora), l. 57 (busqueda dirigida #106, 2026-09-21), l. 669-671 (ronda 2026-09-19 desde `refs/deep-research/`) | El GAP de protocolo sistematico esta justificado, pero "que no constan" es absoluto: las busquedas dirigidas tienen fecha y procedencia registradas | Precisar la marca: "... de una busqueda sistematica; el registro solo fecha las busquedas dirigidas (`_candidatos.md`)" |
| T12 | baja | G-T4 | l.56 | "a 433 TC pelvicas ... 1.53 ± 0.57 en S1 y de 1.02 ± 0.33 en S2" | `mclaren2021corridor.md`: "S2 en 433, S1 en 352" (M&M, p. 2); seccion D: 1.02 en Resultados y 1.03 en Discusion | Falta el n de S1 (352, no 433). La ficha registra una discrepancia interna 1.02/1.03 que el texto no hace visible (se copio la de Resultados, que es la correcta de citar) | "... a 433 TC pelvicas (S1 medido en 352)"; opcional nota de la discrepancia 1.02/1.03 |
| T13 | baja | G-T4 | l.54 | "el 36.5 % de los tornillos en S1" | `herman2016.md`: *"in S1 46 (36.5%) screws"* (Resultados, p. 8) | La cifra coincide con la ficha. Pero 46 de 129 no da 36.5 %; la ficha no anota la posible errata del articulo (si anota otras tres inconsistencias del PDF) | Ficha insuficiente: relectura con `lector-papers` para confirmar 46/129 frente a 36.5 %. Mientras, dar "46 de 129 tornillos en S1 (36.5 %, segun los autores)" |
| T14 | baja | P-EA1, G-T4 | l.20, l.50, l.92 | cifras de Ramzan et al. (58.89 -> 63.53; 17 segmentos) | `ramzan2026claim.md`: PDF = arXiv:2506.15549v2; venue "NO ENCONTRADO EN EL PDF"; `.bib`: `@inproceedings`, *Artificial Intelligence in Healthcare* | Las cifras se leyeron del preprint y se citan como actas de 2026 sin declarar la version (supuesto 5 del redactor) | Mantener la cita y anotar en la ficha la version leida; si no se consigue la version de actas, nota al pie: "cifras de la version arXiv v2" |
| T15 | baja | E-F3 | l.72 | "Selles et al." | `overleaf/referencias.bib`: `author = {Selles, Mark and ...}` | El apellido del `.bib` va sin tilde; en la lista de referencias IEEE aparecera "Selles" | Escribir "Selles et al." o corregir en `refs/raw` si el raw trae la tilde (regla 9 raiz) |
| T16 | baja | G-T4 | l.99 (tabla) | Wang et al. 2025: "Metal insertado a mano para entrenar" | `wang2025adaptiveweighting.md`, Evidencia: "Insercion manual de metal en cortes clinicos (DentalCBCT)" (Sec. V-A-2, p. 2414) | La fila de evidencia situa la insercion manual en el conjunto DentalCBCT; la celda la generaliza a todo el entrenamiento | "Metal segmentado de datos clinicos e insertado a mano (conjunto dental)" o citar solo lo que la ficha fija sin condicion |
| T17 | baja | E-R6 (PAT-64) | l.106 | "coloca el metal al azar o a mano, y se valido en un fantoma y en dos dimensiones" | l.40 y l.58 del propio capitulo; `wang2019cochlear.md` (implante atado a la escala timpanica); `karageorgos2024ddpm.md` (regla de solape); `wu2022xcist.md` (validacion "first-order") | Patron PAT-64 reincide. La sintesis vale para Peters et al.; no para Karageorgos (regla de solape, que l.58 si nombra) ni para Wang 2019 (anclaje anatomico), y "se valido en un fantoma" no vale para XCIST ni para Wang 2019 | "La simulacion fisica produce el artefacto con su mecanismo, pero coloca el metal al azar, a mano o con una regla de solape; el protocolo de Peters et al. se valido en un fantoma y en dos dimensiones" |
| T18 | baja | E-P3 (decision §2 "negativos acotados") | l.106 | "La codificacion multiventana ... existe para quitar el artefacto y no para generarlo" | l.66 del capitulo ("En las dos fuentes ..."); `wang2025adaptiveweighting.md`, `li2024.md` | Negativo sin acotar a las fuentes revisadas | "En las fuentes revisadas, la codificacion multiventana sirve para quitar el artefacto y no para generarlo" |
| T19 | baja | G-T4 | l.30 | "Cuatro de los modelos de difusion revisados miden ... por el Dice de una segmentacion posterior" | `zhang2025lefusion.md`, "Dudas": "Los resultados downstream de segmentacion ..."; "SwinUNETR aparece unicamente como segmentador downstream" | LeFusion tambien reporta segmentacion posterior segun su ficha; el recuento "cuatro" se lee como cerrado | "Al menos cuatro ..." o incluir `zhang2025lefusion` si la ficha confirma que la metrica es Dice (la ficha no nombra la metrica: relectura) |

## Inventario

| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| l.8-10 | Estructura: 4 secciones ligadas a Obj 1-4 | `redaccion/MAPA.md`:18; `introduccion.tex` (objetivos) | si |
| l.12 | No hay protocolo de busqueda sistematica | busqueda en `docs/` sin resultado; `_candidatos.md` l.539, 669 | si, con T11 |
| l.12 | Lista de fuentes definida por la autora | `CLAUDE.md` raiz, regla 9 | si |
| l.12 | Ficha con frase original para cada cifra o criterio | `_plantilla.md`; 9 fichas sin tabla Evidencia | no (T10) |
| l.12 | Snowballing a candidatos; autora decide; busquedas dirigidas | `CLAUDE.md` raiz regla 15; `_candidatos.md` | si |
| l.12 | Una sola fuente citada con solo resumen, sin cifra | `_index.md`:62 (`zhang2026pediclescrew` ABSTRACT); resto de claves citadas COMPLETO o PARCIAL (`konz` y `guo`, cuerpo completo) | si |
| l.12 | \GAPDEC protocolo de busqueda | `redaccion/MAPA.md`:68 | si (T11) |
| l.16 | Inpainting acotado: chen2024, ramzan2026, jacob2026, lefusion | fichas respectivas ("Restriccion") | si |
| l.16 | Corte entero desde ruido: diffboost, konz | `zhang2025diffboost.md` Alg. 1; `konz...md` "Restriccion" | si |
| l.16 | Rayas irradian desde el metal | `deman1999.md` "Donde entra" | si |
| l.18 | DiffTumor, difusion latente, mascara + region sana (complemento) | `chen2024tumorsynthesis.md` Evidencia: "Condicionamiento formal", "Definicion de region sana" | si |
| l.18 | No modela textura fuera del tumor | idem, *"we do not intend to model organ textures outside"* §3.2 p. 4 | si |
| l.18 | Truncado [-175, 250] HU | idem, Apendice E.2 p. 21 | si |
| l.18 | Dice higado 62.5 -> 66.5 %, U-Net, media 5-fold, una de tres redes | idem, Tabla 4 p. 17 | si |
| l.18 | Cuatro radiologos; cerca de la mitad tomada por real | idem, §4.1 pp. 5-6 | si |
| l.20 | Ramzan: RM cardiaca, difusion en dominio de imagen | `ramzan2026claim.md` filas 10, 74 | si |
| l.20 | Perdida solo dentro de la mascara; fondo real con ruido en cada paso | idem filas 1-4 | si |
| l.20 | Esquema adaptado de LeFusion | idem fila 11 | si |
| l.20 | LeFusion: nodulos pulmonares en TC, perdida en lesion, fondo real ruidoso | `zhang2025lefusion.md` "Que hace", "Donde entra" | si |
| l.20 | Dice 58.89 -> 63.53, mejor configuracion | `ramzan2026claim.md` filas 50, 52 (Tabla 2 p. 11) | si (T14 version) |
| l.20 | Sin metricas de fidelidad; fondo solo cualitativo | idem filas 58, 9, 59 | si |
| l.22 | LGESynthNet: inpainting, difusion latente con ControlNet | `jacob2026lgesynthnet.md` Abstract p. 1 | si |
| l.22 | Mapa de bordes + imagen enmascarada; decodifica imagen completa | idem Sec. 3.1 p. 3; "Restriccion" pto 2 | si |
| l.22 | Sin paso que restituya pixeles fuera | idem "Buscado sin resultado" | si |
| l.22 | SSIM imagen completa 0.587 | idem Tabla 1 p. 7 | si |
| l.22 | Cicatriz < 1 % de la imagen | idem Sec. 1 p. 2 | si |
| l.22 | Autores atribuyen perdida a compresion latente | idem Sec. 5 p. 8 | si |
| l.22 | Dice 0.72 -> 0.77 con 300 sinteticas | idem Tabla 2 p. 8; Sec. 4.3 p. 7 | si |
| l.24 | DiffBoost: ControlNet sobre SD, imagenes radiologicas, desde ruido, corte a corte | `zhang2025diffboost.md` §III-B, Alg. 1, §IV-B | si |
| l.24 | Texto + borde de mascara; mezcla por parches al azar sin relacion con mascara | idem §III-C, §III-D, Alg. 1 | si |
| l.24 | 78.46 -> 84.56; 94.42 -> 94.78; 62.92 -> 71.65 % | idem Tabla II p. 3678 | si |
| l.24 | Konz: mascara concatenada en cada paso, dominio de imagen, corte desde ruido | `konz...md` "Que hace", "Restriccion" | si |
| l.24 | [0, 255], no HU; Dice 0.8980; 40 pacientes | idem "Numeros" Sec. 3 p. 93, Tabla 1 p. 94, Sec. 2 p. 92 | si |
| l.26 | Hu: sintesis analitica; efecto de masa hasta 1.3 r | `hu2023.md` Tabla 1 p. 7426 | si |
| l.26 | Ese paso solo en la prueba visual | `hu2023.md` Evidencia "Cuales son los cuatro pasos" = NO ENCONTRADO en texto | no (T01) |
| l.26 | Jin: parche 3D completo, GAN, supervisa region de borde | `jin2021freetumor.md` "Restriccion" (Sec. 3.4.1 p. 9) | si |
| l.26 | Wu 2025 prepublicacion; conserva valores fuera de mascara | `wu2025freetumor.md` Ec. 1 (Sec. 4.2 p. 20); `.bib` @misc arXiv | si |
| l.26 | Ventanas <= 600 HU (Hu 189, Jin 600, Wu 250/500) | `hu2023.md` §4 p. 7427; `jin2021freetumor.md` Sec. 4.2 p. 12; `wu2025freetumor.md` Tabla A19 | si |
| l.28 | RePaint: DDPM incondicional preentrenado, sin reentrenar; region conocida | `lugmayr2022repaint.md` "Que hace" | si |
| l.28 | 256 x 256, imagenes naturales 2D, sin TC ni metal | idem Sec. 5.1 p. 11466; "Restriccion" | si |
| l.28 | Sintetizador genera solo una region y copia el resto | TM:79; `capitulo3.tex`:29 | si |
| l.28 | \GAPDEC muestreo de la difusion | #106, #117 ABIERTAS (`04-implicancias.md`:7100, 8068); sin DEC | si |
| l.30 | Cuatro modelos miden por Dice posterior | fichas chen, ramzan, jacob, diffboost | si (T19) |
| l.30 | Dos anaden similitud con imagen real (jacob, diffboost) | `jacob...md` Tabla 1; `zhang2025diffboost.md` Tabla I | si |
| l.30 | Uno con prueba visual (chen) | `chen2024...md` §4.1 | si |
| l.30 | Ninguno trata implantes metalicos | fichas: "Metal ... NO ENCONTRADO" en las seis | si |
| l.34 | Insertar metal virtual es practica establecida en MAR | #9 ABIERTA solo en su reenunciado; hechos en fichas zhang2018, lin2019, wang2019, karageorgos | si |
| l.34 | Zhang y Yu: proyeccion, 120 kVp, Poisson, sinogramas reproyectados | `zhang2018.md` Sec. IV-A p. 6; Sec. II-A-1 p. 2-3 | si |
| l.34 | "no incluye dispersion ni volumen parcial" | `zhang2018.md` NO ENCONTRADO; `lin2019.md` declara volumen parcial | no (T02) |
| l.34 | Lin: 100 mascaras de metal | `lin2019.md` Evidencia Sec. 4 p. 10508 | si |
| l.34 | Wang 2019: electrodos, 1090 volumenes, Beer-Lambert, cinco energias | `wang2019cochlear.md` Abstract, Intro p. 2 | si |
| l.34 | Karageorgos: metal virtual en TC reales, CatSim | `karageorgos2024ddpm.md` Sec. II-A p. 3 | si |
| l.34 | En los cuatro se fabrica para una red que lo elimina | fichas: las cuatro son remocion | si |
| l.36 | Karageorgos: difusion en sinograma, solo sinogramas sin metal | idem Abstract; Sec. II-A p. 4 | si |
| l.36 | Metal reinsertado umbralizando la imagen sin corregir | idem "Restriccion" (*"by thresholding the uncorrected image"*, Sec. II-F) | si |
| l.36 | Yun: correccion de endurecimiento en proyeccion + LDM | `yun2026simulationdriven.md` "Que hace" | si |
| l.36 | Yun: CLINIC-metal; metal = mascara dada, por umbral en clinica | idem Sec. 2.4.2 p. 8 | si |
| l.36 | 31 % de equipos AAPM con difusion | `haneda2025aapm.md` Sec. 3.1 p. 11 | si |
| l.38 | Peters: calibra CatSim/XCIST contra fantoma de equipo comercial | `peters2025hybrid.md` 2.1-2.2 (Lightspeed VCT) | si |
| l.38 | 14 000 casos; TC clinica + metal virtual | idem 2.3 p. 4 | si |
| l.38 | Ocho metricas; 29 escenarios; base de AAPM CT-MAR | idem "Que hace"; 2.4 p. 4 | si |
| l.38 | < 2 % valor medio de TC | idem 3.1 p. 6 | si |
| l.38 | Ruido < 10 %; 13.3 % "en una de las cuatro configuraciones" | idem 3.1 p. 6 (condicion por region) | no (T03) |
| l.38 | Validacion no cubre paso hibrido (compensacion en frecuencia) ni geometria generica | idem Verificacion 4b, 4l, 3a-3b | si |
| l.38 | Todo el conjunto 2D; no cubre osteosintesis pelvica 3D | idem Abstract; "Casos de osteosintesis pelvica" NO ENCONTRADO | si |
| l.40 | Hasta cinco objetos en posiciones aleatorias | idem 2.3 p. 4 | si |
| l.40 | Lo ideal: ubicaciones realistas; manual impracticable | idem Discussion p. 9 | si |
| l.40 | Evaluacion en *meaningful locations*, sin regla | idem Discussion p. 9; Verificacion pto 2 | si |
| l.40 | Karageorgos: solape >= 50 % con region > 200 HU | `karageorgos2024ddpm.md` Sec. II-A p. 4 | si |
| l.40 | Wang 2019: centro de estructura segmentada; 3071 HU | `wang2019cochlear.md` Sec. 2.1 p. 3 | si |
| l.42 | XCIST: evaluacion cualitativa y semicuantitativa de primer orden | `wu2022xcist.md` Validation p. 9 | si |
| l.42 | Varillas Ti 20 mm y Fe 10 mm en fantoma analitico | idem Figura 11 p. 29 | si |
| l.42 | Traza distorsionada > 3.0 cm; 274 de 14 000 | `haneda2025aapm.md` Sec. 4 p. 16 | si |
| l.42 | Cohorte de volumenes reconstruidos, sin datos de proyeccion | `yun2026...md` (*"does not provide sinogram data"*); `docs/02-datos.md` | si |
| l.42 | Ren: sondas de ablacion, modelos de ruido y endurecimiento | `ren2022metalinsertion.md` Sec. 1, 2.1 | si |
| l.42 | Varilla Ti 12.7 mm | idem Sec. 2.1.3 | si |
| l.42 | "lo validan con ... dos casos de crioablacion" | idem Sec. 2.5 (*"used for demonstration"*) | no (T09) |
| l.42 | Requiere datos de proyeccion del fabricante | idem Sec. 4 (*"proper access to vendor projection data"*) | si |
| l.42 | Revisar si aumenta el metal (ortopedico) | idem Sec. 4 p. 035001-15 | si |
| l.48 | Liu: 14 casos clinicos de CTPelvic1K | `liu2025pipeline.md` VI p. 14 | si |
| l.48 | Etiqueta fragmentos, planifica reduccion, numero/posicion/direccion de tornillos | idem "Que hace"; III-D p. 8 | si |
| l.48 | Optimizacion con seguridad, fijacion, ejecutabilidad; plan unico por tornillo | idem III-D.3 pp. 11, 13 | si |
| l.48 | 2.56 mm y 3.31 grados | idem Abstract p. 2; IV-A p. 16 | si |
| l.48 | 86.7 %; tres cirujanos | idem IV-B p. 17 | si |
| l.48 | 10.58 ± 3.84 frente a 4.36 ± 3.83 mm | idem IV-B p. 16; Tabla III p. 38 | si |
| l.48 | No aplica a fracturas de sacro; sin distribucion; sin imagen | idem Discussion p. 18; "Modelado probabilistico" NO ENCONTRADO | si |
| l.50 | Zhang 2026: solo resumen; TC sintetica desde TC de haz conico; tornillo pedicular; mitiga artefacto | `zhang2026pediclescrew.md` (Profundidad: solo abstract; sin cifra citada) | si |
| l.50 | Ramzan: modelo clinico de 17 segmentos | `ramzan2026claim.md` filas 18-19 | si |
| l.50 | Chen: elipsoides refinados con radiologos | `chen2024...md` §3.3 p. 5 | si |
| l.52 | Zwingmann 2009: cuatro niveles, TC posoperatoria | `zwingmann2009navigated.md` M&M p. 1835 | si |
| l.52 | Grado 0: 69 % y 40 %; p = 0.02 | idem Results pp. 1836-1837 | si |
| l.52 | Dos series = referencia clinica | BITACORA §2 (2026-09-29); `capitulo3.tex` sec:sap | si |
| l.52 | Metaanalisis: 2.6 % (1832) y 0.1 % (262) | `zwingmann2013.md` Abstract p. 1257 | si (el articulo tambien imprime 2.3 %; no afecta) |
| l.52 | Cohorte 2009 con cero en ambas series | idem Fig. 2 p. 1261 | si |
| l.52 | "porque, segun los propios autores ..." | idem Discusion p. 1264 (criterio general, sin enlace causal) | no (T05) |
| l.54 | Zwingmann 2010: 63 navegados, 131 convencionales | `zwingmann2010percutaneous.md` Resumen p. 1501 | si |
| l.54 | 81/11/3/5 %; 42/22/21/13 % + 2 % grado 4 no definido | idem Tabla 1 p. 1503; Metodos p. 1502 | si |
| l.54 | Posible solapamiento con 2009 | idem "Donde entra"; #113 | si |
| l.54 | \GAPDEC Zwingmann 2010 | #113 ABIERTA (`04-implicancias.md`:7619); sin DEC | si |
| l.54 | Herman: definicion binaria; 36.5 % S1, 14.8 % S2, p = 0.035 | `herman2016.md` Resultados p. 8; Patients and Methods p. 6 | si (T13) |
| l.54 | Ningun tornillo integramente fuera del hueso | idem Resultados p. 7 | si |
| l.54 | Lectura como cota del muestreador | TM:52 (*"the latter bounds the range"*) | si |
| l.56 | Kaiser: marco calculable sobre TC | `kaiser2014dysmorphism.md` "Que hace"; TM:52, :78 | si |
| l.56 | McLaren: procedimiento reproducible, 433 TC | `mclaren2021corridor.md` M&M p. 2 | si (T12) |
| l.56 | 1.53 ± 0.57 (S1), 1.02 ± 0.33 (S2) | idem Results p. 4 | si (T12) |
| l.56 | Tornillo de 7 mm; 150 mm piel-sacro estimada | idem M&M p. 3 | si |
| l.56 | Ziran: 17 pelvis cadavericas | `ziran2007fluoroscopic.md` M&M p. 348 | si |
| l.56 | CV 7-25 %; hasta 140 % ala superior de S1 | idem Variabilidad pp. 351-352; TM:52 | no (T04) |
| l.56 | Ramadanov: descripcion cualitativa | `ramadanov2025safezone.md` "Restriccion" | si (T08 nombre) |
| l.56 | Marco y criterio de viabilidad en sec:corredor; distribucion propia | `capitulo3.tex`; TM:52, :78 | si |
| l.58 | Planificacion: trayectoria por tornillo, no cubre sacro | `liu2025pipeline.md` Verificacion pto 4 | si |
| l.58 | Simuladores: al azar o regla de solape | fichas peters, karageorgos | si |
| l.58 | Sin generador de poses comparado con distribucion clinica, en fuentes revisadas | negativo acotado; fichas de la seccion | si |
| l.62 | Recortes de sintesis <= 600 HU | ver l.26 | si |
| l.62 | MAR: umbral 2500 HU | `wang2025adaptiveweighting.md` Sec. V-A-2 p. 2413; `li2024.md` Sec. IV-E p. 1878 | si |
| l.64 | Tres ventanas [-1000, 2000], [-320, 480], [-160, 240] HU | `wang2025...md` Sec. V-A-1 p. 2412 | si |
| l.64 | Aprender el peso de la perdida de cada ventana | idem "Que hace" (AdaW) | si |
| l.64 | Cascada de etapas, de ancha a estrecha | idem Sec. III p. 2410 | si |
| l.64 | Marco atribuido a trabajo anterior | idem *"Motivated by the existing work [24]"* | si |
| l.64 | \GAPLIT fuente primaria del marco | `_candidatos.md`:113 PENDIENTE (Niu y Wang); `MAPA.md`:71 | si |
| l.64 | 26.76 dB frente a 32.67 dB en la ventana estrecha | `wang2025...md` Sec. V-B p. 2414 | si |
| l.64 | CLINIC-metal; cinco medicos; sin imagen limpia | idem Sec. V-A-3, V-C-3 | si |
| l.66 | Li: ventanas en perdida y evaluacion; entrada [-1000, 2000] HU | `li2024.md` Sec. III-D p. 1870 | si |
| l.66 | +0.64 dB en el grupo de metal mas grande | idem Sec. IV-B.4 p. 1873 | si |
| l.66 | Ninguna fuente usa las ventanas como codificacion de entrada de un generador | fichas wang2025, li2024; #2, #24 (APLICADA en redaccion) | si |
| l.66 | Techo de 2000 HU satura el metal | TM:77 (*"whose 2000 HU ceiling clips metal"*) | si |
| l.68 | Compuerta del Obj 1 | TM:77 | si |
| l.68 | Rombach: compresion quita alta frecuencia; cuello de botella en precision por pixel | `rombach2022latentdiffusion.md` §1 p. 2; §5 p. 9 | si |
| l.68 | Chen 2026: prepublicacion "de otro grupo" | `.bib`; TM:77 ("concurrent") | no (T06) |
| l.68 | Autoencoders de video congelados a TC sin ajuste medico | `chen2026foundationvae.md` Abstract, §1 | si |
| l.68 | PSNR, SSIM, MSE sin unidades; sin hueso ni metal; [-1000, 1000] HU en generacion | idem §4.1 p. 5; filas NO ENCONTRADO | si |
| l.68 | Guo: autoencoder con TC; similitud, no error en HU; rango no declarado | `guo2025maisi.md` Tabla 1; N4, N6 NO ENCONTRADO | si |
| l.70 | De Man: mecanismos aislados modificando el sinograma | `deman1999.md` "Restriccion" | si |
| l.70 | Lin: 31.45 frente a 33.51 dB; variante recibe sinograma interpolado | `lin2019.md` Tabla 1 p. 10509; config C | si |
| l.70 | Li: rama de solo imagen desde reconstruccion con artefacto, por debajo | `li2024.md` Sec. IV-B p. 1871; Ec. 5 | si |
| l.70 | \GAPDATO ablacion de Li | `li2024.md` "Advertencia de transcripcion"; DEC fila #71 (`01-decisiones.md`:988 "Sin cifras de li2024") | si |
| l.70 | Problema mal planteado (paciente y metal en la misma traza) | `lin2019.md` Sec. 2 p. 10506 | si |
| l.70 | Sin precedente de sintesis del artefacto solo en imagen, en fuentes revisadas | `lin2019.md` "Gap nuevo"; #61 ABIERTA tratado como supuesto | si |
| l.72 | De Man: rayas desde el metal; simulacion 2D; varilla de hierro y amalgama dental; sin alcance | `deman1999.md` "Que hace", l. 106-111 | si |
| l.72 | Park: cupping dentro, rayas fuera | `park2015ct.md` "Que hace", Introduccion p. 2 | si |
| l.72 | Glover: rayas que conectan estructuras con haz monocromatico; hueso, no metal | `glover1980nonlinear.md` "Restriccion", "Donde entra" | si |
| l.72 | Selles: 25 pacientes, fusion sacroiliaca; HU en hueso y musculo cerca y contralateral; sin distancia | `selles2023ai.md` "Numeros" Sec. 2.3; "Donde entra" (prosa) | si (T10, T15) |
| l.72 | Li: artefacto presente en toda la imagen, sin medir | `li2024.md` Sec. I p. 1866 (*"present globally"*) | si |
| l.74 | Radzi: 2.0, 2.6, 1.6, 2.0 mm | `radzi2014metalartifacts.md` Resultados p. 167 | si |
| l.74 | Cassanego: 3.1 a 4.2 mm; metodo tomado de Radzi | `cassanego2026evolution.md` Tabla 3 p. 7; M&M p. 3 | si |
| l.74 | Radzi: desde el eje; umbral no publicado | `radzi...md` Abstract p. 163; Evidencia "Valor del umbral" NO ENCONTRADO | si |
| l.74 | Tornillos de 3.5 a 4.0 mm; un tobillo cadaverico | idem M&M p. 165 | si |
| l.74 | Cassanego sin punto de referencia; ninguna en HU | `cassanego...md` Evidencia filas 137-138, 172 | si |
| l.74 | B_delta ~12 mm = convencion, no medida heredada | TM:79 (*"the 12 mm value remains a declared construction"*); #57 (ABIERTA en evidencia externa, DEC fila 57 `01-decisiones.md`:990) | si |
| l.76 | Sin precedente de banda numerica fuera de mascara de implante | fichas park, glover, selles, radzi, cassanego; #57 | si |
| l.76 | Hu 1.3 r; Jin region de borde sin mm | `hu2023.md`; `jin2021freetumor.md` | si |
| l.76 | Banda trunca rayas lejanas; sec:amenazas | TM:79; DEC fila 57 | si |
| l.80 | Muestreador y SAP ejecutados | #116 act. 2026-09-24 (`04-implicancias.md`:8742) | si |
| l.80 | \GAPDATO sin muestras sinteticas | #116 (`04-implicancias.md`:8753); `MAPA.md`:30 | si |
| l.91-99 | Filas de tabla (enfoque, colocacion, fuera, evaluacion) de los 9 trabajos | fichas citadas arriba en cada fila | si, salvo T16 |
| l.101 | Fila propia: muestreador + difusion en imagen; poses preinscritas; G = M ∪ B_delta y copia; SAP; *streak amplitude* frente a copia y protocolo | `capitulo3.tex`:27-31, 125, 244; TM:78-79 | si |
| l.106 | Lectura por filas: "al azar o a mano ... fantoma y dos dimensiones" | fichas peters, karageorgos, wang2019, wu2022xcist | no (T17) |
| l.106 | Multiventana "existe para quitar" | l.66 | parcial (T18) |
| l.108 | Brecha = tension de la introduccion | BITACORA §2 (2026-09-30, capitulo2-r00) | si |
| l.108 | Protocolo fisico sobre poses del muestreador | `capitulo3.tex` sec:apariencia | si |
| l.108 | \GAPDEC sintetizador aprendido | #128.1 ABIERTA; `MAPA.md`:66 | si |
| l.110 | Aporte en tres elementos | TM; `introduccion.tex`:58; #56 (ajuste 2026-09-21 no aplicado) | si |
| l.110 | Primer elemento sin salvedad de mascaras umbralizadas | #128.4 ABIERTA; `introduccion.tex`:58 | no (T07) |
| l.110 | Xie: cortes simulados, 2500 HU, sensibilidad 100 %, Dice 82.92 % | `xie2024implantsegmentation.md` Results p. 6; Tabla 2 p. 11 | si |
| l.110 | "cobertura en exceso" como lectura propia | idem *"covered the ground truth"*; BITACORA §2 "este trabajo lee" | si |
| l.110 | Segundo elemento: muestreador comparado sin ajustarse | TM:52 (*"No parameter of the sampler is derived from those distributions"*) | si |
| l.110 | Ningun objetivo aisla el primero ni el tercero | `introduccion.tex`:58; #128.3 | si |
| l.112 | Publicado: insercion de metal y difusion frente a metal | seccion 2.2 | si |
| l.112 | Konz, Ramzan (mascara en dominio de imagen); LeFusion (exterior conservado); Hu, Jin (fuera de mascara) | fichas; #56 ronda 2026-09-21 | si |
| l.112 | \GAPDEC reformulacion de novedad | #56 act. 2026-09-21 "No aplicado" (`04-implicancias.md`:8023-8066) | si |
| l.114 | Supuesto (dominio de imagen) y convencion (ancho de B_delta) | #61 ABIERTA; TM:79 | si |
| l.114 | Evaluacion por coherencia fisica y quirurgica, no por segmentacion posterior | `docs/00-tesis.md` Fuera de alcance pto 1; TM | si |
| global | Claves `\cite` (42) | todas presentes en `overleaf/referencias.bib` | si |
| global | Alcance retirado (Dice/HD95 como objetivo, difusion latente/ControlNet vigente, "31-60%", BFC/ISC) | texto completo | si: ausente |
| global | Cita como sujeto gramatical (E-F3) | texto completo | si: ninguna |
| global | Apellidos frente a primer autor del `.bib` | 40 coinciden; Ramadanov (T08), Selles (T15) | parcial |
| global | Fuentes de fabricante | ninguna citada | si |
| global | Prepublicaciones señaladas | `wu2025freetumor`, `chen2026foundationvae` (@misc) | si |

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Cifra ajena pierde la condicion de la fuente (region, plano) al citarse | G-T4, E-P3 | "hasta 140 % en el ala superior de S1" | PAT-31 |
| Se copia la formulacion menos precisa aunque TM trae la exacta | G-T4 | Ziran sin "en el plano frontal sacro" (TM:52 lo trae) | PAT-65 |
| La cita atribuye a los autores el enlace causal que hace la ficha | E-R6 | "porque, segun los propios autores, ... solo llama malposicion" | PAT-6 |
| Sintesis de fila que generaliza a todo un enfoque lo que vale para una fuente | E-R6 | "coloca el metal al azar o a mano, y se valido en un fantoma" | PAT-64 |
| Un "NO ENCONTRADO" de la ficha se redacta como negacion sobre el metodo, o una demostracion como validacion | E-R6 | "su simulacion no incluye dispersion ni volumen parcial" | nuevo |
| Relacion entre autores o grupos ("de otro grupo") afirmada sin fuente | G-T4 | "Una prepublicacion de otro grupo, Chen et al." | nuevo |
| Entrada de dos autores citada con "et al." pese a la decision de §2 | E-F3 | "como la de Ramadanov et al." | nuevo (decision §2 2026-09-29 existe; no hay PAT) |
| Salvedad de un aporte, presente en la introduccion, omitida al repetirlo en otro capitulo | OC-3, G-T4 | primer elemento sin "se entrena con mascaras umbralizadas" (#128.4) | nuevo (decision §2 "GAP replicados", 2026-09-30) |
