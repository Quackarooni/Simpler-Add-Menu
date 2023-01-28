import bpy
from .__baseclasses import BaseMenu, BaseSubmenu
from .basic_menus import (
    NODE_MT_custom_add_menu_input_scene,
    NODE_MT_custom_add_menu_input_fields,
    NODE_MT_custom_add_menu_input_constants,
    NODE_MT_custom_add_menu_mesh_data,
    NODE_MT_custom_add_menu_mesh_setters,
    NODE_MT_custom_add_menu_mesh_operations,
    NODE_MT_custom_add_menu_mesh_primitives,
    NODE_MT_custom_add_menu_mesh_topology,
    NODE_MT_custom_add_menu_curve_data,
    NODE_MT_custom_add_menu_curve_setters,
    NODE_MT_custom_add_menu_curve_operations,
    NODE_MT_custom_add_menu_curve_primitives,
    NODE_MT_custom_add_menu_curve_topology,
    NODE_MT_custom_add_menu_utilities_color,
    NODE_MT_custom_add_menu_utilities_fields,
    NODE_MT_custom_add_menu_utilities_string,
    NODE_MT_custom_add_menu_utilities_vector,
    NODE_MT_custom_add_menu_utilities_rotation,
    NODE_MT_custom_add_menu_utilities_converter,
)

class NODE_MT_custom_add_menu_input(BaseMenu, BaseSubmenu):
    bl_label = "Input"
    bl_idname = "NODE_MT_custom_add_menu_input"

    items_compact = [
        "NODE_MT_custom_add_menu_input_scene",
        "NODE_MT_custom_add_menu_input_fields",
        "NODE_MT_custom_add_menu_input_constants",
        ]
    
    items_expanded = items_compact

class NODE_MT_custom_add_menu_mesh(BaseMenu, BaseSubmenu):
    bl_label = "Mesh"
    bl_idname = "NODE_MT_custom_add_menu_mesh"

    items_compact = [
        "NODE_MT_custom_add_menu_mesh_data",
        "NODE_MT_custom_add_menu_mesh_setters",
        "SeparateMenu",
        "NODE_MT_custom_add_menu_mesh_operations",
        "NODE_MT_custom_add_menu_mesh_primitives",
        "NODE_MT_custom_add_menu_mesh_topology",
        ]

    items_expanded = [
        "NODE_MT_custom_add_menu_mesh_data",
        "CombineMenu",
        "NODE_MT_custom_add_menu_mesh_setters",
        "NODE_MT_custom_add_menu_mesh_operations",
        "NODE_MT_custom_add_menu_mesh_primitives",
        "CombineMenu",
        "NODE_MT_custom_add_menu_mesh_topology",
        ]

class NODE_MT_custom_add_menu_curve(BaseMenu, BaseSubmenu):
    bl_label = "Curve"
    bl_idname = "NODE_MT_custom_add_menu_curve"

    items_compact = [
        "NODE_MT_custom_add_menu_curve_data",
        "NODE_MT_custom_add_menu_curve_setters",
        "SeparateMenu",
        "NODE_MT_custom_add_menu_curve_operations",
        "NODE_MT_custom_add_menu_curve_primitives",
        "NODE_MT_custom_add_menu_curve_topology",
        ]
    
    items_expanded = [
        "NODE_MT_custom_add_menu_curve_data",
        "NODE_MT_custom_add_menu_curve_setters",
        "NODE_MT_custom_add_menu_curve_operations",
        "NODE_MT_custom_add_menu_curve_primitives",
        "CombineMenu",
        "NODE_MT_custom_add_menu_curve_topology",
        ]

class NODE_MT_custom_add_menu_utilities(BaseMenu, BaseSubmenu):
    bl_label = "Utilities"
    bl_idname = "NODE_MT_custom_add_menu_utilities"

    items_compact = [
        "NODE_MT_custom_add_menu_utilities_color",
        "NODE_MT_custom_add_menu_utilities_string",
        "NODE_MT_custom_add_menu_utilities_vector",
        "SeparateMenu",
        "NODE_MT_custom_add_menu_utilities_fields",
        "NODE_MT_custom_add_menu_utilities_rotation",
        "NODE_MT_custom_add_menu_utilities_converter",
        ]

    items_expanded = [
        "NODE_MT_custom_add_menu_utilities_color",
        "CombineMenu",
        "NODE_MT_custom_add_menu_utilities_fields",
        "NODE_MT_custom_add_menu_utilities_string",
        "NODE_MT_custom_add_menu_utilities_vector",
        "CombineMenu",
        "NODE_MT_custom_add_menu_utilities_rotation",
        "NODE_MT_custom_add_menu_utilities_converter",
        ]

classes = (
        NODE_MT_custom_add_menu_input,
        NODE_MT_custom_add_menu_mesh,
        NODE_MT_custom_add_menu_curve,
        NODE_MT_custom_add_menu_utilities,
        )

def register():  
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)