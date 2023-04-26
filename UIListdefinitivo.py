import bpy
from bpy.types import UIList, Operator, Panel

# Define la estructura de datos de un elemento de ubicación y rotación
class LocationRotationItem(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty()
    description: bpy.props.StringProperty()
    location: bpy.props.FloatVectorProperty(
        name="Location",
        size=3,
        subtype='TRANSLATION'
    )
    rotation: bpy.props.FloatVectorProperty(
        name="Rotation",
        size=3,
        subtype='EULER'
    )

# Función de actualización que se ejecuta cuando se selecciona un elemento en la lista
def update_object_transform(self, context):
    if self.location_rotation_group:
        selected_item = self.location_rotation_group[self.location_rotation_group_index]
        self.location = selected_item.location
        self.rotation_euler = selected_item.rotation

# Personaliza la apariencia de los elementos de la lista UIList
class LocationRotationList(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            row = layout.row()
            row.label(text="", icon='OUTLINER_OB_EMPTY')  # Añade un ícono de empty al lado izquierdo del nombre
            row.prop(item, "name", text="", emboss=False)
            row.label(text=item.description)
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=icon)

# Crea un panel en la vista 3D para mostrar la lista y las operaciones relacionadas
class LocationRotationPanel(Panel):
    bl_label = "Location Rotation Group"
    bl_idname = "VIEW3D_PT_location_rotation_group"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "mypanel"
    bl_context = "objectmode"

    def draw(self, context):
        obj = context.object
        layout = self.layout
        row = layout.row()

        # Muestra la lista de elementos de ubicación y rotación
        row.template_list("LocationRotationList", "", obj, "location_rotation_group", obj, "location_rotation_group_index")

        # Muestra los botones para agregar y eliminar elementos de la lista
        col = row.column(align=True)
        col.operator("object.add_location_rotation_item", text="", icon="ADD")
        col.operator("object.remove_location_rotation_item", text="", icon="REMOVE")

        # Muestra las propiedades de ubicación y rotación del elemento seleccionado debajo de la lista
        if obj.location_rotation_group:
            index = obj.location_rotation_group_index
            selected_item = obj.location_rotation_group[index]

            box = layout.box()
            box.prop(selected_item, "location")
            box.prop(selected_item, "rotation")

# Define el operador para agregar un nuevo elemento de ubicación y rotación a la lista
class AddLocationRotationItem(Operator):
    bl_idname = "object.add_location_rotation_item"
    bl_label = "Add Location / Rotation"
    bl_description = "Add a new Location / Rotation to the group"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.object
        item = obj.location_rotation_group.add()
        item.name = "pos {}".format(len(obj.location_rotation_group))

        item.location = obj.location.copy()
        item.rotation = obj.rotation_euler
        item.location = obj.location.copy()
        item.rotation = obj.rotation_euler.copy()

        if len(obj.location_rotation_group) == 1:
            item.description = "Main"
        else:
            item.description = "Sub"

        return {'FINISHED'}

# Define el operador para eliminar un elemento de ubicación y rotación seleccionado de la lista
class RemoveLocationRotationItem(Operator):
    bl_idname = "object.remove_location_rotation_item"
    bl_label = "Remove Location / Rotation"
    bl_description = "Remove the selected Location / Rotation from the group"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        obj = context.object
        group = obj.location_rotation_group
        index = obj.location_rotation_group_index
        group.remove(index)
        obj.location_rotation_group_index = min(index, len(group) - 1)
        return {'FINISHED'}

# Función para registrar todas las clases y propiedades en Blender
def register():
    bpy.utils.register_class(LocationRotationItem)
    bpy.utils.register_class(LocationRotationList)
    bpy.utils.register_class(LocationRotationPanel)
    bpy.utils.register_class(AddLocationRotationItem)
    bpy.utils.register_class(RemoveLocationRotationItem)

    bpy.types.Object.location_rotation_group = bpy.props.CollectionProperty(type=LocationRotationItem)
    bpy.types.Object.location_rotation_group_index = bpy.props.IntProperty(default=0, update=update_object_transform)

# Función para desregistrar todas las clases y propiedades en Blender
def unregister():
    bpy.utils.unregister_class(LocationRotationItem)
    bpy.utils.unregister_class(LocationRotationList)
    bpy.utils.unregister_class(LocationRotationPanel)
    bpy.utils.unregister_class(AddLocationRotationItem)
    bpy.utils.unregister_class(RemoveLocationRotationItem)

    del bpy.types.Object.location_rotation_group
    del bpy.types.Object.location_rotation_group_index

# Llama a la función de registro cuando se ejecuta el script
if __name__ == "__main__":
    register()
