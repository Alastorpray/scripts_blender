import bpy

def imprimir_objetos_de_coleccion_y_hacer_single_user(coleccion, view_layer, objetos_para_single_user):
    for obj in coleccion.objects:
        print(f"Objeto: {obj.name}, Tipo de Dato: {obj.type}")
        if obj.name in view_layer.objects and obj.library:
            objetos_para_single_user.append(obj)  # Agregar objeto a la lista
            view_layer.objects[obj.name].select_set(True)  # Seleccionar el objeto para el override

    for subcoleccion in coleccion.children:
        print(f"Subcolección: {subcoleccion.name}")
        imprimir_objetos_de_coleccion_y_hacer_single_user(subcoleccion, view_layer, objetos_para_single_user)

# El nombre de la colección principal
nombre_coleccion_principal = bpy.context.active_object.name

# Intenta obtener la colección principal
coleccion_principal = bpy.data.collections.get(nombre_coleccion_principal)

if coleccion_principal:
    objetos_para_single_user = []  # Lista para almacenar objetos para hacer single user
    view_layer = bpy.context.view_layer  # Capa de visualización actual

    # Imprimir objetos de la colección y seleccionarlos para el override
    imprimir_objetos_de_coleccion_y_hacer_single_user(coleccion_principal, view_layer, objetos_para_single_user)
    
    # Asegúrate de que la vista 3D esté en modo 'OBJECT'
    if bpy.context.object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')

    # Aplicar library override en los objetos seleccionados
    bpy.ops.object.make_override_library()

    # Deselecciona todos los objetos antes de aplicar single user
    bpy.ops.object.select_all(action='DESELECT')

    # Seleccionar objetos específicos para aplicar single user
    for obj in objetos_para_single_user:
        obj.select_set(True)
    imprimir_objetos_de_coleccion_y_hacer_single_user(coleccion_principal, view_layer, objetos_para_single_user)
    # Aplicar 'make_single_user' para los materiales de los objetos seleccionados
    bpy.ops.object.make_single_user(type='SELECTED_OBJECTS', object=False, obdata=False, material=True, animation=False)

    print(f"Library override y single user aplicados a objetos en la colección '{nombre_coleccion_principal}'.")
else:
    print(f"No se encontró una colección con el nombre '{nombre_coleccion_principal}'.")
