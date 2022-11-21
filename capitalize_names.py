import bpy

obj = bpy.context.selected_objects

for i in obj:
    i.name = i.name.capitalize()
print("done")

#selecciona todos los objetos que quieras y luego ejecuta el script para volver mayusculas
#todas las primeras letras
