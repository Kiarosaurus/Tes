# Conteo descriptivo de tornillos en los pacientes reales (2026-10-08)

Para el texto de la tesis (contexto para los evaluadores). **No lo pide ningun objetivo** y no cambia
ningun resultado. Archivo a llenar: `tornillos_conteo.csv`.

## Procedencia

- **Pedido:** la autora, 2026-10-08. Quiere reportar cuantos pacientes reales tienen tornillos (IS en
  particular) y clasificarlos, con una columna por evaluador.
- **Preguntas y categorias:** las redacto Claude a partir de:
  - la taxonomia (a)-(e) de `tornillos_candidatos.md`;
  - las definiciones de IS y TS de esa misma ronda (pedido de la autora tras #154).
  La autora no las ha validado como definicion final. Si cambian, se anota aqui con fecha.
- **Columna `agente`:** transcrita a mano por Claude desde `propuesta_lote-tornillos-{A,B,C,D}.csv`.
  Esos archivos son la revision de 4 agentes `clasificador-metal` sobre laminas a 2500 HU. La columna
  `fuente_agente` indica el lote. Si hay duda, manda el lote, no este CSV.
- **Generado con** un script temporal, no versionado. Si hay que regenerarlo, se rehace desde los lotes.

## Formato

Una fila por paciente y pregunta: 65 casos x 5 preguntas. Tres columnas de respuesta:

| Columna | Quien | Estado |
|---|---|---|
| `agente` | 4 agentes `clasificador-metal` sobre laminas a 2500 HU | lleno, propuesta sin validar |
| `autora` | Kiara, en cortes (`explorar.py cortes`) | vacio |
| `evaluador_externo` | traumatologo o radiologo, si colabora | vacio |

Cada columna de respuesta tiene su columna `nota_*`. Si una de tus respuestas no coincide con la del
agente, explica por que en tu nota. El agente vio 16 cortes y proyecciones, no todo el CT.

`nota_autora` ya trae tu revision anterior (`tornillos_revision_autora.csv`) en 0039, 0040, 0053, 0054,
0055 y 0066, solo como recordatorio. La columna `autora` sigue vacia.

`cuenta = no` solo en `0053`: es la misma persona que `0054` (#156). Se lista, pero no suma.
Quedan 64 pacientes.

## Preguntas

1. **`1_tornillo`**: hay al menos un tornillo intraoseo, aislado o unido a placa o barra. Los clavos de
   fijador externo NO cuentan.
2. **`2_n_IS`**: numero de tornillos iliosacros aislados. Van del ilion al cuerpo del sacro sin llegar
   al ilion contralateral.
3. **`3_n_TS`**: numero de tornillos o barras transiliacos-transsacros aislados. Van de ilion a ilion
   a traves del sacro.
4. **`4_n_otros_aislados`**: numero de tornillos aislados que no son IS ni TS (por ejemplo, de pubis a
   acetabulo o supraacetabulares).
5. **`5_clases`**: categorias presentes, separadas por `;`:
   - (a) tornillo intraoseo aislado
   - (b) placa con tornillos
   - (c) fijador externo
   - (d) protesis o masivo
   - (e) otro

"Aislado" significa que el tornillo no esta unido a una placa ni a una barra. Las categorias describen
morfologia, no un diagnostico.

## Como llenar (autora o evaluador externo)

1. Abre el CSV en Excel y filtra la columna `pregunta` para responder una pregunta a la vez. Si solo
   quieres IS, empieza por `2_n_IS`.
2. Revisa cada caso en cortes: `python experiments/exploration-3d/explorar.py cortes <Caso>`. Las
   laminas sirven de apoyo, no bastan.
3. Escribe en tu columna solo los valores de `valores`:
   - `si` / `no` / `incierto`;
   - un entero;
   - letras a-e separadas por `;`, sin espacios.
4. Responde sin mirar la columna `agente`, o al menos sin copiarla. Si tu respuesta no coincide con
   la del agente, explica por que en tu `nota_*`.
5. Usa `incierto` cuando no lo puedas decidir. No adivines.
6. Anota la fecha de tu revision en `nota_*` de la pregunta `1_tornillo` de cada caso, por ejemplo
   `2026-10-15: ...`.
7. No cambies `Caso`, `pregunta`, `valores`, `agente` ni `fuente_agente`.
8. El evaluador externo llena solo `evaluador_externo` y `nota_externo`. Anota tambien su
   especialidad y la fecha en la seccion de abajo.

## Registro de evaluadores

| Evaluador | Especialidad | Fecha | Casos revisados |
|---|---|---|---|
| agente (`clasificador-metal` x4) | no clinico | 2026-10-08 | 65 |
| autora | no clinica | | |
| externo | | | |

## Lo que dice el agente (64 pacientes, sin validar)

| Indicador | Pacientes |
|---|---|
| Con algun tornillo intraoseo | 54, mas 1 incierto (`0035`) |
| Con al menos un IS seguro | 22, mas 2 inciertos (`0009`, `0055`) |
| Con TS | 1 (`0040`), mas 1 incierto (`0066`) |
| Con IS o TS | entre 23 y 26 |
| Tornillos IS contados en los 22 seguros | 30 |

Tus revisiones previas ya resuelven en parte tres inciertos:

- `0055`: 3 transversos sueltos.
- `0040` y `0066`: barra de ilion a ilion.

La columna `autora` las registra formalmente.

En la tesis convendria reportar por separado lo que dice el agente, lo que dices tu y, si existe, el
acuerdo con el evaluador externo. Si no hay evaluador externo, el conteo es de una sola observadora no
clinica, y hay que declararlo.
