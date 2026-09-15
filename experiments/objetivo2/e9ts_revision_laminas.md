# Revision dirigida de laminas del Objetivo 2 (autora)

Condicion de reapertura de la decision 2026-09-14 (4): el recorte de 6 mm se mantiene como principal salvo que
esta revision muestre un fallo suyo. Plantilla: `e9ts_revision_laminas_autora.csv` (16 casos). Solo la llena la
autora; las columnas `veredicto` y `nota` empiezan vacias.

## Que casos y por que

- **14 casos** de la cohorte del Objetivo 2 (QC de nivel, F = 0.001) donde el recorte cambia el corredor
  transsacro en 1 mm o mas: `|D_TS(6 mm) - D_TS(3 mm)| >= 1 mm`.
- **`CLINIC_0022` y `CLINIC_0043`**: cajas desplazadas mas de 10 mm entre recortes tras la limpieza (E10b, #49).
  `CLINIC_0022` tiene ademas un componente de S1 del 31-44% (E10).

## Que abrir por caso (rutas en el CSV; las laminas estan en `outputs/`, ignorado por git)

1. **`lamina_corredor_6mm`** (`outputs/e9ts/laminas/`) y **`lamina_corredor_3mm`** (`outputs/e9ts_3mm/laminas/`).
   - Izquierda: perfil del mejor `D_TS` por nivel, en mm respecto al platillo de S1; lineas guia a 8.5, 10 y 12 mm.
   - Derecha: corte coronal por el centro del mejor corredor. Linea roja = eje; amarillas = bordes del cilindro
     de diametro `D_TS`. El corte proyecta el eje: no muestra toda la mascara.
2. **`lamina_mascaras`** (`outputs/ts_total_qc/laminas/<caso>_planos.png`).
   - Fila 1 = recorte de 3 mm; fila 2 = 6 mm; fila 3 = diferencias (rojo solo 3 mm, azul solo 6 mm).
   - Colores: `sacrum` naranja, `vertebrae_S1` rojo, `hip_left` cian, `hip_right` verde. Cortes por el punto de
     S1 de R1 (no por el corredor).

## Que mirar

- **Cilindro:** dentro de hueso, sin cruzar forámenes ni canal sacro y sin salir a tejido blando.
- **Nivel:** el corredor esta a la altura de S1, no en S2 ni en L5.
- **Por que difieren 6 y 3 mm:** otro nivel (pico del perfil a otra altura), otro angulo, o una mascara distinta.
- **Mascaras:** siguen la cortical del sacro y del ala, sin fuga a tejido blando ni a L5; S1 (rojo) ocupa el
  primer segmento sacro.
- **Fallo de recorte:** una mascara cortada en linea recta, o una parte del sacro o del ala ausente, en un
  recorte y no en el otro.
- **`CLINIC_0022` y `CLINIC_0043`:** fragmentos separados del sacro o de S1. ¿Fractura real o error de etiqueta?

## Como llenar `veredicto`

| Valor | Cuando |
|---|---|
| `ok` | sin error visible en ninguno de los dos recortes |
| `fallo_6mm` | error visible solo con 6 mm (**reabre la decision 2026-09-14 (4)**) |
| `fallo_3mm` | error visible solo con 3 mm |
| `fallo_ambos` | error visible con los dos |
| `dudoso` | no se puede juzgar con estos cortes |

En `nota`, que se ve y en que panel. Las laminas son cortes sueltos: no demuestran ausencia de error (#19, #21).
Un `dudoso` se resuelve mirando la mascara entera, que esta en Khipu (`~/metalsynth/data/ts_total/`).
