# Registro de metodos y datos para cerrar GAPDATO (2026-10-15)

Pedido de la autora (2026-10-15): "Cierra los GAPDATOS que se puedan cerrar con experimentos baratos y/o data que ya
tenemos". Cada seccion dice que GAPDATO cierra, de donde sale y como se reproduce. Nada de lo que sigue es un
experimento nuevo sobre test del Objetivo 3; los calculos nuevos son de Objetivo 2 y de datos de entrenamiento.

## 1. Compresion arcoseno hiperbolico de la codificacion `pub+asinh` (cap. 1)

Fuente: `experiments/objetivo1/e6c_techo_lw.py` (l. 42-72), importada por `src/common/ventanas.py`.

- Canal ancho (LW): `u = (asinh(clip(h, -1000, 20000) / s) - a) / (b - a)`, con `s = 500` HU (`ASINH_ESCALA`),
  `a = asinh(-1000 / 500) = asinh(-2)`, `b = asinh(20000 / 500) = asinh(40)`; inversa `h = s * sinh(u (b - a) + a)`.
  `u` en [0, 1]. Fino cerca de 0 HU y grueso en el rango alto.
- MW y SW: ventanas lineales `[-320, 480]` y `[-160, 240]` HU.
- Resultado de la configuracion: Objetivo 1, P1 (`experiments/objetivo1/outputs/p1/`), MAE 61.84 HU en validacion
  al paso 30 000 (`curva_pub+asinh.csv`); veredicto de la compuerta en `docs/00-tesis.md`.

## 2. Ajuste del decodificador del Objetivo 1 (cap. 3)

Fuente: `experiments/objetivo1/p1_decodificador_sd15.py` (docstring l. 25-36; argumentos l. 748-760; bucle l. 222-344)
y `p1_entrenar.sbatch` (l. 41-42: no fija pasos, lote ni lr, que quedan por omision; las curvas confirman los 30 000 pasos).

- Parte ajustada: `post_quant_conv` + `decoder` del VAE de SD 1.5; `encoder` y `quant_conv` congelados (control de
  hash identico).
- Datos: cortes axiales completos de los pacientes `train` de `p1_particion.csv`, mezclados con una reserva de 3 000
  cortes; latente = media de la posterior; entrada y salida en [-1, 1] (`u -> 2u - 1`).
- Perdida L1; AdamW (`weight_decay` 0), lr 1e-4 con calentamiento lineal de 500 pasos y despues constante; recorte
  de gradiente 1.0; float32; lote 4 cortes; semilla 0.
- **Criterio de parada: numero fijo de pasos, 30 000**; se usa el ultimo paso. La validacion (8 cortes por volumen,
  cada 1 000 pasos) solo registra la curva y no elige punto de control. Las tres curvas (`outputs/p1/curva_*.csv`)
  terminan en el paso 30 000 (1-2 epocas).

## 3. Busqueda del eje del corredor (cap. 3)

Fuente: `experiments/objetivo2/e9ts_corredor.py` (docstring "METODO"), que importa `evaluar_linea`, `picos` y
`angulos_kaiser` de `experiments/objetivo2/e9_corredor.py` (docstring "METODO", pasos 2-5).

1. Mascara osea: union de `sacrum`, `vertebrae_S1`, `hip_left`, `hip_right` de TotalSegmentator, recorte
   `default6mm`, limpieza por fraccion `F`, cierre morfologico de 2 mm y despues resta de los voxeles ocupados.
2. Centros candidatos en el plano sagital del S1 de R1: rejilla de 3 mm, de 3 a 75 mm bajo el platillo y de 45 mm
   detras a 10 mm delante, solo sobre hueso.
3. En cada centro, 81 direcciones: inclinacion axial y coronal de -20 a +20 grados en pasos de 5, respecto del eje
   izquierda-derecha.
4. Por trayectoria: tramo oseo continuo que contiene el centro (huecos de hasta 2 mm), con salida a tejido blando por
   los dos extremos sin reencontrar hueso en 40 mm, cada salida al menos tan lateral como la EIPS de su lado.
   `D = 2 x min EDT` sobre el tramo sin 8 mm por extremo (exacto para cilindro recto; trunca sobre 16 mm).
5. El eje del caso es la trayectoria de `D_TS` maximo; el perfil por nivel separa candidatos S1 y S2 por picos a
   >= 12 mm (heuristica declarada).

## 4. Localizacion de las referencias anatomicas (cap. 3)

Fuente: `experiments/objetivo2/r1_landmarks.py` (docstring "HEURISTICA DE LOCALIZACION", v2 2026-09-10).

Todo en RAS+ y mm; mascara osea HU > 150 sin metal (HU > 2500 dilatado 3 mm); deteccion sobre rejilla de ~1.5 mm.
1. Componente osea conexa mas grande no plana en y (descarta rieles de mesa); `x_mid` = mediana de x.
2. Crestas: sobre el ilion, banda |x - x_mid| > 60 mm de cada lado, percentil 99.9 de z.
3. Platillo de S1: de la cresta hacia abajo (max. 130 mm), primer nivel con ancho >= 100 mm sostenido 10 mm y
   precedido de >= 5 mm de nivel estrecho; dos detectores (sagital primario, ala de control).
4. EIPS: en cada lado, z en [z_S1 - 40, z_cresta], banda 25 < |x - x_mid| < 100 mm, percentil 0.1 de y.
Legibilidad por region (esfera de 12 mm): fracciones oscura (< -200 HU), brillante (> 2500 HU) y osea (> 150 HU),
distancia al metal y margen de 5 mm al borde del FOV. Es una cota superior de localizabilidad, revisada por laminas.

## 5. Intervalo del 90 % del exceso por anillo (D1, cap. 3)

Fuente: `experiments/objetivo3/d1_alcance_rayas.py` (docstring paso 5; `ic_pacientes`, l. 156-161).
Agregacion por medianas corte -> componente -> paciente; IC90 de la mediana entre pacientes por remuestreo de
pacientes con reemplazo, 2 000 remuestreos, percentiles 5 y 95 (`np.nanpercentile`).

## 6. Valores p de Fisher de las amenazas a la validez (cap. 1)

Fuente: `experiments/registro/r_fisher_amenazas.py` (nuevo). Recalculo con `scipy.stats.fisher_exact`
(scipy 1.15.3), bilateral; su convencion es la *minlike* (`fay2010two`). **Reproduce las cuatro cifras
registradas** (1.000, 0.272, 0.264, 0.109; tablas de `docs/04-implicancias.md` del cribado de fractura). El programa
original no consta; se declara que los valores coinciden con la convencion *minlike*.

## 7. Razon de parches de solo banda del modelo evaluado (cap. 3)

Fuente: `experiments/registro/r_razon_banda_run04.py` (nuevo). Manifiesto de run04 reconstruido exacto (14 182
parches, 39 casos): **5 526 de solo banda frente a 8 656 con metal, razon 0.638** (0.620 antes de las retiradas).

## 8. Objetivo 2: W1 por remuestreo de pacientes y sensibilidad sin los dos casos (cap. 3, introduccion)

Fuente: `experiments/objetivo2/e15_w1_sensibilidad.py` -> `e15_w1_sensibilidad.md` (nuevo; 2026-10-08 ptos 18 y 22).
Regresion exacta de E13 (0.206 / 0.230). IC95 por remuestreo de pacientes (2 000, semilla 20261015): navegado
[0.152, 0.313], convencional [0.089, 0.364] (los intervalos se solapan: la cohorte no distingue cual serie esta mas
cerca). Sin `CLINIC_0022` y `CLINIC_0024` (70 casos): 0.203 y 0.237.

## 9. IC95 del contraste primario de v1 (cap. 3; #194)

Fuente: `experiments/objetivo3/resultados_dec_2026-10-15.md`, seccion "IC95 del contraste primario de v1":
[-516.2, -85.7] HU (excluye 0).
