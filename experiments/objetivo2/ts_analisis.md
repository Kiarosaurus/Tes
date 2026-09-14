# TS cohorte — analisis de la QC (generado por `ts_analisis.py`)

Volumenes en uso: 168 (sin los 11 de `exclusiones.csv`); pacientes: 168. Procedencia de la referencia de nivel: `auditoria_S1_clinico` = medico ORL; `auditoria_S1` = agente. **No decide nada.**

## 1. Nivel de S1: techo de `vertebrae_S1` de TS frente al platillo de R1

Estado `R1 arriba de TS`: dz < -10 mm con los dos recortes. Diferencia maxima de dz entre recortes: 1.6 mm; casos cuyo estado cambia con el recorte: 0.

| estrato | R1 arriba de TS | concordante | sin S1 en R1 | sin techo | total |
|---|---|---|---|---|---|
| calibracion, discordante | 6 | 18 | 0 | 0 | 24 |
| calibracion, no discordante | 1 | 35 | 9 | 0 | 45 |
| evaluacion, clinico +1 | 6 | 0 | 0 | 1 | 7 |
| evaluacion, clinico ? | 0 | 0 | 0 | 1 | 1 |
| evaluacion, clinico no hallado | 0 | 0 | 4 | 0 | 4 |
| evaluacion, clinico ok | 0 | 51 | 0 | 0 | 51 |
| evaluacion, clinico otro | 1 | 1 | 0 | 0 | 2 |
| otro, discordante | 10 | 5 | 0 | 0 | 15 |
| otro, no discordante | 1 | 15 | 3 | 0 | 19 |
| total | 25 | 125 | 16 | 2 | 168 |

dz (3 mm) por estrato y estado:

| estrato | estado_TS | count | median | min | max |
|---|---|---|---|---|---|
| calibracion, discordante | R1 arriba de TS | 6 | -30.8 | -52.2 | -24.6 |
| calibracion, discordante | concordante | 18 | 6.6 | 3.7 | 9.7 |
| calibracion, no discordante | R1 arriba de TS | 1 | -22.5 | -22.5 | -22.5 |
| calibracion, no discordante | concordante | 35 | 6.3 | 4.8 | 14.6 |
| calibracion, no discordante | sin S1 en R1 | 0 |  |  |  |
| evaluacion, clinico +1 | R1 arriba de TS | 6 | -32.5 | -34.3 | -24.3 |
| evaluacion, clinico +1 | sin techo | 0 |  |  |  |
| evaluacion, clinico ? | sin techo | 0 |  |  |  |
| evaluacion, clinico no hallado | sin S1 en R1 | 0 |  |  |  |
| evaluacion, clinico ok | concordante | 51 | 6.3 | 3.7 | 15.7 |
| evaluacion, clinico otro | R1 arriba de TS | 1 | -14.3 | -14.3 | -14.3 |
| evaluacion, clinico otro | concordante | 1 | 6.1 | 6.1 | 6.1 |
| otro, discordante | R1 arriba de TS | 10 | -34.2 | -54.1 | -16.0 |
| otro, discordante | concordante | 5 | 6.8 | 5.6 | 14.6 |
| otro, no discordante | R1 arriba de TS | 1 | -27.2 | -27.2 | -27.2 |
| otro, no discordante | concordante | 15 | 6.4 | 3.1 | 8.3 |
| otro, no discordante | sin S1 en R1 | 0 |  |  |  |

Concordancia con el clinico (ok / +1, con techo en los dos recortes): **57 de 57**. `+1`: dz (peor recorte) entre -34.3 y -24.3 mm. `ok`: dz (peor recorte) entre 3.7 y 14.9 mm. Los dos rangos no se solapan: cualquier umbral mayor que -24.3 y de hasta 3.7 mm da la misma concordancia.

Casos de evaluacion donde TS no coincide con el clinico, o clinico `otro`:

| Caso | auditoria_S1_clinico | auditoria_S1_agente | dz_S1_3mm | dz_S1_6mm | n_vox_S1_3mm | S1_toca_fov | estado_TS |
|---|---|---|---|---|---|---|---|
| dataset7_CLINIC_metal_0026_data | +1 | ok |  |  | 45778 |  | sin techo |
| dataset7_CLINIC_metal_0046_data | otro | ok | 6.1 | 6.1 | 89564 |  | concordante |
| dataset7_CLINIC_metal_0058_data | otro | error grosero | -14.3 | -12.7 | 110702 |  | R1 arriba de TS |

Fuera de evaluacion (sin auditoria), `R1 arriba de TS`: 18 casos: `C0071` (-54), `C0057` (-52), `C0019` (-41), `C0032` (-40), `C0069` (-38), `m0068` (-36), `C0053` (-36), `C0046` (-35), `C0007` (-32), `C0054` (-27), `C0085` (-27), `m0061` (-26), `C0099` (-25), `m0064` (-25), `C0002` (-25), `C0005` (-23), `C0095` (-22), `C0068` (-16)

## 2. `sacrum` sin techo con S1 hallado en R1

28 filas, 16 casos. De ellos, 12 casos (23 filas) son casos con R1 un nivel arriba (por TS o por el clinico): la columna media cae sobre L5, anterior al sacro. Sin esa explicacion: 4 casos (5 filas).

| Caso | modo | n_vox | estado_TS |
|---|---|---|---|
| dataset6_CLINIC_0045_data | robust3mm | 422656 | concordante |
| dataset6_CLINIC_0066_data | robust3mm | 262901 | concordante |
| dataset6_CLINIC_0066_data | default6mm | 260050 | concordante |
| dataset7_CLINIC_metal_0007_data | default6mm | 414110 | concordante |
| dataset7_CLINIC_metal_0054_data | robust3mm | 307256 | concordante |

## 3. Recorte 3 mm frente a 6 mm (#49)

| estructura | grupo | n | dice_p50 | dice_p05 | dice_min | excl3_p50 | excl6_p50 | caja_max_mm |
|---|---|---|---|---|---|---|---|---|
| hip_left | con osteosintesis (g1) | 65 | 0.957 | 0.946 | 0.944 | 4.308 | 4.248 | 90.6 |
| hip_left | sin osteosintesis (g2+g3) | 103 | 0.966 | 0.949 | 0.939 | 3.438 | 3.473 | 19.2 |
| hip_right | con osteosintesis (g1) | 65 | 0.956 | 0.946 | 0.943 | 4.285 | 4.389 | 80.0 |
| hip_right | sin osteosintesis (g2+g3) | 103 | 0.963 | 0.948 | 0.941 | 3.607 | 3.565 | 98.3 |
| sacrum | con osteosintesis (g1) | 65 | 0.94 | 0.918 | 0.904 | 5.821 | 5.858 | 4.3 |
| sacrum | sin osteosintesis (g2+g3) | 103 | 0.95 | 0.929 | 0.918 | 4.955 | 4.911 | 78.2 |
| vertebrae_S1 | con osteosintesis (g1) | 64 | 0.946 | 0.924 | 0.915 | 5.413 | 5.08 | 8.6 |
| vertebrae_S1 | sin osteosintesis (g2+g3) | 103 | 0.952 | 0.933 | 0.848 | 4.885 | 4.696 | 16.4 |

Peores Dice:

| Caso | estructura | dice_3v6 | dif_caja_3v6_max_mm | excl_3mm_% | excl_6mm_% | grupo |
|---|---|---|---|---|---|---|
| dataset6_CLINIC_0022_data | vertebrae_S1 | 0.848 | 7.8 | 10.828 | 19.069 | sin osteosintesis (g2+g3) |
| dataset7_CLINIC_metal_0028_data | sacrum | 0.904 | 1.5 | 12.071 | 7.027 | con osteosintesis (g1) |
| dataset7_CLINIC_metal_0019_data | sacrum | 0.908 | 1.3 | 9.337 | 8.966 | con osteosintesis (g1) |
| dataset7_CLINIC_metal_0060_data | vertebrae_S1 | 0.915 | 0.8 | 7.974 | 9.01 | con osteosintesis (g1) |
| dataset7_CLINIC_metal_0020_data | sacrum | 0.917 | 1.6 | 8.837 | 7.793 | con osteosintesis (g1) |
| dataset6_CLINIC_0083_data | sacrum | 0.918 | 2.9 | 8.242 | 8.126 | sin osteosintesis (g2+g3) |

Cajas que cambian > 10 mm entre recortes (en el piloto, <= 1.6 mm; causa no verificada: islas de voxeles o extension distinta de la estructura): 10 casos, 11 estructuras.

| Caso | estructura | x_max_mm_default6mm | x_max_mm_robust3mm | x_min_mm_default6mm | x_min_mm_robust3mm | z_max_mm_default6mm | z_max_mm_robust3mm | z_min_mm_default6mm | z_min_mm_robust3mm | dif_caja_mm |
|---|---|---|---|---|---|---|---|---|---|---|
| dataset6_CLINIC_0013_data | hip_right | 393.3 | 399.2 | 269.4 | 269.4 | 242.4 | 242.4 | 34.4 | 12.8 | 21.6 |
| dataset6_CLINIC_0022_data | sacrum | 280.7 | 280.7 | 174.4 | 96.2 | 219.2 | 220.0 | 74.4 | 74.4 | 78.2 |
| dataset6_CLINIC_0029_data | vertebrae_S1 | 212.7 | 214.3 | 143.1 | 159.5 | 229.3 | 227.7 | 182.2 | 182.2 | 16.4 |
| dataset6_CLINIC_0032_data | vertebrae_S1 | 197.2 | 193.8 | 132.2 | 132.9 | 215.2 | 201.6 | 156.0 | 156.0 | 13.6 |
| dataset6_CLINIC_0081_data | hip_right | 353.4 | 352.6 | 221.5 | 123.3 | 231.2 | 231.2 | 21.6 | 21.6 | 98.3 |
| dataset6_CLINIC_0090_data | hip_left | 230.3 | 241.0 | 80.6 | 79.7 | 247.7 | 266.8 | 40.7 | 40.7 | 19.2 |
| dataset6_CLINIC_0090_data | hip_right | 372.7 | 373.6 | 233.9 | 233.0 | 246.1 | 266.8 | 37.6 | 37.6 | 20.8 |
| dataset7_CLINIC_metal_0037_data | hip_left | 209.4 | 300.0 | 70.6 | 70.6 | 228.8 | 228.8 | 0.8 | 0.8 | 90.6 |
| dataset7_CLINIC_metal_0051_data | hip_right | 336.9 | 336.9 | 137.4 | 217.4 | 223.2 | 223.2 | 28.8 | 28.8 | 80.0 |
| dataset7_CLINIC_metal_0067_data | hip_left | 225.2 | 214.4 | 92.2 | 91.4 | 268.0 | 248.8 | 32.8 | 32.8 | 19.2 |
| dataset7_CLINIC_metal_0069_data | hip_left | 296.1 | 211.7 | 81.0 | 81.0 | 250.4 | 250.4 | 39.2 | 39.2 | 84.4 |

## 4. Tabla de #50 rehecha con TS (esferas de E9b, recorte 3 mm)

Una esfera con mediana < 150 HU cuenta como "hueso bajo 150" solo si queda >= 90% dentro de `sacrum` o `vertebrae_S1`. Con 6 mm las fracciones cambian poco (ver `ts_qc_esferas.csv`).

| grupo | n | alguna esfera < 150 HU (E9b) | ala < 150 con esfera >= 90% en sacrum/S1 de TS | ala < 150 con esfera > 50% fuera de mascaras |
|---|---|---|---|---|
| evaluacion, clinico ok (E9b de #48) | 51 | 18 (35%) | 4 (8%) | 14 (27%) |
|   ... y TS concordante | 51 | 18 (35%) | 4 (8%) | 14 (27%) |
|   ... y TS: R1 arriba | 0 | 0 | 0 | 0 |
| evaluacion, clinico +1 | 7 | 7 (100%) | 0 (0%) | 7 (100%) |
| calibracion, sin auditar (E9b de #48) | 60 | 26 (43%) | 9 (15%) | 16 (27%) |
|   ... y TS concordante | 53 | 19 (36%) | 9 (17%) | 9 (17%) |
|   ... y TS: R1 arriba | 7 | 7 (100%) | 0 (0%) | 7 (100%) |

Esferas por estado de nivel (todas las cohortes con S1 en R1):

| estado_TS | esfera | n | en_sacro_S1_p50 | fuera_p50 | fuera_mayoria | en_cadera_max |
|---|---|---|---|---|---|---|
| R1 arriba de TS | ala_der | 25 | 0.0 | 1.0 | 25 | 0.0 |
| R1 arriba de TS | ala_izq | 25 | 0.0 | 1.0 | 25 | 0.0 |
| R1 arriba de TS | cuerpo | 25 | 0.0 | 1.0 | 25 | 0.0 |
| concordante | ala_der | 125 | 0.881 | 0.119 | 24 | 0.0 |
| concordante | ala_izq | 125 | 0.895 | 0.105 | 17 | 0.0 |
| concordante | cuerpo | 125 | 1.0 | 0.0 | 1 | 0.0 |

## 5. Fraccion de voxeles <= 150 HU dentro de cada mascara (mediana por grupo) (#48)

Grupos de `grupos.csv`: 1 = osteosintesis, 2 = objeto no ortopedico, 3 = limpio. Incluye borde de la mascara (volumen parcial) y, en grupo 1, voxeles de metal y estriacion. Los grupos no estan emparejados por edad ni sexo.

| estructura | modo | grupo 1 | grupo 2 | grupo 3 |
|---|---|---|---|---|
| hip_left | default6mm | 0.17 | 0.182 | 0.233 |
| hip_left | robust3mm | 0.17 | 0.181 | 0.234 |
| hip_right | default6mm | 0.165 | 0.185 | 0.222 |
| hip_right | robust3mm | 0.166 | 0.184 | 0.222 |
| sacrum | default6mm | 0.321 | 0.377 | 0.426 |
| sacrum | robust3mm | 0.317 | 0.375 | 0.428 |
| vertebrae_S1 | default6mm | 0.098 | 0.11 | 0.133 |
| vertebrae_S1 | robust3mm | 0.1 | 0.109 | 0.133 |

## 6. Mascaras que tocan el borde del FOV

19 volumenes en uso. Los 7 de FOV cortado de R1 estan todos: 7 de 7.

| Caso | estructuras (ambos recortes) | de los 7 (R1) | Grupo |
|---|---|---|---|
| dataset6_CLINIC_0010_data | hip_left z+, hip_right z+, vertebrae_S1 z+ | False | grupo 3 |
| dataset6_CLINIC_0011_data | hip_left z+, hip_right z+, sacrum z+, vertebrae_S1 z+ | False | grupo 3 |
| dataset6_CLINIC_0028_data | hip_left z+, hip_right z+ | False | grupo 2 |
| dataset6_CLINIC_0060_data | hip_left z- | False | grupo 3 |
| dataset6_CLINIC_0073_data | hip_left z+ | False | grupo 3 |
| dataset6_CLINIC_0079_data | hip_left z+ | False | grupo 3 |
| dataset7_CLINIC_metal_0002_data | hip_left z+ | True | grupo 1 |
| dataset7_CLINIC_metal_0003_data | hip_right z+ | True | grupo 1 |
| dataset7_CLINIC_metal_0005_data | hip_left z-, hip_right z- | False | grupo 1 |
| dataset7_CLINIC_metal_0009_data | hip_left z-, hip_right z-, sacrum z- | False | grupo 1 |
| dataset7_CLINIC_metal_0015_data | hip_left z+, hip_right z+, sacrum z+, vertebrae_S1 z+ | True | grupo 1 |
| dataset7_CLINIC_metal_0022_data | hip_left z+, hip_right z+, sacrum z+, vertebrae_S1 z+ | True | grupo 1 |
| dataset7_CLINIC_metal_0023_data | hip_right z+ | True | grupo 1 |
| dataset7_CLINIC_metal_0031_data | hip_left z-, hip_right z-, sacrum z- | False | grupo 1 |
| dataset7_CLINIC_metal_0045_data | hip_left z-, hip_right z-, sacrum z- | False | grupo 1 |
| dataset7_CLINIC_metal_0048_data | hip_left z-, hip_right z- | False | grupo 1 |
| dataset7_CLINIC_metal_0053_data | hip_left z+, hip_right z+, sacrum z+ | True | grupo 1 |
| dataset7_CLINIC_metal_0054_data | hip_left z+, hip_right z+ | True | grupo 1 |
| dataset7_CLINIC_metal_0063_data | hip_left z-, hip_right z-, sacrum z- | False | grupo 1 |

## 7. Tornillos de E8 frente a las mascaras

17 pacientes, 21 componentes (sin `metal_0065`, secundario).

| modo | frac_eje_fuera_median | frac_eje_fuera_max | frac_eje_fuera_min | frac_metal_en_mascaras_median | frac_metal_en_mascaras_max | frac_metal_en_mascaras_min |
|---|---|---|---|---|---|---|
| default6mm | 0.052 | 0.299 | 0.0 | 0.984 | 1.0 | 0.7 |
| robust3mm | 0.057 | 0.35 | 0.0 | 0.978 | 1.0 | 0.685 |

| Caso | comp | frac_eje_fuera_default6mm | frac_eje_fuera_robust3mm | frac_metal_en_mascaras_default6mm | frac_metal_en_mascaras_robust3mm | frac_vol_E8_en_cilindro_default6mm | frac_vol_E8_en_cilindro_robust3mm |
|---|---|---|---|---|---|---|---|
| dataset7_CLINIC_metal_0001_data | 1 | 0.036 | 0.036 | 0.98 | 0.951 | 1.0 | 1.0 |
| dataset7_CLINIC_metal_0002_data | 2 | 0.083 | 0.092 | 0.987 | 0.989 | 0.738 | 0.738 |
| dataset7_CLINIC_metal_0004_data | 2 | 0.0 | 0.0 | 1.0 | 1.0 | 0.978 | 0.978 |
| dataset7_CLINIC_metal_0008_data | 1 | 0.058 | 0.175 | 0.984 | 0.952 | 0.755 | 0.755 |
| dataset7_CLINIC_metal_0008_data | 2 | 0.08 | 0.057 | 0.977 | 0.983 | 0.842 | 0.842 |
| dataset7_CLINIC_metal_0018_data | 2 | 0.051 | 0.061 | 0.985 | 0.966 | 0.936 | 0.936 |
| dataset7_CLINIC_metal_0024_data | 3 | 0.299 | 0.35 | 0.7 | 0.685 | 0.885 | 0.885 |
| dataset7_CLINIC_metal_0028_data | 3 | 0.0 | 0.0 | 0.977 | 1.0 | 1.018 | 1.018 |
| dataset7_CLINIC_metal_0033_data | 1 | 0.0 | 0.019 | 0.961 | 0.95 | 0.991 | 0.991 |
| dataset7_CLINIC_metal_0039_data | 1 | 0.013 | 0.039 | 0.994 | 0.998 | 0.879 | 0.879 |
| dataset7_CLINIC_metal_0040_data | 3 | 0.176 | 0.176 | 1.0 | 1.0 | 1.053 | 1.053 |
| dataset7_CLINIC_metal_0042_data | 2 | 0.136 | 0.167 | 0.973 | 0.971 | 0.897 | 0.897 |
| dataset7_CLINIC_metal_0045_data | 1 | 0.052 | 0.072 | 0.987 | 0.978 | 0.787 | 0.787 |
| dataset7_CLINIC_metal_0047_data | 3 | 0.0 | 0.0 | 1.0 | 0.994 | 0.976 | 0.976 |
| dataset7_CLINIC_metal_0047_data | 4 | 0.068 | 0.08 | 0.999 | 1.0 | 0.716 | 0.716 |
| dataset7_CLINIC_metal_0048_data | 1 | 0.049 | 0.049 | 0.99 | 0.991 | 0.837 | 0.837 |
| dataset7_CLINIC_metal_0048_data | 2 | 0.068 | 0.057 | 0.985 | 0.983 | 0.841 | 0.841 |
| dataset7_CLINIC_metal_0049_data | 2 | 0.102 | 0.102 | 0.933 | 0.93 | 0.996 | 0.996 |
| dataset7_CLINIC_metal_0050_data | 1 | 0.041 | 0.041 | 0.973 | 0.968 | 0.999 | 0.999 |
| dataset7_CLINIC_metal_0050_data | 2 | 0.063 | 0.063 | 0.942 | 0.953 | 0.999 | 0.999 |
| dataset7_CLINIC_metal_0051_data | 2 | 0.034 | 0.045 | 0.965 | 0.971 | 0.999 | 0.999 |

