import bpy
from bpy.types import UIList, Operator, Panel


class LocationRotationItem(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty()
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


class LocationRotationList(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.prop(item, "name", text="", emboss=False, icon_value=icon)
            layout.prop(item, "location", text="")
            layout.prop(item, "rotation", text="")
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=icon)

    def invoke(self, context, event):
        pass

    def filter_items(self, context, data, propname):
        return


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
        row.template_list("LocationRotationList", "", obj, "location_rotation_group", obj, "location_rotation_group_index")
        col = row.column(align=True)
        col.operator("object.add_location_rotation_item", text="", icon="ADD")
        col.operator("object.remove_location_rotation_item", text="", icon="REMOVE")

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        pass


class AddLocationRotationItem(Operator):
    bl_idname = "object.add_location_rotation_item"
    bl_label = "Add Location / Rotation"
    bl_description = "Add a new Location / Rotation to the group"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.object
        item = obj.location_rotation_group.add()
        item.name = "Location / Rotation {}".format(len(obj.location_rotation_group))

        item.location = obj.location.copy()
        item.rotation = obj.rotation_euler.copy()

        return {'FINISHED'}


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


def register():
    bpy.utils.register_class(LocationRotationItem)
    bpy.utils.register_class(LocationRotationList)
    bpy.utils.register_class(LocationRotationPanel)
    bpy.utils.register_class(AddLocationRotationItem)
    bpy.utils.register_class(RemoveLocationRotationItem)

    bpy.types.Object.location_rotation_group = bpy.props.CollectionProperty(type=LocationRotationItem)
    bpy.types.Object.location_rotation_group_index = bpy.props.IntProperty(default=0)

def unregister():
    bpy.utils.unregister_class(LocationRotationItem)
    bpy.utils.unregister_class(LocationRotationList)
    bpy.utils.unregister_class(LocationRotationPanel)
    bpy.utils.unregister_class(AddLocationRotationItem)
    bpy.utils.unregister_class(RemoveLocationRotationItem)

    del bpy.types.Object.location_rotation_group
    del bpy.types.Object.location_rotation_group_index

if __name__ == "__main__":
    register()
