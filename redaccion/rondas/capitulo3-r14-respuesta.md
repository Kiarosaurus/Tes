# capitulo3 — r14: respuesta del redactor (encargo acotado `ENCARGO_2026-10-11.md`, M1-M6)

Modo: corregir por encargo (sin reportes de revisores). Archivos editados: `overleaf/secciones/capitulo3.tex`,
`overleaf/secciones/trabajosFuturos.tex` (una linea, M6), `redaccion/MAPA.md`. No se tocaron `tesis/main.tex` ni
otros capitulos. No se escribio ninguna cifra de #164 ni de la corrida final con run04 (en curso).

## Puntos del encargo

| Punto | Decision | Detalle |
|---|---|---|
| M1 un solo modelo | APLICADO | Retiradas todas las menciones a `mejor_37k`, run01/run02, 37 500, 140 000, 144 500, 30 000 pasos, "los dos entrenamientos", el cotejo a 0.5 mm (8 frente a 7 de 46), el 11 frente a 5, 324/162 HU, "10 u 11 de 12", "150 a 200 HU", "~900 HU", "47 pacientes" y las amplitudes 815/1229 HU del sintetizador anterior. Frase de transparencia en §Sintetizador, parrafo nuevo del conjunto de entrenamiento: auditoria de duplicados -> dos volumenes de la misma persona (antes y despues de la cirugia) en entrenamiento y prueba -> se retira el de entrenamiento, se reentrena, se regeneran los resultados que dependen del modelo; ninguno de los resultados presentados proviene del modelo afectado. **Salvedad anadida:** el limite de 0.05 de la lectura de HU se calibro (`a16`) con un modelo anterior, archivado por #166, y no se recalibro; la frase lo dice y abre un `\GAPDEC` (ver abajo). §Vision general: el diseno se fijo el 9 y se enmendo el 11 de octubre; la corrida final es "la unica que procesa la particion de prueba con el modelo evaluado". §Resumen del diseno: "entrenado antes de la enmienda que lo incorpora" (antes "entrenado antes", falso para run04, que se entreno despues del 9). |
| M2 conjunto y entrenamiento | APLICADO | 14 182 parches de 39 casos; validacion 896 parches, 3 casos; retiros: secundarios de mismo paciente, el duplicado de #166, 3 componentes no ortopedicos (dos fragmentos de pulsera y un DIU). 60 000 pasos, hiperparametros fijados antes; minimo de validacion en el paso 16 500, despues sube mientras la de entrenamiento baja; "no se afirma que ningun numero de pasos sea optimo". Sin cifras de perdida (#168 ABIERTA). #167 en §Amenazas, validez de constructo: 19 de 39 casos con objeto no ortopedico, regla por caso, solo una muestra revisada por componente. Saturacion: "39 casos". |
| M3 punto de control | APLICADO + ESCALADO | Candidatos fijados antes de generar (16 500 y 60 000); 1 mm fijado antes de entrenar run04; gana 16 500 por 12 frente a 10 de 24; sin empate. Hallazgos: p95 bajo la envolvente en 8 y 10 de 12; dentro de `M` el elegido da p50/p95 3297/4641 HU frente a 3465/5283 reales, distancia 810 frente a 160 HU; la regla no usa el histograma salvo empate. Rango entre semillas 342 frente a 243 HU. Sensibilidad (opcion (b)) en §Sintetizador y §Analisis. **Escalado** el "destacar": el texto afirma como hecho lo de #171 (la sensibilidad con el final no acerca el sintetizador al protocolo fisico, porque genera rayas 228 y 162 HU mas debiles), y abre `\GAPDEC` sobre la frase de `00-tesis.md`/encargo ("la eleccion del principal no acerca"): en validacion el principal genera rayas mas intensas que el final y el protocolo fisico con Ti (2051/1279 HU) queda por encima o dentro del rango de semillas del principal (901-1057, 1188-1360 HU), asi que esa frase no se sostiene como esta. |
| M4 Delta y copia y pegado | APLICADO | Delta = 163.8 HU (s = 163.8, r = 23.2) en §Analisis (dos sitios) y Tabla de diseno; sensibilidad s = 100.3, Delta = 100.3 HU y segunda lectura con 163.8 HU, en parrafo propio. Copia y pegado 5371 HU, mediana de 1 781 741 voxeles de 14 182 parches de 39 casos. |
| M5 GPU | APLICADO | Una frase en §Sintetizador, junto a las 5 semillas: misma porcion de tarjeta grafica, la corrida final en esa porcion compartida, control sobre un paciente de validacion identico bit a bit. Sin numeros de job. Se evito la sigla GPU (no definida en el documento). |
| M6 amenazas y futuro | APLICADO | #171: una frase en validez interna (prueba evaluada una vez con el modelo afectado; reentrenamiento, punto de control y margen fijados sobre validacion y por reglas previas). #165: en validez externa, ningun tornillo transiliaco-transsacro en los 56 pacientes de CLINIC-metal contados por la autora; se sintetiza un tipo ausente del entrenamiento y de la referencia de realismo. Sin cifra de IS. `trabajosFuturos.tex`: una linea (varios volumenes de un mismo paciente dentro de una particion de entrenamiento), debajo del texto de plantilla, que se conserva. |

Ajustes colaterales minimos (romperian al lado si no se hacian): §Amenazas, validez interna, el ancho de cascara se
cambio "antes de entrenar el modelo evaluado"; la frase del criterio de 30 000 pasos se sustituye por "la eleccion
por cotejo se adopto tras resultados de validacion, antes de entrenar el modelo evaluado". §Material del brazo
fisico: se conservan las cifras de Peters (no usan el sintetizador) y las del sintetizador pasan a las de run04.

## Fuente de cada cifra nueva

| Cifra | Ubicacion | Fuente |
|---|---|---|
| 14 182 parches, 39 casos; 896 parches, 3 casos | §Sintetizador, conjunto | `EXPERIMENTOS.md` §1; DEC 2026-10-11 |
| 3 componentes (pulsera x2, DIU) | §Sintetizador, conjunto | DEC 2026-10-11; #167 |
| 60 000 pasos; minimo en 16 500 | §Sintetizador | `EXPERIMENTOS.md` §2; #168 (log job 55706) |
| 12 frente a 10 de 24; sin empate | §Sintetizador, cotejo | `a17_cotejo_resultado_run04.md`; DEC 2026-10-11 (3) pto 1 |
| 342 frente a 243 HU (rango max. entre semillas) | §Sintetizador, cotejo | `a17_cotejo_resultado_run04.md`, columna "rango entre semillas" (`a17_cotejo.py`: maximo) |
| 8 y 10 de 12 cascaras bajo la envolvente (p95) | §Sintetizador, hallazgos | `a17_cotejo_resultado_run04.md`, tabla bajo/dentro/sobre; #169 |
| 3297/4641 HU; 3465/5283 HU; 810 y 160 HU | §Sintetizador, hallazgos | #169 (DECIDIDA); `a17_cotejo_resultado_run04.md` |
| +228 y +162 HU (60k mas debil) | §Sintetizador, sensibilidad | `a20_resultados_run04.md` |
| 901-1057 y 1188-1360 HU (semillas del elegido) | §Brazos (material) y `\GAPDEC` | `a20_resultados_run04.md`, filas run04_mejor (min y max de la fila, sin calculo) |
| 5380/2205 HU Fe, 2051/1279 HU Ti | §Brazos (sin cambio) | Peters, `a20_resultados.md` filas de Peters (vigentes segun `EXPERIMENTOS.md` §4) |
| 5371 HU; 1 781 741 voxeles | §Brazos | DEC 2026-10-11 (3) pto 5; #169 |
| Delta 163.8 (s 163.8, r 23.2); 100.3 | §Analisis, Tabla de diseno | `a20_resultados_run04.md`; DEC 2026-10-11 (3) pto 3-4 |
| 19 de 39 casos | §Amenazas, constructo | #167 (ABIERTA; como limitacion, por el encargo) |
| 0 de 56 pacientes con TS | §Amenazas, externa | #165, conteo vigente en #167 (ABIERTA; como limitacion, por el encargo) |

## GAP

- Abiertos: `\GAPDATO` razon de parches de solo banda del conjunto de run04 (el 0.62 es del conjunto anterior);
  `\GAPDEC` recalibrar o declarar heredado el limite 0.05 (sustituye al `\GAPDATO` de su resultado citable);
  `\GAPDEC` recuentos de §Datos (167/64; 11 + 8) frente a `02-datos.md` 2026-10-11 (159 pacientes, grupo 1 = 59,
  test 20 + 13), descansan en #163 ABIERTA; `\GAPDEC` sentido de la eleccion del principal frente al brazo fisico.
- Cerrados: `\GAPDATO` de la calibracion de 0.05 (convertido en `\GAPDEC`).
- Valores actualizados en filas ya cerradas de MAPA: 5373 -> 5371; 188.7 -> 163.8; lote 16 ("el entrenamiento").
- Totales del lint: 2 `\GAPLIT`, 13 `\GAPDATO`, 19 `\GAPDEC` (antes 2/13/16). Ningun `\GAPLIT` nuevo:
  `_candidatos.md` no cambia.

## Conflictos entre fuentes para la autora (fuera del alcance M1-M6, sin editar el texto salvo la marca)

1. **§Datos y §Reconstruccion de implantes reales** siguen con 167 pacientes, grupo 1 = 64 y 19 pacientes de
   prueba con metal (11 ortopedicos + 8 no ortopedicos). `02-datos.md` (2026-10-11) da 159 pacientes, grupo 1 = 59 y
   test = 20 (dataset6) + 13 (CLINIC-metal); `00-tesis.md`:158-159 dice E-A1 sobre 13. Las cifras de E-A1 por grupo
   salen de #164 y no se citan. Marcado con un solo `\GAPDEC` en §Datos.
2. **Frase "la eleccion del principal no acerca el sintetizador al brazo fisico"** (`00-tesis.md`:148-149 y M3):
   el dato de #171 la sostiene solo para la sensibilidad. `\GAPDEC` en §Sintetizador.
3. **Limite 0.05**: calibrado con un modelo archivado (#166, lista de archivados incluye `a16`); `00-tesis.md`:154
   lo mantiene sin recalibrar. `\GAPDEC` en §Sintetizador.
4. **§Geometria** (no tocada): "17 pacientes en que el censo morfologico identifico un candidato a tornillo
   transiliaco-transsacro" convive ahora con la frase de #165 (ninguno en el conteo de la autora). No es
   contradiccion (candidato por forma frente a tipo revisado), pero un revisor puede pedir aclararlo.

## Lint

`python scripts/lint_redaccion.py capitulo3 --compilar`: **PASA**, alta 0, media 0, baja 13 (E-P1, cifras sin cita
en la linea, todas preexistentes o con fuente propia en esta tabla). Compila: `redaccion/.build/main.pdf`, 132 paginas.

## Decisiones de redaccion

- **Nombres de los dos candidatos de run04:** "el punto de control del paso 16 500" (o "el elegido") y "el estado
  final" (del paso 60 000). No se usan `run04_mejor`/`run04_60k` ni "mejor".
- **La fuga se nombra sin la palabra "fuga"** en el cap. 3: "el modelo afectado" / "el paciente compartido entre
  particiones", remitiendo a §Sintetizador, donde la frase de transparencia cuenta el hecho.
- **GPU sin sigla:** "porcion de una tarjeta grafica", porque "GPU" no esta definida en el documento.
- **Transparencia con salvedad:** si un parametro decidido se calibro con un modelo archivado, la frase "ninguna
  cifra proviene del modelo afectado" no se escribe absoluta; se dice cual se hereda y se marca.
