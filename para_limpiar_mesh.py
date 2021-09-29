import bpy

bpy.ops.object.editmode_toggle()

for i in range(20):
    bpy.ops.mesh.remove_doubles()

bpy.ops.mesh.tris_convert_to_quads()
bpy.ops.object.mode_set()
bpy.ops.object.clear_normals()
