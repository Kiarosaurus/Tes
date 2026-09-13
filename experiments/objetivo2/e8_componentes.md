# E8 — censo morfologico del metal en dataset7 (#41, #13)

Propuesta de script sin validar. Clases morfologicas, no tipos de implante. Laminas en `outputs/e8_qc/`.

Volumenes: 76; con error: 0.

## Cohorte: evaluacion (`grupo 1`, una unidad por paciente) (n = 65)

| Clase (objetos dentro del cuerpo) | objetos | volumenes con >= 1 |
|---|---|---|
| alargado | 57 | 36 |
| laminar | 1 | 1 |
| masivo | 23 | 17 |
| otro | 170 | 58 |

- Volumenes con **>= 1 candidato a tornillo iliosacro/transsacro**: **17 de 65** (21 objetos).
- Volumenes sin ningun objeto dentro del cuerpo: 0.

## Cohorte: todos los archivos analizados (75 de dataset7 + union derivada) (n = 76)

| Clase (objetos dentro del cuerpo) | objetos | volumenes con >= 1 |
|---|---|---|
| alargado | 64 | 39 |
| laminar | 1 | 1 |
| masivo | 26 | 20 |
| otro | 203 | 66 |

- Volumenes con **>= 1 candidato a tornillo iliosacro/transsacro**: **18 de 76** (22 objetos).
- Volumenes sin ningun objeto dentro del cuerpo: 3.

## Objetos alargados (cohorte de evaluacion)

- Objetos: 57; formados por mas de un fragmento a HU > 2500: **9**.

| Medida (mm) | mediana | p10 | p90 |
|---|---|---|---|
| `L_mm` | 79.30 | 36.40 | 107.08 |
| `d_eq_2500_mm` | 4.25 | 2.71 | 5.59 |
| `d_ext_2500_mm` | 4.97 | 3.97 | 6.25 |
| `d_ext_semimax_mm` | 5.08 | 2.99 | 6.11 |

- `d_ext_2500 - d_ext_semimax`: mediana 0.24 mm (p10 -1.21, p90 1.45).
- `d_ext_semimax` dentro de 6.0-8.0 mm: 5 de 57; por debajo: 49; por encima: 3.
- Umbral de semimaximo local: mediana 2818 HU (p10 1991, p90 6587); HU p50 del objeto: mediana 3296.

### Candidatos a tornillo iliosacro/transsacro

| Caso | L | fragmentos | d_ext_2500 | d_ext_semimax | dz a S1 | HU p50 |
|---|---|---|---|---|---|---|
| dataset7_CLINIC_metal_0001_data | 83 | 1 | 4.97 | 4.90 | -5 | 3456 |
| dataset7_CLINIC_metal_0002_data | 108 | 1 | 3.90 | 3.91 | -5 | 2771 |
| dataset7_CLINIC_metal_0004_data | 43 | 1 | 2.84 | 5.68 | -17 | 2787 |
| dataset7_CLINIC_metal_0008_data | 102 | 3 | 4.56 | 4.26 | -11 | 3080 |
| dataset7_CLINIC_metal_0008_data | 87 | 1 | 4.92 | 4.45 | -25 | 3199 |
| dataset7_CLINIC_metal_0018_data | 98 | 5 | 4.07 | 4.46 | -17 | 2842 |
| dataset7_CLINIC_metal_0024_data | 117 | 1 | 4.01 | 3.71 | -6 | 3015 |
| dataset7_CLINIC_metal_0028_data | 45 | 3 | 4.63 | 6.08 | -16 | 2730 |
| dataset7_CLINIC_metal_0033_data | 107 | 1 | 4.75 | 5.13 | -26 | 2988 |
| dataset7_CLINIC_metal_0039_data | 77 | 1 | 4.93 | 4.65 | -36 | 3092 |
| dataset7_CLINIC_metal_0040_data | 33 | 2 | 6.16 | 6.78 | -30 | 2719 |
| dataset7_CLINIC_metal_0042_data | 66 | 3 | 5.11 | 6.16 | -16 | 2772 |
| dataset7_CLINIC_metal_0045_data | 97 | 2 | 4.26 | 4.02 | -16 | 2914 |
| dataset7_CLINIC_metal_0047_data | 36 | 1 | 4.16 | 5.61 | -14 | 2893 |
| dataset7_CLINIC_metal_0047_data | 87 | 2 | 4.37 | 3.76 | -23 | 3083 |
| dataset7_CLINIC_metal_0048_data | 102 | 1 | 4.75 | 4.19 | -8 | 3103 |
| dataset7_CLINIC_metal_0048_data | 87 | 1 | 4.97 | 4.38 | -20 | 3255 |
| dataset7_CLINIC_metal_0049_data | 98 | 1 | 4.47 | 5.08 | -29 | 2994 |
| dataset7_CLINIC_metal_0050_data | 72 | 1 | 5.20 | 5.57 | -11 | 3247 |
| dataset7_CLINIC_metal_0050_data | 63 | 1 | 5.14 | 5.66 | -24 | 3278 |
| dataset7_CLINIC_metal_0051_data | 88 | 1 | 5.33 | 4.80 | -16 | 3934 |
