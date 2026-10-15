# Corrida final del Objetivo 3, version 1 preinscrita (run04, pose corregida) — evaluacion de prueba, 2026-10-13

Copia versionada de `a24` y `a23` sobre la particion de prueba. Diseno: `diseno_A.md` seccion 0 + ENMIENDA run04 +
correccion #173. Generacion: jobs 56243 / 56244 (difusor), 56245 (Peters), 56355 (E-A1). Evaluacion local:
`a20_evaluador_ea2.py --corrida-final` -> `outputs/obj3_pose/a20_test/a20_ea2_test.csv` (Peters 65 filas, copia y
pegado 13, difusor 130 = 2 puntos de control x 13 x 5 semillas; sin duplicados) -> `a24_contrastes.py` ->
`outputs/obj3_pose/a24/{run04_mejor,run04_60k}/`. `Delta` de validacion: `resultados_validacion_pose.md` §3.
Implicancia: #177.

## E-A2, 13 pacientes de prueba sin metal

| Lectura | Contraste | n | diferencia media (HU) | IC90 | p TOST | resultado |
|---|---|---|---|---|---|---|
| **`run04_mejor`, `Delta` 196.3** | **PRIMARIO: frente a Peters Ti** | 13 | **-301.0** | **[-477.0, -124.9]** | 0.845 | no se concluye equivalencia |
| | frente a Peters Fe | 13 | -3814.2 | [-4405.9, -3222.6] | 1.000 | no se concluye equivalencia |
| | sin corredores angostos | 10 | -261.1 | [-479.8, -42.4] | 0.700 | no se concluye equivalencia |
| `run04_60k`, `Delta` propio 115.8 | frente a Peters Ti | 13 | -384.0 | [-566.5, -201.4] | 0.989 | no se concluye equivalencia |
| | frente a Peters Fe | 13 | -3897.2 | [-4495.4, -3299.1] | 1.000 | no se concluye equivalencia |
| | sin corredores angostos | 10 | -353.9 | [-585.7, -122.1] | 0.954 | no se concluye equivalencia |
| `run04_60k`, `Delta` principal 196.3 | frente a Peters Ti | 13 | -384.0 | [-566.5, -201.4] | 0.954 | no se concluye equivalencia |
| | sin corredores angostos | 10 | -353.9 | [-585.7, -122.1] | 0.878 | no se concluye equivalencia |

Cordura (Wilcoxon de rangos con signo, una cola, difusor > copia y pegado): n = 13, p = 0.000122 en los dos puntos de
control: supera el piso. La copia y pegado da amplitud 0 (las ROIs excluyen `M`), asi que la prueba es degenerada:
p = 2^-13 es el minimo alcanzable y no se reporta tamano de efecto (DEC 2026-10-15 pto 12). Fraccion de la ROI en el
suelo de -1000 HU: difusor 0.000; Peters Ti 0.017 (maximo por paciente; medida el 2026-10-15, #186).

## Lecturas fijadas el 2026-10-15 (posteriores para v1)

`01-decisiones.md` 2026-10-15 fijo los desenlaces (pto 15), la sensibilidad por permutacion (pto 14), el margen
minimo (pto 16) y las lecturas de acuerdo (pto 22) **despues** de ver esta tabla (`visto.md`): para v1 son lecturas
posteriores. Calculo: `a26_lecturas.py` sobre el CSV congelado -> `outputs/a26/v1_congelado/`.

| modelo | `Delta` | desenlace (pto 15) | direccion | IC90 por permutacion | margen minimo |
|---|---|---|---|---|---|
| **`run04_mejor` (confirmatorio)** | 196.3 | **no concluyente** | difusor < Peters (IC90 excluye 0) | [-477.2, -124.1] | 477.0 HU (30 % de Ti) |
| `run04_60k` | 115.8 y 196.3 | no equivalencia con los dos | difusor < Peters | [-567.3, -200.4] | 566.5 HU (36 %) |

La permutacion coincide con *t* a menos de 2 HU: no baja ninguna categoria.

Acuerdo (#185, descriptivo): CV entre pacientes difusor 0.076 frente a Ti 0.241; Pitman-Morgan r = -0.89,
p = 3.8e-5; Pearson r = 0.40; Bland-Altman sesgo -301.0 HU, limites [-999.0, +397.1]. El difusor casi no cambia de
paciente a paciente; el TOST de medias no lo ve.

Asimetrias (#186): Peters medido en cortes `k = 2` (62 341 voxeles mediana) frente a 124 679 del difusor; piso de ruido
de Peters (`limpia_A - limpia_B`) 183.5 HU mediana; costura mediana difusor 4.3 HU, Peters 1.2 HU (pto 5). Variantes
que corrigen las asimetrias y comparador parametrico: `resultados_dec_2026-10-15.md` (ninguna cambia el desenlace;
#187).

## E-A1, reconstruccion de implantes reales (13 pacientes de prueba con metal, `run04_mejor`, 0.030)

`outputs/obj3_pose/a23_final_run04_d003/a23_pacientes.csv` (3840 parches). Medianas por grupo:

| grupo | n | MAE `G` | MAE `M` | MAE `B_delta` | hueso SDC | hueso dVol | metal SDC | metal dVol | exceso costura |
|---|---|---|---|---|---|---|---|---|---|
| 1 (material ortopedico) | 9 | 270.9 | 2312.5 | 198.0 | 0.717 | -0.041 | 0.928 | -0.078 | 6.3 |
| 2 (objetos no ortopedicos; fuera de la distribucion de entrenamiento) | 4 | 199.8 | 2747.9 | 165.8 | 0.534 | 0.324 | 0.753 | -0.255 | 9.0 |

Todas las cifras en HU salvo SDC y dVol (fraccion). Descriptivo, sin prueba de hipotesis.

## Pendiente

Realismo (diseno_A.md seccion 0, opcion 3): no hay script (H5, prioridad 1); la lista de pacientes de prueba con tornillo intraoseo
aislado (revision de la autora) sigue como `\GAPDATO`.
