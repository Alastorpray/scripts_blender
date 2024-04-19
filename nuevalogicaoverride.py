#obtenemos el nombre de la coleccion mas alta + 1
#En este caso tenemos que tener una coleccion activa para tomar el nombre
#Si no hay ninguna coleccion activa, no se puede ejecutar el script


import bpy
import re

# Coloca aquí el nombre base de las colecciones que deseas buscar.
nombre_primario = bpy.context.collection.name
nombre_base = bpy.context.collection.name.split('.')[0]

# Compilamos una expresión regular que encuentra los números al final de los nombres.
number_pattern = re.compile(fr"{re.escape(nombre_base)}\.(\d+)$")

# Lista para almacenar los números encontrados.
numbers_found = []

# Iteramos sobre todas las colecciones en la escena.
for coll in bpy.data.collections:
    match = number_pattern.search(coll.name)
    if match:
        # Añadimos el número encontrado a la lista.
        numbers_found.append(int(match.group(1)))

# Encontramos el número más alto si hay números en la lista y le sumamos 1.
if numbers_found:
    next_number = max(numbers_found) + 1
    new_collection_name = f"{nombre_base}.{str(next_number).zfill(3)}"
    print(f"El nombre de la próxima colección debe ser: {new_collection_name}")
else:
    # Si no se encontraron colecciones con el nombre base y numeración, comenzamos desde 001.
    new_collection_name = f"{nombre_base}.001"
    print(f"No se encontraron colecciones con numeración. El nombre de la próxima colección debe ser: {new_collection_name}")
