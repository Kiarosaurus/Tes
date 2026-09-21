# E11 — perfil de diametro a lo largo del eje de los implantes reales

> Corrida sobre los **178 volumenes** el **2026-09-20**. Script: `e11_perfil_axial.py`. Tabla por componente
> versionada aqui como `e11_componentes.csv` (copia exacta de la salida; la tabla por tramo,
> `e11_perfil_axial.csv`, 119 KB, y el informe generado quedan en `outputs/e11/`, fuera de git).
> Origen: implicancia **#97**, paso 4 de la decision del 2026-09-20. Resultado registrado en **#101**.

## Para que se corrio

El Objetivo 3 condiciona la generacion por una **mascara** del implante. La mascara de sintesis es parametrica; la
de entrenamiento sale de umbralizar metal real. Las fuentes leidas el 2026-09-19/20 dan un tornillo con **tres
diametros distintos**: rosca 7.3 mm, fuste 4.8 mm (`synthes2003guide`) y cabeza 8.0 mm (`sayres2014comparison`).
E8 midio **un solo** diametro por componente y no podia decir cual de los tres ve el CT. E11 mide el diametro
**a lo largo del eje**, que es lo que separa las tres hipotesis.

## EL FILTRO GEOMETRICO — que selecciona, que deja fuera, y por que se declara

Esta seccion existe porque el filtro **no es una anotacion clinica**: es un criterio de forma, y cualquier cifra
que salga de E11 hereda sus limites.

Un componente entra si cumple **las tres** condiciones:

| Criterio | Valor | Por que |
|---|---|---|
| Umbral de metal | HU > 2500 | El de cribado (#22), validado en E1 con 0 falsos negativos sobre 113 candidatos |
| Longitud del eje principal | >= 30 mm | Un tornillo iliosacro cruza el corredor; por debajo de 30 mm no puede serlo |
| Los dos anchos transversales | <= 12 mm | Un tornillo de 7.3 mm no llega a 12 mm; una placa o una protesis si |

Fragmentos por debajo de `MIN_FRAG_MM3` se descartan antes. El eje principal sale de PCA sobre los voxeles del
componente, y el diametro local es **2 x p95 de la distancia al eje** en tramos de 2 mm: el mismo estimador radial
de E8, elegido por ser robusto a la canulacion y a los fragmentos.

**Resultado del filtro:** de los 178 volumenes salen **79 componentes esbeltos**, repartidos en **43 casos**.
Los otros 65 casos quedan etiquetados `sin metal` en `e11_componentes.csv`.

### Lo que el filtro NO hace, y hay que citar junto a cualquier cifra

1. **No identifica el tipo de implante.** Es geometrico. Entre los 79 esbeltos hay material alargado que **no** es
   tornillo iliosacro (clavos, tornillos de otra region, componentes alargados de un montaje mayor). E11 **no
   puede** afirmar "estos son tornillos iliosacros"; afirma "estos son componentes metalicos alargados y finos".
2. **No distingue cabeza de rosca.** Reporta los dos extremos del eje (`A` = t bajo, `B` = t alto) y el centro.
   Cual extremo es la cabeza se decidiria mirando donde apoya respecto a la cortical, y **eso no se midio**.
3. **Puede partir un implante en varios componentes, y eso SESGA la muestra.** A 2500 HU los tornillos salen
   fragmentados en 9 de 57 (E8, #46). Un tornillo partido en tres da piezas de ~20 mm que **no llegan al
   criterio de 30 mm**, asi que **quedan fuera de esta medicion**. El filtro **no repara** la fragmentacion:
   la hereda.
   - **Consecuencia directa sobre las cifras de abajo:** `d_centro` = 4.91 mm se midio sobre los tornillos que
     **sobrevivieron enteros** al umbral. La muestra esta **sesgada hacia los mejor segmentados**, que
     previsiblemente son los mas densos o los mas gruesos. **La cifra no se invalida** —coincide con el
     catalogo (4.8 mm, `synthes2003guide`) y con E8 (5.00 mm) por vias independientes, y las tres caen dentro
     de un cuarto de voxel— pero **cualquier uso de ella debe declarar este sesgo**.
   - Cuanto pesa el sesgo **no esta medido**. Medirlo exigiria repetir el perfil con una definicion de mascara
     que no fragmente (semimaximo local, la propuesta abierta de #22/#46). Registrado en **#111**.
4. **Deja fuera placas y protesis a proposito**, que son las que mas voxeles de metal aportan a la cohorte. Por eso
   las cifras de E11 **no** describen "el metal de CLINIC-metal": describen su subconjunto alargado.
5. **5 de los componentes esbeltos estan en casos `dataset6`**, el grupo nominalmente sin metal. Es un dato sobre la
   clasificacion de la cohorte, no sobre geometria, y conviene mirarlo aparte.
6. **El umbral fijo de 2500 HU ensancha o adelgaza segun el caso.** El perfil con semimaximo local (la propuesta
   abierta de #22/#46) **no se midio**.

### Cobertura: los casos que el filtro selecciona ya estan anotados

Comprobado el 2026-09-20 contra `experiments/exploration-3d/revision.csv`: de los **43 casos con al menos un
componente esbelto**, faltan **0** en `Tipo de estructura observada`, **0** en `Artefactos` y **0** en `Severidad`.
Las filas incompletas de `revision.csv` (67 de 178) son casos **sin** metal, donde esas columnas no aplican.

## Resultados

| Magnitud | mediana | p10 | p90 |
|---|---|---|---|
| `d_centro_mm` | **4.91** | 3.39 | 7.37 |
| `d_extremo_A_mm` | 5.87 | 4.42 | 8.72 |
| `d_extremo_B_mm` | 5.91 | 4.45 | 8.74 |
| `d_max_mm` | 8.10 | 5.72 | 12.46 |
| `L_mm` | 60.03 | 35.95 | 107.21 |

**Ensanchamiento de extremo** (extremo mas ancho menos centro), sobre los **59** componentes con los tres valores:

| Estadistico | Valor |
|---|---|
| mediana | **0.96 mm** (~1 voxel) |
| p90 | 3.41 mm |
| maximo | 4.07 mm |
| > 0.78 mm (1 voxel) | 33 / 59 |
| > 2.0 mm | **12 / 59** |
| > 3.0 mm | 7 / 59 |

`d_centro` no se pudo calcular en 2 de 79 componentes y los dos extremos faltan en 20 (tramos con menos voxeles
que el minimo).

## Lectura

**El cuerpo del tornillo queda confirmado por tres vias independientes**: catalogo del fabricante 4.8 mm
(`synthes2003guide`), censo E8 5.00 mm y perfil axial 4.91 mm. Las tres caen dentro de **un cuarto de voxel**.
Es la cifra mejor sostenida de toda la geometria.

**El ensanchamiento de extremo es del orden de un voxel en la mediana (0.96 mm).** En el caso tipico el volumen
parcial promedia cabeza y rosca, asi que **un cilindro uniforme de ~5 mm queda justificado con medicion propia**,
no por comodidad. Pero **12 de 59 superan 2 mm**, que es lo que se esperaria si el CT estuviera resolviendo una
cabeza de 8.0 mm sobre un cuerpo de ~5 mm: no es un efecto despreciable en una minoria de los casos.

**`d_max` (mediana 8.10 mm) es un maximo sobre tramos y esta sesgado al alza.** No debe citarse como "diametro de
cabeza medido": coincide con los 8.0 mm del catalogo por construccion del estimador, no por confirmacion.

**Lo que E11 no resuelve:** #95. E11 dice como es el metal real; no dice cuanto se parece la mascara por umbral a
la mascara parametrica de sintesis. Esa brecha sigue abierta y hay que declararla.
