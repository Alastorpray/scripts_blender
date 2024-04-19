import bpy

def mostrar_y_seleccionar_objetos(coleccion, view_layer, nombres_objetos):
    """ Hace visibles las colecciones en el viewport y selecciona todos sus objetos. """
    coleccion.hide_viewport = False
    for obj in coleccion.objects:
        # Solo seleccionar si el objeto está en la capa de visualización actual
        if obj.name in view_layer.objects and obj.library:
            nombres_objetos.append(obj.name)  # Guardar el nombre del objeto
            view_layer.objects[obj.name].select_set(True)
    for subcoleccion in coleccion.children:
        mostrar_y_seleccionar_objetos(subcoleccion, view_layer, nombres_objetos)

# Asumimos que el objeto activo es un objeto vinculado que puede contener varios objetos o colecciones.
objeto_vinculado = bpy.context.active_object
view_layer = bpy.context.view_layer
nombres_objetos = []  # Lista para almacenar los nombres de los objetos

# Verifica si el objeto activo es de hecho un objeto vinculado
if objeto_vinculado and objeto_vinculado.instance_type == 'COLLECTION' and objeto_vinculado.instance_collection:
    # La colección vinculada del objeto seleccionado
    coleccion_vinculada = objeto_vinculado.instance_collection
    
    # Deselecciona todos los objetos primero para evitar conflictos
    bpy.ops.object.select_all(action='DESELECT')
    
    # Hacer visibles las colecciones en el viewport y seleccionar todos sus objetos
    mostrar_y_seleccionar_objetos(coleccion_vinculada, view_layer, nombres_objetos)
    
    # Asegurarse de que la vista 3D esté en modo 'OBJECT' para evitar errores
    if bpy.context.object and bpy.context.object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    
    # Aplicar library override en los objetos seleccionados
    bpy.ops.object.make_override_library()
    
    # Aplicar 'make_single_user' para los materiales de los objetos seleccionados
    bpy.ops.object.make_single_user(object=False, obdata=False, material=True, animation=False, obdata_animation=False)
    
    print("Library override y make_single_user aplicados a todos los objetos vinculados seleccionados.")
    print("Nombres de los objetos procesados:", nombres_objetos)
else:
    print("El objeto seleccionado no es un objeto vinculado de una colección.")
