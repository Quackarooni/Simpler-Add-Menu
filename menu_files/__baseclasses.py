import bpy
from .__globals import (
    draw_assets_for_catalog, 
    fetch_user_preferences, 
    subcategory_spacing, 
    add_node_type,
    spacing
)

from bpy.app.translations import (
    pgettext_iface as iface_,
    contexts as i18n_contexts,
)

class BaseMenu(bpy.types.Menu):
    bl_label = "Menu"
    bl_space_type = "NODE_EDITOR"

    draw_assets = False
    items = []

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'GeometryNodeTree'

    def draw(self, context):
        layout = self.layout

        for item in self.items:
            if item == "SeparateMenu":
                layout.separator(factor=spacing)
            elif isinstance(item, str):
                add_node_type(layout, item)
            elif isinstance(item, dict):
                node = item.get("node")
                label = iface_(item.get("label", None))
                props = item.get("props", None)
                
                operator = add_node_type(layout, node, label=label)

                if props is not None:
                    settings = operator.settings.add()
                    for key, value in props.items():
                        setattr(settings, key, value)
            else:
                raise TypeError(f"{item} is not a recognized format.")
        
        if self.draw_assets:
            draw_assets_for_catalog(layout, catalog_path=self.bl_label)

class BaseMultilevelMenu(bpy.types.Menu):
    items_compact = []
    items_expanded = []

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'GeometryNodeTree'

    @staticmethod
    def draw_compact(layout, items):
        for item in items:
            if item == "CombineMenu":
                raise ValueError

            if item == "SeparateMenu":
                layout.separator(factor=spacing)
            else:
                item = getattr(bpy.types, item)
                layout.menu(item.bl_idname)

    #@staticmethod
    def draw_expanded(self, layout, items):
        row = layout.row()
        col = None

        combine_next_menu = False
        for item in items:
            if item == "SeparateMenu":
                raise ValueError

            if item == "CombineMenu":
                combine_next_menu = True
                continue

            item = getattr(bpy.types, item)

            if combine_next_menu:
                col.separator(factor=subcategory_spacing)
                combine_next_menu = False
            else:
                col = row.column()

            col.label(text=item.bl_label)
            col.separator(factor=spacing)
            col.menu_contents(item.bl_idname)

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'
        prefs = fetch_user_preferences()

        if prefs.ui_mode == "COMPACT":
            self.draw_compact(layout, items=self.items_compact)
        else:
            self.draw_expanded(layout, items=self.items_expanded)  
        
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)

