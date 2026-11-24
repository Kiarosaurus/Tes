# Pruebas de auditoria en Khipu (solo inferencia / CPU; no entrenan, no tocan ~/metalsynth ni su rama)
Usuario: kiara.balcazar@khipu.utec.edu.pe. Archivos: audit_gpu.sbatch (MODO r4|r1|r2|r9|r3|r12), audit_r9_contexto.py, audit_r11.sbatch,
audit_r11_sigma.py, casos_val2.txt (12 casos, regla fijada antes de ver resultados: indices pares de la lista ordenada de 27 candidatos, primeros 12; ver analysis/r3_candidatos.csv).

## 1. Enviar (local -> Khipu), sin git. Desde WSL:
    rsync -av ~/audit_ws/khipu/ kiara.balcazar@khipu.utec.edu.pe:~/audit_khipu/
(alternativa, PowerShell: scp -r \\wsl$\Ubuntu\home\kiara\audit_ws\khipu kiara.balcazar@khipu.utec.edu.pe:~/audit_khipu)
Verificar que no pisa nada: el destino es ~/audit_khipu/, fuera de ~/metalsynth.

## 2. Lanzar (en Khipu; cuenta tesis, MaxJobsPU=3: contar tu job maestro T/P/A; `squeue -u $USER`)
    cd ~/audit_khipu
    # prueba en seco de cada uno antes del real:
    sbatch --test-only -p all --gres=gpu:tesla:1 --export=ALL,MODO=r4 audit_gpu.sbatch
    # orden sugerido (de mayor a menor valor/coste):
    sbatch -p all --gres=gpu:tesla:1 --export=ALL,MODO=r4  audit_gpu.sbatch   # R-4  T4 (la del ajuste fino). Repetir con --gres=gpu:rtxa6000:1 para tener la otra tarjeta
    sbatch -p all --gres=gpu:tesla:1 --export=ALL,MODO=r2  audit_gpu.sbatch   # R-2
    sbatch -p all --gres=gpu:tesla:1 --export=ALL,MODO=r9  audit_gpu.sbatch   # R-9 (control + contexto suavizado)
    sbatch -p all --gres=gpu:tesla:1 --export=ALL,MODO=r1  audit_gpu.sbatch   # R-1: solo genera si no existe obj3_pose/nulo/run04_mejor_nulo con los 13
    sbatch audit_r11.sbatch                                                      # R-11, CPU (big-mem n006)
    # antes de r3/r12, confirmar la identidad de paciente de casos_val2.txt (F-H5; no garantizada para volumenes sin metal):
    sbatch -p all --gres=gpu:tesla:1 --export=ALL,MODO=r3  audit_gpu.sbatch   # R-3  validacion 2
    sbatch -p all --gres=gpu:tesla:1 --export=ALL,MODO=r12 audit_gpu.sbatch   # R-12 poses perturbadas
Los jobs son reanudables (se saltan lo ya generado). Los logs quedan en ~/audit_khipu/audit_<id>.log.
Si algun flag de a15 no existe en la rama que este en Khipu, el job aborta con ERROR antes de gastar GPU.

## 3. Traer resultados (Khipu -> local). Solo CSV/logs, sin NIfTI ni npz:
    mkdir -p ~/audit_ws/khipu_out
    rsync -av --include='*/' --include='*_perfil.csv' --include='*_cotejo.csv' --include='*_resumen.csv' --exclude='*' \
        kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/obj3_pose/audit/ ~/audit_ws/khipu_out/audit/
    rsync -av --include='*/' --include='*_perfil.csv' --exclude='*' \
        kiara.balcazar@khipu.utec.edu.pe:~/metalsynth/data/obj3_pose/nulo/ ~/audit_ws/khipu_out/nulo/        # R-1, ya existente
    rsync -av --include='e13_*_fs*' --include='*.log' --exclude='*' kiara.balcazar@khipu.utec.edu.pe:~/audit_khipu/r11/ ~/audit_ws/khipu_out/r11/
    rsync -av --include='audit*.log' --exclude='*' kiara.balcazar@khipu.utec.edu.pe:~/audit_khipu/ ~/audit_ws/khipu_out/logs/

## 4. Comparar en local (CPU), con ~/.venvs/audit/bin/python ~/audit_ws/khipu/comparar_perfiles.py ...
    # R-4: nuevo vs referencia del 15-oct (delta/run04_mejor)
    ... r4 /mnt/c/Users/Usuario/Downloads/pesados/outputs_obj3_pose/delta/run04_mejor ~/audit_ws/khipu_out/audit/r4_<GPU> run04_mejor
    # R-1: piso por anillo de los 13 de prueba
    ... anillos ~/audit_ws/khipu_out/nulo/run04_mejor_nulo run04_mejor_nulo
    # R-2: diferencia de piso entre variantes de eta
    ... var ~/audit_ws/khipu_out/audit/r2_piso_eta run04_mejor_nulo_p50_e0 run04_mejor_nulo_p100_e0.3
    # R-9: contexto suavizado frente a original
    ... var ~/audit_ws/khipu_out/audit/r9_contexto run04_mejor_ctxorig run04_mejor_ctxsuave
R-3 y R-12 no tienen aun comparador: la regla de lectura (ranking, s_sem, amplitud por grado) hay que fijarla ANTES de mirar sus salidas.

## Limites conocidos (sin probar contra GPU/datos de Khipu)
- Verificado aqui: bash -n de los dos sbatch, sintaxis Python, mediana de R-9 (G intacto), comparador de perfiles sobre archivos reales (autocomparacion = 0 HU).
- NO verificado: que a15 acepte `--particiones train` y `--sin-nifti` con casos sin metal (R-3/R-12/R-2) y que escriba *_perfil.csv con --sin-nifti.
  Probar primero con --test-only y con 1 caso antes de lanzar R-3/R-12.
- R-9: el filtro de mediana mezcla el valor -1000 de G con el contexto vecino en el borde de G (efecto de borde); es un diagnostico, no una correccion.
- R-3: candidatos = 27 (C contaba 30 con un filtro distinto); excluidos los que estan en el manifiesto de entrenamiento de run04.
