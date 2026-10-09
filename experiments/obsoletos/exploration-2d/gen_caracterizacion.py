from pathlib import Path
import pandas as pd
OUT = Path.home() / "metalsynth" / "outputs"
scr = pd.read_csv(OUT / "metal_screening.csv")
d7 = scr[scr.dataset == "dataset7"].copy().sort_values("total_mm3", ascending=False)
exc = set(pd.read_csv(OUT / "excluded_metal_ids.csv").file)
d7["en_cohorte"] = d7.file.apply(lambda f: "excluido_dup" if f in exc
                                 else ("C_test" if any(t in f for t in
                                       [f"{i:04d}" for i in range(14)]) else "B"))
car = d7[["file", "en_cohorte", "n_comp", "total_mm3", "hu_max"]].copy()
car["png"] = car.file.str.replace(".nii.gz", "", regex=False) + "_z" + \
             d7.z_best.astype(str) + ".png"
car["tipo"] = ""        # <- a llenar en el triaje
car["ortopedico"] = ""  # <- si / no / dudoso
car["nota"] = ""
car.to_csv(OUT / "caracterizacion_metal_d7.csv", index=False)
print(f"{len(car)} filas -> caracterizacion_metal_d7.csv")
print(car.en_cohorte.value_counts().to_string())
