import bpy

val = bpy.context.selected_objects#

for i in val:
    i.name = i.name.replace("joder", "whats")




#bpy.context.object.name = bpy.context.object.name.replace("joder", "whats")