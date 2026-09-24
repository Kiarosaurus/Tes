# Revision dirigida de laminas del Objetivo 2

Condicion de reapertura de la decision **2026-09-14 (4)** (`#49`: recorte principal de 6 mm; se retira
la preferencia por 3 mm): el recorte de 6 mm se mantiene como principal **salvo que esta revision
muestre un fallo suyo**. Planilla: `e9ts_revision_laminas_autora.csv`, **16 casos**.

> **Actualizado el 2026-09-23.** Tres cambios respecto de la version del 2026-09-14: las rutas del CSV
> ahora siguen la misma convencion que las otras dos revisiones; se anadio la columna `revisor`; y **el
> criterio de nivel se retiro**, porque contradecia lo que se midio despues. Ver el apartado
> *Que cambio y por que* al final.

## Que casos y por que

- **14 casos** de la cohorte del Objetivo 2 (QC de nivel, F = 0.001) donde el recorte cambia el corredor
  transsacro en 1 mm o mas: `|D_TS(6 mm) - D_TS(3 mm)| >= 1 mm`. El signo se reparte: en **7** el
  recorte de 6 mm da **menos** corredor y en **7** da **mas**. No es un sesgo de direccion, es
  inestabilidad; por eso se juzgan **fallos**, no diferencias.
- **`CLINIC_0022` y `CLINIC_0043`**: cajas desplazadas mas de 10 mm entre recortes tras la limpieza
  (E10b, #49), con diferencia de corredor **cero**. `CLINIC_0022` tiene ademas un componente de S1 del
  31-44% (E10).

## Que abrir por caso

Las rutas estan en el CSV, **relativas a `experiments/objetivo2/`**, igual que en
`r1_revision_laminas_revisor.csv` y `r2_nivel_pico_revisor.csv`. Las 48 laminas (3 por caso) estan en
disco; `outputs/` esta ignorado por git.

1. **`lamina_corredor_6mm`** (`outputs/e9ts/laminas/<caso>.png`) y
   **`lamina_corredor_3mm`** (`outputs/e9ts_3mm/laminas/<caso>.png`).
   - Izquierda: perfil del mejor `D_TS` por nivel, en mm respecto al platillo de S1; lineas guia a
     8.5, 10 y 12 mm.
   - Derecha: corte coronal por el centro del mejor corredor. Linea roja = eje; amarillas = bordes del
     cilindro de diametro `D_TS`. El corte proyecta el eje: no muestra toda la mascara.
2. **`lamina_mascaras`** (`outputs/ts_total_qc/laminas/<caso>_planos.png`).
   - Fila 1 = recorte de 3 mm; fila 2 = 6 mm; fila 3 = diferencias (rojo solo 3 mm, azul solo 6 mm).
   - Colores: `sacrum` naranja, `vertebrae_S1` rojo, `hip_left` cian, `hip_right` verde. Cortes por el
     punto de S1 de R1 (no por el corredor).

## Que mirar

- **Cilindro:** dentro de hueso, sin cruzar foramenes ni canal sacro y sin salir a tejido blando.
- **Por que difieren 6 y 3 mm:** otro nivel (pico del perfil a otra altura), otro angulo, o una mascara
  distinta. **Identificar cual de los tres es el motivo es la parte util de esta revision.**
- **Mascaras:** siguen la cortical del sacro y del ala, sin fuga a tejido blando ni a L5; S1 (rojo)
  ocupa el primer segmento sacro.
- **Fallo de recorte:** una mascara cortada en linea recta, o una parte del sacro o del ala ausente, en
  un recorte y no en el otro.
- **`CLINIC_0022` y `CLINIC_0043`:** fragmentos separados del sacro o de S1. ¿Fractura real o error de
  etiqueta? Enlaza con **#125**, que deja abierto que la cohorte se selecciono **sin osteosintesis**,
  no verificada **sin fractura**.

### El nivel NO es criterio de fallo

La version anterior de este documento pedia comprobar que *"el corredor esta a la altura de S1, no en
S2 ni en L5"*. **Eso se retira**, porque contradice lo medido despues:

- El **mejor corredor global** de la cohorte de 72 esta a una mediana de **20 mm por debajo** del punto
  de S1 (p10 -33, p90 -9), y **36 de 72 casos** lo tienen a mas de 20 mm.
- La revision del segundo corredor (**#121**) encontro que corredores a **-24 mm** ya se juzgan **S2**,
  y que el nivel **no lo determina la profundidad**: un corredor a -39 mm resulto S2 mientras otros a
  -36 y -33 mm resultaron S3.

Con el criterio antiguo se marcarian como fallo corredores anatomicamente correctos. **Si el nivel
llama la atencion, anotarlo en `nota`, no puntuarlo como fallo.**

## Como llenar la planilla

| Columna | Que poner |
|---|---|
| `revisor` | quien juzga. **Nuevo el 2026-09-23**; antes la planilla no registraba autoria |
| `veredicto` | una de las cinco categorias de abajo |
| `nota` | que se ve y en que panel. Obligatoria en todo lo que no sea `ok` |

| `veredicto` | Cuando |
|---|---|
| `ok` | sin error visible en ninguno de los dos recortes |
| `fallo_6mm` | error visible solo con 6 mm (**reabre la decision 2026-09-14 (4)**) |
| `fallo_3mm` | error visible solo con 3 mm |
| `fallo_ambos` | error visible con los dos |
| `dudoso` | no se puede juzgar con estos cortes |

Las laminas son cortes sueltos: **no demuestran ausencia de error** (#19, #21). Un `dudoso` se resuelve
mirando la mascara entera, que esta en Khipu (`~/metalsynth/data/ts_total/`).

## Que cambio y por que (2026-09-23)

1. **Rutas del CSV.** Eran relativas a la raiz del repositorio
   (`experiments/objetivo2/outputs/...`), mientras que las otras dos revisiones usan rutas relativas a
   `experiments/objetivo2/` (`outputs/...`). Unificadas a esta ultima. Las 48 resuelven.
2. **Columna `revisor`.** No existia. El original quedo en
   `e9ts_revision_laminas_autora.sin_revisor.csv`.
3. **Criterio de nivel retirado**, por lo explicado arriba. Es el unico cambio de **fondo**: los otros
   dos son de forma.

Lo demas —los 16 casos, los tres paneles, las cinco categorias de `veredicto`, la condicion de
reapertura y la advertencia de #19/#21— **no cambia**. La especificacion de 2026-09-14 seguia siendo
correcta en todo eso.
