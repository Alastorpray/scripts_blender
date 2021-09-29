# import bpy

# obj = bpy.data.objects #nombres

# for i in obj:
#     if len(bpy.data.objects.get(i.name).data.polygons) == 1476:
#         i.select_set(True)

        



import bpy


val = bpy.data.objects

for i in val:
    if "Cube" in i.name:
        i.select_set(True)
        #bpy.context.active_object.hide_set(True)
        





        

