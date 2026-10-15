# xcist2025example — Scripts del protocolo AAPM CT-MAR

- **DOI / URL:** https://github.com/xcist/example/tree/4993e87360912277d6c6f2235b91031b85f363f1/AAPM_datachallenge/simulation_scripts
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** NO APLICA — fuente de software versionada en GitHub

## Que hace (3 lineas maximo)
Repositorio de ejemplos de XCIST que publica los scripts de simulación del desafío AAPM CT-MAR. La revisión usada
por la tesis queda fijada por el commit completo `4993e87360912277d6c6f2235b91031b85f363f1`.

## Restriccion o supuesto clave
La fuente respalda el código publicado, su revisión y su licencia. El fallo de serialización y el parche de una
línea son observaciones de la ejecución local de la tesis, no afirmaciones de XCIST.

## Que toco de aqui
- [x] metodo que reimplemento
- [ ] numero que cito
- [x] baseline de comparacion
- [ ] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Tres materiales | “phmetal_json['n_materials'] = 3” | `run.py`, línea 40 |
| Densidad de agua desplazada $-1.0$ | “density_scale'].append(-1.0)” | `run.py`, línea 78 |
| Densidad de metal $+1.0$ | “density_scale'].append(1.0)” | `run.py`, línea 79 |

## Donde entra en mi tesis
Capítulo 3, protocolo físico: identifica la revisión exacta del repositorio de ejemplos y el script publicado del
que se tomó la implementación; respalda además la licencia BSD 3-Clause.

## Dudas para el asesor
- Ninguna sobre la identificación de la revisión; el parche local debe seguir declarado como modificación propia.

## Evidencia textual

| Tipo | Dato | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|---|
| Revisión | `4993e87360912277d6c6f2235b91031b85f363f1` | “Commit 4993e87” | Página del commit, GitHub |
| Licencia | BSD 3-Clause | “BSD 3-Clause License” | `LICENSE`, línea 1 |
| Titular | GE Precision HealthCare | “Copyright (c) 2024, GE Precision HealthCare” | `LICENSE`, línea 3 |
| Materiales | Paciente, agua desplazada y metal | “phmetal_json['n_materials'] = 3” | `run.py`, línea 40 |
| Desplazamiento | Resta agua donde entra el metal | “density_scale'].append(-1.0)” | `run.py`, línea 78 |
| Metal | Añade el material metálico | “density_scale'].append(1.0)” | `run.py`, línea 79 |
| Ejecución | Una llamada de simulación | “ct.run_all()” | `run.py`, línea 92 |
