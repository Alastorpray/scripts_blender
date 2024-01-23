
import bpy

def imprimir_objetos_de_coleccion(coleccion):
    print(f"Nombre de la Colección: {coleccion.name}, hide_viewport: {coleccion.hide_viewport}")
    
    # Hacer los objetos y datos únicos (si es necesario)
    

    for obj in coleccion.objects:
        print(f"  Objeto: {obj.name}, Tipo de Dato: {obj.type}")
        #obj.select_set(True)  # Selecciona el objeto

    for subcoleccion in coleccion.children:
        print(f"  Subcolección: {subcoleccion.name}, hide_viewport: {subcoleccion.hide_viewport}")
        subcoleccion.hide_viewport = False
        print(f"    ¡Se cambió hide_viewport de {subcoleccion.name} a False!")
        seleccionar_objetos_de_subcoleccion(subcoleccion)
        imprimir_objetos_de_coleccion(subcoleccion)
        
        
def seleccionar_objetos_de_subcoleccion(subcoleccion):
    for obj in subcoleccion.objects:
        

        obj.select_set(True)  # Selecciona el objeto
        
    for subcoleccion_hija in subcoleccion.children:
        seleccionar_objetos_de_subcoleccion(subcoleccion_hija)  # Recursividad para subcolecciones anidadas
        
        

# Obtener el nombre de la colección desde el objeto activo (si existe y es parte de una colección)
objeto_activo = bpy.context.active_object
nombre_coleccion_principal = objeto_activo.users_collection[0].name if objeto_activo and objeto_activo.users_collection else None

# Intenta obtener la colección principal
coleccion_principal = bpy.data.collections.get(nombre_coleccion_principal)
bpy.ops.object.make_override_library()



if coleccion_principal:
    imprimir_objetos_de_coleccion(coleccion_principal)
    bpy.ops.object.make_single_user(object=True, obdata=True, material=True, animation=False)
    bpy.ops.object.select_all(action='DESELECT')
else:
    print(f"No se encontró una colección con el nombre '{nombre_coleccion_principal}'.")

# Nota: Removí la línea bpy.ops.object.make_override_library() ya que su propósito no estaba claro en el contexto del script.
