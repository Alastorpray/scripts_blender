



import os
import pandas as pd
from natsort import natsorted, ns

# Directorio donde se encuentran los archivos .glb
directory = 'C:/Users/Nevan/Desktop/FIles Pixcap/'

# Obtener lista de archivos .glb en el directorio
files = natsorted([file for file in os.scandir(directory) if file.name.endswith('.glb')], key=lambda x: x.name)

# Crear una lista de tuplas con el número y el nombre de cada archivo
archivos = [(i+1, os.path.splitext(file.name)[0]) for i, file in enumerate(files)]

# Crear un Dataframe con los nombres de los archivos y la numeración
df = pd.DataFrame(archivos, columns=['Número', 'Nombres'])

# Guardar el Dataframe en un archivo .xlsx
df.to_excel('archivos.xlsx', engine='openpyxl', index=False)