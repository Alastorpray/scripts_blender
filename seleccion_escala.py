import bpy
import math

# Des-selecciona todos los objetos
bpy.ops.object.select_all(action='DESELECT')


obj = bpy.context.visible_objects
# Recorre todos los objetos en la escena
for i in obj:
    if i.scale.x != 1:
        i.select_set(True)
    elif i.scale.y != 1:
        i.select_set(True)
    elif i.scale.z != 1:
        i.select_set(True)