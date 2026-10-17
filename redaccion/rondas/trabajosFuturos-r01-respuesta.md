# Respuesta — trabajosFuturos — r01

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 | guia | APLICADO | "Formulacion residual" solo aparece en `docs/04-implicancias.md` #193 opcion (c) como rotulo, sin entrada, referencia ni residuo predicho; ningun otro archivo de `docs/` la define. Se retiro la variante; quedan banda mas ancha y refinamiento sobre simulacion fisica, introducidas con "por ejemplo" para no presentar la lista de #193 como cerrada, y "sus tres variantes" pasa a "sus variantes". Sin GAP. |
| T01 | trazabilidad | APLICADO | Eliminada la oracion "Su expectativa, fijada sin umbral numerico, era que la amplitud variara poco entre grados" (l. 35, PAT-178). |
| ES-02 | estilo | APLICADO | Retirada "y las dos condiciones admiten una extension directa". |
| ES-03 | estilo | APLICADO | Oracion partida: "La fractura ... impide atribuir el estrechamiento solo a la anatomia sacra"; "Establecerla" pasa a "Establecer esa causa". |
| ES-04 | estilo | APLICADO | "Medir la posicion del voxel mas craneal y extender la revision en cortes ... permitiria comprobar ambos supuestos". |
| ES-06 | estilo | APLICADO | Parrafo de l. 29 partido (PAT-58): el nuevo parrafo abre con "Las mediciones del Objetivo~3 cuantifican lo que una version nueva tendria que corregir." |
| ES-07 | estilo | APLICADO | "permitiria evaluar juntos los dos componentes". |
| ES-08 | estilo | APLICADO | Misma correccion que T01. |

Bajas aplicadas: ES-01 (referente explicito "la codificacion multiventana"), ES-05 ("sus resultados describirian el realismo visual").

Lint: PASA (0 alta, 0 media, 0 baja; 0 GAP). Sin cifras tocadas.

## Decisiones de redaccion

- Una opcion de diseno registrada en una implicancia solo como rotulo ("formulacion residual") no se nombra en la tesis si el repositorio no fija su entrada, referencia y salida; se retira en vez de definirla por cuenta propia.
