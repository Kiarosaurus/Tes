# wagner2017 — Critical Dimensions of Trans-sacral Corridors Assessed by 3D CT Models

- **DOI / URL:** 10.1002/jor.23554
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** papers/wagner2017.pdf

## Que hace (3 lineas maximo)
Reconstruye modelos 3D de sacro e ilion desde CT de 156 pelvis (92 europeas, 64
japonesas) para medir los diametros criticos de los corredores trans-sacros S1, S2 y
S3, clasificar cuantos individuos permiten la colocacion de un implante trans-sacro y
construir un modelo estadistico 3D (PCA) de la forma del corredor S1.

## Restriccion o supuesto clave
No es un paper de sintesis generativa; es geometria anatomica descriptiva. La
restriccion clave para esta tesis es que TODAS las pelvis fueron excluidas si tenian
fractura: *"Excluded from the study were CT scans with evidence of bony pathology
(13) or fractures (6)"* (Materials and methods — Image data and processing). El modelo
estadistico PCA se corrio solo sobre las 92 pelvis europeas, tambien sin fractura. El
propio paper reconoce la limitacion en la Discusion: *"displaced fractures of the
sacrum may limit the safe corridors substantially"* (Discussion — Limitations),
citando otra fuente (ref. 44), sin cuantificar cuanto.

## Que toco de aqui
- [x] numero que cito (umbrales 12/8 mm, diametros S1/S2/S3, % criticos por nivel)
- [ ] metodo que reimplemento
- [ ] baseline de comparacion
- [x] solo contexto (poblacion anatomicamente intacta, no fractura+implante)

## Numeros que cito de este paper
Ver tabla completa en "Evidencia textual". Resumen de los 7 puntos solicitados:

1. **Diametros S1/S2 (mm):** S1cc media 11.6 mm (DE 5.4); S2cc media 14 mm (DE 2.4).
   Direccion: cc = cranio-caudal, ap = antero-posterior; el cc siempre fue menor que
   el ap en S1, por lo que es el que limita la colocacion.
2. **Umbrales "critico"/"imposible":** >12 mm = no-critico, <12 mm = critico
   (subdividido en 8-12 mm "narrow" y <8 mm "imposible"). Los umbrales se ELIGEN, no
   se miden: se derivan del diametro de los implantes quirurgicos usados (6.0-7.3 mm)
   y el de >12 mm se atribuye a una referencia externa (ref. 29, Carlson et al. 2000,
   "vestibule concept").
3. **% criticos/imposibles:** S1 critico 52%, S1 imposible 26%; S2 critico 21%, S2
   imposible 0%.
4. **Forma del corredor:** ovalada de forma consistente (S1); modelo estadistico
   construido con parametrizacion cilindrica + Thin Plate Spline + PCA sobre 92
   superficies homologas (solo europeos; japoneses excluidos por corredores
   demasiado pequenos para computar homologia). El metodo se remite a un trabajo
   previo de los mismos autores ("as previously described[16]"), no es enteramente
   autocontenido en este PDF.
5. **Limites oseos:** antero-superior de S1 limitado por el ala sacra (zona 1,
   medial), el limite craneal de la articulacion sacroiliaca (zona 2, intermedia) o
   la fosa iliaca (zona 3, lateral). La fosa iliaca limito el corredor en 40% del
   total.
6. **Punto de entrada / angulos / margen al foramen:** NO ENCONTRADO EN EL PDF (solo
   se menciona cualitativamente que el corredor esta "consistently inclined in the
   sagittal view", sin grados).
7. **Poblacion:** n=156 (92 europeos: 48F/44M; 64 japoneses: 29F/35M), edad media
   66.7 anos (DE 13.7, rango 26-91). Europeos: serie clinica retrospectiva por
   motivos distintos a fractura pelvica. Japoneses: TC POST MORTEM. Se excluyeron
   explicitamente casos con fractura (6) y con patologia osea (13): **la poblacion
   es de pelvis anatomicamente intactas, no fracturadas ni con implante**.

## Donde entra en mi tesis
Candidato a informar restricciones geometricas del corredor S1/S2 en el muestreador,
pero medido sobre pelvis INTACTAS (sin fractura, sin implante). No es transferible
directamente al escenario de la tesis (CT con fractura e implante) sin ajuste
explicito; el propio paper marca esa brecha como limitacion sin cuantificarla.

## Dudas para el asesor
- Como ajustar los umbrales de 12/8 mm (medidos en pelvis sanas, no fracturadas) para
  el caso de fractura + implante que trabaja la tesis.
- Si conviene usar el modelo estadistico PCA (solo 92 europeos) o los percentiles
  descriptivos combinados (europeos + japoneses, n=156) como referencia geometrica.
- El origen real del umbral de >12 mm "no-critico" queda en Carlson et al. 2000 (ref.
  29, "vestibule concept"), no medido por Wagner: seguir la cadena si se necesita el
  origen primario.

## Evidencia textual

| Cifra / dato | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Poblacion total n=156 | "3D models were reconstructed from pelvic CT scans from 92 Europeans and 64 Japanese" | Abstract |
| Europeos n=92 (48F, 44M) | "92 Europeans (EU; 48 females, 44 males)" | Materials and methods — Image data and processing |
| Japoneses n=64 (29F, 35M) | "64 Japanese (JP; 29 females, 35 males)" | Materials and methods — Image data and processing |
| Edad media 66.7 (+/-13.7, rango 26-91) | "mean age of 66.7 years (+/- 13.7, 26 – 91 years)" | Materials and methods — Image data and processing |
| Exclusion por fractura (n=6) y patologia (n=13) | "Excluded from the study were CT scans with evidence of bony pathology (13) or fractures (6)" | Materials and methods — Image data and processing |
| Europeos: CT clinicas por motivos distintos a fractura pelvica | "consecutive retrospective series of scans obtained for clinical reasons other than pelvic fractures" | Materials and methods — Image data and processing |
| Japoneses: escaneos post-mortem | "The Japanese CT scans were obtained from post-mortem scans using the GE LightSpeed VCT CT scanner" | Materials and methods — Image data and processing |
| Voxel medio europeos 0.75x0.75x1.02 mm | "The mean voxel size was 0.75 x 0.75 x 1.02 mm" | Materials and methods — Image data and processing |
| Voxel medio japoneses 0.68x0.68x1.11 mm | "The mean voxel size was 0.68 x 0.68 x 1.11 mm" | Materials and methods — Image data and processing |
| Diametro de implantes quirurgicos 6.0-7.3 mm | "surgical implants used to treat sacral fractures usually have a diameter of 6.0 – 7.3 mm" | Materials and methods — Study of trans-sacral corridors |
| Umbral "no-critico" >12 mm (atribuido a ref. 29) | "an anatomical corridor with a maximal diameter of >12 mm was classified as 'non-critical' ... allowing trans-sacral implant positioning with some safety space[29]" | Materials and methods — Study of trans-sacral corridors |
| Umbral "critico" <12 mm, subdividido "imposible" <8 mm y "narrow" 8-12 mm | "'Critical' corridors (<12mm) were further divided into 'impossible' (<8 mm) and 'narrow' (8 - 12mm)" | Materials and methods — Study of trans-sacral corridors |
| Zonas del limite antero-superior S1 (1: medial, 2: intermedia, 3: lateral) | "the medial two thirds of the sacral ala (zone 1...), the lateral third of sacral ala or cranial limitation of the SIJ (zone 2...), and the iliac fossa (zone 3...)" | Materials and methods — Study of trans-sacral corridors |
| S1cc media 11.6 mm (DE 5.4) | "limiting cranio-caudal diameter was 11.6 mm (+/- 5.4) for S1" | Abstract |
| S2cc media 14 mm (DE 2.4) | "14 mm (+/- 2.4) for S2" | Abstract |
| S1 critico en 52% de casos | "Trans-sacral implant positioning was critical in 52% of cases for S1" | Abstract |
| S2 critico en 21% de casos | "and in 21% for S2" | Abstract |
| S1 imposible en 26%, S2 sin corredor imposible | "The S1 corridor was impossible in 26%, with no impossible corridor in S2" | Abstract |
| Fosa iliaca limita S1 en 40% | "the S1 corridor was limited not only by the sacrum but in 40% by the iliac fossa" | Abstract |
| Forma consistentemente ovalada de S1 | "The statistical model demonstrated a consistent oval shape of the trans-section of corridor S1" | Abstract |
| S1cc total: media 11.6, DE 5.4, min 0, max 21.8 (n=156) | Tabla de valores (Total, S1cc) | Table 1 — Trans-sacral corridor dimensions |
| S1ap total: media 23.2, DE 5.7, min 0, max 30.8 (n=156) | Tabla de valores (Total, S1ap) | Table 1 |
| S2cc total: media 14.0, DE 2.4, min 8.1, max 19.2 (n=156) | Tabla de valores (Total, S2cc) | Table 1 |
| S2ap total: media 17.6, DE 2.3, min 11.6, max 23.9 (n=156) | Tabla de valores (Total, S2ap) | Table 1 |
| S3cc total: media 8.6, DE 2.1, min 5.3, max 14.4 (n=36) | Tabla de valores (Total, S3cc) | Table 1 |
| S3ap total: media 12.2, DE 2.0, min 8.0, max 17.8 (n=36) | Tabla de valores (Total, S3ap) | Table 1 |
| Europeos S1cc > Japoneses S1cc (12.5 vs 10.3), p=0.01 | Tabla comparativa por etnia, S1cc, p 0.01* | Table 1 |
| S1cc siempre menor que S1ap (limita la colocacion) | "The cranio-caudal diameter in S1 (S1cc) was always smaller than the antero-posterior one (S1ap)" | Results — Dimensions of the S1 and S2 trans-sacral corridors |
| S1cc mas variable que S2cc (DE 5.4 vs 2.4) | "cranio-caudal corridor dimension at level S1 (S1cc) was more variable than at level S2 (S2cc), with a standard deviation +/-5.4 mm vs. +/-2.4 mm" | Results — Dimensions of the S1 and S2 trans-sacral corridors |
| Correlacion S1cc-S1ap fuerte | "S1cc correlated strongly with S1ap (R 0.749, p <0.001)" | Results — Dimensions of the S1 and S2 trans-sacral corridors |
| Correlacion inversa S1cc-S2cc | "S1cc exhibited an inverse correlation to S2cc (R -0.430, p <0.001)" | Results — Dimensions of the S1 and S2 trans-sacral corridors |
| No-critico S1 48%, no-critico S2 79% | "Half of the studied pelves (48%) exhibited non-critical anatomical conditions for trans-sacral implant positioning at level S1, whereas 79% were non-critical at S2" | Results — Dimensions for trans-sacral implant positioning in S1 and S2 |
| S1cc no-critico 75(48%), narrow 41(26%), imposible 40(26%) | Tabla de conteos (Total n=156) | Table 2 — Corridor dimensions for trans-sacral implant positioning |
| S2cc no-critico 123(79%), narrow 33(21%) | Tabla de conteos (Total n=156) | Table 2 |
| Solo 4 pelvis (2.5%) donde S2cc no fue la dimension limitante | "With the exception of four pelves (2.5%), the same was valid for S2" | Results — Dimensions of the S1 and S2 trans-sacral corridors |
| Fiabilidad intra-observador (repeticion no significativa) | "The repeated measurements did not differ significantly (S1cc p 0.31, S1ap p 0.08, S2cc p 0.06, S2ap p 0.58)" | Results — Dimensions of the S1 and S2 trans-sacral corridors |
| Zona 3 (fosa iliaca) en 40% total, distinto por etnia | "Around 40% each were limited in zones 1 and 3; however, there were significant differences between Europeans and Japanese" | Results — Antero-superior border of the S1 trans-sacral corridor |
| Zona 1: 41%, Zona 2: 19%, Zona 3: 40% (n=156) | Tabla de conteos (Total) | Table 3 — Antero-superior border of trans-sacral corridor S1 |
| Zona 3 en 62% de corredores criticos de S1 (50/81) | "in 62% of the pelves with critical corridors of S1 (50 of 81 cases)" | Results — Antero-superior border of the S1 trans-sacral corridor |
| Zona 3 en 73% de corredores imposibles de S1 (29/40) | "in 73% of the pelves with an impossible corridor of S1 (29 of 40 cases)" | Results — Antero-superior border of the S1 trans-sacral corridor |
| Zona 3 en 16% de corredores no-criticos de S1 (12/75) | "and in 16% of pelves with non-critical S1 trans-sacral corridors (12 of 75 cases)" | Results — Antero-superior border of the S1 trans-sacral corridor |
| Estadistico: PCA sobre superficies homologas (parametrizacion cilindrica + TPS) | "Using cylindrical parameterisation and a Thin Plate Spline Transformation, homologous surfaces ... were computed and a statistical model with size and shape analysis was calculated using principal component analysis (PCA)" | Materials and methods — Statistical modelling of the S1 trans-sacral corridor |
| Japoneses excluidos del modelo estadistico | "Japanese data was excluded as some of these corridors were too small to create a homologous triangulated surface" | Materials and methods — Statistical modelling of the S1 trans-sacral corridor |
| 1a componente principal = longitud del corredor | "The largest 3D statistical variability of the S1 trans-sacral corridor was the length as shown by 1st PC" | Results — Statistical model of the S1 trans-sacral corridor in 92 Europeans |
| 2a componente principal = forma/tamano transversal, ovalada | "The large variability in cross-sectional size and shape was demonstrated by the 2nd PC with a relatively consistent oval shape" | Results — Statistical model of the S1 trans-sacral corridor in 92 Europeans |
| Corredor S3 anatomicamente disponible en 37% (57 indiv.) | "This was observed in 57 individuals (37%; 21 EU and 36 JP)" | Results — S3 trans-sacral corridors |
| Corredor S3 quirurgicamente usable en 23% (36 pelvis) | "leaving 36 pelves (23%; 11 EU and 27 JP) with a surgically usable corridor at the S3 level" | Results — S3 trans-sacral corridors |
| S3cc media 8 mm (rango 3-10.5), S3ap media 11.9 mm (rango 4.5-17.2) | "S3cc average of 8 mm, range 3 – 10.5 mm; S3ap average of 11.9 mm, range 4.5 – 17.2 mm" | Results — S3 trans-sacral corridors |
| 89% de esos S3 usables en pelvis con S1 critico | "Thirty-two of these (89%) were in individuals with critical S1 corridors" | Results — S3 trans-sacral corridors |
| 55% de esos S3 usables en pelvis con S1 imposible | "and 20 (55%) in individuals with impossible S1 corridors" | Results — S3 trans-sacral corridors |
| Diametro >=8mm en S3cc y S3ap en 15% (23 individuos) | "A diameter of >= 8mm in S3cc and S3ap was present in 23 individuals (15%; 8 EU, 15 JP)" | Results — S3 trans-sacral corridors |
| Significancia estadistica p<=0.05 | "Statistical significance was defined as p <= 0.05" | Materials and methods — Statistics |
| Corredores limitados: superficie anterior del sacro, canal sacro posterior, foramenes adyacentes | "They are limited by the anterior sacral surface, posteriorly by the sacral canal, superiorly and inferiorly by the adjacent sacral foramina" | Discussion |
| Corredor consistentemente inclinado en vista sagital (sin grados) | "the trans-sacral corridors were consistently inclined in the sagittal view" | Results — Statistical model of the S1 trans-sacral corridor in 92 Europeans |
| Limitacion: solo pelvis sin fractura, ligado a uso clinico de implantes en FFP no desplazadas | "We included only pelves without evidence of fractures, since in our institution, trans-sacral implants are mainly used to treat FFP which are often non-displaced" | Discussion — Limitations |
| Limitacion reconocida: fractura desplazada podria reducir el corredor seguro | "displaced fractures of the sacrum may limit the safe corridors substantially" | Discussion — Limitations |
| Un solo observador (DW) midio; sin fiabilidad interobservador | "The corridor's dimensions were measured only by one observer (DW), an interobserver reliability is therefore not provided" | Discussion — Limitations |
| Punto de entrada, angulos de trayectoria o margen al foramen (en grados o mm) | NO ENCONTRADO EN EL PDF | — |
