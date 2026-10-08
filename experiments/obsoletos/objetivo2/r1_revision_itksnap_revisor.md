# Revision del nivel de S1 en ITK-SNAP (segundo juicio del revisor clinico, #53)

Decision de la autora (2026-09-15): el revisor mira los **61 casos** que tienen punto de S1. La planilla es
`r1_revision_itksnap_revisor.csv` y se genero desde `r1_cortes_itksnap.csv`. Es **ciega**: no trae ningun juicio
anterior (ni el suyo, ni el del agente, ni el de TotalSegmentator). Su juicio va a esta planilla nueva y **no**
sobrescribe `r1_auditoria_s1_clinico.csv`.

## Que se le entrega al revisor

1. `r1_revision_itksnap_revisor.csv` y este documento.
2. Los 61 CT de la columna `Archivo` (`data/dataset7/...nii.gz`). Son volumenes de CTPelvic1K, dataset publico con
   licencia CC-BY-NC-SA 4.0: uso no comercial y solo para esta revision.
3. **No** se le entregan el mosaico, `r1_auditoria_s1_clinico.csv`, `r1_estados.csv` ni ninguna lamina con juicios.

## Que hacer en cada caso

1. Abrir el CT de `Archivo` en ITK-SNAP.
2. **Comprobar la convencion de indices** (no verificada por el asistente). Llevar el cursor a los cortes
   `corte_sagital`, `corte_coronal`, `corte_axial`, contados desde 0, y leer el HU del cursor.
   - Si coincide con `HU_voxel` (tolerancia de unos pocos HU; `HU_mediana_3x3x3` es la mediana del entorno), anotar
     `0` en `convencion_indices`.
   - Si no coincide, probar con las columnas `_1`, contadas desde 1; si esas coinciden, anotar `1`.
   - Anotar en `HU_cursor` el HU leido. Si ninguna convencion coincide, anotar `?` y no juzgar ese caso.
   - En general basta con hacerlo en el primer caso: la convencion es la misma para todos.
   - `mundo_RAS_mm` y `mundo_LPS_mm` son la misma posicion en milimetros, por si ITK-SNAP la muestra asi.
3. **Juzgar el nivel** con el volumen completo, contando vertebras desde la columna lumbar. Pregunta: el punto,
   ¿esta en el platillo superior del primer segmento sacro (S1)?

| `juicio_nivel` | Significado (mismas categorias que el juicio sobre el mosaico) |
|---|---|
| `ok` | el punto esta en el platillo superior de S1 |
| `+1` | el punto esta un nivel arriba (platillo de la ultima vertebra lumbar) |
| `otro` | el punto esta en otro sitio (otro nivel, lateral, ligamentos); detallar en `comentario` |
| `?` | no se puede decidir |

4. `vertebra_transicion`: `si` si hay una vertebra de transicion lumbosacra (sacralizacion o lumbarizacion) que haga
   ambiguo que segmento es S1; `no` si no la hay; `?` si no se puede decir. Si es `si`, explicar en `comentario` como
   se conto.
5. `comentario`: libre; en `otro` y en `?`, obligatorio.

## Despues

- El asistente compara esta planilla con el juicio sobre el mosaico y con TotalSegmentator **solo** cuando este
  completa, y reporta los acuerdos por categoria. No se edita a mano ninguna otra tabla.
- Si ITK-SNAP numera desde 1, se anota en `r1_cortes_itksnap.py` para las proximas tablas.
