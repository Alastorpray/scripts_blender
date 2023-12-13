import bpy
#Esto es para blender
# El nombre de la colección vinculada

#obj = bpy.context.active_object.name
linked_collection_name = bpy.context.active_object.name

# Intenta obtener la colección vinculada
linked_collection = bpy.data.collections.get(linked_collection_name)

if linked_collection and linked_collection.library:
    # La colección es un enlace, así que vamos a iterar a través de los objetos que contiene
    for obj in linked_collection.objects:
        # Imprime la información de cada objeto
        print(f"Objeto: {obj.library}, Tipo de Dato: {obj.type}")
        # Si necesitas acceder a más propiedades específicas, puedes hacerlo aquí
else:
    print(f"No se encontró una colección vinculada con el nombre '{linked_collection_name}', o no es una colección vinculada.")
