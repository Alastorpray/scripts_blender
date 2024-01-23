import bpy



#funcion en ciclo para convertir en override los objetos seleccionados

objs = bpy.context.selected_objects

for obj in objs:
    # Deselecciona todos los objetos en la vista actual
    bpy.ops.object.select_all(action='DESELECT')
    # Asegura que el contexto está correctamente establecido para el objeto
    bpy.context.view_layer.objects.active = obj
    # Selecciona solo el objeto actual
    obj.select_set(True)
    # Crea el Library Override para el objeto seleccionado
    bpy.ops.object.make_override_library()

#-----------------------------------------------------------------------------

import bpy

# Función recursiva para imprimir nombres de objetos en una colección y sus subcolecciones
def imprimir_nombres_de_objetos(coleccion):
    for objeto in coleccion.objects:
        print(objeto.name)

    for subcoleccion in coleccion.children:
        imprimir_nombres_de_objetos(subcoleccion)

# Nombre de la colección principal que deseas imprimir
nombre_coleccion_principal = "objeto"

# Obtiene la colección principal por su nombre
coleccion_principal = bpy.data.collections.get(nombre_coleccion_principal)

if coleccion_principal:
    imprimir_nombres_de_objetos(coleccion_principal)
else:
    print(f"No se encontró la colección llamada {nombre_coleccion_principal}")

#-----------------------------------------------------------------------------


