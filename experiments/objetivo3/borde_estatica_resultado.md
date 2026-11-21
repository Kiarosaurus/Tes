# Observaciones visuales de la autora cuantificadas (exploratorio; `borde_estatica.py`)

Validación 0101/0102, semillas 0–4, cortes con M de Peters. Mediana por paciente (cortes y semillas); entre paréntesis, los dos pacientes.

| brazo | salto en el borde de G, mediana \|Δ\| 1 px dentro (HU) | M con \|HU − mediana 3×3\| > 1500 HU | M por debajo de 2500 HU |
|---|---|---|---|
| peters_Ti | 123 (0101 86, 0102 161) | 3.4 % (0101 6.4 %, 0102 0.4 %) | 14.0 % (0101 2.4 %, 0102 25.6 %) |
| run04_mejor | 36 (0101 34, 0102 38) | 0.2 % (0101 0.2 %, 0102 0.3 %) | 18.2 % (0101 22.1 %, 0102 14.3 %) |
| run04_mejor_p50_e0.3 | 36 (0101 34, 0102 39) | 0.2 % (0101 0.0 %, 0102 0.5 %) | 15.6 % (0101 19.3 %, 0102 11.9 %) |
| run04_mejor_p100_e0.3 | 35 (0101 33, 0102 37) | 0.3 % (0101 0.0 %, 0102 0.6 %) | 15.6 % (0101 19.1 %, 0102 12.1 %) |
| b_min_l0 | 32 (0101 29, 0102 35) | 0.3 % (0101 0.4 %, 0102 0.2 %) | 40.2 % (0101 43.2 %, 0102 37.2 %) |
| b_min_l0.8_t1000 | 34 (0101 31, 0102 37) | 0.9 % (0101 1.2 %, 0102 0.7 %) | 27.5 % (0101 29.7 %, 0102 25.2 %) |
| b_min_l3_t300 | 33 (0101 30, 0102 36) | 0.4 % (0101 0.7 %, 0102 0.1 %) | 11.1 % (0101 12.5 %, 0102 9.7 %) |

Límites: 2 pacientes; Peters = referencia física; un solo umbral de «estática» (1500 HU) y de «gris» (2500 HU); el real no se calcula porque su M se define por umbral.
