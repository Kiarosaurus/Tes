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
control: supera el piso. La copia y pegado da amplitud 0 (las ROIs excluyen `M`). Fraccion de la ROI en el suelo de
-1000 HU: 0.000 (maximo por paciente).

Lectura descriptiva (no fijada en el diseno, ver `\GAPDEC` "que desenlace cuenta en contra"): con el principal, el IC90
queda entero bajo 0 y su extremo superior (-124.9) dentro de [-196.3, 196.3]; con `run04_60k`, el IC90 queda entero
fuera de los dos margenes (por 5.1 HU frente a 196.3).

## E-A1, reconstruccion de implantes reales (13 pacientes de prueba con metal, `run04_mejor`, 0.030)

`outputs/obj3_pose/a23_final_run04_d003/a23_pacientes.csv` (3840 parches). Medianas por grupo:

| grupo | n | MAE `G` | MAE `M` | MAE `B_delta` | hueso SDC | hueso dVol | metal SDC | metal dVol | exceso costura |
|---|---|---|---|---|---|---|---|---|---|
| 1 (material ortopedico) | 9 | 270.9 | 2312.5 | 198.0 | 0.717 | -0.041 | 0.928 | -0.078 | 6.3 |
| 2 (objetos no ortopedicos; fuera de la distribucion de entrenamiento) | 4 | 199.8 | 2747.9 | 165.8 | 0.534 | 0.324 | 0.753 | -0.255 | 9.0 |

Todas las cifras en HU salvo SDC y dVol (fraccion). Descriptivo, sin prueba de hipotesis.

## Pendiente

Realismo (diseno_A.md seccion 0, opcion 3): no hay script; la lista de pacientes de prueba con tornillo intraoseo
aislado (revision de la autora) sigue como `\GAPDATO`.
