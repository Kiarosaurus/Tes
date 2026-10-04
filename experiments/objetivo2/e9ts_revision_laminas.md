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

## Como mirar la lamina, paso a paso

> Anadido el 2026-10-03. Las secciones de arriba dicen **que** se juzga; esta dice **como se ve**, con el
> vocabulario minimo. No cambia ningun criterio.

### Vocabulario, solo el necesario

- **Cortical**: el borde blanco brillante del hueso. Es su capa dura exterior.
- **Ala del sacro**: las dos partes anchas, a izquierda y derecha del cuerpo central.
- **Canal sacro**: el conducto oscuro que baja por el centro.
- **Foramenes**: los agujeros oscuros a los lados del canal.
- **Contorno**: en la lamina de mascaras no se pinta el hueso relleno, sino **la linea de su borde**.
  `sacrum` naranja, `vertebrae_S1` rojo, `hip_left` cian, `hip_right` verde.

### La lamina de mascaras (`outputs/ts_total_qc/laminas/<caso>_planos.png`)

Nueve paneles: tres columnas (axial, coronal, sagital) por tres filas.

| Fila | Que es |
|---|---|
| 1 | contornos con el recorte de **3 mm** |
| 2 | contornos con el recorte de **6 mm** |
| 3 | **solo las diferencias**: rojo = esta solo en 3 mm; azul = esta solo en 6 mm |

**La fila 3 es donde se juzga**, y trae la cifra hecha: el titulo de cada panel imprime cuantos voxeles
son rojos y cuantos azules. En `CLINIC_0076`, el panel coronal dice *"rojo solo 3 mm: 527 vox, azul solo
6 mm: 1430 vox"*. Azul casi el triple que rojo significa que el recorte de **3 mm perdio** hueso que el
de 6 mm si tiene.

Como leerlo sin interpretar de mas:

1. **Diferencias finas que siguen el borde**, repartidas y de pocos voxeles: ruido entre dos
   segmentaciones. **No es fallo.**
2. **Mancha compacta de un solo color** dentro del hueso, o un trozo de ala que esta en una fila y no en
   la otra: perdida de mascara. Anota de que color es, que dice cual recorte la perdio.
3. **Borde recto, como cortado con regla**, que no sigue la forma del hueso: es la firma de un recorte
   mal puesto. El hallazgo mas claro.
4. **Contorno que se sale hacia el musculo o hacia L5**: fuga de la mascara.

Los **circulos amarillos** son las esferas de densidad de E9b. **Ignoralos**: no son de esta revision.

### La lamina de corredor (`outputs/e9ts/laminas/<caso>.png` y su gemela de 3 mm)

Dos paneles.

- **Izquierda, el perfil.** Vertical: altura en mm respecto del platillo de S1, negativa hacia abajo.
  Horizontal: el mejor diametro de corredor a esa altura. Las punteadas marcan 8.5, 10 y 12 mm. Hay uno
  o dos picos: el de arriba es el corredor principal, el de abajo el segundo.
- **Derecha, el corte coronal** por el centro del mejor corredor. La **linea roja** es el eje; las
  **amarillas**, los bordes del cilindro de diametro `D_TS`.

Lo util es **poner los dos perfiles uno al lado del otro**: si el pico principal cambia de altura, la
diferencia entre recortes viene de que cada uno encontro el corredor **en otro nivel**, no de que uno
este roto. Eso va en `nota` y **no es fallo por si solo**.

**Aviso del propio dibujo:** el panel derecho **proyecta** el eje sobre un unico corte coronal. Que el
cilindro se vea fuera del hueso ahi no prueba que lo este en 3D, ni al reves.

### Orden sugerido por caso

1. Abre las **dos** laminas de corredor y compara la altura del pico principal.
2. Abre la de mascaras y ve directo a la **fila 3**. Lee las dos cifras de voxeles de cada panel.
3. Decide: ¿hay mancha compacta o borde recto, y en que recorte? Eso da el `veredicto`.
4. En `nota`, **que panel** miraste y **que viste**. Si no alcanza para decidir, `dudoso`.

Un caso bien anotado toma pocos minutos. Si uno se alarga mucho, probablemente sea `dudoso`.

## Dudas frecuentes

> Anadido el 2026-10-03, a partir de las preguntas de la autora.

### ¿Que es exactamente un fallo?

**Un fallo es de la MASCARA, no del tornillo.** Esta revision no juzga si la trayectoria es
quirurgicamente buena: eso es otra revision, que **todavia no existe** y que ademas depende de #130.

Es fallo, y solo esto:

- una **region compacta** de hueso que un recorte tiene y el otro no;
- un **borde recto**, como cortado con regla, que no sigue la forma del hueso;
- la mascara **fugandose** hacia el musculo o hacia L5.

### "La mascara no cubre todo el hueso, pero el tornillo se ve bien". ¿Que anoto?

**Anota el fallo de la mascara e ignora que el tornillo se vea bien.** Que se vea bien no es prueba de
nada aqui, y la razon importa:

El diametro del cilindro dibujado, `D_TS`, **se calcula a partir de esa misma mascara**. Si la mascara
perdio hueso, `D_TS` sale mas chico, y el cilindro se dibuja mas delgado — justo lo necesario para
caber. Por eso **un cilindro que se ve perfecto es compatible con una mascara rota**: el dibujo se
encogio con el error. Juzgar por el cilindro seria circular.

**Pero mira primero si falla en los dos recortes o en uno solo.** Si los dos pierden el mismo hueso, es
un error de la segmentacion, no del recorte: eso es `fallo_ambos`, se anota, y **no reabre la decision**.
Lo unico que la reabre es `fallo_6mm`.

### ¿Y si quiero abrir ITK-SNAP?

Puedes, pero **no vas a ver lo que necesitas**. Verificado: de los 16 casos, **16 tienen el CT en esta
computadora y 0 tienen la mascara**. Las mascaras de TotalSegmentator estan solo en Khipu
(`~/metalsynth/data/ts_total/`).

Entonces, en ITK-SNAP ves **el hueso**, no **lo que el programa considero hueso**. La lamina es el unico
sitio donde la mascara es visible.

Para lo que **si** sirve: confirmar que el hueso realmente esta ahi donde la mascara no lo cubre. Eso
**refuerza** un `fallo`, porque la premisa de "la mascara perdio hueso" es que el hueso exista. Lo que
**no** puede hacer es desmentir la lamina.

### "En la foto no se aprecia todo el hueso, pero en ITK-SNAP si"

Eso **no es una contradiccion**, y no cambia el veredicto. La lamina muestra **tres cortes sueltos**, no
el volumen entero; es normal que en ITK-SNAP veas hueso que el corte no alcanza. La pregunta de esta
revision no es "¿se ve todo el hueso?", sino "¿los dos recortes lo cubren igual **en estos cortes**?".

Si de verdad no alcanza para decidir, la respuesta es **`dudoso`**, y se resuelve trayendo la mascara
entera de Khipu. No se resuelve con el CT.

### ¿Que es "mejor `D_TS` en el nivel"?

Es el eje horizontal del perfil. A **cada altura**, el programa prueba muchos centros y 81 direcciones, y
se queda con **el corredor mas ancho que encuentra a esa altura**. Asi que el perfil responde: *si
tuviera que pasar un tornillo justo a esta altura, ¿cual es el mejor diametro posible?*

Un valor **0** significa que a esa altura **no se encontro ningun corredor valido** — normal por encima
y por debajo del sacro.

### Veo campanas en el perfil. ¿Eso es bueno o malo?

**Ninguna de las dos: es anatomia.** Cada campana es una altura donde existe un corredor ancho. Lo
normal son **dos**: la de arriba es el corredor principal, y la de abajo el segundo, que **#121** midio
que cae en S2 en 13 de 18 casos, pero en S3 en 4 y en S4 en 1.

Para **esta** revision la forma de la campana no se juzga. Lo unico que importa es **si cambia entre los
dos recortes**:

- **misma altura, diametro parecido** -> los dos recortes encontraron el mismo corredor;
- **el pico se mueve de altura** -> cada recorte encontro el corredor **en otro nivel**. Es el motivo de
  la diferencia, se anota en `nota`, y **no es fallo por si solo**;
- **una campana desaparece en un recorte** -> eso si apunta a que ese recorte perdio hueso. Ve a la
  fila 3 de la lamina de mascaras a confirmarlo.

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
