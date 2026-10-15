# Resultados de las mediciones de DEC 2026-10-15 (posteriores; se completa a medida que llegan)

> Cada bloque cita su script y su salida. Lo visto se registra en `visto.md`.

## D4 — diferencia de diametro entre mascaras (semimaximo local frente a 2500 HU)

Fuente: `experiments/objetivo2/e8_componentes.csv` (E8 ya media `d_ext_2500_mm` y `d_ext_semimax_mm` por componente),
filtrado a pacientes de entrenamiento de `p1_particion.csv` y `vol_mm3` en [500, 4000]. Calculo del 2026-10-15.

- 32 componentes (todos de clase `alargado`) de 23 pacientes de entrenamiento.
- `d_ext_semimax - d_ext_2500`: mediana **-0.24 mm**, IQR [-0.54, 0.02], p10 -1.32, p90 0.39.
- Medianas: 5.17 mm a 2500 HU y 5.02 mm a semimaximo.
- Lectura (sin regla, dato de la limitacion): en tornillos la mascara por semimaximo seria de mediana un cuarto de
  milimetro mas estrecha, por debajo de un voxel. La sensibilidad no se entreno (coste); su efecto sobre el modelo no
  se midio.

## D8 — preservacion del protocolo fisico fuera de `G`

Fuente: `a27_preservacion_peters.py` -> `outputs/obj3_pose/a27/`. 13 pacientes de E-A2 x 2 replicas, cortes simulados,
fuera de `G`, dentro del cuerpo (> -500 HU, mayor componente, agujeros rellenos).

| | mediana | rango |
|---|---|---|
| RMSE (HU) | 31.4 | 20.1 a 42.4 |
| SSIM ([-1000, 2000] HU) | 0.9069 | 0.8268 a 0.9653 |

El sintetizador vale 0 / 1 por construccion en esta region (no es resultado).
