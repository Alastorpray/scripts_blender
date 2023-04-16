import bpy

# Establece como nombre el layer activo, generalmente donde se encuentran los objetos 3d
active_collection = bpy.context.view_layer.active_layer_collection.collection.name


filepath = "I:/exporttest/" + active_collection + ".glb"


# Exportar los objetos en formato .glb
bpy.ops.export_scene.gltf(filepath=filepath, export_format="GLB", use_selection=True, export_draco_mesh_compression_enable=True,
export_draco_mesh_compression_level=6, export_draco_position_quantization=14, export_draco_normal_quantization=10, export_draco_texcoord_quantization=12, export_draco_color_quantization=10, export_draco_generic_quantization=12,
export_tangents=False, export_materials='EXPORT', export_animations=False)