#!/usr/bin/env python3
"""Lint determinista del documento de tesis en overleaf/.

Capa "test" del ciclo de redaccion: comprueba lo que se puede comprobar sin opinar
(lista negra de estilo, oraciones largas, siglas sin definir, citas inexistentes,
relleno de plantilla, marcas GAP) y, con --compilar, que el documento compile sin
errores ni citas o referencias indefinidas.

Los criterios salen de redaccion/ESTILO.md y redaccion/RUBRICA.md; cada hallazgo
lleva el ID del criterio. Sale con codigo 1 si hay hallazgos de severidad alta o
media, y 0 si solo quedan de severidad baja.

Uso:
    python scripts/lint_redaccion.py                  # todo el documento
    python scripts/lint_redaccion.py capitulo3        # una seccion
    python scripts/lint_redaccion.py --compilar       # ademas compila
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OVERLEAF = ROOT / "overleaf"
BUILD = ROOT / "redaccion" / ".build"

SEVERIDADES = ("alta", "media", "baja")

# Espanol normalizado sin tildes; se compara contra el texto tambien sin tildes.
LISTA_IA = [
    r"cabe (destacar|senalar|mencionar|resaltar)",
    r"es importante (destacar|senalar|mencionar|resaltar|notar)",
    r"vale la pena", r"es (fundamental|crucial|esencial)",
    r"en este (sentido|orden de ideas)", r"dicho (esto|lo anterior)",
    r"en la actualidad", r"hoy en dia", r"en el panorama actual", r"en el ambito de",
    r"(juega|juegan|desempena|desempenan) un papel", r"papel (crucial|fundamental|clave)",
    r"crucial(es)?", r"vital(es)?", r"innovador(a|es|as)?", r"novedos[oa]s?",
    r"revolucion(ar|a|an)", r"sin precedentes", r"de vanguardia", r"transformador(a|es)?",
    r"holistic[oa]s?", r"sinergias?", r"potenciar", r"aprovech(ar|a|an|ando)",
    r"una amplia gama", r"un amplio abanico", r"significativamente",
    r"profundiz(ar|a|an|ando)", r"adentr(arse|a|an)", r"sumergirse",
    r"arrojar luz", r"allanar el camino", r"sentar las bases",
    r"no solo\b.{0,80}\bsino", r"en resumen,", r"en conclusion,", r"en definitiva,",
    r"en base a", r"a nivel de", r"jugar un rol", r"hacer sentido", r"en orden a", r"remarcar",
]
LISTA_INF = [
    r"super", r"bastante", r"un monton", r"cosas?", r"basicamente", r"obviamente",
    r"claramente", r"evidentemente", r"por supuesto", r"realmente", r"increible",
    r"etc\.", r"yo", r"nosotros", r"nuestr[oa]s?",
]
# "robusto" solo es hallazgo si no se define operacionalmente; lo marca el lint como baja.
LISTA_BAJA = [r"robust[oa]s?", r"robustez", r"diversos", r"multiples", r"abordar"]

RELLENO = [r"lorem", r"ipsum", r"palabra clave \d", r"keyword \d",
           r"titulo de la tesis", r"sed eu orci", r"primer subtitulo",
           # Instrucciones de la plantilla UTEC que quedan como texto del documento.
           r"un resumen debe ser", r"esta seccion le brinda", r"una tesis sin trabajos futuros",
           r"los algoritmos desarrollados \.\.\."]

# Siglas que son nombres propios o numerales y no necesitan definicion.
SIGLAS_EXENTAS = {
    "II", "III", "IV", "VI", "VII", "VIII", "IX", "XI", "XII", "UTEC", "IEEE", "ORCID",
    "CLINIC", "XCIST", "AAPM", "S1", "S2", "S3", "S4", "L5", "PDF", "GAP", "LIT", "DATO",
    "DEC", "ABSTRACT", "RESUMEN", "ANEXOS",
}

CITA = re.compile(r"\\cite[tp]?\*?(?:\[[^\]]*\])*\{([^}]*)\}")
GAP = re.compile(r"\\GAP(LIT|DATO|DEC)\{")


@dataclass
class Hallazgo:
    """Un hallazgo del lint, anclado a archivo y linea."""

    archivo: str
    linea: int
    severidad: str
    criterio: str
    texto: str


def sin_tildes(s: str) -> str:
    """Quita diacriticos y pasa a minusculas, para comparar contra las listas."""
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn").lower()


def quitar_comentarios(linea: str) -> str:
    """Elimina el comentario LaTeX de una linea, respetando \\%."""
    return re.sub(r"(?<!\\)%.*", "", linea)


def orden_de_secciones() -> list[Path]:
    """Lee overleaf/main.tex y devuelve los \\input en orden de aparicion."""
    main = (OVERLEAF / "main.tex").read_text(encoding="utf-8")
    rutas = []
    for linea in main.splitlines():
        m = re.search(r"\\input\{([^}]+)\}", quitar_comentarios(linea))
        if m:
            p = OVERLEAF / (m.group(1) + ("" if m.group(1).endswith(".tex") else ".tex"))
            if p.exists():
                rutas.append(p)
    return rutas


def texto_plano(linea: str) -> str:
    """Aproxima el texto visible: quita matematicas, citas, referencias y comandos."""
    s = re.sub(r"\$[^$]*\$", " X ", linea)
    s = CITA.sub(" ", s)
    s = re.sub(r"\\(ref|eqref|label|includegraphics|input|GAPLIT|GAPDATO|GAPDEC)\*?\{[^}]*\}", " ", s)
    s = re.sub(r"\\[a-zA-Z]+\*?", " ", s)
    return re.sub(r"[{}\\~]", " ", s)


def claves_bib() -> set[str]:
    """Claves presentes en overleaf/referencias.bib."""
    bib = OVERLEAF / "referencias.bib"
    if not bib.exists():
        return set()
    return set(re.findall(r"@\w+\{([^,\s]+),", bib.read_text(encoding="utf-8")))


def revisar_archivo(ruta: Path, siglas_definidas: set[str], bib: set[str],
                    reportar: bool) -> tuple[list[Hallazgo], dict[str, int]]:
    """Revisa un .tex; actualiza siglas_definidas aunque no se reporte."""
    rel = str(ruta.relative_to(ROOT)).replace("\\", "/")
    es_resumen = ruta.stem == "resumen"
    en_ingles = ruta.stem == "abstract"
    es_propio = ruta.stem == "capitulo4"
    hallazgos: list[Hallazgo] = []
    gaps = {"LIT": 0, "DATO": 0, "DEC": 0}
    lineas = ruta.read_text(encoding="utf-8").splitlines()
    en_entorno_excluido = 0

    def h(n: int, sev: str, crit: str, txt: str) -> None:
        if reportar:
            hallazgos.append(Hallazgo(rel, n, sev, crit, txt.strip()[:110]))

    # Oraciones: se acumula el texto de cada parrafo con la linea donde empieza.
    parrafo: list[tuple[int, str]] = []

    def cerrar_parrafo() -> None:
        if not parrafo:
            return
        texto = " ".join(t for _, t in parrafo)
        inicio = parrafo[0][0]
        for oracion in re.split(r"(?<=[.?!])\s+(?=[A-ZÁÉÍÓÚÑ¿])", texto):
            n = len(re.findall(r"\w+", oracion))
            if n > 40 and not en_ingles:
                h(inicio, "media", "E-O1", f"oracion de {n} palabras: {oracion[:80]}...")
        parrafo.clear()

    for n, cruda in enumerate(lineas, start=1):
        linea = quitar_comentarios(cruda)
        if re.search(r"\\begin\{(equation|align|table|tabular|figure|itemize|enumerate)", linea):
            en_entorno_excluido += 1
        if re.search(r"\\end\{(equation|align|table|tabular|figure|itemize|enumerate)", linea):
            en_entorno_excluido = max(0, en_entorno_excluido - 1)

        for m in GAP.finditer(linea):
            gaps[m.group(1)] += 1

        norm = sin_tildes(linea)
        for pat in RELLENO:
            if re.search(pat, norm):
                h(n, "alta", "G-T1", f"relleno de plantilla: /{pat}/")
                break

        for m in CITA.finditer(linea):
            for clave in (k.strip() for k in m.group(1).split(",")):
                if clave and clave not in bib:
                    h(n, "alta", "G-T6", f"cita sin entrada en referencias.bib: {clave}")
            if es_resumen:
                h(n, "alta", "P-R2", "cita dentro del resumen")

        plano = texto_plano(linea)
        norm_plano = sin_tildes(plano)
        if not en_ingles:
            for lista, crit, sev in ((LISTA_IA, "E-IA", "media"), (LISTA_INF, "E-INF", "media"),
                                     (LISTA_BAJA, "E-P4", "baja")):
                for pat in lista:
                    m = re.search(rf"(?<![\w-]){pat}(?![\w-])", norm_plano)
                    if m:
                        h(n, sev, crit, f"'{m.group(0)}' en: {plano.strip()[:70]}")
            if re.search(r"---|—", linea):
                h(n, "media", "E-IA", "guion largo como inciso")
            if "!" in plano:
                h(n, "media", "E-INF", "signo de exclamacion")

        # Siglas: la primera aparicion debe ser "(SIGLA)" o "SIGLA (". Los titulos van
        # en mayusculas por plantilla y no son siglas.
        es_titulo = re.search(r"\\(chapter|customchapter|section|subsection|introsection|addcontentsline|markboth)", linea)
        for m in [] if es_titulo else re.finditer(r"(?<![\w\\{-])([A-ZÁÉÍÓÚÑ]{2,}[0-9]?)(?![\w-])", plano):
            sigla = m.group(1)
            if sigla in SIGLAS_EXENTAS:
                continue
            if es_resumen:
                h(n, "alta", "P-R2", f"sigla en el resumen: {sigla}")
                continue
            if sigla in siglas_definidas:
                continue
            antes, despues = plano[:m.start()], plano[m.end():]
            if antes.rstrip().endswith("(") or despues.lstrip().startswith("("):
                siglas_definidas.add(sigla)
            elif not en_ingles:
                h(n, "media", "E-T3", f"sigla sin definir en su primera aparicion: {sigla}")
                siglas_definidas.add(sigla)

        # Cifras sin fuente visible, fuera del capitulo de resultados propios.
        if (not es_propio and not en_ingles and not en_entorno_excluido
                and re.search(r"\d+(\.\d+)?\s*(%|\\%|mm|HU|dB|grados)|\d+\.\d+", plano)
                and not re.search(r"\\cite|\\ref|\\GAP", linea)):
            h(n, "baja", "E-P1", f"cifra sin cita, \\ref ni GAP en la linea: {plano.strip()[:70]}")

        if en_entorno_excluido or not plano.strip() or re.match(r"\s*\\(chapter|section|subsection|customchapter|introsection|paragraph)", linea):
            cerrar_parrafo()
        else:
            parrafo.append((n, plano.strip()))
    cerrar_parrafo()
    return hallazgos, gaps


def compilar() -> list[Hallazgo]:
    """Compila overleaf/main.tex en redaccion/.build y reporta errores y avisos."""
    BUILD.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, BIBINPUTS=str(OVERLEAF) + os.pathsep, BSTINPUTS=str(OVERLEAF) + os.pathsep)
    subprocess.run(["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error",
                    f"-outdir={BUILD}", "main.tex"], cwd=OVERLEAF, env=env,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    log = BUILD / "main.log"
    if not log.exists():
        return [Hallazgo("overleaf/main.tex", 0, "alta", "G-T1", "no se genero main.log")]
    texto = log.read_text(encoding="latin-1", errors="replace")
    out: list[Hallazgo] = []
    for m in re.finditer(r"^! (.*)$", texto, re.M):
        out.append(Hallazgo("overleaf/main.tex", 0, "alta", "G-T1", f"error LaTeX: {m.group(1)}"))
    for clave in sorted(set(re.findall(r"Citation `([^']+)' .*?undefined", texto))):
        out.append(Hallazgo("overleaf/main.tex", 0, "alta", "G-T6", f"cita indefinida al compilar: {clave}"))
    for ref in sorted(set(re.findall(r"Reference `([^']+)' .*?undefined", texto))):
        out.append(Hallazgo("overleaf/main.tex", 0, "alta", "G-T4", f"referencia indefinida: {ref}"))
    overfull = len(re.findall(r"^Overfull \\hbox", texto, re.M))
    if overfull:
        out.append(Hallazgo("overleaf/main.tex", 0, "baja", "G-T1", f"{overfull} lineas desbordadas (Overfull hbox)"))
    paginas = re.search(r"Output written on .*?\((\d+) pages?", texto, re.S)
    if paginas:
        print(f"PDF: {BUILD / 'main.pdf'} ({paginas.group(1)} paginas)")
    return out


def main() -> int:
    """Corre el lint y escribe el reporte en stdout."""
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("seccion", nargs="?", help="nombre del .tex sin extension (p. ej. capitulo3)")
    ap.add_argument("--compilar", action="store_true", help="compila y revisa el log")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    bib = claves_bib()
    siglas: set[str] = set()
    hallazgos: list[Hallazgo] = []
    gaps_total = {"LIT": 0, "DATO": 0, "DEC": 0}
    rutas = orden_de_secciones()
    if args.seccion and not any(r.stem == args.seccion for r in rutas):
        print(f"seccion desconocida: {args.seccion}", file=sys.stderr)
        return 2
    for ruta in rutas:
        reportar = args.seccion is None or ruta.stem == args.seccion
        hs, gaps = revisar_archivo(ruta, siglas, bib, reportar)
        hallazgos += hs
        if reportar:
            for k in gaps_total:
                gaps_total[k] += gaps[k]
    if args.compilar:
        hallazgos += compilar()

    hallazgos.sort(key=lambda x: (SEVERIDADES.index(x.severidad), x.archivo, x.linea))
    print("| Sev | Criterio | Ubicacion | Hallazgo |\n|---|---|---|---|")
    for x in hallazgos:
        print(f"| {x.severidad} | {x.criterio} | {x.archivo}:{x.linea} | {x.texto.replace('|', '/')} |")
    cuenta = {s: sum(1 for x in hallazgos if x.severidad == s) for s in SEVERIDADES}
    print(f"\nTOTAL alta={cuenta['alta']} media={cuenta['media']} baja={cuenta['baja']} | "
          f"GAP lit={gaps_total['LIT']} dato={gaps_total['DATO']} dec={gaps_total['DEC']}")
    print("LINT: " + ("FALLA" if cuenta["alta"] or cuenta["media"] else "PASA"))
    return 1 if cuenta["alta"] or cuenta["media"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
