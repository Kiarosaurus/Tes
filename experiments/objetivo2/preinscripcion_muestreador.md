# Preinscripcion del muestreador de poses y de SAP — Objetivo 2

> **Congelado el 2026-09-22, ANTES de calcular ningun Wasserstein-1.** Cumple D-O2.7 de
> `docs/01-decisiones.md`. Mismo procedimiento que `experiments/objetivo3/diseno_A.md` y que el criterio
> de inclusion R1-R3.
>
> Si algo de este documento cambia despues de ver un resultado, **deja de ser preinscripcion** y hay que
> escribirlo como desviacion declarada, con fecha y motivo, en la seccion final.

## 0. Para que sirve este documento

El resultado propio del Objetivo 2 es la distancia entre la distribucion de grados de brecha que produce
el muestreador y las dos distribuciones clinicas de `zwingmann2009navigated`. Esa distancia solo
significa algo si la distribucion de poses se fijo **antes** de medirla. Si se ajustara despues, se
estaria comparando contra lo mismo que se uso para ajustar (D-O2.1, opcion (b) rechazada) y el resultado
seria vacio.

## 1. Cohorte

- **Primaria: 72 casos** — grupos 2 y 3 con QC de nivel (`estado_TS = concordante` y S1 sin tocar FOV).
  Verificado al escribir este documento: la consulta devuelve exactamente 72 casos unicos.
- **Sensibilidad: 49 casos** — grupo 3.
- Los casos con FOV cortado son 4 y todos de grupo 1: **no entran** en ninguna de las dos (#119).

## 2. Eje base

Por caso, la fila de `e9ts_corredor.csv` con `modo = default6mm`, `F_limpieza = 0.0`,
`politica_metal = hueso`. De ella se toman:

- centro `c = (c_x_mm, c_y_mm, c_z_mm)`, direccion `u = (u_x, u_y, u_z)`;
- longitud del corredor `L = L_TS_mejor_mm`, usada solo para fijar la dispersion angular;
- `D_TS_max_mm`, usada solo para la viabilidad de corredor.

**El muestreador no busca trayectoria: perturba una ya medida.**

### 2.1 Anclaje de la pose base

`c_*_mm` es el punto **desde el que se lanzo la busqueda** del corredor, no el punto medio del tramo
oseo encontrado. En unos casos coinciden y en otros no. Antes de perturbar nada, la pose base de cada
caso se **ancla** al punto medio de su tramo de corredor (`sap.pose_base`), y de ese mismo tramo sale la
**longitud del implante**. Es una operacion por caso, previa al muestreo, que usa solo geometria ya
medida. Sin ella, un implante simetrico alrededor de `c` queda descentrado y la identidad "implante
sobre el eje del corredor => brecha 0" deja de cumplirse (lo detecto el control C6 de E12).

## 3. Distribucion de poses

Por pose, con direccion **isotropa** en el plano perpendicular al eje y magnitud media-normal truncada:

1. **Desplazamiento del centro**: magnitud `|N(0, sigma_t)|`, direccion uniforme en ese plano.
2. **Inclinacion del eje**: magnitud `|N(0, sigma_a)|`, eje de giro uniforme en ese plano.

### 3.1 De donde sale la escala — una sola constante, y no es de Zwingmann

| Parametro | Valor | Procedencia |
|---|---|---|
| Holgura `h` | **5.0 mm** | `kaiser2014dysmorphism`, margen operativo ya adoptado en `00-tesis.md` |
| `h = 2 sigma` | convencion | **propia, declarada**; no es un dato medido |
| `sigma_t` | `h / 2` = **2.5 mm** | derivado |
| `sigma_a` | `atan(h / (L/2)) / 2`, **por caso** | derivado; con `L` mediana de 138 mm da **2.07 grados** |
| Truncamiento | **3 sigma** | declarado, para que la cola no domine |
| Poses por caso | **50** | declarado |
| Semilla | **20260922**, derivada por caso | fija; la corrida no se re-tira |

La semilla es **por caso** (`muestreo.rng_de_caso`, `blake2b` del nombre del caso combinado con la
semilla global) y no un generador que avance de caso en caso. La cohorte de sensibilidad (49) es un
**subconjunto** de la primaria (72): con un generador global el mismo paciente recibiria poses
distintas en las dos corridas y la diferencia entre ambas cifras mezclaria efecto de cohorte con
ruido de muestreo. Asi, cada paciente recibe las mismas poses en cualquier corrida que lo incluya.

`sigma_a` es la misma holgura de 5 mm expresada como el angulo que la produce en la punta del corredor.
No introduce ninguna constante nueva y se adapta a cada caso.

**Lo que NO se uso, a proposito:** ninguna cifra de `zwingmann2009navigated`, incluido el umbral angular
de 4 grados que su introduccion cita de terceros. Aunque sea cita ajena, esta en el mismo paper contra
el que se compara, y usarlo abriria la puerta que D-O2.1 cierra.

### 3.2 Por que isotropa

No se privilegia ninguna direccion anatomica de error. Privilegiar una exigiria un dato de
direccionalidad clinica que esta tesis no tiene; ponerlo a ojo seria el mismo defecto que calibrar
contra el benchmark.

## 4. Metrica

`SAP` segun D-O2.3 y D-O2.4, implementada en `src/muestreador/sap.py`:

- **Diametro: 7.0 mm** (calibre del benchmark). Sensibilidad: 4.91 y 7.3 mm.
- **Brecha**: `max sobre t de max(0, radio + sd(c + t u))`, con `sd` la distancia signada a la
  envolvente osea.
- **Tramo evaluado**: el **propio implante**, de longitud fija igual a la del corredor de ese caso,
  centrado en la pose anclada y recortado **8 mm por extremo** (entrada y salida por la cortical del
  ilion son por diseno). La longitud **no depende de donde este el hueso**: si dependiera, la metrica
  premiaria a las poses que se salen, porque el tramo se encogeria con ellas. Esto lo fijaron los
  controles C5 y C6 de E12, y esta explicado en `sap._span_pose`.
- **Grados**: 0 sin perforacion; 1 en `(0, 2)`; 2 en `[2, 4]`; 3 en `(4, inf)` mm.
- **Poses sin travesia osea suficiente** (`sin_hueso`, `travesia_corta`): **grado 3**, con su frecuencia
  reportada (#120, opcion (b)).
- **Resolucion declarada: 0.083 mm** (control C1 de E12). Por debajo, la metrica no distingue.

## 5. Comparacion

- **Wasserstein-1 ordinal** sobre los grados 0-3 tratados como equiespaciados (convencion declarada;
  la unidad del resultado es "grados", no milimetros).
- Contra **las dos** distribuciones de `zwingmann2009navigated`, **solo en S1**:
  navegado **69/15/8/8**, convencional **40/37/11.5/11.5**.
- `zwingmann2010percutaneous` **no entra** (#113).

## 6. Que se acepta de antemano

- **El W1 puede salir alto. Ese resultado es reportable** y sigue siendo el resultado propio del
  Objetivo 2. Lo que no seria reportable es un W1 bajo obtenido moviendo parametros.
- La comparacion es entre **una poblacion simulada sobre pelvis receptoras** y **dos series clinicas
  pequenas** (26 y 35 tornillos). No es una prueba de equivalencia y no se presentara como tal.

## 7. Limite conocido en el momento de congelar

**S2 no tiene eje medido.** D-O2.5 dice muestrear en S1 y S2, con benchmark ordinal solo en S1. Pero
`e9ts_corredor.csv` guarda **un solo eje por caso**, el del mejor corredor, con los centros en el
sagital de S1; de S2 solo hay `pico_inf_z_rel_mm` y `pico_inf_D_mm`, es decir posicion y diametro del
pico inferior del perfil, **sin direccion**. Por tanto:

- Esta preinscripcion cubre **S1**.
- El muestreo en S2 queda **pendiente de medir un eje de corredor en S2** y se preinscribira aparte.
  Ver **#121**.

## 8. Trazabilidad de la implementacion

La semilla por caso (seccion 3.1) se corrigio el 2026-09-22, antes de cualquier corrida de cohorte:
la version inicial usaba un generador global que avanzaba caso a caso y habria hecho incomparables la
corrida de 72 y la de 49.

La definicion del tramo evaluado (seccion 4) se fijo **durante la implementacion de SAP el 2026-09-22**,
a base de tumbar dos versiones previas con los controles de E12, y **antes de correr la cohorte**: a esa
fecha no se habia calculado ningun Wasserstein-1 sobre los 72 casos. La unica corrida existente es
`e13_sap_piloto.md`, sobre **2 casos de grupo 1** que **no pertenecen a la cohorte** y que solo sirven
para comprobar que el camino completo corre. Sus cifras **no son un resultado del Objetivo 2** y no se
han usado para elegir nada.

## 9. Desviaciones declaradas

Ninguna al 2026-09-22.
