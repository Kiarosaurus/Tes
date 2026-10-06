"""Copia local de `repos/xcist-example/AAPM_datachallenge/simulation_scripts/run.py`
(commit 4993e87, 2025-10-08), con UN parche minimo documentado mas abajo.

POR QUE ESTA COPIA EXISTE
-------------------------
`repos/` es el clon tal como lo publica el proyecto XCIST y **no se edita**, igual que
`refs/raw/`. Pero el script publicado **no corre tal como viene** con numpy actual, asi que
reproducir el protocolo exige un parche. El parche va aqui, anotado en el sitio exacto, para
que la diferencia entre lo publicado y lo ejecutado quede visible y citable. `main.tex` promete
documentar *"the code revision, configuration, reconstruction settings and access conditions"*;
esta cabecera y el comentario del parche son parte de esa documentacion.
"""
import skimage.transform
import json
from scipy.io import loadmat, savemat
import numpy as np
import gecatsim as xc
from gecatsim.reconstruction.pyfiles import recon

def dumpjson(filename, jsondict):
    out_file = open(filename, "w") 
    json.dump(jsondict, out_file, indent = 4) 
    out_file.close()

# load metal masks, of size 256x256
metal_file = loadmat("./metal_masks.mat")
metal_file = metal_file['tumor_imgs']/255
metal_file[metal_file>=0.1] = 1
metal_file[metal_file<0.1] = 0

metal = np.float32(metal_file[0])
metaldiam = float(2.*np.sqrt(metal.sum()/np.pi)) # effective diameter
# PARCHE LOCAL 2026-10-05, no del repositorio original: sin el `float()`, `metaldiam` es
# `np.float32` y `mt_pixsize` lo hereda, de modo que `json.dump` de `sim.json` aborta con
# `TypeError: Object of type float32 is not JSON serializable`. El script publicado falla asi
# tal como viene. El clon de `repos/` se deja INTACTO; el parche vive solo en esta copia.
with open("metal.vf", 'wb') as fout:
    tmp1 = np.float32(metal)
    tmp1 = tmp1.copy(order="C")
    fout.write(tmp1)  # Write the phantom layer to the matching file name

# pix size for phantoms (excluding metal)
ph_pixsize = 400./512 #in mm/pixel

# following parameters are random/customizable in real simulations
tgt_mtdiam = 10 # effective diameter in mm
x_offset = 100 # offset (position) of metal, in pixels
y_offset = 100
metal_mat = 'Ti' # material of metal
# end of random parameters

# metal pixel size, in mm/pixel
mt_pixsize = tgt_mtdiam/metaldiam

phmetal_json = json.load(open("sim_base.json"))
phmetal_json['n_materials'] = 3
phmetal_json['mat_name'].append("water")
phmetal_json['volumefractionmap_datatype'].append('float')
phmetal_json["volumefractionmap_filename"].append("phantom.vf")
phmetal_json['cols'].append(int(512))
phmetal_json['rows'].append(int(512))
phmetal_json['slices'].append(int(1))
phmetal_json['x_size'].append(ph_pixsize)
phmetal_json['y_size'].append(ph_pixsize)
phmetal_json['z_size'].append(100.0)
phmetal_json['x_offset'].append(256.5)
phmetal_json['y_offset'].append(256.5)
phmetal_json['z_offset'].append(1.0)
phmetal_json['density_scale'].append(1.0)
phmetal_json['mat_name'].append("water")
phmetal_json['mat_name'].append(metal_mat)
phmetal_json['volumefractionmap_datatype'].append('float')
phmetal_json['volumefractionmap_datatype'].append('float')
phmetal_json["volumefractionmap_filename"].append("metal.vf")
phmetal_json["volumefractionmap_filename"].append("metal.vf")
phmetal_json['cols'].append(int(256))
phmetal_json['cols'].append(int(256))
phmetal_json['rows'].append(int(256))
phmetal_json['rows'].append(int(256))
phmetal_json['slices'].append(int(1))
phmetal_json['slices'].append(int(1))
phmetal_json['x_size'].append(mt_pixsize)
phmetal_json['x_size'].append(mt_pixsize)
phmetal_json['y_size'].append(mt_pixsize)
phmetal_json['y_size'].append(mt_pixsize)
phmetal_json['z_size'].append(100.0)
phmetal_json['z_size'].append(100.0)
phmetal_json['x_offset'].append(x_offset*ph_pixsize/mt_pixsize)
phmetal_json['x_offset'].append(x_offset*ph_pixsize/mt_pixsize)
phmetal_json['y_offset'].append(y_offset*ph_pixsize/mt_pixsize)
phmetal_json['y_offset'].append(y_offset*ph_pixsize/mt_pixsize)
phmetal_json['z_offset'].append(1.0)
phmetal_json['z_offset'].append(1.0)
phmetal_json['density_scale'].append(-1.0)
phmetal_json['density_scale'].append(1.0)

dumpjson("sim.json", phmetal_json) 

# simulations
ct = xc.CatSim("AAPM_MAR_phantom",
               "AAPM_MAR_protocol",
               "AAPM_MAR_physics",
               "AAPM_MAR_scanner",
               "AAPM_MAR_recon")

ct.resultsName = "out"

ct.run_all()  # run the scans defined by protocol.scanTypes

# to convert prep to raw
sino = xc.rawread(ct.resultsName+'.prep', [ct.protocol.viewCount, ct.scanner.detectorRowCount, ct.scanner.detectorColCount], 'float')
sino = np.squeeze(sino[:, 0, :])
xc.rawwrite(ct.resultsName+"_%dx%d.raw"%(ct.scanner.detectorColCount, ct.protocol.viewCount), sino.copy(order="C"))

# reconstruction
cfg = ct.get_current_cfg();
cfg.do_Recon = 1
cfg.waitForKeypress = 0
recon.recon(cfg)
