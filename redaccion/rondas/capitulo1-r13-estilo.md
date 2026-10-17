# Revision de estilo — capitulo1 — r13

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Texto actual (max 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| ES-1 | media | E-O2, E-M1 | `overleaf/secciones/capitulo1.tex:33` | "Este documento distingue dos dominios: el dominio de proyeccion" | Abrir un parrafo nuevo antes de "Este documento distingue dos dominios": el primero explica la reconstruccion y el segundo define los dominios usados por este trabajo. Patron PAT-58 reincide. |
| ES-2 | media | E-O2, E-M1 | `overleaf/secciones/capitulo1.tex:48-53` | "La tercera conserva las dos ventanas estrechas y sustituye la ventana ancha" | Abrir un parrafo nuevo con "La tercera conserva las dos ventanas estrechas..."; asi, la ecuacion y la explicacion de su pendiente quedan en un bloque propio. Patron PAT-58 reincide. |
| ES-3 | media | E-O2, E-M1 | `overleaf/secciones/capitulo1.tex:135` | "Su unidad es el grado" | Abrir un parrafo nuevo con "Su unidad es el grado": el primero define y operacionaliza la distancia; el segundo interpreta su escala y su ventaja. Patron PAT-58 reincide. |

TOTAL alta=0 media=3 baja=0

## Impresion general
Leido seguido, el capitulo mantiene una voz sobria, precisa y calibrada; no suena informal ni generado.
El unico defecto apreciable es estructural: tres parrafos exceden siete oraciones y acumulan definicion, uso e interpretacion.
No reaparecen las metadeclaraciones, las ambiguedades terminologicas ni los cierres redundantes de rondas anteriores.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Parrafo ampliado hasta superar siete oraciones y reunir mas de una funcion | E-O2, E-M1 | "Este documento distingue dos dominios" | PAT-58 |
