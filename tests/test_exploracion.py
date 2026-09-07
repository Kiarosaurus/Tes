"""Regresiones del inventario y de las barreras de elegibilidad."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from argparse import Namespace

import nibabel as nib
import numpy as np

spec = importlib.util.spec_from_file_location('explorar', Path(__file__).resolve().parents[1] / 'experiments/exploration-3d/explorar.py')
explorar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(explorar)


class ExplorationTest(unittest.TestCase):
    def test_views_with_anisotropic_reoriented_volume(self):
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            values = np.zeros((8, 9, 10), dtype=np.int16)
            values[2:5, 3:6, 4:7] = 5000
            image = nib.Nifti1Image(values, np.diag([-1., 2., 3., 1.]))
            image.header.set_xyzt_units('mm')
            case = 'dataset6_A_data'
            nib.save(image, root / (case + '.nii.gz'))
            args = Namespace(data=root, out=root / 'out', hu=2500, case=case)
            explorar.scan(args)
            explorar.view(args)
            html = (args.out / 'outputs' / (case + '.html')).read_text(encoding='utf-8')
            self.assertIn('"showlegend":true', html)
            self.assertTrue((args.out / 'outputs' / (case + '_cortes.png')).exists())
            with patch.object(plt, 'show') as show:
                explorar.cuts(args)
                show.assert_called_once()
            plt.close('all')

    def test_scaled_hu_duplicates_and_manual_preservation(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            data, out = root / 'data', root / 'out'
            data.mkdir()
            voxels = np.zeros((4, 5, 6), dtype=np.int16)
            voxels[1, 2, 3] = 1800
            for name in ('dataset6_A_data', 'dataset7_B_data'):
                image = nib.Nifti1Image(voxels, np.diag([.7, .8, 1.2, 1]))
                image.header.set_xyzt_units('mm')
                image.header.set_slope_inter(2, -1000)
                nib.save(image, data / (name + '.nii.gz'))
            args = Namespace(data=data, out=out, hu=2500)
            explorar.scan(args)
            rows = explorar.read_csv(out / 'revision.csv')
            self.assertEqual(float(rows[0]['HU máximo']), 2600)
            self.assertEqual(rows[0]['Vóxeles sobre umbral'], '1')
            self.assertEqual(rows[0]['Grupo duplicado'], rows[1]['Grupo duplicado'])
            self.assertEqual(rows[0]['Cohorte propuesta'], 'resolver duplicado')
            rows[0]['Notas'] = 'Anotación manual, con coma'
            explorar.save(rows, out)
            explorar.scan(args)
            self.assertEqual(explorar.read_csv(out / 'revision.csv')[0]['Notas'], 'Anotación manual, con coma')

    def test_incomplete_uncertain_and_patient_overlap(self):
        row = dict.fromkeys(explorar.MANUAL + explorar.AUTO, '')
        row.update({'Caso': 'A', 'Metal': 'no', 'Objeto extraño': 'no'})
        explorar.cohorts([row])
        self.assertEqual(row['Cohorte propuesta'], 'pendiente')
        row.update({'Revisión 3D y cortes': 'completa', 'Revisor': 'R', 'Fecha': '2026-09-06', 'Grupo paciente': 'P'})
        explorar.cohorts([row])
        self.assertEqual(row['Cohorte propuesta'], 'entrenamiento candidato')
        row['Metal'] = 'incierto'
        explorar.cohorts([row])
        self.assertEqual(row['Cohorte propuesta'], 'pendiente')
        row['Metal'] = 'no'
        other = dict(row, Caso='B', Metal='sí')
        explorar.cohorts([row, other])
        self.assertTrue(all(r['Cohorte propuesta'] == 'resolver grupo paciente' for r in [row, other]))

    def test_unknown_units_do_not_become_clean_cases(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            nib.save(nib.Nifti1Image(np.zeros((2, 3, 4)), np.eye(4)), root / 'dataset6_A_data.nii.gz')
            explorar.scan(Namespace(data=root, out=root / 'out', hu=2500))
            row = explorar.read_csv(root / 'out/revision.csv')[0]
            self.assertTrue(row['Error'])
            self.assertEqual(row['Cohorte propuesta'], 'error')


if __name__ == '__main__':
    unittest.main()


class BatchViewsTest(unittest.TestCase):
    def build(self, root: Path, names: tuple[str, ...]) -> None:
        """Volumenes minimos: uno con metal y uno sin nada sobre el umbral."""
        for name, peak in zip(names, (5000, 100)):
            values = np.zeros((8, 9, 10), dtype=np.int16)
            values[2:5, 3:6, 4:7] = peak
            image = nib.Nifti1Image(values, np.diag([-1., 2., 3., 1.]))
            image.header.set_xyzt_units('mm')
            nib.save(image, root / (name + '.nii.gz'))

    def test_batch_covers_candidates_and_skips_existing(self):
        import matplotlib
        matplotlib.use('Agg')
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            names = ('dataset7_A_data', 'dataset6_B_data')
            self.build(root, names)
            args = Namespace(data=root, out=root / 'out', hu=2500, todos=False,
                             rehacer=False, cortes_html=False, plotlyjs='directory')
            explorar.scan(args)
            explorar.views(args)
            outputs = args.out / 'outputs'
            self.assertTrue((outputs / 'dataset7_A_data.html').exists())
            self.assertFalse((outputs / 'dataset6_B_data.html').exists())
            self.assertFalse((outputs / 'dataset7_A_data_cortes.html').exists())
            self.assertTrue((outputs / 'dataset7_A_data_cortes.png').exists())
            stamp = (outputs / 'dataset7_A_data.html').stat().st_mtime_ns
            explorar.views(args)
            self.assertEqual((outputs / 'dataset7_A_data.html').stat().st_mtime_ns, stamp)
            args.todos = True
            explorar.views(args)
            self.assertTrue((outputs / 'dataset6_B_data.html').exists())
