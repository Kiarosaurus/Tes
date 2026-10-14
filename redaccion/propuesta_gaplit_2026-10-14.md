# Propuesta de fuentes para los `\GAPLIT` del documento — 2026-10-14

Encargo de bibliotecario. No se toco `refs.bib`, `refs/raw/`, `refs/clean/` ni ningun `.tex`; no se descargo
ningun PDF. Los candidatos tipo C quedaron como PENDIENTE en `docs/literatura/_candidatos.md`, seccion
"Ronda 2026-10-14 — GAPLIT del documento".

**Limite de la verificacion (leer antes de usar los metadatos).** Desde esta sesion no se pudo abrir doi.org,
api.crossref.org, arXiv, PubMed ni las paginas de los editores (DNS sin resolver en WebFetch; el proxy rechaza el
CONNECT). Los metadatos se confirmaron **solo con resultados del buscador** que muestran la pagina del editor o de
un indice (SPIE Digital Library, epubs.siam.org, Project Euclid, nowpublishers, catalogos de bibliotecas). Cada
dato que ninguna de esas fuentes mostro dice NO VERIFICADO. Lo unico verificado de primera mano es el codigo de
XCIST (marca 7), clonado en el scratchpad de la sesion. **Ningun dato de esta propuesta reemplaza al raw:** la
regla 9 raiz sigue mandando y cada entrada nace de un archivo del editor pegado en `refs/raw/`.

Clasificacion: (A) referencia ya en el repositorio con ficha y PDF, solo falta citarla; (B) candidato ya
identificado en el repositorio, falta PDF o raw; (C) sin candidato identificado en el repositorio (las filas
"sin identificar" de las rondas 2026-10-03 y 2026-10-08 de `_candidatos.md` cuentan como C).

## Tabla resumen

| # | Marca (archivo:linea) | Tipo | Referencia propuesta | DOI | Acceso abierto | Que tiene que hacer la autora |
|---|---|---|---|---|---|---|
| 1 | `capitulo1.tex:35` fisica de TC (Beer-Lambert, HU, FBP) | C | Hsieh, *Computed Tomography*, 4a ed., SPIE Press 2022 (principal); Kak y Slaney, *Principles of Computerized Tomographic Imaging*, SIAM 2001 (complemento) | 10.1117/3.2605933 (Hsieh, desde catalogos); Kak y Slaney: NO VERIFICADO | Hsieh no; Kak y Slaney si (copia de los autores, uso personal) | Pegar raw de Hsieh (y de Kak-Slaney si lo quiere) y conseguir el libro o los capitulos |
| 2 | `capitulo1.tex:74` anatomia de la pelvis | C | Standring (ed.), *Gray's Anatomy*, 42a ed., Elsevier 2020; alternativa atlas: Netter, *Atlas of Human Anatomy*, 8a ed. | sin DOI (ISBN 978-0-7020-7705-0) | no | Elegir tratado o atlas, pegar raw (registro de catalogo del editor) y conseguir el capitulo de pelvis |
| 3 | `capitulo1.tex:124` Wasserstein-1 y su forma en la recta | C | Vallander 1974 (forma 1D, primaria); Peyre y Cuturi 2019 (referencia moderna) | 10.1137/1118101; 10.1561/2200000073 | Vallander no (SIAM de pago; original ruso en mathnet.ru, NO VERIFICADO); Peyre-Cuturi si (arXiv:1803.00567) | Pegar raw de uno o ambos y conseguir los PDF |
| 4 | `capitulo1.tex:130` Wilcoxon, TOST y su IC del 90 %, bootstrap, Fisher exacta | C | Wilcoxon 1945; Schuirmann 1987; Efron 1979 (y opcional Efron y Tibshirani 1993 / Davison y Hinkley 1997); Fisher 1935 o Agresti 2013 | 10.2307/3001968; 10.1007/BF01068419 (NO VERIFICADO); 10.1214/aos/1176344552; 10.2307/2342435; Agresti: NO VERIFICADO | Efron 1979 si (Project Euclid, segun buscador); resto NO VERIFICADO / no | Decidir cuantas fuentes (una por metodo o un libro de texto), pegar los raw y conseguir los PDF |
| 5 | `capitulo2.tex:82` origen del esquema multiventana de MAR | **B** | Niu y Wang, "Multiple-window learning for CT metal artifact reduction", Proc. SPIE 11840, 1184015 (2021) | 10.1117/12.2596239 | no encontrado | Conseguir PDF y pegar raw desde SPIE Digital Library; el titulo correcto no coincide con la fila de `_candidatos.md` |
| 6 | `capitulo3.tex:202` parametrizacion de prediccion `v` | C | Salimans y Ho, "Progressive Distillation for Fast Sampling of Diffusion Models", ICLR 2022 | sin DOI; arXiv:2202.00512 | si (arXiv, OpenReview) | Pegar raw (BibTeX de arXiv u OpenReview) y conseguir el PDF |
| 7 | `capitulo3.tex:355` repositorio del protocolo fisico (revisiones y licencia) | **B** | Software XCIST: `github.com/xcist/main` (gecatsim 1.6.8, commit `4cf3544`) y `github.com/xcist/example` (commit `4993e87`), ambos BSD 3-Clause | sin DOI (no hay `CITATION.cff`) | si (codigo publico) | Pegar raw de software (no hay PDF que conseguir); antes, resolver el `\GAPDEC` de #158 que decide si y como se cita el repositorio |

Totales: **A = 0, B = 2, C = 5**.

## Detalle por marca

### 1. `capitulo1.tex:35` — fisica de TC (tipo C)

**Marca:** "fuente de referencia de física de TC que enuncie la ley de Beer-Lambert con el coeficiente de atenuación
lineal, dé la definición de la escala Hounsfield como transformación de ese coeficiente y los fundamentos de la
reconstrucción por retroproyección filtrada".
**Afirmacion:** las HU son una escala normalizada de la atenuacion reconstruida (agua 0 HU, aire -1000 HU), y la
conversion entre coeficiente de atenuacion y HU se apoya en el coeficiente del agua.
**En el repositorio:** `wu2022xcist` (solo los anclajes 0 / -1000 HU) y `wang2019cochlear` (nombra la formula sin
escribirla) ya estan citados; ninguna ficha enuncia Beer-Lambert, la formula de HU ni FBP. Fila "sin identificar"
en `_candidatos.md` (ronda 2026-10-03).

**Propuesta principal.** J. Hsieh, *Computed Tomography: Principles, Design, Artifacts, and Recent Advances*, 4th
ed., SPIE Press Monograph 344, Bellingham, WA: SPIE, 2022. DOI 10.1117/3.2605933; ISBN electronico
978-1-5106-4688-9, impreso 978-1-5106-4687-2 (los dos ISBN segun catalogos distintos). Verificado en catalogos
(KIT, Heidelberg, BVB); la pagina de SPIE no aparecio. xviii + 766 pp. segun un catalogo. Capitulos y paginas de
cada contenido: NO VERIFICADO. Acceso abierto: no. Por que: libro de texto estandar que cubre los tres contenidos y
ademas el endurecimiento del haz y los artefactos metalicos.
- Catalogo: <https://bvbvf1.bib-bvb.de/vufind/Record/DE-604.BV048389391/Details>
- Catalogo: <https://katalog.bibliothek.kit.edu/bib/1311551>

**Complemento de acceso abierto.** A. C. Kak, M. Slaney, *Principles of Computerized Tomographic Imaging*, Classics
in Applied Mathematics 33, Philadelphia: SIAM, 2001 (reedicion integra de IEEE Press, 1988), xiv + 327 pp., ISBN
0-89871-494-X. DOI: NO VERIFICADO (no aparecio la pagina de epubs.siam.org). Los autores alojan una copia electronica
identica al libro, para uso personal: <https://engineering.purdue.edu/~malcolm/pct>. Cubre FBP y la medicion de
proyecciones por atenuacion; que defina la escala HU: NO VERIFICADO.

### 2. `capitulo1.tex:74` — anatomia de la pelvis (tipo C)

**Marca:** "fuente de anatomía de la pelvis que defina e ilustre la cortical ósea, el platillo vertebral, el ala
sacra, el foramen neural, la tabla externa del ilion y la articulación sacroilíaca".
**Afirmacion:** el tornillo iliosacro atraviesa tres corticales (dos del ilion, una del ala sacra); el ala sacra
desciende hacia lateral y caudal desde el cuerpo vertebral superior.
**En el repositorio:** `routt1997` describe solo la pendiente del ala; `docs/03-glosario.md` no define las
estructuras. Fila "sin identificar" (ronda 2026-10-03).

**Propuesta principal.** S. Standring (editora en jefe), *Gray's Anatomy: The Anatomical Basis of Clinical
Practice*, 42nd ed., Elsevier, 2020. ISBN 978-0-7020-7705-0. Sin DOI. Paginas: 1606 en un listado, 1588 y ano 2021
en otro (NO VERIFICADO). Capitulo de pelvis y que defina cada estructura de la marca: NO VERIFICADO. Acceso abierto:
no. Pagina de Elsevier (educadores): <https://www.educate.elsevier.com/book/details/9780702077050>.

**Alternativa si el texto debe "ilustrar".** F. H. Netter, *Atlas of Human Anatomy: Classic Regional Approach*,
8th ed., Philadelphia: Elsevier, 2022 o 2023 (los catalogos difieren). ISBN rustica 978-0-323-68042-4. Tiene un
capitulo "Pelvis"; laminas de sacro: NO VERIFICADO. Catalogo: <https://catalog.lib.ecu.edu/catalog/5959089>.

### 3. `capitulo1.tex:124` — distancia de Wasserstein-1 (tipo C)

**Marca:** "fuente de referencia de la distancia de Wasserstein-1 y de su forma para distribuciones sobre una recta".
**Afirmacion:** sobre los cuatro grados de brecha, W1 es la suma de las diferencias absolutas entre las funciones de
distribucion acumulada (Ec. `eq:w1`); vale 1 si una distribucion esta un grado mas arriba y 3 como maximo.
**En el repositorio:** ninguna ficha. Fila "sin identificar" (ronda 2026-10-03).

**Primaria de la forma 1D.** S. S. Vallander, "Calculation of the Wasserstein distance between probability
distributions on the line," *Theory of Probability and Its Applications*, vol. 18, no. 4, pp. 784-786, 1974. DOI
10.1137/1118101. Original ruso: *Teor. Veroyatnost. i Primenen.* 18(4):824-827, 1973. **Ojo: el apellido es
Vallander, no "Vallender".** Segun el abstract indexado, la distancia entre distribuciones en la recta es la
distancia L1 entre sus funciones de distribucion: es exactamente la forma que usa el documento. Acceso: SIAM de pago;
la ficha del original en mathnet.ru existe, su texto libre NO VERIFICADO.
- Editor: <https://epubs.siam.org/doi/10.1137/1118101>
- Original ruso: <https://mathnet.ru/eng/tvp4387>

**Referencia moderna de acceso abierto.** G. Peyre, M. Cuturi, "Computational Optimal Transport: With Applications
to Data Science," *Foundations and Trends in Machine Learning*, vol. 11, no. 5-6, pp. 355-607, 2019. DOI
10.1561/2200000073. Google Research da pp. 355-602 (discrepancia; el editor da 355-607). arXiv:1803.00567 (v4,
2020). Seccion del caso unidimensional: NO VERIFICADO.
- Editor: <https://nowpublishers.com/article/Details/MAL-073>
- Acceso abierto: <https://arxiv.org/abs/1803.00567>

### 4. `capitulo1.tex:130` — pruebas estadisticas (tipo C)

**Marca:** "fuentes de referencia de la prueba de rangos con signo de Wilcoxon, de las dos pruebas unilaterales de
equivalencia y de su relación con el intervalo de confianza del 90 %, del intervalo de confianza por remuestreo y
de la prueba exacta de Fisher".
**Afirmacion (parrafos :126-130):** superioridad del Obj 3 por Wilcoxon pareada de una cola; equivalencia por dos
pruebas unilaterales, concluida si el IC 90 % cae en [-Delta, +Delta]; IC 95 % del Obj 1 por remuestreo de
pacientes con reemplazo; Fisher exacta bilateral en tablas 2x2 de §Amenazas.
**En el repositorio:** las fichas solo registran el uso por terceros (`wasserthal2023`, `isensee2021`,
`zwingmann2009navigated`). Fila "sin identificar" (ronda 2026-10-03), que ademas **no incluye Fisher** (se anadio
a la marca en capitulo1-r06).

Una fuente por metodo:

| Metodo | Referencia | DOI | Acceso abierto | Verificacion |
|---|---|---|---|---|
| Wilcoxon de rangos con signo | F. Wilcoxon, "Individual comparisons by ranking methods," *Biometrics Bulletin*, vol. 1, no. 6, pp. 80-83, 1945 | 10.2307/3001968 | NO VERIFICADO | vol., num., pp. y DOI coinciden en varias fuentes del buscador; pagina de JSTOR no abierta |
| TOST y su relacion con el IC 90 % | D. J. Schuirmann, "A comparison of the two one-sided tests procedure and the power approach for assessing the equivalence of average bioavailability," *J. Pharmacokinet. Biopharm.*, vol. 15, no. 6, pp. 657-680, 1987 | 10.1007/BF01068419: **NO VERIFICADO** (no aparecio en ningun resultado) | NO VERIFICADO (hay registro en Zenodo, contenido no comprobado) | vol., num. y pp. en Wikidata y en una lista de referencias de GMDS. Que el articulo enuncie TOST(alfa = 0.05) = IC 90 %: NO VERIFICADO (lo dicen fuentes secundarias, atribuyendo el IC a Westlake) |
| Bootstrap | B. Efron, "Bootstrap methods: another look at the jackknife," *Ann. Statist.*, vol. 7, no. 1, pp. 1-26, 1979 | 10.1214/aos/1176344552 | si, segun el buscador (Project Euclid marca "Open Access"): <https://projecteuclid.org/euclid.aos/1176344552> | metadatos en Project Euclid via buscador |
| Bootstrap (libro, IC por percentiles) | B. Efron, R. J. Tibshirani, *An Introduction to the Bootstrap*, Monographs on Statistics and Applied Probability 57, New York: Chapman & Hall, 1993, ISBN 0-412-04231-2 | 10.1201/9780429246593 (asociado a un registro CRC con ano 1998) | no | catalogos de biblioteca; capitulo del IC: NO VERIFICADO |
| Remuestreo por paciente (opcional) | A. C. Davison, D. V. Hinkley, *Bootstrap Methods and their Application*, Cambridge University Press, 1997, ISBN 0-521-57391-2 | DOI del libro NO VERIFICADO (los capitulos usan 10.1017/CBO9780511802843.xxx) | no | una resena dice que los cap. 2-3 cubren datos jerarquicos; remuestreo por conglomerados: NO VERIFICADO |
| Fisher exacta (primaria) | R. A. Fisher, "The logic of inductive inference," *J. R. Stat. Soc.*, vol. 98, no. 1, 1935 | 10.2307/2342435 | NO VERIFICADO | es la fuente que cita la documentacion de `fisher.test` de R; **paginas en conflicto: 39-54 o 39-82** segun la version de esa documentacion: NO VERIFICADO |
| Fisher exacta (libro) | A. Agresti, *Categorical Data Analysis*, 3rd ed., Wiley Series in Probability and Statistics, Hoboken: Wiley, 2013, ISBN 978-0-470-46363-5 | NO VERIFICADO | no | ISBN y ano en registro de la Library of Congress via buscador; la doc. de R cita la 2a ed. (2002), pp. 91-101; paginas de la 3a ed.: NO VERIFICADO |

No se propone Fisher (1922, *J. R. Stat. Soc.* 85(1):87-94, DOI 10.2307/2340521): trata los grados de libertad de
chi cuadrado en tablas de contingencia, no la prueba exacta.

Enlaces: Wilcoxon <https://www.springerprofessional.de/introduction-to-wilcoxon-1945-individual-comparisons-by-ranking-/13752920>;
Schuirmann <https://zenodo.org/record/1232484>; Fisher 1935 y Agresti en la doc. de R
<https://search.r-project.org/R/refmans/stats/html/fisher.test.html>; Davison-Hinkley
<https://statwww.epfl.ch/davison/BMA>.

Opcion minima, si la autora prefiere menos entradas: Wilcoxon 1945 + Schuirmann 1987 + Efron y Tibshirani 1993 +
Agresti 2013.

### 5. `capitulo2.tex:82` — origen del esquema multiventana (tipo B)

**Marca:** "fuente primaria del esquema multiventana de MAR, que Wang et al. y Li et al. citan y de la que el
repositorio no tiene ficha".
**Afirmacion:** Wang et al. atribuyen la cascada multiventana a un trabajo anterior.
**En el repositorio:** fila PENDIENTE (nivel 1) en `_candidatos.md`, "Prioridad maxima — el origen del marco
multi-ventana (C3)", y fila 2 de PRIORIDAD VIGENTE. Sin PDF en `papers/`, sin raw, sin ficha.

**Referencia (desde la pagina de SPIE, via buscador).** "Multiple-window learning for CT metal artifact reduction,"
*Proc. SPIE* vol. 11840 (Developments in X-Ray Tomography XIII: NO VERIFICADO), art. 1184015, 2021. DOI
10.1117/12.2596239. Autores (Niu, Wang; Li segun `li2024`): NO VERIFICADO, la pagina no mostro la lista. **Titulo
distinto al de las dos citas secundarias** ("...for CT metal artifact reduction"; `wang2025adaptiveweighting` dice
"Multiple window learning for metal artifact reduction" y `li2024` "Multi-window learning..."). El abstract
indexado confirma que entrena una red sobre varias ventanas de HU a la vez. Acceso abierto: no encontrado.
- Editor: <https://ebooks.spiedigitallibrary.org/conference-proceedings-of-spie/11840/1184015/Multiple-window-learning-for-CT-metal-artifact-reduction/10.1117/12.2596239.full>

**Que hacer:** descargar desde SPIE la cita (raw) y el PDF; la lectura via `lector-papers` cerrara autores, mes y
paginas, y aclarara la discrepancia de titulos.

### 6. `capitulo3.tex:202` — prediccion `v` (tipo C)

**Marca:** "fuente de la parametrización de predicción $v$ con que se entrena el sintetizador".
**Afirmacion:** el sintetizador se entrena con el objetivo de prediccion `v` (DEC 2026-10-08 pto 3).
**En el repositorio:** ninguna ficha la define; `ho2020denoising` y `nichol2021improved` usan prediccion del ruido.
Fila "sin identificar" (ronda 2026-10-08).

**Referencia.** T. Salimans, J. Ho, "Progressive Distillation for Fast Sampling of Diffusion Models," International
Conference on Learning Representations (ICLR), 2022. arXiv:2202.00512 (v1 1-feb-2022, v2 7-jun-2022). Sin DOI
(ICLR no los asigna). El abstract anuncia "new parameterizations of diffusion models that provide increased
stability when using few sampling steps"; una patente secundaria atribuye la parametrizacion `v` a este trabajo.
**Que el texto defina `v = alfa_t eps - sigma_t x`: NO VERIFICADO** (el buscador no devolvio el cuerpo); se
confirma al leer el PDF. Acceso abierto: si.
- arXiv: <https://arxiv.org/abs/2202.00512>
- ICLR: <https://iclr.cc/virtual/2022/poster/6537>

### 7. `capitulo3.tex:355` — repositorio del protocolo fisico (tipo B)

**Marca:** "referencia bibliográfica del repositorio publicado del protocolo físico, con las revisiones y la licencia
que se revisaron; el código no tiene ficha ni entrada de bibliografía".
**Afirmacion:** la revision se hizo sobre `4cf3544` del simulador y `4993e87` de los ejemplos, BSD 3-Clause; el
script publicado exige un parche de una linea.
**En el repositorio:** fila PENDIENTE de la ronda 2026-10-05 (software de Peters et al.) y fila PENDIENTE de
`haneda2025aapm` (`xcist/example/tree/main/AAPM_datachallenge`). El articulo del simulador, `wu2022xcist`, ya esta
en `refs.bib`, pero no da las revisiones ni la licencia. Sin raw.

**Verificado de primera mano (clon de solo lectura en el scratchpad, 2026-10-14):**
- `https://github.com/xcist/main`: commit `4cf3544dc1205564adfbc70f0b23f7b0402788ee`, 27-mar-2026, "Update material
  name from 'pmma' to 'PMMA'"; es el HEAD actual. `LICENSE`: "BSD 3-Clause License", "Copyright 2024, GE Precision
  HealthCare". `setup.py`: paquete `gecatsim`, version 1.6.8, autores Mingye Wu, Paul FitzGerald, James Jobin,
  Jiayong Zhang, Nandan Reddy, Anupama Debnath, Brion Sarachan, Bruno De Man. Sin `CITATION.cff`; el README pide
  citar los articulos listados en <https://github.com/xcist/documentation/wiki/Publications-and-citing>.
- `https://github.com/xcist/example`: commit `4993e87360912277d6c6f2235b91031b85f363f1`, 8-oct-2025, "Update
  readme.md"; es el HEAD actual. `LICENSE`: BSD 3-Clause, "Copyright (c) 2024, GE Precision HealthCare".

Las revisiones y la licencia que afirma el capitulo coinciden con el codigo. **Que hacer:** no hay PDF; falta un raw
de software. Como el repositorio no trae archivo de cita, la autora decide de donde sale (por ejemplo, una ficha
escrita a partir de la pagina del repositorio) y si lo registra como excepcion en `refs/MAPEO.md`, como hizo con
los catalogos de fabricante. Va atado al `\GAPDEC` de `capitulo3.tex` (implicancia #158): si el repositorio del
desafio AAPM se cita como fuente de la implementacion y en que forma.

## Evaluacion de impacto (regla 13)

- Marca 5: el titulo publicado no es el de las dos fuentes secundarias. Afecta la fila de `_candidatos.md`, no un
  argumento; se corrige al hacer el raw.
- Marca 7: las revisiones citadas son hoy el HEAD de los dos repositorios; la cita de software sigue dependiendo
  de #158.
- Ninguno cambia el alcance, un supuesto ni un baseline. **Sin implicancias nuevas sobre la tesis.**
