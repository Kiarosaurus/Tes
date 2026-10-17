# Respuesta del redactor — capitulo1 — r11

Archivo: `overleaf/secciones/capitulo1.tex`. Encargo: `redaccion/ENCARGO_2026-10-16.md`. El capitulo no tiene `\REVVISUAL`
ni `\GAPDATO` de realismo (lo confirma la auditoria de trazabilidad), asi que el encargo no exige cambios aqui. Ningun
hallazgo pide lo contrario de algo APLICADO en `capitulo1-r10-respuesta.md` (ES-6 solo cambia la construccion de la
oracion del recalculo; conserva "reproduce", no "se calcularon con", como decidio r10). No se toco `capitulo3.tex`.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 | guia | APLICADO | Beer--Lambert sin simbolo nuevo: "la integral de $\mu$ a lo largo del rayo: $\int_{\mathrm{rayo}} \mu\,\mathrm{d}l=\ln(N_{\mathrm{in}}/N_{\mathrm{d}})$". $L$ queda solo para la longitud del corredor (BITACORA 2026-10-03). Se descartaron $\Gamma$ (ya es $\Gamma_M$ en `capitulo3.tex`:276) y $s$ (ya es $s_n$). |
| ES-1 | estilo | APLICADO | Las cuatro oraciones "La Seccion..." se reescriben en tres con aperturas distintas ("Que mide una tomografia...", "De la fijacion iliosacra...", "Los modelos de difusion..."), conservando cada `\ref` en el nombre de su seccion. Se revisaron las aperturas de :11-13 juntas (PAT-119). |
| ES-2 | estilo | APLICADO | El parrafo de HU se parte en "En la cohorte primaria, con el recorte por defecto...": el nuevo parrafo tiene la mediana 0.42 y la consecuencia para la medicion del corredor (PAT-58). Sin cambios de cifra. |
| ES-3 | estilo | APLICADO | "Esa regla no se aplico: su desenlace cambia..." (hecho, no metadeclaracion; DEC 2026-10-15 pto 1). Se prefirio "no se aplico" a "no es aplicable" porque la no aplicacion fue una decision fechada, no una propiedad de la regla. |
| ES-6 | estilo | APLICADO | "El recalculo con la prueba bilateral de `scipy.stats.fisher_exact`, en la version 1.15.3 de SciPy, cuya convencion es la *minlike*, reproduce los valores de las cuatro tablas." Se conserva la clausula de la convencion (registro §6:71-74). |
| ES-7 | estilo | APLICADO | "...son descriptivos, no se corrigen por multiplicidad y solo pueden bajar la categoria del desenlace, nunca subirla". |

Bajos: ES-4 APLICADO con reordenamiento (el motivo de excluir la densidad pasa a la primera oracion; Arand et al. como
sujeto con verbo "describen"; cierre "Esa diferencia motiva evaluar la densidad osea en un trabajo futuro").
ES-5 APLICADO. ES-8 APLICADO. Lint E-P1 en :53 (antes :51, se movio por el parrafo partido): falso positivo, igual
que en r10; es la definicion propia de la compresion ("500 HU"), con fuente `experiments/registro/registro_metodos_2026-10-15.md`:7-16.

Lint: `python scripts/lint_redaccion.py capitulo1 --compilar` PASA (alta 0, media 0, baja 1; GAP 0/0/0; 164 paginas).
GAP abiertos: ninguno. GAP cerrados: ninguno. Sin cambios de titulos.

## Decisiones de redaccion

- En una ecuacion del marco donde el dominio de integracion solo necesita un nombre, se usa un subindice textual
  (`\int_{\mathrm{rayo}}`) en vez de una letra nueva, para no reusar simbolos reservados ($L$ para la longitud del
  corredor, $\Gamma_M$ para el termino de artefacto, $s_n$ en la difusion) (PAT-14).
- Una regla preinscrita que se dejo sin efecto por decision se escribe "no se aplico" (hecho fechado), no "se declaro
  no aplicable" ni "no es aplicable" (PAT-5).
