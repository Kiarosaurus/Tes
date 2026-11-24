#!/usr/bin/env python3
"""Inventario determinista por seccion de la tesis. Salida: state/inventory.json y .md"""
import re, json, sys, pathlib
base = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "review/thesis")
ORDER = ["introduccion","capitulo1","capitulo2","capitulo3","capitulo4","conclusiones","trabajosFuturos","resumen","abstract","anexos"]
SEC = re.compile(r'\\(chapter|section|subsection|subsubsection)\*?\{([^}]*)\}(?:\\label\{([^}]*)\})?')
def words(t):
    t = re.sub(r'(?m)(?<!\\)%.*$', '', t)
    t = re.sub(r'\\(cite[a-z]*|ref|eqref|label|autoref|cref)\{[^}]*\}', '', t)
    t = re.sub(r'\$[^$]*\$', ' M ', t)
    t = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?', ' ', t)
    return len(re.findall(r"[A-Za-zÁÉÍÓÚÑáéíóúñü]{2,}", t))
out = []
for name in ORDER:
    p = base/"secciones"/f"{name}.tex"
    if not p.exists(): continue
    lines = p.read_text(encoding="utf-8").splitlines()
    marks = [(i, m) for i, l in enumerate(lines) for m in [SEC.search(l)] if m]
    marks.append((len(lines), None))
    for (i, m), (j, _) in zip(marks, marks[1:]):
        chunk = "\n".join(lines[i:j])
        out.append(dict(file=name, level=m.group(1), title=m.group(2)[:90], label=m.group(3), lines=f"{i+1}-{j}",
            words=words(chunk), tables=len(re.findall(r'\\begin\{table',chunk)), figures=len(re.findall(r'\\begin\{figure',chunk)),
            cites=len(re.findall(r'\\cite[a-z]*\{',chunk)), eqs=len(re.findall(r'\\begin\{(equation|align)',chunk)),
            GAPLIT=chunk.count(r'\GAPLIT'), GAPDATO=chunk.count(r'\GAPDATO'), GAPDEC=chunk.count(r'\GAPDEC'), REVVISUAL=chunk.count(r'\REVVISUAL')))
pathlib.Path("state").mkdir(exist_ok=True)
json.dump(out, open("state/inventory.json","w"), ensure_ascii=False, indent=1)
with open("state/inventory.md","w") as f:
    f.write("| file | lvl | title | lines | words | tab | fig | cite | GAPL/D/C | REVV |\n|---|---|---|---|---|---|---|---|---|---|\n")
    for r in out:
        f.write(f"| {r['file']} | {r['level'][:3]} | {r['title']} | {r['lines']} | {r['words']} | {r['tables']} | {r['figures']} | {r['cites']} | {r['GAPLIT']}/{r['GAPDATO']}/{r['GAPDEC']} | {r['REVVISUAL']} |\n")
print(len(out),"unidades; palabras (heuristica, no texcount):",sum(r['words'] for r in out if r['level']=='chapter' or True and False) or "ver md")
