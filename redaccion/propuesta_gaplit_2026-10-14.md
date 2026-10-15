# Fuentes pendientes para los `\GAPLIT` del documento — actualización 2026-10-14

Esta versión contiene únicamente la fuente que todavía falta. Se retiraron todas las fuentes que ya tienen raw,
entrada normalizada, ficha y uso en la redacción. Esto incluye `fay2010two` y las dos fuentes versionadas del
software XCIST (`xcist2026main` y `xcist2025example`). Niu--Li--Wang permanece porque el artículo no es accesible
de momento.

**Regla bibliográfica.** El DOI indicado aquí no autoriza por sí solo una entrada. La autora debe aportar el raw
del editor y el PDF; `refs/raw/` manda sobre esta propuesta. La columna «Procedencia del DOI» identifica la página
donde se verificó el identificador, no un metadato que deba copiarse a mano.

## Resumen residual

| # | Marca vigente | Fuente propuesta | DOI | Procedencia del DOI | Qué falta |
|---|---|---|---|---|---|
| 1 | `capitulo2.tex`, origen del esquema multiventana de MAR | C. Niu, M. Li y G. Wang, “Multiple window learning for CT metal artifact reduction”, *Proc. SPIE* 11840, 1184015 (2021) | `10.1117/12.2596239` | [página del artículo en SPIE Digital Library](https://ebooks.spiedigitallibrary.org/conference-proceedings-of-spie/11840/1184015/Multiple-window-learning-for-CT-metal-artifact-reduction/10.1117/12.2596239.full); autores corroborados en la [página de publicaciones de Chuang Niu](https://chuangniu.info/publications/) | PDF y raw del editor cuando sean accesibles; después, ficha `niu2021multiple.md` |

## Esquema multiventana de MAR

La marca permanece porque `wang2025adaptiveweighting` y `li2024` atribuyen el esquema a un trabajo anterior, pero
el repositorio aún no contiene el PDF ni el raw de esa fuente primaria. La página de SPIE incorpora el DOI en su
propia URL y el registro bibliográfico del autor confirma la autoría de Chuang Niu, Mengzhou Li y Ge Wang. No se
debe cerrar la marca desde las citas secundarias.

## Evaluación de impacto

Las fuentes versionadas de XCIST cierran la trazabilidad bibliográfica de los commits y de la licencia sin cambiar
el alcance, los supuestos ni el *baseline*. El fallo de serialización y el parche continúan declarados como
observaciones de la ejecución local. **Sin implicancias nuevas sobre la tesis.**
