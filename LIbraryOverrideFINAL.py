#ESTE SCRIPT ES PARA PREDECIR EL NOMBRE DE LA SIGUIENTE COLECCIÓN QUE SE VA A CREAR EN LA ESCENA
import bpy
import re

# Coloca aquí el nombre base de las colecciones que deseas buscar.
#nombre_primario = bpy.context.collection.name

coll_names = bpy.data.collections

for i in coll_names:
    nombre_base = i.split('.')[0]

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



#----------------------------------------------------------------------------

#funcion recursica para seleccionar objetos de una coleccion y sus subcolecciones y hacerlos single user

import bpy

def sel_coll_objects(lista_nombres_colecciones):
    """
    Selecciona todos los objetos en las colecciones y sus subcolecciones proporcionadas en la lista.

    Args:
    lista_nombres_colecciones (list): Lista de nombres de las colecciones cuyos objetos se van a seleccionar.
    """
    def seleccionar_objetos_coleccion(coleccion):
        """Función auxiliar para seleccionar objetos de una colección."""
        for obj in coleccion.objects:
            obj.select_set(True)
        for subcol in coleccion.children:
            seleccionar_objetos_coleccion(subcol)

    # Deselecciona todos los objetos primero.
    bpy.ops.object.select_all(action='DESELECT')

    # Flag para verificar si se encontró alguna colección.
    coleccion_encontrada = False

    # Itera sobre la lista de nombres de colecciones y selecciona los objetos.
    for nombre_coleccion in lista_nombres_colecciones:
        coleccion = bpy.data.collections.get(nombre_coleccion)
        if coleccion:
            coleccion_encontrada = True
            seleccionar_objetos_coleccion(coleccion)
            bpy.ops.object.make_single_user(object=False, obdata=False, material=True, animation=False, obdata_animation=False)


    # Actualiza la vista 3D para reflejar la selección.
    bpy.context.view_layer.update()

    if coleccion_encontrada:
        print(f"Objetos de las colecciones y subcolecciones en la lista seleccionados.")
    else:
        print(f"No se encontraron colecciones en la lista proporcionada.")

# Llamada a la función con una lista de nombres de colecciones.
# Reemplaza los siguientes nombres con los nombres reales de tus colecciones.


nombres_colecciones = ['Amazed Chatbot', 'Lampara', 'Lampara.001', 'Amazed Chatbot.001', 'Lampara.002','Cubon']
sel_coll_objects(nombres_colecciones)



#-----------------------------------------------------
#script para predecir nombres de las colecciones que se van a crear en la escena si necesidad
# de convertilos en library override


import bpy
import re

# Función para obtener el próximo número de colección disponible.
def get_next_collection_number(base_name, existing_collections):
    # Encuentra todos los números existentes para el nombre base dado.
    number_pattern = re.compile(rf"{re.escape(base_name)}\.(\d+)")
    existing_numbers = [int(match.group(1)) for coll in existing_collections 
                        for match in [number_pattern.search(coll.name)] if match]
    if existing_numbers:
        # Retorna el próximo número en la secuencia.
        return max(existing_numbers) + 1
    else:
        # Si no hay números existentes, comienza desde 1.
        return 1

# Obtiene los nombres base de los objetos seleccionados.
selected_objects = bpy.context.selected_objects
base_names = {obj.name.rsplit('.', 1)[0] for obj in selected_objects if '.' in obj.name}

# Obtiene todas las colecciones existentes en la escena.
existing_collections = bpy.data.collections

# Diccionario para almacenar el próximo número de colección para cada nombre base.
next_collection_numbers = {}

# Calcula el próximo número de colección para cada nombre base.
for base_name in base_names:
    next_collection_numbers[base_name] = get_next_collection_number(base_name, existing_collections)

# Genera y muestra los nombres de las próximas colecciones.
for base_name, next_num in next_collection_numbers.items():
    for i in range(next_num, next_num + len([obj for obj in selected_objects if obj.name.startswith(base_name)])):
        print(f"El nombre de la próxima colección para '{base_name}' debe ser: {base_name}.{str(i).zfill(3)}")


#--------------------------------------------------------------

import bpy

def get_base_name(name):
    """Extrae el nombre base de un objeto."""
    if '.' in name:
        return name.rsplit('.', 1)[0]
    return name

def next_collection_name(name):
    """Encuentra el próximo nombre de colección disponible."""
    i = 1
    new_name = f"{name}.{str(i).zfill(3)}"
    while new_name in bpy.data.collections and collection_in_outliner(new_name):
        i += 1
        new_name = f"{name}.{str(i).zfill(3)}"
    return new_name

def collection_in_outliner(name):
    """Verifica si una colección está en el Outliner (vinculada a la escena)."""
    return name in bpy.context.scene.collection.children

def predict_collection_name_for_selected_objects():
    """Imprime el nombre base o la predicción para objetos seleccionados."""
    for obj in bpy.context.selected_objects:
        base_name = get_base_name(obj.name)
        # Si el nombre base no existe como colección o no está en el Outliner, imprime el nombre base
        if base_name not in bpy.data.collections or not collection_in_outliner(base_name):
            print(f"Nombre de colección: {base_name}")
        # Si el nombre base existe y está en el Outliner, encuentra el siguiente nombre disponible
        else:
            predicted_name = next_collection_name(base_name)
            print(f"Nombre de colección predicha: {predicted_name}")

# Ejecutar la función
predict_collection_name_for_selected_objects()


#------------------FORMA MUCHO MAS OPTIMIZADA DE PREDECIR LOS NOMBRES
# DE LAS COLECCIONES A CREARSE EN LA ESCENA--------------------------
#aqui trabajamos con una lista de nombres base y consultamos si existen en la escena
import bpy

def get_base_name(name):
    """Extrae el nombre base de un objeto."""
    return name.split('.')[0] if '.' in name else name

def next_collection_name(name):
    """Encuentra el próximo nombre de colección disponible."""
    i = 1
    new_name = f"{name}.{str(i).zfill(3)}"
    while new_name in bpy.data.collections and new_name in bpy.context.scene.collection.children:
        i += 1
        new_name = f"{name}.{str(i).zfill(3)}"
    return new_name

def predict_collection_name_for_base_names(base_names):
    """Imprime el nombre base o la predicción para una lista de nombres base."""
    for base_name in base_names:
        if base_name not in bpy.data.collections or base_name not in bpy.context.scene.collection.children:
            print(f"Nombre de colección: {base_name}")
        else:
            predicted_name = next_collection_name(base_name)
            print(f"Nombre de colección predicha: {predicted_name}")

# Lista para almacenar los nombres base de los objetos seleccionados
base_names = [get_base_name(obj.name) for obj in bpy.context.selected_objects]

# Ejecutar la función con la lista de nombres base
predict_collection_name_for_base_names(base_names)
