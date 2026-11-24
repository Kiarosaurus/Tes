"""R-11 (auditoria): sensibilidad de W1 a la convencion h = k*sigma del muestreador. Solo CPU, sin tocar el repo.
Fija muestreo.FACTOR_SIGMA (2.0 = decidido; 4.0 -> sigma x0.5; 1.0 -> sigma x2) y ejecuta e13_muestreo_sap.py sin modificarlo.
Uso: FACTOR_SIGMA=4 python audit_r11_sigma.py <args de e13> (incluir --refs-dir con symlinks de entrada y --out-sufijo)"""
import os, runpy, sys
from pathlib import Path
REPO = Path(os.environ.get('REPO', Path.home() / 'metalsynth'))
sys.path.insert(0, str(REPO / 'src' / 'muestreador'))
import muestreo  # noqa: E402
muestreo.FACTOR_SIGMA = float(os.environ['FACTOR_SIGMA'])
print('R11: FACTOR_SIGMA =', muestreo.FACTOR_SIGMA, flush=True)
script = REPO / 'experiments' / 'objetivo2' / 'e13_muestreo_sap.py'
sys.argv = [str(script)] + sys.argv[1:]
runpy.run_path(str(script), run_name='__main__')
