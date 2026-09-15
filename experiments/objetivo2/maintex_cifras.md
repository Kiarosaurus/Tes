# Cifras de `main.tex` recalculadas (`Corridor measurement on the local cohort`)

Generado por `maintex_cifras.py` desde `e9ts_corredor.csv` y `grupos.csv` (versionados).
Recorte principal `default6mm`, sensibilidad `robust3mm`, F = 0.001. Cada frase se busca literal en `tesis/main.tex`. No cubre `Field limitation` (R1).

| # | Cifra | Frase buscada | Resultado |
|---|---|---|---|
| 1 | Cohorte sin osteosintesis | `Among 103 patients without osteosynthesis` | COINCIDE |
| 2 | Con S1 localizado | `91 had a located S1` | COINCIDE |
| 3 | Pasan la QC de nivel | `72 passed level quality control` | COINCIDE |
| 4 | Discordancia, grupo 2 | `excluded 11 of 34 patients with non-orthopaedic objects` | COINCIDE |
| 5 | Discordancia, grupo 3 | `7 of 57 clean patients` | COINCIDE |
| 6 | S1 en el borde del FOV | `one further patient was excluded because S1 reached the field-of-view border` | COINCIDE |
| 7 | Mediana e IQR de D_TS (6 mm) | `median of 9.5~mm (IQR 7.4--11.7)` | COINCIDE |
| 8 | Viables a 10 mm, 6 mm y 3 mm | `met in 29 of 72 patients with the default crop and in 27 with the robust crop` | COINCIDE |
| 9 | Limpieza sin efecto en D_TS ni viabilidad (F en 0-0.05, ambos recortes) | `Component cleaning changed neither the transsacral corridor diameter nor its 10~mm viability in this cohort at any tested fraction up to 5\%` | COINCIDE |
| 10 | Fraccion del eje <= 150 HU (6 mm) | `inside the sacral masks was 0.42` | COINCIDE |
| 11 | Grupo 1: hueso -> semimaximo | `from 53.8\% to 40.4\% in 52 patients with the default crop` | COINCIDE |
| 12 | Grupo 1: 2500 HU igual que semimaximo | `gave the same proportion` | COINCIDE |

**12 de 12 cifras coinciden.**

Informativo (no impreso en `main.tex`): medidas que cambian con F en la cohorte: ['D_IS_izq_max_mm'], en 1 caso x recorte: ['dataset6_CLINIC_0012_data'].
