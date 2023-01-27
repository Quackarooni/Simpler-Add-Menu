import bpy
from pathlib import Path

dir_path = Path(__file__).parent.parent
spacing = 0.65

from bpy.app.translations import (
    pgettext_iface as iface_,
    contexts as i18n_contexts,
)
#taken from https://github.com/blender/blender/blob/master/release/scripts/startup/bl_ui/node_add_menu.py
def add_node_type(layout, node_type, *, label=None):
    """Add a node type to a menu."""
    bl_rna = bpy.types.Node.bl_rna_get_subclass(node_type)
    if not label:
        label = bl_rna.name if bl_rna else iface_("Unknown")
    translation_context = bl_rna.translation_context if bl_rna else i18n_contexts.default
    props = layout.operator("node.add_node", text=label, text_ctxt=translation_context)
    props.type = node_type
    props.use_transform = True
    return props

def fetch_user_preferences():
    return bpy.context.preferences.addons['Simpler Add Menu'].preferences

def draw_assets_for_catalog(layout, catalog_path):
    prefs = fetch_user_preferences()

    if prefs.include_nodegroups_asset:
        layout.template_node_asset_menu_items(catalog_path=catalog_path)