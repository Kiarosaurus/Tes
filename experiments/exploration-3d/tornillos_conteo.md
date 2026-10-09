# Conteo descriptivo de tornillos en los pacientes reales (2026-10-08)

Para el texto de la tesis (contexto para los evaluadores). **No lo pide ningun objetivo** y no cambia
ningun resultado. Archivo a llenar: `tornillos_conteo.csv`.

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
