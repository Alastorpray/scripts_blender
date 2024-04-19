import bpy


bpy.ops.object.select_all(action='SELECT')

bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))


# Itera a través de cada objeto en la escena
for obj in bpy.context.scene.objects:

    # Si el objeto es un padre (tiene hijos) y no tiene un padre en sí mismo, selecciónalo
    if obj.children and not obj.parent:
        obj.select_set(True)
    else:
        obj.select_set(False)
        


bpy.context.scene.cursor.location = (0, 0, 0)

bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)
s