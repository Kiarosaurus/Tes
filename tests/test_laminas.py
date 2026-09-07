"""Regresiones de las laminas de apoyo a la clasificacion visual."""
import importlib.util
from argparse import Namespace
from pathlib import Path
import json
import tempfile
import unittest

import nibabel as nib
import numpy as np

spec = importlib.util.spec_from_file_location(
    'laminas', Path(__file__).resolve().parents[1] / 'experiments/exploration-3d/laminas.py')
laminas = importlib.util.module_from_spec(spec)
spec.loader.exec_module(laminas)


class LaminasTest(unittest.TestCase):
    def build(self, root: Path, case: str = 'dataset7_X_data') -> Path:
        """CT sintetico con dos objetos densos separados, uno en el borde."""
        root.mkdir(parents=True, exist_ok=True)
        voxels = np.full((32, 30, 28), -1000, dtype=np.int16)
        voxels[10:20, 10:20, 8:18] = 300
        voxels[12:15, 12:15, 10:13] = 6000
        voxels[0:3, 5:8, 20:23] = 5000
        image = nib.Nifti1Image(voxels, np.diag([-.8, .9, 1.2, 1.]))
        image.header.set_xyzt_units('mm')
        nib.save(image, root / (case + '.nii.gz'))
        return root

    def test_sheet_reports_components_without_deciding(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            data = self.build(root / 'data')
            args = Namespace(data=data, out=root / 'out', hu=2500, min=5)
            facts = laminas.sheet('dataset7_X_data', args)
            out = args.out / 'outputs' / 'laminas' / 'dataset7_X_data'
            for name in ('proyecciones.png', 'ortogonales.png', 'axiales.png'):
                self.assertTrue((out / name).exists(), name)
            self.assertEqual(len(facts['componentes']), 2)
            self.assertEqual(facts['voxeles_sobre_umbral'], 3 * 3 * 3 + 3 * 3 * 3)
            biggest, border = facts['componentes']
            self.assertGreaterEqual(biggest['voxeles'], border['voxeles'])
            self.assertTrue(any(c['toca_borde_fov'] for c in facts['componentes']))
            self.assertEqual(json.loads((out / 'hallazgos.json').read_text(encoding='utf-8')),
                             facts)

    def test_empty_mask_still_draws_and_reports_nothing(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            data = root / 'data'
            data.mkdir()
            voxels = np.zeros((12, 11, 10), dtype=np.int16)
            image = nib.Nifti1Image(voxels, np.diag([1., 1., 1., 1.]))
            image.header.set_xyzt_units('mm')
            nib.save(image, data / 'dataset6_Y_data.nii.gz')
            args = Namespace(data=data, out=root / 'out', hu=2500, min=5)
            facts = laminas.sheet('dataset6_Y_data', args)
            self.assertEqual(facts['componentes'], [])
            self.assertEqual(facts['voxeles_sobre_umbral'], 0)
            self.assertEqual(len(facts['laminas']), 3)

    def test_missing_case_fails_loudly(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaises(SystemExit):
                laminas.locate('inexistente', Path(temp))

    def test_units_not_in_mm_are_refused(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            data = root / 'data'
            data.mkdir()
            image = nib.Nifti1Image(np.zeros((6, 6, 6), dtype=np.int16), np.eye(4))
            nib.save(image, data / 'dataset6_Z_data.nii.gz')
            args = Namespace(data=data, out=root / 'out', hu=2500, min=5)
            with self.assertRaises(SystemExit):
                laminas.sheet('dataset6_Z_data', args)


if __name__ == '__main__':
    unittest.main()
