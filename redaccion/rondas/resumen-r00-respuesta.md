# resumen-r00 — respuesta del redactor (redaccion inicial)

Modo: redactar. Archivo: `overleaf/secciones/resumen.tex` (antes, plantilla). Pedido explicito de la autora:
DEC 2026-10-16 (7) pto 4 (cede la regla 7 de `overleaf/CLAUDE.md`). `abstract.tex` no se toco.

No hay reportes de revision en esta etapa: la tabla de hallazgos queda vacia.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| — | — | — | Redaccion inicial; sin reportes de ronda |

## Estructura (P-R3)

| Bloque IMRyC | Oraciones | Contenido |
|---|---|---|
| Introduccion | 3 | escasez de anotaciones con metal; plausibilidad antes que utilidad y brecha; proposito |
| Marco metodologico | 4 | compuerta; muestreador y comparacion con dos series clinicas; sintetizador; comparacion por equivalencia y control |
| Resultados | 6 | compuerta; Wasserstein-1 (dos oraciones); diferencia media; intervalo y desenlace; copia y pegado |
| Conclusiones | 3 | resultados acotados; realismo visual no reclamado; segmentacion fuera de alcance |

P-R2: sin `\cite`, `\ref`, figuras ni tablas. Siglas reemplazadas por su forma completa: "tomografia computarizada"
(TC), "unidades Hounsfield" (HU), "intervalo de confianza" (IC); SAP, MAR y S1 no se nombran; las series de la
referencia clinica se describen ("serie clinica con navegacion" / "sin navegacion") y no se nombran autores. Se
conservan nombres propios: CTPelvic1K, Wasserstein-1, Wilcoxon y *streak amplitude* (termino fijo en ingles, E-T1).

## Fuente de cada cifra (copiada, no recalculada)

| Cifra en el resumen | Fuente |
|---|---|
| 25 unidades Hounsfield (criterio de la compuerta) | `introduccion.tex`:37; `capitulo4.tex`:14; `conclusiones.tex`:14 |
| seis combinaciones, 34 pacientes de prueba | `capitulo4.tex`:14, Tabla `tab:res-compuerta`; `conclusiones.tex`:14 |
| 61.72 (mejor media, en HU) | `capitulo4.tex`:31 y :37; `conclusiones.tex`:14 |
| unos 12 mm (banda) | `introduccion.tex`:41 |
| 72 pacientes, 3 600 poses | `capitulo4.tex`:49, Tabla `tab:res-sap`; `conclusiones.tex`:16 |
| 0.206 y 0.230 grados (Wasserstein-1 frente a serie navegada y convencional) | `capitulo4.tex`:65 y :80; `conclusiones.tex`:16 |
| 0.395 grados (distancia entre las dos series) | `capitulo4.tex`:62-63 y :80; `conclusiones.tex`:16 |
| intervalos por remuestreo que no ordenan las series | `capitulo4.tex`:82; `conclusiones.tex`:16 |
| 13 pacientes de prueba sin metal | `capitulo4.tex`:94; `introduccion.tex`:52 |
| $-301.0$ HU (diferencia media pareada) | `capitulo4.tex`:94 y :106; `conclusiones.tex`:18 |
| IC 90 % de $-477.0$ a $-124.9$ | `capitulo4.tex`:94 y :106; `conclusiones.tex`:18 |
| margen 196.3 | `capitulo4.tex`:94; `conclusiones.tex`:18 |
| $p = 0.000122$ (Wilcoxon, copia y pegado) | `conclusiones.tex`:20 |

Lecturas copiadas de `conclusiones.tex` sin endurecer ni suavizar: compuerta negativa que "llevo la sintesis al
dominio de imagen" (:8); Objetivo 2 descriptivo, sin regla de decision (:16, :24); Objetivo 3 no concluyente con
amplitud menor que el protocolo fisico con titanio (:18, :24); copia y pegado como control de cordura que no cuenta a
favor (:20, :24); realismo visual no reclamado por juicio de la autora y decision con su asesor de no redisenar (:30);
perfil que no reproduce la caida de la amplitud con la distancia (:36); segmentacion fuera de alcance (:38).
"Ninguno de los enfoques revisados produce a la vez una distribucion de poses del implante y la apariencia de su
artefacto": `introduccion.tex`:62.

Se omitieron, por el limite de oraciones de P-R3, el intervalo del 95 % de la compuerta (55.12-68.99), la cota de
saturacion del generador de Guo et al. (42.24) y el caso negativo de los 15 corredores estrechos (3.3 % frente a
64.2 %); todos constan en `capitulo4.tex` y `conclusiones.tex`.

## Lint

`python scripts/lint_redaccion.py resumen --compilar`: PASA, alta=0, media=0, baja=2 (E-P1, cifras sin `\ref`;
inevitables porque P-R2 prohibe referencias en el resumen). Compila (193 paginas).

## GAP

Abiertos: ninguno. Cerrados: ninguno.

## Decisiones de redaccion

- En resumen y abstract, las siglas se sustituyen por su forma completa en cada aparicion ("unidades Hounsfield",
  "tomografia computarizada", "intervalo de confianza"); las series de Zwingmann et al. se describen como "serie
  clinica con navegacion" y "serie sin navegacion", sin autores.
- El abstract (P-R4) deberia traducir este texto con las mismas cifras y omisiones.
