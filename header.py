import bpy

class NODE_MT_editor_menus(bpy.types.Menu):
    bl_idname = "NODE_MT_editor_menus"
    bl_label = ""

    def draw(self, context):
        layout = self.layout
        layout.menu("NODE_MT_view")
        layout.menu("NODE_MT_select")

        if context.space_data.tree_type == "GeometryNodeTree":
            layout.menu("NODE_MT_custom_add_menu")
        else:
            layout.menu("NODE_MT_add")

        layout.menu("NODE_MT_node")

def register():
    bpy.utils.register_class(NODE_MT_editor_menus)

def unregister():
    from bl_ui import space_node
    bpy.utils.register_class(space_node.NODE_MT_editor_menus)