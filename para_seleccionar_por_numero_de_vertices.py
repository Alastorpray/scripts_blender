import bpy

obj = bpy.data.objects

active_object = bpy.context.view_layer.objects.active # tomamos informacion del objeto activo
active_verts = len(active_object.data.polygons) #tomamos el numero de polygonos del objeto activo

for i in obj:
    if i.type == 'MESH': #solo si es tipo MESH podra entrar a la validacion
        facescount = len(bpy.data.objects[i.name].data.polygons)
        if facescount == active_verts:
            i.select_set(state = True)
        






#en modo objeto


#----------------------------------
# for all_objects in  bpy.context.view_layer.objects:
#     if all_objects.type == 'MESH':
#         all_objects_verts = len(all_objects.data.vertices)           
#         if all_objects_verts == 12:
#             all_objects.select_set(state = True)
        
            
      
      
#en modo edicion
            
#import bpy, bmesh

# vertCount = 6 # <-- Faces with this amount of verts will be selected

# bpy.ops.object.mode_set( mode = 'EDIT' )
# bm = bmesh.from_edit_mesh( bpy.context.object.data )

# bpy.ops.mesh.select_mode( type = 'FACE' )
# bpy.ops.mesh.select_all( action = 'DESELECT' )

# for f in bm.faces: 
#     if len( f.verts ) == vertCount: 
#         f.select = True

# bm.select_flush(True)