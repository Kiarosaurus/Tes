# Propuesta de cierre de las `\GAPDEC` — revision experta, 2026-10-15

> Escrita por Claude a pedido de la autora ("ponte en la postura de un PhD en generacion de TC con pocos datos;
> se estricto y severo; aunque haya que re-correr"). **No es una decision** (regla 3): cada bloque trae un texto
> propuesto para `01-decisiones.md` que solo la autora pega. Se redacto **sin leer**
> `propuesta_gapdec_2026-10-14.md`. Un borrador paso por un revisor independiente (agente en rol de tribunal severo,
> sin acceso a la propuesta anterior), que verifico cada cifra contra el repositorio y rechazo dos recomendaciones
> (D1 y D16) y ajusto otras doce; esta version las incorpora. Las cifras recalculadas hoy se marcan **(recalculo
> 2026-10-15)** con su fuente.
>
> Inventario: **18 marcas `\GAPDEC` = 16 decisiones** (cap. 1:48 = cap. 3:198; cap. 3:377 (contingencia) =
> introduccion:90).

## 0. Criterio con que se juzga

1. **Integridad de la preinscripcion.** Lo fijado antes de ver prueba no se mueve; lo agregado despues se rotula
   posterior y **solo puede bajar** la fuerza de una conclusion, nunca subirla.
2. **Simetria de la comparacion.** Si un brazo se mide con una vara que el otro no tiene, el contraste no es
   interpretable.
3. **Anclaje en la realidad.** Equivalencia frente a un simulador que exagera el artefacto (#159; Ti sobre lo real en
   22 de 24 cascaras, #174) no es realismo.
4. **Regla practica:** medicion barata -> se toma; sensibilidad cara que no puede cambiar ninguna conclusion -> se
   retira con justificacion escrita; ninguna regla nueva cuyo desenlace ya se pueda calcular se presenta como previa.

## 1. Hallazgos transversales

**H1. Que queda "previo".** `a20_v2` (56847) aborto antes de la etapa de prueba (#184). Ya se vieron: `Delta` de run05a
(157.1 HU), las amplitudes de validacion de run05b, E-A1 de v2 (#184), y los HTML de prueba de run04 (#176). Por eso
las reglas que se fijen hoy son **previas solo al TOST de prueba de v2** y posteriores a todo lo demas. Hace falta un
**inventario fechado de lo visto** antes de cada decision (ver D-extra 4); sin el, ningun "previo" es auditable.

**H2. El margen `Delta` es fragil y autorreferente.** `Delta = max(s, r)` = 196.3 HU con `s` = **rango** entre 5
semillas (crece con el numero de semillas) promediado sobre **2 pacientes** (291.6 y 100.9 HU), y `r` = 6.1 HU. Un
metodo mas ruidoso obtiene margen mas ancho. Ademas, en v2 cada modelo trae su propio `Delta` (run05a 157.1), asi que
los desenlaces de los tres modelos **no son comparables entre si** con su margen propio. El primario de v1 no se toca
(congelado); se cierra con D15-D16 y D-extra 3. Registro desfasado: DEC 2026-10-11 (3) aun dice 163.8 / `r` 23.2; los
vigentes son 196.3 / 6.1 (#175).

**H3. El difusor varia poco entre pacientes; Peters mucho mas** (recalculo 2026-10-15,
`outputs/obj3_pose/a24/run04_mejor/a24_por_paciente.csv`, n = 13, prueba v1 ya vista, descriptivo): media 1293.7
frente a 1594.7 HU; coeficiente de variacion **0.076 frente a 0.241**; Pearson r = 0.40 (p = 0.17), Spearman
rho = 0.37 (p = 0.21). Prueba de igualdad de varianzas pareadas de **Pitman-Morgan**: r(suma, diferencia) = -0.89,
p = 3.8e-5 (calculo del revisor). **Lectura prudente:** con n = 13 el IC95 de r va aprox. de -0.19 a 0.78, asi que no
se puede afirmar "no sigue al paciente"; si se puede afirmar que su dispersion entre pacientes es significativamente
menor. Parte de la dispersion de Peters puede venir de que exagera (#159). Ancla externa disponible: la dispersion
entre pacientes del artefacto real de tornillos (`d1_d2_resultado.md`, 18 pacientes). Implicancia **#185**.

**H4. La cordura frente a copia y pegado es degenerada.** Copia y pegado = 0.0 HU en los 13 (las ROIs excluyen `M`);
el Wilcoxon da `p = 2^-13 = 1.22e-4`, el minimo alcanzable con n = 13. Solo descarta "el difusor no genera nada".

**H5. Lo unico anclado en la realidad no tiene script ni regla.** El realismo frente a tornillos reales de prueba sigue
como `\GAPDATO`, y ademas **no tiene regla de lectura**: un descriptivo sin criterio no lo falsea nada. Tampoco esta
verificada la condicion de DEC 2026-10-09 (7) (columna `autora` de `tornillos_conteo.csv` completa). Prioridad 1.

**H6. El contraste primario tiene tres asimetrias entre brazos no declaradas** (recalculo 2026-10-15,
`a20_ea2_test.csv`; implicancia **#186**):
- **Cortes:** Peters se mide en cortes alternos (`k = 2`) y el difusor en todos: mediana de 62 341 frente a 124 679
  voxeles por paciente. `a20 --interseccion` existe y no se uso.
- **Piso de ruido:** la amplitud de `limpia_A - limpia_B` de Peters (solo ruido, sin metal) tiene mediana **184 HU**
  (media 177): casi `Delta`. La amplitud de Peters incluye ese ruido; la del difusor incluye su propia textura
  generada, que nunca se midio sin metal.
- **Suelo:** el difusor no puede bajar de -1000 HU; Peters si, y su fraccion bajo el suelo **no se midio** (`suelo_frac`
  vacio en sus 65 filas). Una reconstruccion aproximada del revisor sugiere ~1 % de la ROI de Ti y un efecto de
  recorte del orden de 100 HU sobre la diferencia; **no citable** hasta medirlo con `a20`.

## 2. Resumen

| # | `\GAPDEC` | Recomendacion | Computo | Cuando |
|---|---|---|---|---|
| D1 | suelo en HU (c1:48, c3:198) | la regla no es aplicable (post hoc y dependiente del percentil): se reportan los dos valores y se mide el suelo de forma simetrica | CPU local | antes de `a20_v2` |
| D2 | cabeza (c3:143) | desviacion declarada + sensibilidad CPU excluyendo ROIs cerca de la cabeza, en los dos brazos | CPU local | antes de `a20_v2` |
| D3 | lote 4 vs 16 (c3:204) | nota de correccion en DEC | ninguno | ya |
| D4 | semimaximo (c3:214) | no reentrenar (coste); medir diametro en tornillos 500-4000 mm3; declarar limitacion | CPU local | antes de redactar |
| D5 | costura en E-A2 (c3:228) | medirla en los dos brazos, como se fijo, + perfil de amplitud a traves del borde de `G` | CPU local | antes de `a20_v2` |
| D6 | `CLINIC_0066` (c3:232) | manda `grupos.csv` (grupo 2) | ninguno | ya |
| D7 | mecanismo del p95 (c3:242) | diagnostico de #152 con control de ida y vuelta real | GPU corta | antes de redactar |
| D8 | preservacion de Peters (c3:317) | caracterizar la referencia: RMSE/SSIM y piso de ruido | CPU local | antes de redactar |
| D9 | pose sin perturbar (c3:327) | justificar + exploratorio con expectativa fijada antes | GPU, horas | opcional |
| D10 | QC visual (c3:341) | regla fija; declarar lo ya visto; protocolo aparte para D3 a ciegas | ninguno | antes de mirar v2 |
| D11 | repositorio AAPM (c3:355) | citar version fija + tabla de desviaciones | ninguno | ya |
| D12 | efecto del Wilcoxon (c3:375) | declarar la degeneracion; comparador nuevo: artefacto parametrico | CPU local | antes de `a20_v2` |
| D13 | contingencia #90 (c3:377, intro:90) | retirar las marcas | ninguno | ya |
| D14 | supuesto *t* (c3:377) | enunciarlo; IC exacto por permutacion; sensibilidades solo bajan la categoria | CPU local | **antes de `a20_v2`** |
| D15 | desenlaces del TOST (c3:377) | tres desenlaces + direccion + multiplicidad declarada | ninguno | **antes de `a20_v2`** |
| D16 | margen no fijado por el difusor (c3:433) | margen minimo de equivalencia (sin elegir margen) + margen comun para los 3 modelos | CPU local | **antes de `a20_v2`** |

Mas cuatro decisiones nuevas que no son `\GAPDEC` (seccion 4, D-extra 1-4).

## 3. Detalle por decision

### D1 — Suelo de -1000 HU

**Hechos (recalculo 2026-10-15, `outputs/a9/a9_suelo_por_parche.csv`, 23 058 parches de entrenamiento y validacion,
77 pacientes):** `a9` ya guarda los vanos en HU (`vano_real`, `vano_ida_vuelta`). Perdida = vano real - vano tras ida y
vuelta:
- con el **p95 por paciente** (espejo del "p5 de la fraccion" ya elegido post hoc): mediana entre pacientes
  **225.0 HU > `Delta` = 196.3**; la superan **40 de 77** pacientes;
- con la **mediana por paciente**: **1.2 HU**.

**Lectura severa:** la regla del 2026-10-05 ya no puede funcionar como regla. (1) Su desenlace se puede calcular hoy,
asi que cualquier conversion que se fije ahora es post hoc. (2) Que se dispare o no depende enteramente del percentil,
que ya se habia elegido despues de ver la distribucion. (3) Su rama "cambiar la representacion" esta bloqueada por el
congelamiento. (4) El vano de la imagen no es la `streak amplitude` (que se calcula sobre la diferencia con la TC sin
metal), y lo dominan valores sin sentido fisico (minimo por paciente con mediana -3376 HU, #141).

**Recomendacion:**
1. Declarar la regla **no aplicable** y reportar los dos valores (225.0 con p95; 1.2 con mediana), sin elegir uno.
2. Medir en cambio el efecto del suelo **sobre el contraste primario**, de forma simetrica y siempre (sin disparador):
   (a) fraccion de la ROI de Peters Ti bajo -1000 HU; (b) TOST con las imagenes de Peters (con metal **y** limpia)
   recortadas a [-1000, inf), los dos brazos con el mismo suelo. Rotulado posterior, con su direccion conocida (baja la
   amplitud de Peters y acerca los brazos), y sujeto a D14 punto 3: **no puede subir la categoria del desenlace**.
3. El suelo queda como limitacion con esas cifras.

**Texto (DEC):** "La regla del suelo (2026-10-05) se declara no aplicable: su desenlace depende del percentil (225.0 HU
con p95 por paciente, 1.2 HU con mediana; `a9`), ya era calculable antes de fijar una conversion y su rama de cambio
de representacion esta bloqueada por el congelamiento. En su lugar se reportan la fraccion de la ROI de Peters bajo
-1000 HU y el TOST con los dos brazos recortados al mismo suelo, como analisis posterior que no puede elevar la
categoria del desenlace."

### D2 — Cabeza del tornillo

**Hechos:** D3 (2026-09-20) dejaba la cabeza como sensibilidad; el congelamiento (`diseno_A.md` §0) fijo "con cabeza".
La cabeza (`a11`: 8.0 x 4.5 mm, extremo +u) esta en los **dos** brazos. Las ROIs se recortan 8 mm desde el borde de
`M`, que incluye la cabeza: sus voxeles quedan fuera, pero en los primeros planos la cabeza es lo mas cercano para
radios > ~7 mm (revisor), asi que su influencia no esta excluida.

**Recomendacion:** declarar **desviacion de D3 absorbida por el congelamiento** (la geometria evaluada es la congelada;
la cabeza es real, Sayres; ensanchamiento de extremo > 2 mm en 12 de 59 componentes, E11). Sensibilidad **CPU, con los
dos brazos y sobre las salidas existentes**: recalcular `a20` excluyendo las ROIs a menos de 20 mm del extremo con
cabeza (12 mm de banda + 8 mm de guarda, fijado ahora). Sin GPU y sin la regla `Delta/2` sobre los 2 pacientes que ya
fijaron `Delta`.

**Texto (DEC):** "La sintesis usa el tornillo con cabeza congelado el 2026-10-09; se declara como desviacion de D3
(2026-09-20). Sensibilidad posterior: E-A2 sin las ROIs a menos de 20 mm del extremo con cabeza, en los dos brazos."

### D3 — Lote 4 frente a 16

Verificado: `a7_run04.sbatch`:65 `--lote 16` (tambien run05a/run05b). DEC 2026-10-08 punto 3 dice 4: error de
registro.

**Texto (DEC):** "Correccion de 2026-10-08 punto 3: el lote corrido es 16 (`a7_run04.sbatch`, metadatos, #148); 'lote 4'
fue un error de registro. No cambia ningun resultado."

### D4 — Mascara por semimaximo

**Recomendacion:** **no se entrena, por coste, y se dice asi** (no "se retira con evidencia"). Se mide lo unico barato
e interpretable: la **diferencia de diametro** (mm) entre semimaximo local y 2500 HU, **solo en componentes de
500-4000 mm3** (tamano tornillo; con todos los componentes dominan las placas). No se usa Dice: con ~5 voxeles de
diametro, un voxel de desplazamiento lo baja de 0.9. La cifra se reporta junto a la limitacion (#95; H3 de #176); no
decide nada.

**Texto (DEC):** "La sensibilidad por semimaximo (2026-09-20) no se entrena por coste. Se reporta la diferencia de
diametro entre las dos mascaras en componentes de 500-4000 mm3 de entrenamiento, como dato de la limitacion."

### D5 — Costura en E-A2

**Hechos:** DEC 2026-10-08 punto 7 la fijo **en E-A2, para los dos brazos, descriptiva**; el congelamiento la omitio.
En Peters no es un numero fabricado: es la **referencia fisica de continuidad** (exceso esperado ~0). `a10` espera
salidas de `a8`; se reutilizan `anillos()`/`salto()` o la funcion de `a23` que calcula `exceso_costura`.

**Recomendacion:** medirla como se fijo, en los dos brazos. Agregar el **perfil de `streak amplitude` por anillos de
2 mm a traves del borde de `G`** (8-10, 10-12, 12-14, 14-16 mm) en los dos brazos: el difusor da 0 exacto fuera de `G`
por construccion, y el perfil muestra cuanto artefacto real queda cortado (H2 de #176). El salto de medianas no lo ve.

**Texto (DEC):** "La costura de 2026-10-08 punto 7 se mide en E-A2 para los dos brazos, como se fijo; el congelamiento
la omitio. Se agrega el perfil de amplitud en anillos de 2 mm entre 8 y 16 mm, descriptivo y posterior."

### D6 — `CLINIC_0066`

Manda `grupos.csv` (grupo 2, objeto no ortopedico en el borde del FOV; auditoria sistematica posterior a
DEC 2026-09-21 (2)). No cambia receptores (corredor 8.9 mm) ni resultados.

**Texto (DEC):** "`dataset6_CLINIC_0066_data` se clasifica en grupo 2 segun `grupos.csv`, que prevalece sobre
2026-09-21 (2). No cambia receptores ni resultados."

### D7 — Mecanismo del p95

**Hechos:** `a15` ya guarda `u` crudo, `hu_regla` y `hu_lw`, pero **solo dentro de `M`**; el p95 por cascara esta en la
banda, asi que hay que regenerar guardando `u` en `G` (~2 min por paciente, #152).

**Recomendacion:** `0101` y `0102`, 5 semillas, `run04_mejor`; guardar `u` en `G`; decodificar con `regla_suave` y
con solo LW. **Control obligatorio:** la misma doble decodificacion sobre la ida y vuelta de parches **reales** de
validacion, porque LW (asinh, [-1000, 20000]) amplifica el error del modelo y sube el p95 por ruido. Medir el
corrimiento de p5, p50 y p95. Regla (fijada antes): el mecanismo es el decodificador solo si el p95 sintetico con LW
entra en la envolvente real en al menos 4 de las 7 cascaras **y** en las imagenes reales el cambio de decodificacion
no mueve el p95 mas que la mitad de ese corrimiento; si no, se atribuye al modelo o queda indeterminado.

**Texto (DEC):** "Diagnostico de #152 en validacion: `u` guardado en `G`, decodificacion con regla_suave frente a
solo LW, con control sobre la ida y vuelta de imagenes reales y regla de lectura fijada antes. No cambia el modelo ni
la evaluacion."

### D8 — Preservacion del protocolo fisico

**Recomendacion:** no presentarla como "ventaja" del difusor (su 0 es por construccion, la misma degeneracion que H4),
sino como **caracterizacion de la referencia**: RMSE (HU) y SSIM (rango fijo [-1000, 2000] HU) de `limpia_A` frente a
la TC original, fuera de `G` y dentro del cuerpo, en los 13 de E-A2; y, junto a ello, el **piso de ruido**
(`ruido_A-B`, mediana 184 HU, H6). Se aparta de la formulacion inicial (complemento de `B_delta`, que incluia `M`).

**Texto (DEC):** "La preservacion del protocolo fisico se reporta como caracterizacion de la referencia: RMSE y SSIM
de su simulacion sin metal frente a la TC original, fuera de `G`, mas su amplitud de solo ruido. Para el sintetizador
vale 0 por construccion y no se presenta como resultado."

### D9 — Pose sin perturbar

**Justificacion:** E-A2 aisla la apariencia; la pose fija y compartida quita la varianza de colocacion del contraste
pareado; la colocacion la evalua el Objetivo 2; y el protocolo fisico no era multiplicable por poses (sonda: 108.9 h
con `k` = 1, por eso se corrio con `k` = 2).

**Exploratorio opcional (solo difusor, sin referencia fisica):** 5 poses del muestreador por paciente de E-A2,
`run04_mejor`, 5 semillas. **Expectativa fisica fijada antes:** el artefacto depende del metal y del recorrido del
haz, no de que la cortical este perforada, asi que la amplitud deberia variar poco entre grados de brecha; una
variacion grande indicaria dependencia espuria del contexto. Medir tambien `metal integrity`. Si no hay tiempo, queda
la justificacion y se declara.

**Texto (DEC):** "E-A2 usa la pose del eje del corredor para aislar la apariencia de la colocacion y por el coste del
protocolo fisico. Exploratorio opcional con 5 poses del muestreador, solo sintetizador, con expectativa fijada antes."

### D10 — QC visual y comparacion a ciegas

**Recomendacion:**
- **QC (E-A4):** 13 pacientes x semilla 0 x 3 cortes (mayor area de `M`; 1/4 y 3/4 del tramo evaluado), lista cerrada
  de defectos (costura visible, metal fragmentado, artefacto fuera de lugar, anatomia alterada). **Declarar** que para
  run04 la autora ya vio salidas de prueba (#176): el QC de v1 no es ciego.
- **D3 a ciegas (`v2_plan.md`:127), protocolo propio antes de mirar v2:** mismos cortes, tres modelos, etiquetas
  ocultas y orden aleatorio por un tercero (o por script con semilla guardada), pregunta fija (ordenar por realismo del
  artefacto frente a una referencia real), registro antes de destapar. Descriptiva.

**Texto (DEC):** "QC visual: 13 x semilla 0 x 3 cortes por regla, lista cerrada de defectos; control, no evaluacion; no
ciego para run04. Comparacion D3 a ciegas de los tres modelos con protocolo fijado antes de ver las salidas de v2."

### D11 — Repositorio del reto AAPM

Se cita: Peters et al. como fuente del **protocolo**, el repositorio en version fija como fuente de la
**implementacion** (igual que `xcist2026main`/`xcist2025example`), y una tabla con las cinco desviaciones (tejido bajo
el metal a 0, Fe por acero, FOV 459 mm, ruido independiente, cociente de realce acotado).

**Texto (DEC):** "El protocolo fisico se atribuye a Peters et al. (protocolo) y al repositorio del reto AAPM en version
fija (implementacion), con tabla de desviaciones."

### D12 — Tamano de efecto del Wilcoxon y el comparador

**Recomendacion:**
1. **No reportar Hodges-Lehmann ni la biserial**: frente a un brazo que vale 0, son la pseudomediana del difusor y 1.0
   por construccion. Basta declarar la degeneracion (H4) y dar la amplitud del difusor como descriptivo.
2. **Comparador nuevo, posterior y descriptivo: artefacto parametrico.** Insertar en `G` el tornillo a HU constante mas
   un artefacto analitico barato (perfil radial medio del artefacto real de tornillos, `d1_d2_resultado.md`, o la
   plantilla `T` de B, #181), sin difusion. Responde la pregunta que un tribunal hace: **¿la difusion aporta algo
   sobre un modelo analitico de una linea?** Se descarta la copia y pegado de `G` de un donante: mete en `Delta` el
   desajuste anatomico, que no es artefacto.

**Texto (DEC):** "La cordura declara su degeneracion (copia y pegado = 0 por construccion; p = 2^-13 minimo alcanzable)
y no reporta tamano de efecto. Se agrega, posterior y descriptivo, un comparador de artefacto parametrico (perfil
radial real o plantilla T) sin difusion."

### D13 — Contingencia #90

Retirar las dos marcas: #90 CERRADA por ejecucion (2026-10-14). La introduccion dice que el Objetivo 3 tiene resultado
(#177) y el `\GAPDATO` "modelo final no elegido" se actualiza (run04 elegido; v2 exploratoria).

### D14 — Supuesto del IC con *t*

**Recomendacion:**
1. Enunciar el supuesto: diferencias pareadas aproximadamente normales e independientes entre pacientes.
2. Sensibilidad: **IC90 exacto por inversion de la prueba de permutacion pareada** (cambios de signo, 2^13 = 8192
   combinaciones, sin semilla). No bootstrap: con n = 13 cubre de menos y su IC es mas estrecho, lo que favorece la
   equivalencia.
3. **Regla asimetrica:** una sensibilidad solo puede **bajar** la categoria del desenlace (D15), nunca subirla a
   equivalencia.
- Descriptivo v1 (ya visto): Shapiro-Wilk W = 0.971, p = 0.906 (poca potencia con n = 13).

**Texto (DEC):** "El IC90 con *t* supone diferencias pareadas aproximadamente normales. Sensibilidad: IC90 exacto por
permutacion pareada. Ninguna sensibilidad puede elevar la categoria del desenlace; solo bajarla."

### D15 — Desenlaces del TOST

| desenlace | IC90 de la diferencia (difusor - Peters) |
|---|---|
| **equivalencia** | entero dentro de [-`Delta`, +`Delta`] |
| **no equivalencia** (en contra) | entero fuera: superior < -`Delta` o inferior > +`Delta` |
| **no concluyente** | cruza -`Delta` o +`Delta` |

Siempre: si el IC90 excluye 0, se reporta la **direccion**. Se declara la **multiplicidad** (3 modelos, 2 margenes,
sensibilidades) sin correccion, porque solo run04 con su `Delta` es confirmatorio; el resto es descriptivo. La
incertidumbre de `Delta` (n = 2) no la recoge el IC y se declara aparte.

**Consecuencia para v1 (posterior):** `run04_mejor` IC90 [-477.0, -124.9], `Delta` 196.3 -> **no concluyente respecto
de la equivalencia, con diferencia significativa a la baja**. El texto no debe heredar de #164 "entero bajo -`Delta`"
(eso era la corrida con fuga). `run04_60k`: [-566.5, -201.4] -> no equivalencia con su `Delta` (115.8) y con 196.3
(por 5.1 HU).

**Texto (DEC):** "Desenlaces del TOST: equivalencia (IC90 dentro de +-Delta), no equivalencia (IC90 entero fuera), no
concluyente (cruza un limite); direccion siempre que el IC90 excluya 0. Confirmatorio: solo run04_mejor con su Delta;
lo demas descriptivo, multiplicidad declarada. Previo al TOST de prueba de v2; posterior para v1."

### D16 — Margen no fijado por el sintetizador

**Se descarta el margen 0.80-1.25** del borrador: elegido despues de ver la razon 0.831, equivale en HU a -319/+399
(1.6 veces mas laxo que `Delta`, justo del lado del difusor), y viene de la farmacocinetica, no de la fisica del HU.

**Recomendacion:**
1. **Margen minimo de equivalencia:** el menor `Delta` con el que se concluiria equivalencia = max(|limite inferior|,
   |limite superior|) del IC90. Para v1: **477.0 HU, aprox. 30 % de la media de Peters Ti**. No elige margen y es
   inmune al post hoc: el lector juzga si 477 HU es "comparable".
2. **Margen comun para comparar los tres modelos:** el `Delta` de run04 (196.3), ademas del propio de cada uno; asi
   los desenlaces de v2 son comparables con v1.
3. Opcional, solo si se fija **y calcula antes de relanzar `a20_v2`**: un margen externo anclado en la dispersion del
   artefacto real de tornillos entre pacientes (`d1_d2`). Si no se puede fijar antes, no se usa.
4. Declarar el sentido conjunto de las tres elecciones sobre los mismos receptores (#162 (3)).

**Texto (DEC):** "Se reporta el margen minimo de equivalencia (mayor |limite| del IC90) para cada modelo y el TOST de
los tres modelos con el margen comun de run04 (196.3 HU), ademas del propio. Se declara el sentido conjunto de las
tres elecciones (#162 (3))."

## 4. Decisiones nuevas (no son `\GAPDEC`)

**D-extra 1. Simetria de cortes (H6).** Sensibilidad del primario con `a20 --interseccion` (los dos brazos en los
mismos cortes). CPU. Sujeta a la regla asimetrica de D14.

**D-extra 2. Piso de ruido de cada brazo (H6).** Amplitud nula: Peters `limpia_A - limpia_B` (ya existe, 184 HU) y el
difusor **generando `G` sin `M`** sobre el mismo receptor (GPU, 13 x 5). Se reporta la amplitud de cada brazo junto a
su piso. Sin esto no se sabe que parte de los ~1300 HU del difusor y de los ~1600 de Peters es artefacto.

**D-extra 3. Margen comun y `--delta` de decodificacion en v2.** Los tres modelos se decodifican con `--delta`
distinto (0.03/0.05/0.2, #184): la comparacion mezcla modelo y lectura. Reportar ademas E-A1 de v2 con `--delta`
0.03 (el de run04), o declararlo como confusor no resuelto.

**D-extra 4. Inventario fechado de lo visto** (`experiments/objetivo3/visto.md`): que resultados vio la autora y
cuando, antes de cada decision de v2. Sin el, ninguna regla "previa" es auditable.

## 5. Orden de ejecucion

1. **Autora:** registra D14, D15, D16, D1, D12, D-extra 1-4 y escribe el inventario (D-extra 4) **antes de relanzar
   `a20_v2`**. D3, D6, D11, D13 cuando quiera (no dependen de nada).
2. **Local, CPU (Claude):** D1 (suelo de Peters, TOST con suelo simetrico), D2 (sin ROIs cerca de la cabeza), D5,
   D8, D-extra 1, H3 (acuerdo), D4, y el script de realismo con regla de lectura (H5).
3. **Khipu:** `a20_v2` ajustado a las nuevas lecturas; D-extra 2 (difusor sin `M`); D7; D9 si se aprueba.
4. **Redaccion:** ronda de cap. 3 / introduccion con todo lo anterior.
