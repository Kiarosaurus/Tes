# MAPEO — procedencia de cada entrada de `refs.bib`

> Tres capas. `raw/` es lo que entrego el editor y **no se edita nunca**.
> `clean/` es la version normalizada a mano, un archivo por entrada.
> `refs.bib` es el producto: se regenera con `python scripts/build_refs.py`.
>
> Nada aqui se completo con conocimiento del asistente. Todo campo sale de `raw/`
> o venia ya en `refs.bib` escrito por la autora; los heredados sin confirmar
> llevan `% VERIFICAR` dentro de su archivo de `clean/`.

## Precedencia (dictada por la autora, 2026-09-07)

Ante cualquier discrepancia, **manda `refs/raw/`**, y en su defecto `refs/clean/`.
Un campo que el raw no confirme no se conserva por costumbre: se baja la fuente real
y, si tampoco la trae, se elimina. `refs.bib` no lleva ninguna marca pendiente: si
esta ahi, tiene respaldo. Recogido en la regla 9 de `CLAUDE.md`.

## Reglas de normalizacion aplicadas en `clean/`

1. **Clave.** Se conserva la clave de la autora (`apellidoANIOpalabraclave`). La clave
   del editor se descarta y queda registrada en la tabla de abajo.
2. **Autores.** Se expanden a la lista completa del raw. Antes 25 de 27 decian
   `{Apellido, X. and others}`. Nombres de pila completos, `Apellido, Nombre`.
3. **Titulos.** Se conserva el titulo en Title Case de `refs.bib`, entre dobles llaves
   `{{...}}` para que BibTeX no cambie las mayusculas. PubMed exporta en sentence case
   y con punto final; ese formato no se adopta.
4. **Revistas.** Nombre oficial completo. Se eliminan las abreviaturas: `IEEE TMI`,
   `Int J CARS` y `CORR`. Esta ultima era ambigua con el repositorio de preprints
   *CoRR* de arXiv.
5. **`issue` -> `number`.** BibTeX clasico descarta `issue` sin avisar. Tres entradas
   lo usaban y su fasciculo no se habria impreso: `liu2021ctpelvic1k`,
   `xie2024implantsegmentation`, `zhang2026pediclescrew`.
6. **Rangos de paginas.** Guion doble `--`. Se expande la abreviatura de PubMed
   (`234-8` -> `234--238`) y se sustituye el guion largo Unicode de Springer
   (`34–44` -> `34--44`).
7. **Campos que se descartan** (siguen intactos en `raw/`): `abstract`, `keywords`,
   `url`, `eprint`, `numpages`, `location`, `organization`, `issn`, `note` con PMID,
   `volume`/`number` vacios de IEEE. El PMID queda en la tabla de abajo.
   `ARTICLE-NUMBER` de MDPI se mapea a `pages`, que es como cita la propia revista.
8. **Campos que se conservan en actas:** `editor`, `publisher`, `address`, `series`,
   `isbn`. Aportan detalle y no estorban.
9. **Orden.** Alfabetico por clave. Antes `liu2025` iba antes de `liu2021`,
   `wang2025` antes de `wang2019` y `zhang2023`/`2026`/`2025` en ese orden.

## Tabla de procedencia

| Clave (autora) | Archivo raw | Formato | Clave o id del editor | PMID |
|---|---|---|---|---|
| `arand2019pelvicring` | `arand2019pelvicring.nbib` | PubMed nbib | — | 30575034 |
| `chen2024tumorsynthesis` | `chen2024tumorsynthesis.bib` | BibTeX IEEE | `10656868` | — |
| `chen2026foundationvae` | `chen2026foundationvae.bib` | BibTeX arXiv | `chen2026foundationvaes3dct` | — |
| `deman2007catsim` | `deman2007catsim.bib` | BibTeX SPIE | `10.1117/12.710713` | — |
| `grass2016` | `grass2016.nbib` | PubMed nbib | — | 27392768 |
| `haneda2025aapm` | `haneda2025aapm.nbib` | PubMed nbib | — | 41058545 |
| `hinsche2002fluoroscopy` | `hinsche2002fluoroscopy.nbib` | PubMed nbib | — | 11937873 |
| `isensee2021` | `isensee2021.nbib` | PubMed nbib | — | 33288961 |
| `jacob2026lgesynthnet` | `jacob2026lgesynthnet.bib` | BibTeX Springer | `10.1007/978-3-032-17734-6_4` | — |
| `kaiser2014dysmorphism` | `kaiser2014dysmorphism.nbib` | PubMed nbib | — | 25031382 |
| `karageorgos2024ddpm` | `karageorgos2024ddpm.nbib` | PubMed nbib | — | 38963746 |
| `kazerouni2023diffusionsurvey` | `kazerouni2023diffusionsurvey.nbib` | PubMed nbib | — | 37295311 |
| `keating1999iliosacral` | `keating1999iliosacral.nbib` | PubMed nbib | — | 10052785 |
| `lee2014` | `lee2014.nbib` | PubMed nbib | — | 25231682 |
| `liu2021ctpelvic1k` | `liu2021ctpelvic1k.nbib` | PubMed nbib | — | 33864189 |
| `liu2025pipeline` | `liu2025pipeline.nbib` | PubMed nbib | — | 39012731 |
| `mclaren2021corridor` | `mclaren2021corridor.nbib` | PubMed nbib | — | 33649991 |
| `peters2025hybrid` | `peters2025hybrid.nbib` | PubMed nbib | — | 41058534 |
| `ramadanov2025safezone` | `ramadanov2025safezone.bib` | BibTeX MDPI | `jcm14103567` | 40429562 |
| `ramzan2026claim` | `ramzan2026claim.bib` | BibTeX Springer | `10.1007/978-3-032-00652-3_20` | — |
| `ren2022metalinsertion` | `ren2022metalinsertion.nbib` | PubMed nbib | — | 35721310 |
| `rombach2022latentdiffusion` | `rombach2022latentdiffusion.bib` | BibTeX IEEE | `9878449` | — |
| `selles2024marreview` | `selles2024marreview.nbib` | PubMed nbib | — | 38142571 |
| `singhrao2024fiducial` | `singhrao2024fiducial.nbib` | PubMed nbib | — | 38055419 |
| `smith2006iliosacral` | `smith2006iliosacral.nbib` | PubMed nbib | — | 16418646 |
| `templeman1996proximity` | `templeman1996proximity.nbib` | PubMed nbib | — | 8769451 |
| `vanbosse2011pelvicpositioning` | `vanbosse2011pelvicpositioning.nbib` | PubMed nbib | — | 21365336 |
| `wagner2017` | `wagner2017.bibtex` | BibTeX Wiley | `https://doi.org/10.1002/jor.23554` | — |
| `wang2019cochlear` | `wang2019cochlear.bib` | BibTeX Springer | `10.1007/978-3-030-32226-7_14` | — |
| `wang2025adaptiveweighting` | `wang2025adaptiveweighting.bib` | BibTeX IEEE | `10887049` | — |
| `wasserthal2023` | `wasserthal2023.bib` | BibTeX RSNA | `doi:10.1148/ryai.230024` | — |
| `wu2022xcist` | `wu2022xcist.bib` | BibTeX IOP | `Wu_2022` | 36096127 |
| `xie2024implantsegmentation` | `xie2024implantsegmentation.nbib` | PubMed nbib | — | 39107679 |
| `yun2026simulationdriven` | `yun2026simulationdriven.nbib` | PubMed nbib | — | 41699969 |
| `zhao2012` | `zhao2012.nbib` | PubMed nbib | — | 22610442 |
| `zhang2023controlnet` | `zhang2023controlnet.bib` | BibTeX IEEE | `10377881` | — |
| `zhang2025diffboost` | `zhang2025diffboost.bib` | BibTeX IEEE | `10804854` | — (ver "Cambio de raw de DiffBoost") |
| `zhang2026pediclescrew` | `zhang2026pediclescrew.bib` | BibTeX SAGE | `doi:10.1177/08953996261443500` | 42141954 |
| `zwingmann2009navigated` | `zwingmann2009navigated.nbib` | PubMed nbib | — | 19034594 |

## Alta de tres fuentes (2026-09-08)

La autora pego tres archivos nuevos en `refs/raw/`, que es como se anade una fuente
segun la regla 9. Con su autorizacion explicita se renombraron al estilo del resto
(`apellidoANIOpalabraclave`); el CONTENIDO de los raw no se toco.

| Nombre entregado | Nombre en el repo | PDF en `papers/` |
|---|---|---|
| `hinsche2002.nbib` | `hinsche2002fluoroscopy.nbib` | si |
| `mclaren2021.nbib` | `mclaren2021corridor.nbib` | si |
| `templeman1996.nbib` | `templeman1996proximity.nbib` | **no** |
| `kaiser2014.nbib` | `kaiser2014dysmorphism.nbib` | si (alta del 2026-09-08) |

`templeman1996proximity` entra a `refs.bib` con metadatos completos desde el raw, pero
sin PDF. Es un estado de acceso, no un descarte.

**Dos avisos de BibTeX, ambos correctos y ambos sin arreglo posible:**
`Warning--there's a number but no volume` en `hinsche2002fluoroscopy` y
`templeman1996proximity`. *Clinical Orthopaedics and Related Research* de esa epoca
numeraba por fasciculo sin volumen, y el raw lo confirma: trae `IP` y no trae `VI`.
Poner un volumen seria inventarlo. La cita sale bien impresa: `(395):135--144, 2002`.

**Subtitulo de revista recortado en `mclaren2021corridor`.** El raw da
`JT - European journal of orthopaedic surgery & traumatology : orthopedie traumatologie`.
Se conserva `European Journal of Orthopaedic Surgery \& Traumatology` y se descarta el
titulo paralelo en frances que anade NLM. Es la regla 4 (nombre oficial completo), no
una correccion de contenido.

## Lo que el raw CONFIRMO

- **Los 27 DOIs.** Ninguno cambio. Todos coinciden con el `raw` correspondiente.
- **Los tres fasciculos que se perdian por usar `issue`:** `liu2021ctpelvic1k` 16(5),
  `xie2024implantsegmentation` 24(1), `zhang2026pediclescrew` 34(4).
- **`deman2007catsim` volume 6510**, que faltaba y estaba marcado como pendiente.
- **`wu2022xcist` `pages = {194002}`**, que el registro de PubMed no traia: el .bib de
  IOP lo confirma junto con volumen 67 y numero 19.
- **`ramadanov2025safezone` 14(10):3567** y el titulo con los dos puntos, desde el .bib
  de MDPI que sustituyo al .txt degradado.
- Fasciculos que `refs.bib` ya traia y ahora tienen respaldo: `singhrao2024fiducial`
  51(1), `smith2006iliosacral` 31(2), `vanbosse2011pelvicpositioning` 469(6),
  `yun2026simulationdriven` 53(2).

## Campos RETIRADOS por falta de respaldo (2026-09-07)

Se aplico la regla de precedencia. El .bib oficial de Springer **no trae `series` ni
`volume`** en sus capitulos de actas: su exportador los omite. Por eso las tres actas
de Springer (`jacob2026lgesynthnet`, `ramzan2026claim`, `wang2019cochlear`) no llevan
serie ni volumen.

**Decision de la autora (2026-09-07): el asunto queda CERRADO.** No se persiguen esos
volumenes en otra fuente y los valores que tenian no se conservan aqui, para que nadie
los reintroduzca sin respaldo en `refs/raw/`. Si algun dia se quisieran, se empieza por
pegar en `refs/raw/` un archivo del editor que si los traiga.

**Ningun campo queda ya sin respaldo.** `refs.bib` no lleva ninguna marca: ni
`% VERIFICAR` ni `% NOTA`.

**Aviso sobre los ISBN.** Al sustituir los raw de Springer por los oficiales, el ISBN
de `jacob2026lgesynthnet` paso de `978-3-032-17733-9` a `978-3-032-17734-6` y el de
`wang2019cochlear` de `978-3-030-32225-0` a `978-3-030-32226-7`. Son el ISBN impreso y
el electronico del mismo volumen; se conserva el del raw oficial.

**`ramadanov2025safezone`: RESUELTO el 2026-09-07.** La autora sustituyo el `.txt`
degradado por el `.bib` real de MDPI y borro el `.txt`. El raw confirma volumen 14,
numero 10, articulo 3567 y el DOI que ya estaba, y confirma que el titulo **si** lleva
los dos puntos (`Placement: A CT-Based`). MDPI usa `ARTICLE-NUMBER = {3567}`; se mapea
a `pages`, que es como cita la propia revista. Se descartan `url`, `issn` y `abstract`.
Importa porque es la fuente de la implicancia #7, la mas urgente del proyecto.

## Fuentes que siguen sin PDF

`zhang2026pediclescrew` y `templeman1996proximity` no estan en `papers/`. Sus metadatos
**si** quedaron completos desde el raw del editor. Falta de PDF es estado de acceso, no
motivo de descarte.

**`wang2025adaptiveweighting` YA TIENE PDF** desde el 2026-09-08. Era la unica fuente de
nivel 1 sin texto completo y el origen de la implicancia #1.

## Alta de van den Bosch (2026-09-08)

`refs/raw/vandenbosch2002.nbib` (PMID 12131388) ->
`refs/clean/vandenbosch2002.bib` -> `refs.bib`. Alta por el encargo de lectura e
integracion de la autora. Autores de FAU; titulo de TI; revista de JT; ano de DP;
volumen 53 de VI; numero 1 de IP; paginas 44-8 de PG expandidas a 44--48;
DOI de AID. PDF local completo. Ningun campo completado desde otra fuente.

## Alta de Keating (2026-09-08)

`refs/raw/keating1999iliosacral.nbib` (PMID 10052785) ->
`refs/clean/keating1999iliosacral.bib` -> `refs.bib`. Autores de FAU; titulo de TI;
revista de JT; ano de DP; volumen 13 de VI; numero 2 de IP; paginas 107-13 de PG
expandidas a 107--113; DOI de AID. Texto completo local en DOCX, sin paginacion
conservada. Ningun campo bibliografico se completo desde el DOCX.

## Alta de cuatro fuentes de geometria sacra (2026-09-11)

Orden explicita de la autora: anadir a `refs.bib` las cuatro fuentes cuyo raw ya estaba en
`refs/raw/` y cuya ficha se leyo el 2026-09-08. `refs.bib` pasa de 36 a 40 entradas; el
diff solo anade estas cuatro. Motivo: la decision #41 (geometria parametrica) usa calibres
y longitudes que estas fuentes publican.

- `refs/raw/grass2016.nbib` (PMID 27392768) -> `refs/clean/grass2016.bib`. Autores de FAU
  (`Schröder` como `Schr\"{o}der`), titulo de TI sin punto final, revista de JT en nombre
  oficial (`Clinical Orthopaedics and Related Research`, regla 4), ano de DP, volumen 474,
  numero 10, paginas 2304-11 -> 2304--2311, DOI de LID. **Aviso de clave:** la clave de la
  autora es `grass2016` (doble s), pero el primer autor en el raw es **Gras**, Florian. Se
  conserva la clave (regla 1: la define la autora y la usan la ficha y `_index.md`); el
  campo `author` sale del raw, que es lo que se imprime.
- `refs/raw/lee2014.nbib` (PMID 25231682) -> `refs/clean/lee2014.bib`. **Aviso de ano:** el
  raw da `DP - 2015 Feb` y `DEP - 20140917` (publicacion electronica en 2014). El campo
  `year` es **2015** (fecha del fasciculo); la clave `lee2014` se conserva por la regla 1 y
  corresponde a la fecha electronica. Revista de JT recortada a `Journal of Orthopaedic
  Research` (se descarta el subtitulo de NLM, como en `mclaren2021corridor`). Paginas
  277-82 -> 277--282.
- `refs/raw/wagner2017.bibtex` (Wiley) -> `refs/clean/wagner2017.bib`. El `doi` del raw
  viene como URL (`https://doi.org/10.1002/jor.23554`); se guarda el identificador sin
  prefijo, igual que en el resto. Paginas 2577-2584 -> 2577--2584. Se descartan
  `keywords`, `url`, `eprint` y `abstract` (regla 7).
- `refs/raw/zhao2012.nbib` (PMID 22610442) -> `refs/clean/zhao2012.bib`. Revista de JT
  recortada a `European Spine Journal` (subtitulo de NLM descartado). Paginas 1807-14 ->
  1807--1814. DOI de AID (el raw no trae `LID`).

Titulos pasados a Title Case entre dobles llaves (regla 3). **Ningun campo se completo
desde otra fuente.**

## Alta de TotalSegmentator (2026-09-14)

Orden explicita de la autora: la autora pego `refs/raw/wasserthal2023.bib` y `papers/wasserthal2023.pdf`
para citar la herramienta de mascaras del Objetivo 2 (decision 2026-09-14, #48-#50). `refs.bib` pasa de
40 a 41 entradas; el diff solo anade esta.

- `refs/raw/wasserthal2023.bib` (exportador RSNA, clave del editor `doi:10.1148/ryai.230024`) ->
  `refs/clean/wasserthal2023.bib`. Clave `wasserthal2023` = nombre de archivo que puso la autora (regla 1).
  Autores, titulo, revista (`Radiology: Artificial Intelligence`), volumen 5, numero 5, `pages = {e230024}`
  y DOI tal como vienen en el raw. Titulo entre dobles llaves (regla 3; ya venia en Title Case). Se
  descartan `URL`, `eprint` y `abstract` (regla 7). **Ningun campo se completo desde otra fuente.**
- Compilacion de `tesis/main.tex` tras el alta: 4 paginas, 41 `\bibitem`, 0 citas indefinidas; los dos
  avisos de BibTeX son los ya conocidos (`hinsche2002fluoroscopy`, `templeman1996proximity`).

## Alta de nnU-Net (2026-09-14)

La autora pego `refs/raw/isensee2021.nbib` y `papers/isensee2021.pdf` y ordeno aplicarlo a `main.tex`: el
README de TotalSegmentator pide citar nnU-Net (#55). `refs.bib` pasa de 41 a 42 entradas.

- `refs/raw/isensee2021.nbib` (PMID 33288961) -> `refs/clean/isensee2021.bib`. Clave = nombre de archivo de la
  autora (regla 1). Autores de FAU con punto en las iniciales (`Kohl, Simon A A` -> `Kohl, Simon A. A.`); titulo
  de TI sin punto final y en Title Case entre dobles llaves, conservando `nnU-Net` (regla 3); revista de JT
  (`Nature methods`) en nombre oficial `Nature Methods` (regla 4); ano de DP (2021; `DEP` 20201207 es la fecha
  electronica); volumen 18 de VI; numero 2 de IP; paginas 203-211 -> 203--211; DOI de LID. **Ningun campo se
  completo desde otra fuente.**

## Cambio de raw de DiffBoost (2026-09-15)

La autora sustituyo `refs/raw/zhang2025diffboost.nbib` (PubMed, PMID 40030730) por
`refs/raw/zhang2025diffboost.bib` (exportador IEEE, clave del editor `10804854`), junto con el PDF de la
version publicada en IEEE TMI. **`refs/clean/zhang2025diffboost.bib` no cambia:** el raw nuevo confirma los
8 autores, el titulo, `IEEE Transactions on Medical Imaging`, 2025, volumen 44, numero 9, paginas
3670-3682 (-> `3670--3682`) y el DOI `10.1109/TMI.2024.3519307`. Se descarta `keywords` (regla 7). El raw
IEEE no trae PMID, asi que la columna PMID queda en `—`: 40030730 solo consta en el `.nbib` retirado, que
sigue en el historial de git. `refs.bib` regenerado sin diferencias.

## Nota sobre `chen2026foundationvae` (alta del 2026-09-15)

Primera entrada del repositorio que **no es un articulo ni unas actas**: es un preprint de arXiv,
y por eso es la unica con tipo `@misc`. Tres cosas quedan registradas aqui y no en `refs.bib`:

1. **`url` descartado por la regla 7**, que ya lo descartaba para todas las entradas. Conviene saber
   que ademas venia roto en el raw (`httpsarxiv.orgabs2605.30893`, sin `://` ni `/`), artefacto de
   copiar del cuadro de citacion de arXiv. No se corrigio: `raw/` no se edita y el campo no se usa.
2. **`eprint`, `archivePrefix` y `primaryClass` SI se conservan**, como excepcion declarada a la
   regla 7. En las demas entradas el `eprint` sobraba porque habia DOI o revista; aqui es el unico
   localizador que trae el raw. Sin el, la entrada no se puede encontrar.
3. **El paper fue aceptado en ICML 2026**, pero el raw solo respalda el preprint de arXiv, asi que por
   la regla de precedencia la entrada cita el preprint. La evidencia de la aceptacion es el pie de la
   primera pagina del PDF, literal: *"Proceedings of the 43 rd International Conference on Machine
   Learning, Seoul, South Korea. PMLR 306, 2026."* **Ese pie es la unica fuente del numero de volumen
   que hay en disco**: la pagina de PMLR no se encontro al buscar (2026-09-15), asi que `PMLR 306` no
   esta confirmado contra el editor. Para citar la version publicada hay que pegar su raw en
   `refs/raw/`.

   **DECIDIDO (2026-09-15, decision 2026-09-15 (3) en `docs/01-decisiones.md`):** se cita el preprint, como
   excepcion declarada, porque es la unica version en `refs/raw/`. Se reabre si el paper llega a citarse en
   `main.tex`: entonces se consigue el raw de las actas antes de escribir la frase. El numero `PMLR 306` **no
   se usa en ninguna parte** hasta confirmarlo contra el editor.

   **Correccion (2026-09-15):** una version anterior de esta nota decia que era "el mismo caso que
   `isensee2021`". Es el **caso espejo**, no el mismo. En `isensee2021` el raw y `refs.bib` traian ya la
   version publicada (Nature Methods 18(2):203-211, PMID 33288961) y lo que estaba desalineado era el
   **PDF**, que era el preprint de arXiv; se resolvio consiguiendo el PDF publicado. Aqui pasa al reves:
   el PDF es el que lleva el pie de ICML y el **raw** es el de arXiv. Lo unico comun es la leccion: un
   mismo trabajo con dos versiones, y `raw/`, `papers/` y `refs.bib` tienen que apuntar a la misma.

La clave del editor (`chen2026foundationvaes3dct`) se descarta por la regla 1, como siempre.
