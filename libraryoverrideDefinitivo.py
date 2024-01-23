import bpy

def guardar_estado_inicial(coleccion):
    """ Guarda el estado inicial de hide_viewport de una colección y sus subcolecciones. """
    estado_inicial_hide_viewport[coleccion.name] = coleccion.hide_viewport
    for subcoleccion in coleccion.children:
        guardar_estado_inicial(subcoleccion)

def mostrar_y_seleccionar_coleccion(coleccion):
    """ Muestra y selecciona una colección y sus subcolecciones. """
    coleccion.hide_viewport = False
    for objeto in coleccion.objects:
        objeto.select_set(True)  # Selecciona el objeto
        bpy.context.view_layer.objects.active = objeto  # Establece el objeto como activo
    for subcoleccion in coleccion.children:
        mostrar_y_seleccionar_coleccion(subcoleccion)

# Identificar colecciones existentes
old_colls = bpy.data.collections
var_old_colls = [i.name for i in old_colls]

# Realizar operaciones en objetos seleccionados (ejemplo: crear Library Overrides)
objs = bpy.context.selected_objects
for obj in objs:
    bpy.ops.object.select_all(action='DESELECT')  # Deselecciona todos los objetos
    bpy.context.view_layer.objects.active = obj  # Activa el objeto
    obj.select_set(True)  # Selecciona el objeto
    bpy.ops.object.make_override_library()  # Crea el Library Override

# Guardar el estado inicial de hide_viewport de todas las colecciones
estado_inicial_hide_viewport = {}
for coleccion in bpy.data.collections:
    guardar_estado_inicial(coleccion)


# Identificar nuevas colecciones creadas
colleciones_despues_del_script = bpy.data.collections
var_colls_despues_script = [i.name for i in colleciones_despues_del_script]
nuevas_collecciones = [nombre for nombre in var_colls_despues_script if nombre not in var_old_colls]

# Mostrar y seleccionar las nuevas colecciones y sus subcolecciones
bpy.ops.object.select_all(action='DESELECT')  # Deselecciona todos los objetos antes de comenzar
for nombre_coleccion in nuevas_collecciones:
    coleccion_principal = bpy.data.collections.get(nombre_coleccion)
    if coleccion_principal:
        mostrar_y_seleccionar_coleccion(coleccion_principal)
        # Aquí puedes añadir más operaciones como aplicar single user material
        bpy.ops.object.make_single_user(type='SELECTED_OBJECTS', object=False, obdata=False, material=True, animation=False)

# Restaurar el estado original de hide_viewport para todas las colecciones
for coleccion in bpy.data.collections:
    coleccion.hide_viewport = estado_inicial_hide_viewport.get(coleccion.name, False)

print("Se ha restaurado el estado original de hide_viewport para todas las colecciones.")






#---------------------------------------------------------------
#Script definitivo actualizado
import bpy

# Función para almacenar los nombres de la colección y sus subcolecciones recursivamente
def almacenar_nombres_colecciones(coleccion, nombres_colecciones):
    nombres_colecciones.append(coleccion.name)
    for subcoleccion in coleccion.children:
        almacenar_nombres_colecciones(subcoleccion, nombres_colecciones)

# Función para mostrar y seleccionar una colección y sus subcolecciones
def mostrar_y_seleccionar_coleccion(coleccion):
    coleccion.hide_viewport = False
    for objeto in coleccion.objects:
        objeto.select_set(True)  # Selecciona el objeto
        bpy.context.view_layer.objects.active = objeto  # Establece el objeto como activo
    for subcoleccion in coleccion.children:
        mostrar_y_seleccionar_coleccion(subcoleccion)

# Guardar el estado inicial de hide_viewport de todas las colecciones y almacenar nombres
estado_inicial_hide_viewport = {}
nombres_colecciones_antes = []
almacenar_nombres_colecciones(bpy.context.scene.collection, nombres_colecciones_antes)

# Realizar operaciones en objetos seleccionados (ejemplo: crear Library Overrides)
objs = bpy.context.selected_objects
for obj in objs:
    bpy.ops.object.select_all(action='DESELECT')  # Deselecciona todos los objetos
    bpy.context.view_layer.objects.active = obj  # Activa el objeto
    obj.select_set(True)  # Selecciona el objeto
    bpy.ops.object.make_override_library()  # Crea el Library Override

# Guardar el estado inicial de hide_viewport de todas las colecciones
for coleccion in bpy.data.collections:
    estado_inicial_hide_viewport[coleccion.name] = coleccion.hide_viewport

# Identificar nuevas colecciones creadas
nombres_colecciones_despues = []
almacenar_nombres_colecciones(bpy.context.scene.collection, nombres_colecciones_despues)
nuevas_colecciones = [nombre for nombre in nombres_colecciones_despues if nombre not in nombres_colecciones_antes]

# Mostrar y seleccionar las nuevas colecciones y sus subcolecciones
bpy.ops.object.select_all(action='DESELECT')  # Deselecciona todos los objetos antes de comenzar
for nombre_coleccion in nuevas_colecciones:
    coleccion_principal = bpy.data.collections.get(nombre_coleccion)
    if coleccion_principal:
        mostrar_y_seleccionar_coleccion(coleccion_principal)
        bpy.ops.object.make_single_user(type='SELECTED_OBJECTS', object=False, obdata=False, material=True, animation=False)

# Restaurar el estado original de hide_viewport para todas las colecciones
for coleccion in bpy.data.collections:
    coleccion.hide_viewport = estado_inicial_hide_viewport.get(coleccion.name, coleccion.hide_viewport)

# Imprimir resultados
print("Nombres de colecciones antes del script:", nombres_colecciones_antes)
print("Nombres de colecciones después del script:", nombres_colecciones_despues)
print("Nuevas colecciones creadas:", nuevas_colecciones)
print("Se ha restaurado el estado original de hide_viewport para todas las colecciones.")
