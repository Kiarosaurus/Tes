# Diseno A — renderizador por difusion en espacio de imagen (Objetivo 3)

> **Estado: BORRADOR para revision de la autora. NO preinscrito.** Decision que lo origina: `01-decisiones.md`,
> 2026-09-19 (tras el No-Go de P1, #91). Se preinscribe (se congela y se registra) **antes de entrenar**. Todo lo marcado
> `[DECIDIR]` necesita respuesta de la autora; lo marcado `[SUPUESTO]` es propuesta del asistente como asesor y queda
> declarado. Nada de este documento esta medido salvo donde se cita un experimento.

## 1. Que resuelve y que no

- **Resuelve:** el error de ida y vuelta del autoencoder (P1: 61.72 HU en hueso, 69.89 HU en `B_delta`). Sin latente,
  lo que no se genera queda identico al CT de origen, voxel a voxel.
- **No resuelve, y se declara:** que la apariencia del artefacto pueda generarse en el dominio de la imagen sin
  proyecciones (supuesto de `main.tex:56`); el streaking lejano mas alla de `B_delta` (truncado por diseno, #57); la
  reconstruccion desconocida de CLINIC-metal (#73).
- **Cambia respecto a `main.tex`:** desaparecen "Latent", "Stable Diffusion 1.5 backbone" y ControlNet (no hay base
  preentrenada en pixeles de CT que congelar; #74 se cierra por reemplazo). Se mantienen multi-ventana, `B_delta`,
  mascara de implante rigido, protocolo de Peters, muestreador y SAP.

## 2. Formulacion

**Inpainting condicionado en la region de generacion `G = M ∪ B_delta`**, donde `M` es la mascara del implante y
`B_delta` la banda de ~12 mm a su alrededor (distancia euclidea 3D con el spacing del header, como en P1).

- **Entrada del modelo:** el parche con `G` borrado (contexto intacto fuera de `G`), la mascara `M` y la mascara `G`.
- **Salida:** los HU dentro de `G`. Fuera de `G` se copia el original (composicion exacta).
- **Entrenamiento:** pares reales. En pacientes de entrenamiento con metal, `M` sale del metal real y el objetivo es el
  CT real dentro de `G`. El modelo aprende "dado este contexto y esta mascara, que aspecto tienen implante y artefacto".
- **Uso (sintesis):** paciente sin metal + mascara de tornillo parametrico en una pose -> el modelo rellena `G`.

## 3. Datos y particion

- **Particion:** la de P1 (`experiments/objetivo1/p1_particion.csv`, semilla 20260917), para cumplir la *Strict
  Isolation Rule* (`main.tex:111`) y reutilizar un test ya fijado. Con metal: **74 pacientes de entrenamiento**
  (52 dataset7 + 22 dataset6), 5 de validacion, **20 de test**. Sin metal en test: 14 (dataset6).
- **Unidad de entrenamiento:** parches 2.5D centrados en cortes axiales que cortan metal. Numero de parches: **sin
  medir** (se cuenta en CPU en la semana 1).
- **`[DECIDIR]` Mascara `M` en entrenamiento.** Opciones (ligadas a #95):
  - (a) umbral 2500 HU (el de cribado, #22). E8: cerca del semimaximo, recorta periferia, fragmenta 10 de 62.
  - (b) semimaximo local por objeto (propuesta abierta de #22/#46). Mas fiel al borde; mas codigo.
  - **Recomendado: (a) para el piloto y (b) como sensibilidad**, porque (a) ya esta validado en E1/E8.
- **`[SUPUESTO]` Que implantes entran:** todo el metal de los pacientes de entrenamiento (placas, protesis, tornillos),
  no solo tornillos. Mas datos de apariencia; el tipo de implante no esta anotado (`main.tex:111`). Riesgo: el modelo
  aprende sobre todo protesis grandes. Se reporta la mezcla por tamano de componente (E8 ya mide componentes de metal).

## 4. Representacion

- **`[SUPUESTO]` Codificacion `pub+asinh`** (3 canales: LW asinh [-1000, 20000], MW, SW). Identidad exacta en hueso y
  metal (E6c: 0.00 HU a float; P1: 0.00 en identidad), y es la primera del orden a priori de #76.
- **Lectura de HU del resultado:** `regla` de P1 (canal mas estrecho no saturado). Mismo codigo (`e6b_vae_sd15.regla`).
- **2.5D:** 3 cortes axiales contiguos -> 9 canales de imagen + 2 de mascara (`M`, `G`) en la entrada; se genera el
  corte central. `[SUPUESTO]`.
- **`[DECIDIR]` Tamano del parche.** Un tornillo iliosacro cruza el corte axial casi de lado a lado: su largo es el
  del corredor (Kaiser, `main.tex:113`) mas 2 x 12 mm de banda. **Recomendado 256 x 256** (~200 mm a ~0.78 mm) para que
  el tornillo entero y su banda quepan; 128 x 128 no los contiene. Es la eleccion que mas pesa en el computo.

## 5. Modelo y entrenamiento `[SUPUESTO]`

- U-Net de difusion condicionada por concatenacion (tipo DDPM/ADM), en pixeles, float32. Sin base preentrenada.
- Objetivo de prediccion de ruido (o `v`) con perdida **solo dentro de `G`** (fuera se copia).
- Muestreo DDIM, 50 pasos, semillas fijas; varias muestras por caso para medir variabilidad.
- Validacion: 5 pacientes con metal; registra curva, **no elige checkpoint** (igual que P1).
- **Presupuesto:** sin medir. Semana 1: prueba corta de 200 pasos en Khipu (s/paso, memoria), como en P1.

## 6. Tornillo sintetico (uso)

- **Geometria (ya decidida, `main.tex:113`, #41 via c):** cilindro liso rigido; diametro 6.5-8.0 mm
  (`gardner2010safezones`) y 6.3-8 mm (`kaiser2014dysmorphism`); largo acotado por el corredor medido en cada volumen.
  Rosca, canulacion, cabeza y arandela: sin fuente textual -> simplificacion declarada.
- **Rasterizacion:** cilindro a la resolucion del CT; `M` = voxeles cuyo centro cae dentro. `[SUPUESTO]`
- **Pose inicial (antes del muestreador P3):** eje del corredor S1 ya medido en E9-TS (`e9ts_corredor.csv`: centro
  `c_x/c_y/c_z`, direccion `u_x/u_y/u_z`, largo `L_TS_mejor_mm`, viabilidad por diametro y holgura). Cuando P3 exista,
  sus poses.
- **`[DECIDIR]` Brecha de mascara (#95):** diametro del cilindro principal 6.5-8.0 mm (publicado) y **sensibilidad con
  5.00 mm** (fuste medido en E8, que es lo que el modelo vio en entrenamiento). Recomendado.

## 7. Evaluacion (a preinscribir; sin umbrales numericos no verificados, como pide `main.tex:115`)

| Bloque | Pacientes | Que se mide | Contra que |
|---|---|---|---|
| E-A1 Reconstruccion de implante real | 20 de test con metal | Bone integrity, metal integrity, streak amplitude (Peters, nombres publicados) dentro de `G`; MAE en HU dentro de `G` (descriptivo) | El CT real (referencia de apariencia, no ground truth fisico, #73) |
| E-A2 Tornillo sintetico | 14 de test sin metal | Las mismas metricas de Peters; **costura en el borde de `B_delta`** (salto de HU a traves del borde) | (i) copia-pega ingenua (voxeles de `M` a HU de metal, sin artefacto), baseline que ya promete `main.tex:98`; (ii) brazo fisico de Peters en el subconjunto reducido |
| E-A3 Preservacion fuera de `B_delta` | todos | RMSE y SSIM fuera de `G` | **Cero por construccion**; se reporta como tal, no como resultado |
| E-A4 QC visual | muestra fija | Laminas con el mismo formato de las de E9-TS | Revision de la autora |

- **Criterio de exito `[DECIDIR]`:** `main.tex:98` dice *"Lower profile discrepancy than naive copy-paste insertion,
  with streak amplitudes statistically comparable to, or better than, the adopted physics-based protocol"*. Falta fijar
  **que prueba estadistica** y **que es "comparable"** antes de ver resultados (patron #76).

## 8. Riesgos conocidos

1. **Contexto con y sin artefacto (nuevo, #96).** En entrenamiento el contexto fuera de `G` ya trae el streaking lejano
   del implante real; en uso, el paciente sin metal tiene contexto limpio. El modelo puede depender de rayas que en uso
   no existen. Se ve en E-A2 como costura o como artefacto debil. Mitigacion posible: entrenar con contexto recortado
   o suavizado fuera de `G`; se decide tras la prueba corta.
2. **Brecha de mascara** (#95).
3. **Mezcla de implantes** dominada por protesis grandes (seccion 3).
4. **Computo sin medir** (#89): la prueba corta de la semana 1 es obligatoria antes de lanzar nada largo.

## 9. Semana 1 (orden)

1. Autora responde los `[DECIDIR]` (mascara de entrenamiento, parche, diametro, criterio de exito).
2. Script de extraccion de parches y conteo (CPU, local), con control: fuera de `G` el parche compuesto es identico
   al original bit a bit.
3. Prueba corta en Khipu (200 pasos): s/paso y memoria.
4. Preinscripcion: este documento pasa a `PREINSCRITO` con fecha, y se registra en `01-decisiones.md`.
5. En paralelo: paso 0 de MAISI (normalizacion de HU en el codigo) y edicion de `main.tex` (titulo, Obj 1, Obj 3).
