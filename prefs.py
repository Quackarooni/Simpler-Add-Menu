import bpy
from bpy.props import BoolProperty, EnumProperty

class SimplerAddMenu(bpy.types.AddonPreferences):
    bl_idname = __package__

    include_nodegroups_asset: BoolProperty(
        name="Include Nodegroup Assets (Experimental)",
        default=True,
        description="Include nodegroups from your asset library in the add menu. (Only appends to categories in the original Add Menu))"
            )

    ui_mode: EnumProperty(
        name="UI Mode",
        items=(
            ("COMPACT", "Compact", "Draws subcategories as nested submenus"),
            ("EXPANDED", "Expanded", "Draws subcategories as separate columns"),
        ),
        default='EXPANDED',
        description="Specifies how the node subcategories are drawn")

    def draw(self, context):
        layout = self.layout
        #col = layout.row().column(heading="Options:")
        layout.prop(self, "include_nodegroups_asset")
        layout.prop(self, "ui_mode")


def register():
    bpy.utils.register_class(SimplerAddMenu)

def unregister():
    bpy.utils.unregister_class(SimplerAddMenu)