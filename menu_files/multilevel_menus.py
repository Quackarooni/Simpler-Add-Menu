import bpy
import json
from .__globals import dir_path
from .__baseclasses import BaseMenu, BaseSubmenu

classes = []

def generate_multilevel_menu(idname, props):
    props["bl_idname"] = idname
    menu_class = type(idname,(BaseMenu, BaseSubmenu), props)
    return menu_class

def register():  
    with open(dir_path / "multilevel_menus.json", "r") as f:
        menu_dict = json.loads(f.read())

    for key, value in menu_dict.items():
        menu_class = generate_multilevel_menu(idname=key, props=value)
    
        classes.append(menu_class)
        bpy.utils.register_class(menu_class)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
    classes.clear()