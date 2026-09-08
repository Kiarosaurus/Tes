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
| `deman2007catsim` | `deman2007catsim.bib` | BibTeX SPIE | `10.1117/12.710713` | — |
| `haneda2025aapm` | `haneda2025aapm.nbib` | PubMed nbib | — | 41058545 |
| `jacob2026lgesynthnet` | `jacob2026lgesynthnet.bib` | BibTeX Springer | `10.1007/978-3-032-17734-6_4` | — |
| `karageorgos2024ddpm` | `karageorgos2024ddpm.nbib` | PubMed nbib | — | 38963746 |
| `kazerouni2023diffusionsurvey` | `kazerouni2023diffusionsurvey.nbib` | PubMed nbib | — | 37295311 |
| `liu2021ctpelvic1k` | `liu2021ctpelvic1k.nbib` | PubMed nbib | — | 33864189 |
| `liu2025pipeline` | `liu2025pipeline.nbib` | PubMed nbib | — | 39012731 |
| `peters2025hybrid` | `peters2025hybrid.nbib` | PubMed nbib | — | 41058534 |
| `ramadanov2025safezone` | `ramadanov2025safezone.bib` | BibTeX MDPI | `jcm14103567` | 40429562 |
| `ramzan2026claim` | `ramzan2026claim.bib` | BibTeX Springer | `10.1007/978-3-032-00652-3_20` | — |
| `ren2022metalinsertion` | `ren2022metalinsertion.nbib` | PubMed nbib | — | 35721310 |
| `rombach2022latentdiffusion` | `rombach2022latentdiffusion.bib` | BibTeX IEEE | `9878449` | — |
| `selles2024marreview` | `selles2024marreview.nbib` | PubMed nbib | — | 38142571 |
| `singhrao2024fiducial` | `singhrao2024fiducial.nbib` | PubMed nbib | — | 38055419 |
| `smith2006iliosacral` | `smith2006iliosacral.nbib` | PubMed nbib | — | 16418646 |
| `vanbosse2011pelvicpositioning` | `vanbosse2011pelvicpositioning.nbib` | PubMed nbib | — | 21365336 |
| `wang2019cochlear` | `wang2019cochlear.bib` | BibTeX Springer | `10.1007/978-3-030-32226-7_14` | — |
| `wang2025adaptiveweighting` | `wang2025adaptiveweighting.bib` | BibTeX IEEE | `10887049` | — |
| `wu2022xcist` | `wu2022xcist.bib` | BibTeX IOP | `Wu_2022` | 36096127 |
| `xie2024implantsegmentation` | `xie2024implantsegmentation.nbib` | PubMed nbib | — | 39107679 |
| `yun2026simulationdriven` | `yun2026simulationdriven.nbib` | PubMed nbib | — | 41699969 |
| `zhang2023controlnet` | `zhang2023controlnet.bib` | BibTeX IEEE | `10377881` | — |
| `zhang2025diffboost` | `zhang2025diffboost.nbib` | PubMed nbib | — | 40030730 |
| `zhang2026pediclescrew` | `zhang2026pediclescrew.bib` | BibTeX SAGE | `doi:10.1177/08953996261443500` | 42141954 |
| `zwingmann2009navigated` | `zwingmann2009navigated.nbib` | PubMed nbib | — | 19034594 |

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

`wang2025adaptiveweighting` y `zhang2026pediclescrew` no estan en `papers/`. Sus
metadatos **si** quedaron completos desde el raw del editor. Esto **no** cierra la
implicancia #1: para eso hace falta el texto, no la ficha bibliografica.
