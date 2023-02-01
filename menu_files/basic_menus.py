import bpy
import json
from pathlib import Path
from bl_ui import node_add_menu

from .__baseclasses import BaseMenu
from .__globals import (
    draw_assets_for_catalog,
    dir_path
)

class NODE_MT_custom_add_menu_group(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_group"
    bl_label = "Group"

    def draw(self, context):
        layout = self.layout
        node_add_menu.draw_node_group_add_menu(context, layout)
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)

def generate_basic_menu(idname, props):
    props["bl_idname"] = idname
    menu_class = type(idname,(BaseMenu,), props)
    return menu_class

generated_menus = []

def register():
    bpy.utils.register_class(NODE_MT_custom_add_menu_group)

    with open(dir_path / "basic_menus.json", "r") as f:
        menu_dict = json.loads(f.read())

    for key, value in menu_dict.items():
        menu_class = generate_basic_menu(idname=key, props=value)
    
        generated_menus.append(menu_class)
        bpy.utils.register_class(menu_class)


def unregister():
    bpy.utils.unregister_class(NODE_MT_custom_add_menu_group) 

    for cls in generated_menus:
        bpy.utils.unregister_class(cls)

    generated_menus.clear()