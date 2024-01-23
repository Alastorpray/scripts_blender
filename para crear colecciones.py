import bpy

# Obtener la colección principal de la escena actual
master_collection = bpy.context.scene.collection

for i in range(1, 16):
    # Crear una nueva colección
    new_collection = bpy.data.collections.new("Parte_" + str(i))
    
    # Vincular la nueva colección a la colección principal
    master_collection.children.link(new_collection)


#-----------------------------------------

#crea colecciones con los objetos seleccinaados y los toma como nombre
#para las colecciones y tambien vincula el objeto seleccionado con su coleccion

import bpy

# Obtener la colección principal de la escena actual
master_collection = bpy.context.scene.collection
objects = bpy.context.selected_objects

for i in objects:
    # Crear una nueva colección
    new_collection = bpy.data.collections.new(i.name)
    
    # Vincular la nueva colección a la colección principal
    master_collection.children.link(new_collection)
    
    for col in i.users_collection:
        col.objects.unlink(i)
        
    new_collection.objects.link(bpy.data.objects[i.name])