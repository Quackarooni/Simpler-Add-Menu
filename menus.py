import bpy
from .menu_files import basic_menus, multilevel_menus, root_menu

class NODE_OT_INVOKE_MENU(bpy.types.Operator):
    bl_label = "Invoke Custom Add Menu"
    bl_idname = "custom_add_menu.invoke_menu"
    bl_description = "Calls the custom add menu when in Geometry Node Editor"
    bl_options = {'INTERNAL'}

    @classmethod
    def poll(cls, context):
        return context.space_data.type == 'NODE_EDITOR'

    def execute(self, context):
        wm = bpy.ops.wm

        if context.space_data.tree_type == "GeometryNodeTree":
            wm.call_menu(name="NODE_MT_custom_add_menu")
        else:
            wm.call_menu(name="NODE_MT_add")

        return {'CANCELLED'}

addon_keymaps = []

def register():
    root_menu.register()
    basic_menus.register()
    multilevel_menus.register()

    bpy.utils.register_class(NODE_OT_INVOKE_MENU)

    if key_config := bpy.context.window_manager.keyconfigs.addon:
        key_map = key_config.keymaps.new(name='Node Editor', space_type="NODE_EDITOR")
        key_entry = key_map.keymap_items.new(
            NODE_OT_INVOKE_MENU.bl_idname, 'A', value='PRESS', shift=True)
        addon_keymaps.append((key_map, key_entry))

def unregister():
    multilevel_menus.unregister()
    basic_menus.unregister()
    root_menu.unregister()

    for key_map, key_entry in addon_keymaps:
        key_map.keymap_items.remove(key_entry)
    addon_keymaps.clear()

    bpy.utils.unregister_class(NODE_OT_INVOKE_MENU)