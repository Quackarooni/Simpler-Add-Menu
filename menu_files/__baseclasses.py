import bpy
from .__globals import (
    draw_assets_for_catalog, 
    fetch_user_preferences, 
    subcategory_spacing, 
    spacing
)

class BaseMenu(bpy.types.Menu):
    bl_label = "Menu"
    bl_space_type = "NODE_EDITOR"

    items = []

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'GeometryNodeTree'

    #def draw(self, context):
    #   pass

class BaseMultilevelMenu():
    items_compact = []
    items_expanded = []

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

