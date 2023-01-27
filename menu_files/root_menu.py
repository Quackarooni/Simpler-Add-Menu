import bpy
from .__baseclasses import BaseMenu
from .basic_menus import *
from .multilevel_menus import *

from .__globals import (
    spacing,
    fetch_user_preferences,
    dir_path,
)

def draw_root_assets(layout):
    prefs = fetch_user_preferences()

    if prefs.include_nodegroups_asset:
        layout.menu_contents("NODE_MT_node_add_root_catalogs")

def is_addon_enabled(addon_id, *, aliases=None):
    is_addon_there = addon_id in bpy.context.preferences.addons.keys()
    is_any_alias_there = False

    if aliases is not None:
        for alias in aliases:
            is_any_alias_there = alias in bpy.context.preferences.addons.keys()
            if is_any_alias_there:
                break

    return (is_addon_there or is_any_alias_there)

def append_addon_menus(addons):
    def draw(self, context):
        layout = self.layout        

        enabled_addon_menus = {addon:items for addon, items 
            in addons.items() if is_addon_enabled(addon, aliases=items["aliases"])}

        if len(enabled_addon_menus) == 0:
            return

        layout.separator(factor=spacing)
        for items in enabled_addon_menus.values():
            if hasattr(bpy.types, items["menu_id"]):
                layout.menu(items["menu_id"], text=items["text"], icon=items["icon"])            

    addon_draw_funcs.append(draw)
    bpy.types.NODE_MT_custom_add_menu.append(draw)
    return draw

class NODE_MT_custom_add_menu(BaseMenu):
    bl_label = "Add"
    bl_idname = "NODE_MT_custom_add_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'

        props = layout.operator("node.add_search", text="Search...", icon='VIEWZOOM')
        props.use_transform = True
        layout.separator(factor=spacing)

        layout.menu(NODE_MT_custom_add_menu_attribute.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_input.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_output.bl_idname)
        layout.separator(factor=spacing)

        layout.menu(NODE_MT_custom_add_menu_geometry.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_mesh.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_curve.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_instance.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_point.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_volume.bl_idname)
        layout.separator(factor=spacing)
        
        layout.menu(NODE_MT_custom_add_menu_material.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_texture.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_utilities.bl_idname)
        
        layout.menu(NODE_MT_custom_add_menu_UV.bl_idname)
        layout.separator(factor=spacing)
        layout.menu(NODE_MT_custom_add_menu_group.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_layout.bl_idname)
        draw_root_assets(layout)

classes = (
        NODE_MT_custom_add_menu,
        )

addon_draw_funcs = []

def register():  
    for cls in classes:
        bpy.utils.register_class(cls)

    with open(dir_path / "addon_menus.json", "r") as f:
        addon_menus = json.loads(f.read())

    append_addon_menus(addon_menus)

def unregister():
    for draw_func in addon_draw_funcs:
        bpy.types.NODE_MT_custom_add_menu.remove(draw_func)

    for cls in classes:
        bpy.utils.unregister_class(cls)