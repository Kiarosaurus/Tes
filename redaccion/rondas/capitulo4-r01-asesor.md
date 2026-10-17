# Asesor — capitulo4 r01

Entradas: `overleaf/secciones/capitulo4.tex` (244 l.), `capitulo4-r01-lint.md` (PASA; GAP lit=0 dato=1 dec=0),
`capitulo4-r00-respuesta.md` (notas 1 y 2 para la autora), `ENCARGO_2026-10-16.md` (meta: solo el `\GAPLIT` de Niu).

| # | GAP (linea) | tipo | clase A/B/C/D | propuesta (1-2 lineas) | fuente |
|---|---|---|---|---|---|
| 1 | l. 172, §Analisis anadidos: "medianas por brazo del coeficiente de Sorensen-Dice y del cambio relativo de volumen del hueso y del metal..." | `\GAPDATO` | **C -> A** (calculado) | Sustituir el GAP por las medianas de 13 pacientes por brazo (texto abajo). Descriptivo; resumen de columnas ya calculadas por `a20`, sin analisis nuevo sobre la prueba | `experiments/registro/registro_2026-10-16.md` §5; `r_integridad_ea2.py`; CSV `objetivo3/outputs/obj3_pose/a20_test/a20_ea2_test.csv` |
| 2 | l. 105 (`tab:res-tost`, fila hierro) y su texto: "No equivalencia, menor" | nota r00 n.o 1 | **A** | Se mantiene. Es la aplicacion literal de D15 (IC90 [-4405.9, -3222.6] entero fuera de +-196.3), y la misma DEC ya rotula asi a `run04_60k`. El rotulo de `resultados_prueba_v1.md` es el texto anterior de `a24`, superado por D15 | `01-decisiones.md` 2026-10-15 pto 15 (l. 2615-2619); `resultados_prueba_v1.md` tabla E-A2 |
| 3 | l. 43, §Obj 1: "los guiones de muestreo del modelo distribuido fijan su salida entre -1000 y 1000 HU" sin cita | nota r00 n.o 2 | **B** | Decidir como se atribuye un hecho que solo consta en el codigo del modelo distribuido (bundle MONAI). La regla de bitacora del 2026-10-05 pide un `\GAPLIT` y la meta del encargo no lo admite | #93 (CERRADA, l. 6771-6789: "la cita del bundle ... pendiente de la autora"); BITACORA §2, 2026-10-05; ficha `guo2025maisi` fila 4 |

No vi afirmaciones de decision no tomada escritas como hecho. Lo comprobe en la discusion y las limitaciones
(l. 205-244): el acotamiento del reclamo se apoya en DEC 2026-10-16, la lectura en dos niveles en DEC 2026-10-15 (3),
y #196 en DEC 2026-10-16 (2).

## Textos para el redactor (clase A y D)

**#1 (l. 172).** Reemplazar la ultima oracion del parrafo ("Los componentes de la \emph{bone integrity} ... sin un
resumen registrado \GAPDATO{...}") por:

> Los componentes de la \emph{bone integrity} y de la \emph{metal integrity}, descriptivos, se resumen con el valor de
> cada paciente: la mediana de sus cinco semillas en el sintetizador y la de sus dos réplicas en el protocolo físico. En
> el hueso, la mediana del coeficiente de Sørensen-Dice entre los 13 pacientes fue de 0.677 en el sintetizador y de
> 0.800 en el protocolo físico con titanio, y la del cambio relativo de volumen, de 0.098 y 0.121. En el metal, el
> coeficiente fue de 0.862 y 0.856. El cambio de volumen fue de $-0.190$ en el sintetizador, que deja menos vóxeles
> sobre 2500~HU que la máscara $M$, y de $+0.283$ en el protocolo físico, que deja más; con hierro, de $+1.683$. Como
> el artefacto cambia los HU de $G$, ninguna de estas cifras indica por sí sola un resultado peor
> (Sección~\ref{sec:ap-reconstruccion}).

Cifras, n y fuente: n = 13 pacientes por brazo; `registro_2026-10-16.md` §5. Los rangos (min-max) estan ahi por si el
redactor prefiere una tabla: sintetizador hueso SDC 0.586-0.775, dVol -0.094 a 0.340, metal SDC 0.769-0.903, dVol
-0.367 a -0.084; Ti 0.736-0.876, -0.002 a 0.319, 0.820-0.892, -0.117 a 0.334. Los de `run04_60k` (estado final) estan
en el registro y no hacen falta en el texto. La copia y pegado da 1 y 0 por construccion, y no se reporta. Regla 5 de
`overleaf/CLAUDE.md`: el redactor cita como fuente `registro_2026-10-16.md` §5 en su tabla de cifras. Al aplicar, el
MAPA queda en -1 `\GAPDATO`.

**#2 (l. 105).** No cambia el texto. Si se quiere blindar la celda ante un revisor, basta con anadir al pie de
`tab:res-tost` o al texto: "categoría según la regla de desenlaces fijada el 15 de octubre, aplicada como descripción
a esta sensibilidad". El texto ya trata como descriptivo todo lo que no es el contraste primario (D15: "lo demas,
descriptivo"). Fuente: DEC 2026-10-15 pto 15.

## Decisiones para la autora (clase B), con texto listo para 01-decisiones.md

**#3. Atribucion del rango de salida del autoencoder de Guo et al. (#93).**

- **Lo que hay:** el hecho ([-1000, 1000] HU) consta en `scripts/sample.py` del bundle `maisi_ct_generative`,
  descargado con `monai.bundle` el 2026-09-20 sin version registrada (#93; `experiments/KHIPU.md`:763). El articulo no
  lo declara (ficha: NO ENCONTRADO), pero si remite su codigo: "The code is available at MONAI Tutorial." (ficha
  `guo2025maisi`, fila 4, nota al pie p. 4430). No hay raw del bundle en `refs/raw/`.
- **Choque:** BITACORA §2 2026-10-05 dice que un hecho observado en codigo publicado entra "con los identificadores en
  prosa ... y un solo `\GAPLIT` por la referencia del software". La meta del ENCARGO 2026-10-16 deja como unico GAP
  el `\GAPLIT` de Niu. El redactor omitio el `\GAPLIT`, y eso se aparta de la bitacora sin decision.
- **Propuesta del asesor: (a).** El hecho entra sin cita de software, con los identificadores en prosa y la remision
  del articulo como puente. El rango no es una cifra del articulo sino una propiedad del codigo que se inspecciono. Lo
  que decide la compuerta es la cota, que es medicion propia (`p1_maisi_cota.csv`). Por eso basta con dejar trazable
  donde se leyo, y la falta de version se declara.
- **Alternativas:** (b) la autora pega en `refs/raw/` la referencia del repositorio de modelos de MONAI (precedente:
  `xcist2026main`, `xcist2025example`) y el texto la cita, lo que es mas limpio pero exige una entrada nueva que solo
  ella puede anadir. (c) Aplicar la bitacora tal cual con un `\GAPLIT`, lo que incumple la meta del documento.
- **Afecta a otros capitulos:** si. La regla de bitacora del 2026-10-05 es transversal. `capitulo3.tex`:93 ("Antes de
  correr ese modelo se comprobo su rango de salida") no dice donde se comprobo y deberia llevar la misma atribucion.
  `capitulo2.tex`:94 ("el articulo no declara su rango de intensidades") es compatible con las tres opciones y no
  cambia. `capitulo1.tex`:157 no menciona el rango.
- **Texto listo para `01-decisiones.md`:**

> ## 2026-10-16 (5) — Atribucion del rango de salida del autoencoder de Guo et al. (#93; capitulo4-r01)
>
> 1. El rango [-1000, 1000] HU del autoencoder de `guo2025maisi` se escribe como hecho observado en los guiones del
>    modelo distribuido (bundle `maisi_ct_generative` de MONAI, `scripts/sample.py`, descargado el 2026-09-20, sin
>    version registrada), con esos identificadores en prosa. Se cita `guo2025maisi` solo por la remision de su codigo
>    a MONAI (nota al pie, p. 4430) y por la ausencia del rango en el articulo, no por el rango. No se crea entrada
>    bibliografica del software ni `\GAPLIT`.
> 2. Esto es una excepcion acotada a la regla de bitacora del 2026-10-05 (un `\GAPLIT` por la referencia del
>    software). Se justifica porque la cifra que decide (la cota de 42.24 HU) es medicion propia, y porque el
>    documento final no admite mas GAP que el `\GAPLIT` de Niu, Li y Wang. La falta de version se declara en el texto.
> 3. Aplica a `capitulo4` §Obj 1 y a `capitulo3` `sec:obj1` (l. 93), que debe decir donde se comprobo el rango con la
>    misma formula. #93 queda sin pendientes de redaccion.

Frase sugerida si se aprueba (a), para cap. 4 l. 43 (y en forma corta para cap. 3 l. 93):

> El artículo no menciona el rango de intensidades y remite su código a los tutoriales de MONAI \cite{guo2025maisi};
> el guion de muestreo del modelo distribuido allí (\texttt{maisi\_ct\_generative}, descargado el 20 de septiembre de
> 2026, sin versión registrada) fija su salida entre $-1000$ y 1000~HU.

## Calculos hechos (clase C -> A) y calculos no baratos que quedan

**Hecho: `experiments/registro/r_integridad_ea2.py`** (local, segundos; `registro_2026-10-16.md` §5; fila nueva en
`experiments/objetivo3/EXPERIMENTOS.md` §6c).

- **Que hace:** resume `hueso_sdc`, `hueso_dvol`, `metal_sdc` y `metal_dvol` del CSV congelado de v1. Agrega con la
  regla de `a24_contrastes.py`: mediana por paciente de 5 semillas o de las replicas A y B, y despues mediana, minimo y
  maximo entre los 13.
- **Control de regresion:** sobre `amp_HU`, con la misma agregacion, reproduce -301.0 HU (difusor `run04_mejor` menos
  Peters Ti, n = 13) y 183.5 HU (ruido de Peters), las dos de `resultados_prueba_v1.md`. **Reproduce.**
- **Resultado (n = 13, medianas):**

| brazo | hueso SDC | hueso dVol | metal SDC | metal dVol |
|---|---|---|---|---|
| sintetizador `run04_mejor` | 0.677 | 0.098 | 0.862 | -0.190 |
| sintetizador `run04_60k` | 0.684 | 0.091 | 0.963 | -0.021 |
| Peters Ti | 0.800 | 0.121 | 0.856 | 0.283 |
| Peters Fe | 0.707 | 0.043 | 0.518 | 1.683 |
| copia y pegado | 1.000 | 0.000 | 1.000 | 0.000 |

- **Estatus:** descriptivo y posterior. El resumen se calculo hoy, despues de ver los desenlaces, pero sobre
  componentes que el diseno ya declaraba descriptivos ("se reportan", cap. 3 l. 371). No hay analisis nuevo sobre la
  particion de prueba ni cambia ninguna cifra confirmatoria. Lo declaro como excepcion a la cabecera del registro
  ("nada toca la particion de prueba").
- **Pendiente fuera de mi permiso:** una fila en `experiments/objetivo3/visto.md` (2026-10-16, componentes de
  integridad E-A2, prueba, v1, decisiones afectadas: ninguna), que exige D-extra 4.
- **Evaluacion de impacto (regla 13):** sin implicancias nuevas sobre la tesis. Los valores no tocan ningun desenlace
  y el diseno no fija umbral para ellos.

**No baratos que quedan:** ninguno.

TOTAL A=2 B=1 C=0 D=0 | GAP que quedarian si se aplica todo: lit=0 dato=0 dec=0
(A incluye #1, que paso de C a A con el calculo. Si la autora elige (c) en #3, quedaria lit=1.)
