# Tornillos candidatos IS/TS en los 65 pacientes con material ortopedico (2026-10-08)

**Propuesta sin validar.** Revision visual por 4 agentes `clasificador-metal` sobre laminas a 2500 HU
(`outputs/laminas/`) y QC del censo `e8` (`experiments/objetivo2/outputs/e8_qc/`). Detalle por caso en
`propuesta_lote-tornillos-{A,B,C,D}.csv`; los 3 pacientes de referencia, ademas, en
`propuesta_lote-tipo-ref.csv`. Morfologia, no modelo ni material. Las longitudes "a ojo" salen del MIP
y son aproximadas. Pedido de la autora tras #154.

Categorias: (a) tornillo intraoseo aislado; (b) placa con tornillos; (c) fijador externo;
(d) protesis/masivo; (e) otro. Candidato **IS** = tornillo aislado de ilion a cuerpo sacro;
**TS** = cruza al ilion contralateral.

## Pacientes con al menos un tornillo aislado candidato IS/TS: 26 de 65 (censo `e8`: 17)

| Particion | Pacientes | Casos |
|---|---|---|
| val | 1 | `0039` (IS: comp e8 1, L 76.9 mm, d 4.93 mm; su otro tornillo aislado, comp e8 2, va de pubis a acetabulo) |
| test | 5 | `0009`, `0024` (2), `0048` (2), `0049`, `0066` (TS dudoso: falta ver si va dentro del hueso) |
| train | 20 | `0000`, `0001`, `0002`, `0004`, `0008` (2), `0012`, `0018`, `0027`, `0028`, `0033`, `0040` (TS), `0042` (2), `0045`, `0047` (2), `0050` (2), `0051`, `0055` (dudoso: puede estar unido a placa), `0058` (2), `0062` (2), `0070` |

- **TS:** solo `0040` (train, claro) y `0066` (test, dudoso). El resto cruza la linea media 12-31 mm
  sin llegar a la sacroiliaca contralateral.
- **Sin tornillo aislado candidato en val:** `0011` (fijador externo) y `0056` (tres placas con tornillos).

## Donde falla el censo automatico `e8`

- **No detecta** 9 pacientes: `0000`, `0009`, `0012`, `0027`, `0055`, `0058`, `0062`, `0066`, `0070`.
  El vastago queda bajo 2500 HU o sale partido en fragmentos cortos que no pasan `L >= 30 mm`.
- **Detecta en parte:** `0004` (solo la punta), `0024` y `0042` (uno de dos tornillos).
- **Subestima L** en tornillos fragmentados: `0028` (45 frente a ~90-100 mm), `0040` (33 frente a ~145 mm),
  `0047` (36 frente a ~126 mm).
- Consecuencia: "17 de 65" es un minimo, y las medianas de L y d de `e8` sobre alargados estan sesgadas
  hacia tornillos densos y enteros.

## Posibles pacientes repetidos sin registrar (alertas)

- `0053` (test) y `0054` (train): placa del anillo anterior casi identica, grupos de paciente distintos.
  **Si fueran el mismo paciente, hay fuga train/test.**
- Solo train (sin fuga): `0025`/`0026`, `0027`/`0028`, `0037`/`0038`, `0019`/`0020` (menos claro).

## Orden sugerido de revision por la autora (`explorar.py cortes`)

`0039` -> `0053`/`0054` -> `0040`, `0066`, `0055` -> resto de casos que el censo no detecto.
