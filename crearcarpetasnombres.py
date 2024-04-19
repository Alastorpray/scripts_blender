import os
from pathlib import Path

# Ruta de la carpeta seleccionada
carpeta_seleccionada = r"/Volumes/Work/Work 2024/Pixcap/Contribuitors/Mockups/Third Batch/5 Kitchen accesories/GLB Kitchen 3"


# Crea una instancia de Path para la carpeta seleccionada
path_seleccionado = Path(carpeta_seleccionada)

# Itera sobre cada archivo en la carpeta seleccionada (ignorando subcarpetas)
for archivo in path_seleccionado.iterdir():
    if archivo.is_file() and archivo.suffix == '.glb':  # Verifica que sea un archivo .glb
        # Construye la ruta de la nueva carpeta basada en el nombre del archivo (sin la extensión)
        nueva_carpeta = path_seleccionado / archivo.stem
        
        # Crea la carpeta si no existe
        nueva_carpeta.mkdir(exist_ok=True)
        
        # Construye la nueva ruta del archivo dentro de su carpeta
        nueva_ruta_archivo = nueva_carpeta / archivo.name
        
        # Mueve el archivo a la nueva carpeta
        archivo.rename(nueva_ruta_archivo)
        print(f"Archivo '{archivo.name}' movido a '{nueva_carpeta}'")

