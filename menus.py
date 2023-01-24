import bpy
import json
from pathlib import Path
from bl_ui import node_add_menu

menu_classes = []
addon_draw_funcs = []
dir_path = Path(__file__).parent
spacing = 0.65
subcategory_spacing = spacing*1

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

class MenuBaseClass(bpy.types.Menu):
    bl_label = "Menu"
    bl_space_type = "NODE_EDITOR"

    items = []

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'GeometryNodeTree'

    def draw(self, context):
        pass

class SubmenuBaseClass():
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
                layout.menu(item.bl_idname)

    @staticmethod
    def draw_expanded(layout, items):
        row = layout.row()
        for item in items:
            if item == "SeparateMenu":
                raise ValueError

            if item != "CombineMenu":
                col = row.column()
            else:
                col.separator(factor=spacing)

            col.label(text=item.bl_label)
            col.separator(factor=spacing)
            col.menu_contents(item.bl_idname)


class NODE_MT_custom_add_menu(MenuBaseClass):
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

class NODE_MT_custom_add_menu_attribute(MenuBaseClass):
    bl_idname = "NODE_MT_custom_add_menu_attribute"
    bl_label = "Attribute"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeAttributeStatistic")
        add_node_type(layout, "GeometryNodeAttributeDomainSize")
        layout.separator(factor=spacing)        
        add_node_type(layout, "GeometryNodeCaptureAttribute")
        add_node_type(layout, "GeometryNodeStoreNamedAttribute")
        add_node_type(layout, "GeometryNodeRemoveAttribute")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)

class NODE_MT_custom_add_menu_input_scene(MenuBaseClass):
    bl_label = "Scene"
    bl_idname = "NODE_MT_custom_add_menu_input_scene"

    def draw(self, context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeCollectionInfo")
        add_node_type(layout, "GeometryNodeObjectInfo")
        add_node_type(layout, "GeometryNodeSelfObject")
        add_node_type(layout, "GeometryNodeIsViewport")
        add_node_type(layout, "GeometryNodeInputSceneTime")

class NODE_MT_custom_add_menu_input_fields(MenuBaseClass):
    bl_label = "Fields"
    bl_idname = "NODE_MT_custom_add_menu_input_fields"

    def draw(self, context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeInputID")
        add_node_type(layout, "GeometryNodeInputIndex")
        add_node_type(layout, "GeometryNodeInputNamedAttribute")
        add_node_type(layout, "GeometryNodeInputNormal")
        add_node_type(layout, "GeometryNodeInputPosition")
        add_node_type(layout, "GeometryNodeInputRadius")

class NODE_MT_custom_add_menu_input_constants(MenuBaseClass):
    bl_label = "Constants"
    bl_idname = "NODE_MT_custom_add_menu_input_constants"

    def draw(self, context):
        layout = self.layout
        add_node_type(layout, "FunctionNodeInputBool")
        add_node_type(layout, "FunctionNodeInputColor")
        add_node_type(layout, "FunctionNodeInputInt")
        add_node_type(layout, "GeometryNodeInputMaterial")
        add_node_type(layout, "FunctionNodeInputString")
        add_node_type(layout, "ShaderNodeValue")
        add_node_type(layout, "FunctionNodeInputVector")

class NODE_MT_custom_add_menu_input(MenuBaseClass, SubmenuBaseClass):
    bl_label = "Input"
    bl_idname = "NODE_MT_custom_add_menu_input"

    items_compact = [
            NODE_MT_custom_add_menu_input_scene,
            NODE_MT_custom_add_menu_input_fields,
            NODE_MT_custom_add_menu_input_constants,
            ]

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'
        prefs = fetch_user_preferences()

        if prefs.ui_mode == "COMPACT":
            self.draw_compact(layout, items=self.items_compact)
        else:
            row = layout.row()
            submenus = (
                NODE_MT_custom_add_menu_input_scene,
                NODE_MT_custom_add_menu_input_fields,
                NODE_MT_custom_add_menu_input_constants,
            )

            for submenu in submenus:
                col = row.column()
                col.label(text=submenu.bl_label)
                col.separator(factor=spacing)
                col.menu_contents(submenu.bl_idname)         
        
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)

class NODE_MT_custom_add_menu_output(MenuBaseClass):
    bl_idname = "NODE_MT_custom_add_menu_output"
    bl_label = "Output"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeViewer")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)
        
class NODE_MT_custom_add_menu_geometry(MenuBaseClass):
    bl_idname = "NODE_MT_custom_add_menu_geometry"
    bl_label = "Geometry"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeBoundBox")
        add_node_type(layout, "GeometryNodeConvexHull")
        add_node_type(layout, "GeometryNodeDeleteGeometry")
        add_node_type(layout, "GeometryNodeDuplicateElements")
        add_node_type(layout, "GeometryNodeMergeByDistance")
        add_node_type(layout, "GeometryNodeTransform")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeJoinGeometry")
        add_node_type(layout, "GeometryNodeGeometryToInstance")
        layout.separator(factor=spacing)        
        add_node_type(layout, "GeometryNodeRaycast")
        add_node_type(layout, "GeometryNodeProximity", label="Proximity")
        add_node_type(layout, "GeometryNodeSampleIndex")
        add_node_type(layout, "GeometryNodeSampleNearest")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeSeparateComponents")
        add_node_type(layout, "GeometryNodeSeparateGeometry")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeSetID")
        add_node_type(layout, "GeometryNodeSetPosition")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)
        
class NODE_MT_custom_add_menu_mesh_data(MenuBaseClass):
    bl_label = "Get Mesh Data"
    bl_idname = "NODE_MT_custom_add_menu_mesh_data"

    def draw(self, context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeInputMeshVertexNeighbors")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeInputMeshEdgeAngle")
        add_node_type(layout, "GeometryNodeInputMeshEdgeNeighbors")
        add_node_type(layout, "GeometryNodeInputMeshEdgeVertices")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeInputMeshFaceArea")
        add_node_type(layout, "GeometryNodeInputMeshFaceNeighbors")
        add_node_type(layout, "GeometryNodeMeshFaceSetBoundaries")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeInputMeshFaceIsPlanar")
        add_node_type(layout, "GeometryNodeInputShadeSmooth")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeInputMeshIsland")
        add_node_type(layout, "GeometryNodeInputShortestEdgePaths")

class NODE_MT_custom_add_menu_mesh_operations(MenuBaseClass):
    bl_label = "Mesh Operations"
    bl_idname = "NODE_MT_custom_add_menu_mesh_operations"

    def draw(self, context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeDualMesh")
        add_node_type(layout, "GeometryNodeExtrudeMesh")
        add_node_type(layout, "GeometryNodeFlipFaces")
        add_node_type(layout, "GeometryNodeSplitEdges")
        add_node_type(layout, "GeometryNodeScaleElements")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeEdgePathsToCurves")
        add_node_type(layout, "GeometryNodeEdgePathsToSelection")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeMeshBoolean")
        add_node_type(layout, "GeometryNodeMeshToCurve")
        add_node_type(layout, "GeometryNodeMeshToPoints")
        add_node_type(layout, "GeometryNodeMeshToVolume")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeSampleNearestSurface")
        add_node_type(layout, "GeometryNodeSampleUVSurface")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeSubdivideMesh")
        add_node_type(layout, "GeometryNodeSubdivisionSurface")
        add_node_type(layout, "GeometryNodeTriangulate")

class NODE_MT_custom_add_menu_mesh_setters(MenuBaseClass):
    bl_label = "Set Mesh Data"
    bl_idname = "NODE_MT_custom_add_menu_mesh_setters"

    def draw(self, context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeSetShadeSmooth")

class NODE_MT_custom_add_menu_mesh_primitives(MenuBaseClass):
    bl_idname = "NODE_MT_custom_add_menu_mesh_primitives"
    bl_label = "Mesh Primitives"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeMeshCone")
        add_node_type(layout, "GeometryNodeMeshCube")
        add_node_type(layout, "GeometryNodeMeshCylinder")
        add_node_type(layout, "GeometryNodeMeshGrid")
        add_node_type(layout, "GeometryNodeMeshIcoSphere")
        add_node_type(layout, "GeometryNodeMeshCircle")
        add_node_type(layout, "GeometryNodeMeshLine")
        add_node_type(layout, "GeometryNodeMeshUVSphere")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)
        
class NODE_MT_custom_add_menu_mesh_topology(MenuBaseClass):
    bl_idname = "NODE_MT_custom_add_menu_mesh_topology"
    bl_label = "Mesh Topology"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeCornersOfFace"),
        add_node_type(layout, "GeometryNodeCornersOfVertex"),
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeEdgesOfCorner"),
        add_node_type(layout, "GeometryNodeEdgesOfVertex"),
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeFaceOfCorner"),
        add_node_type(layout, "GeometryNodeVertexOfCorner")
        add_node_type(layout, "GeometryNodeOffsetCornerInFace"),
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)

class NODE_MT_custom_add_menu_mesh(MenuBaseClass, SubmenuBaseClass):
    bl_label = "Mesh"
    bl_idname = "NODE_MT_custom_add_menu_mesh"

    items_compact = [
            NODE_MT_custom_add_menu_mesh_data,
            NODE_MT_custom_add_menu_mesh_setters,
            "SeparateMenu",
            NODE_MT_custom_add_menu_mesh_operations,
            NODE_MT_custom_add_menu_mesh_primitives,
            NODE_MT_custom_add_menu_mesh_topology,
            ]

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'
        prefs = fetch_user_preferences()

        if prefs.ui_mode == "COMPACT":
            self.draw_compact(layout, items=self.items_compact)
        else:
            row = layout.row()
            col = row.column()
            col.label(text=NODE_MT_custom_add_menu_mesh_data.bl_label)
            col.separator(factor=spacing)
            col.menu_contents(NODE_MT_custom_add_menu_mesh_data.bl_idname)

            col.separator(factor=subcategory_spacing)
            col.label(text=NODE_MT_custom_add_menu_mesh_setters.bl_label)
            col.separator(factor=spacing)
            col.menu_contents(NODE_MT_custom_add_menu_mesh_setters.bl_idname)
            
            col = row.column()
            col.label(text=NODE_MT_custom_add_menu_mesh_operations.bl_label)
            col.separator(factor=spacing)
            col.menu_contents(NODE_MT_custom_add_menu_mesh_operations.bl_idname)

            col = row.column()
            col.label(text=NODE_MT_custom_add_menu_mesh_primitives.bl_label)
            col.separator(factor=spacing)
            col.menu_contents(NODE_MT_custom_add_menu_mesh_primitives.bl_idname)

            col.separator(factor=subcategory_spacing)
            col.label(text=NODE_MT_custom_add_menu_mesh_topology.bl_label)
            col.separator(factor=spacing)
            col.menu_contents(NODE_MT_custom_add_menu_mesh_topology.bl_idname)

        draw_assets_for_catalog(layout, catalog_path=self.bl_label)

class NODE_MT_custom_add_menu_curve_data(MenuBaseClass):
    bl_label = "Get Curve Data"
    bl_idname = "NODE_MT_custom_add_menu_curve_data"

    def draw(self, context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeInputCurveHandlePositions")
        add_node_type(layout, "GeometryNodeInputTangent")
        add_node_type(layout, "GeometryNodeInputCurveTilt")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeCurveEndpointSelection")
        add_node_type(layout, "GeometryNodeCurveHandleTypeSelection")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeInputSplineCyclic")
        add_node_type(layout, "GeometryNodeSplineLength")
        add_node_type(layout, "GeometryNodeSplineParameter")
        add_node_type(layout, "GeometryNodeInputSplineResolution")

class NODE_MT_custom_add_menu_curve_operations(MenuBaseClass):
    bl_label = "Curve Operations"
    bl_idname = "NODE_MT_custom_add_menu_curve_operations"

    def draw(self, context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeCurveToMesh")
        add_node_type(layout, "GeometryNodeCurveToPoints")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeFillCurve")
        add_node_type(layout, "GeometryNodeFilletCurve")
        add_node_type(layout, "GeometryNodeReverseCurve")
        add_node_type(layout, "GeometryNodeTrimCurve")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeSampleCurve")
        add_node_type(layout, "GeometryNodeResampleCurve")
        add_node_type(layout, "GeometryNodeSubdivideCurve")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeCurveLength")
        add_node_type(layout, "GeometryNodeDeformCurvesOnSurface")

class NODE_MT_custom_add_menu_curve_setters(MenuBaseClass):
    bl_label = "Set Curve Data"
    bl_idname = "NODE_MT_custom_add_menu_curve_setters"

    def draw(self, context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeSetCurveNormal")
        add_node_type(layout, "GeometryNodeSetCurveRadius")
        add_node_type(layout, "GeometryNodeSetCurveTilt")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeSetCurveHandlePositions")
        add_node_type(layout, "GeometryNodeCurveSetHandles")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeSetSplineCyclic")
        add_node_type(layout, "GeometryNodeSetSplineResolution")
        add_node_type(layout, "GeometryNodeCurveSplineType")

class NODE_MT_custom_add_menu_curve_primitives(MenuBaseClass):
    bl_idname = "NODE_MT_custom_add_menu_curve_primitives"
    bl_label = "Curve Primitives"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeCurveArc")
        add_node_type(layout, "GeometryNodeCurvePrimitiveBezierSegment")
        add_node_type(layout, "GeometryNodeCurvePrimitiveCircle")
        add_node_type(layout, "GeometryNodeCurvePrimitiveLine")
        add_node_type(layout, "GeometryNodeCurveSpiral")
        add_node_type(layout, "GeometryNodeCurveQuadraticBezier")
        add_node_type(layout, "GeometryNodeCurvePrimitiveQuadrilateral")
        add_node_type(layout, "GeometryNodeCurveStar")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)
        
class NODE_MT_custom_add_menu_curve_topology(MenuBaseClass):
    bl_idname = "NODE_MT_custom_add_menu_curve_topology"
    bl_label = "Curve Topology"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeOffsetPointInCurve")
        add_node_type(layout, "GeometryNodeCurveOfPoint")
        add_node_type(layout, "GeometryNodePointsOfCurve")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)

class NODE_MT_custom_add_menu_curve(MenuBaseClass, SubmenuBaseClass):
    bl_label = "Curve"
    bl_idname = "NODE_MT_custom_add_menu_curve"

    items_compact = [
        NODE_MT_custom_add_menu_curve_data,
        NODE_MT_custom_add_menu_curve_setters,
        "SeparateMenu",
        NODE_MT_custom_add_menu_curve_operations,
        NODE_MT_custom_add_menu_curve_primitives,
        NODE_MT_custom_add_menu_curve_topology,
        ]
        
    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'
        prefs = fetch_user_preferences()

        if prefs.ui_mode == "COMPACT":
            self.draw_compact(layout, items=self.items_compact)
        else:
            row = layout.row()
            col = row.column()
            col.label(text=NODE_MT_custom_add_menu_curve_data.bl_label)
            col.separator(factor=spacing)
            col.menu_contents(NODE_MT_custom_add_menu_curve_data.bl_idname)

            col = row.column()
            col.label(text=NODE_MT_custom_add_menu_curve_setters.bl_label)
            col.separator(factor=spacing)
            col.menu_contents(NODE_MT_custom_add_menu_curve_setters.bl_idname)
            
            col = row.column()
            col.label(text=NODE_MT_custom_add_menu_curve_operations.bl_label)
            col.separator(factor=spacing)
            col.menu_contents(NODE_MT_custom_add_menu_curve_operations.bl_idname)

            col = row.column()
            col.label(text=NODE_MT_custom_add_menu_curve_primitives.bl_label)
            col.separator(factor=spacing)
            col.menu_contents(NODE_MT_custom_add_menu_curve_primitives.bl_idname)

            col.separator(factor=subcategory_spacing)
            col.label(text=NODE_MT_custom_add_menu_curve_topology.bl_label)
            col.separator(factor=spacing)
            col.menu_contents(NODE_MT_custom_add_menu_curve_topology.bl_idname)

        draw_assets_for_catalog(layout, catalog_path=self.bl_label)

class NODE_MT_custom_add_menu_instance(MenuBaseClass):
    bl_idname = "NODE_MT_custom_add_menu_instance"
    bl_label = "Instances"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeInstanceOnPoints")
        add_node_type(layout, "GeometryNodeInstancesToPoints")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeRealizeInstances")
        add_node_type(layout, "GeometryNodeRotateInstances")
        add_node_type(layout, "GeometryNodeScaleInstances")
        add_node_type(layout, "GeometryNodeTranslateInstances")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeInputInstanceRotation")
        add_node_type(layout, "GeometryNodeInputInstanceScale")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)
        
class NODE_MT_custom_add_menu_point(MenuBaseClass):
    bl_idname = "NODE_MT_custom_add_menu_point"
    bl_label = "Point"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeDistributePointsInVolume")
        add_node_type(layout, "GeometryNodeDistributePointsOnFaces")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodePoints")
        add_node_type(layout, "GeometryNodePointsToVertices")
        add_node_type(layout, "GeometryNodePointsToVolume")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeSetPointRadius")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)
        
class NODE_MT_custom_add_menu_volume(MenuBaseClass):
    bl_idname = "NODE_MT_custom_add_menu_volume"
    bl_label = "Volume"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeVolumeCube")
        add_node_type(layout, "GeometryNodeVolumeToMesh")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)
        
class NODE_MT_custom_add_menu_material(MenuBaseClass):
    bl_idname = "NODE_MT_custom_add_menu_material"
    bl_label = "Material"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeReplaceMaterial")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeInputMaterialIndex")
        add_node_type(layout, "GeometryNodeMaterialSelection")
        layout.separator(factor=spacing)
        add_node_type(layout, "GeometryNodeSetMaterial")
        add_node_type(layout, "GeometryNodeSetMaterialIndex")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)
        
class NODE_MT_custom_add_menu_texture(MenuBaseClass):
    bl_idname = "NODE_MT_custom_add_menu_texture"
    bl_label = "Texture"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "ShaderNodeTexBrick")
        add_node_type(layout, "ShaderNodeTexChecker")
        add_node_type(layout, "ShaderNodeTexGradient")
        add_node_type(layout, "GeometryNodeImageTexture")
        add_node_type(layout, "ShaderNodeTexMagic")
        add_node_type(layout, "ShaderNodeTexMusgrave")
        add_node_type(layout, "ShaderNodeTexNoise")
        add_node_type(layout, "ShaderNodeTexVoronoi")
        add_node_type(layout, "ShaderNodeTexWave")
        add_node_type(layout, "ShaderNodeTexWhiteNoise")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)
        
class NODE_MT_custom_add_menu_utilities_color(MenuBaseClass):
    bl_idname = "NODE_MT_custom_add_menu_utilities_color"
    bl_label = "Color"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "ShaderNodeValToRGB", label='Color Ramp')
        add_node_type(layout, "ShaderNodeRGBCurve")
        layout.separator(factor=spacing)
        props = add_node_type(layout, "ShaderNodeMix", label=iface_("Mix Color"))
        ops = props.settings.add()
        ops.name = "data_type"
        ops.value = "'RGBA'"
        add_node_type(layout, "FunctionNodeCombineColor")
        add_node_type(layout, "FunctionNodeSeparateColor")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)
        
class NODE_MT_custom_add_menu_utilities_string(MenuBaseClass):
    bl_idname = "NODE_MT_custom_add_menu_utilities_string"
    bl_label = "String"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeStringJoin")
        add_node_type(layout, "FunctionNodeReplaceString")
        add_node_type(layout, "FunctionNodeSliceString")
        layout.separator(factor=spacing)
        add_node_type(layout, "FunctionNodeStringLength")
        add_node_type(layout, "GeometryNodeStringToCurves")
        add_node_type(layout, "FunctionNodeValueToString")
        layout.separator(factor=spacing)
        add_node_type(layout, "FunctionNodeInputSpecialCharacters")
        draw_assets_for_catalog(layout, catalog_path="Text")        

class NODE_MT_custom_add_menu_utilities_vector(MenuBaseClass):
    bl_idname = "NODE_MT_custom_add_menu_utilities_vector"
    bl_label = "Vector"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "ShaderNodeVectorCurve")
        add_node_type(layout, "ShaderNodeVectorMath")
        add_node_type(layout, "ShaderNodeVectorRotate")
        layout.separator(factor=spacing)
        props = add_node_type(layout, "ShaderNodeMix", label=iface_("Mix Vector"))
        ops = props.settings.add()
        ops.name = "data_type"
        ops.value = "'VECTOR'"
        add_node_type(layout, "ShaderNodeCombineXYZ")
        add_node_type(layout, "ShaderNodeSeparateXYZ")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)
               
class NODE_MT_custom_add_menu_utilities_fields(MenuBaseClass):
    bl_label = "Fields"
    bl_idname = "NODE_MT_custom_add_menu_utilities_fields"

    def draw(self, context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeAccumulateField")
        add_node_type(layout, "GeometryNodeFieldAtIndex")
        add_node_type(layout, "GeometryNodeFieldOnDomain")
        add_node_type(layout, "FunctionNodeRandomValue")

class NODE_MT_custom_add_menu_utilities_rotation(MenuBaseClass):
    bl_label = "Rotation"
    bl_idname = "NODE_MT_custom_add_menu_utilities_rotation"

    def draw(self, context):
        layout = self.layout
        add_node_type(layout, "FunctionNodeAlignEulerToVector")
        add_node_type(layout, "FunctionNodeRotateEuler")

class NODE_MT_custom_add_menu_utilities_converter(MenuBaseClass):
    bl_label = "Converter"
    bl_idname = "NODE_MT_custom_add_menu_utilities_converter"

    def draw(self, context):
        layout = self.layout
        add_node_type(layout, "FunctionNodeBooleanMath")
        add_node_type(layout, "GeometryNodeSwitch")
        layout.separator(factor=spacing)
        add_node_type(layout, "ShaderNodeClamp")
        add_node_type(layout, "FunctionNodeCompare")
        add_node_type(layout, "ShaderNodeFloatCurve")
        add_node_type(layout, "ShaderNodeMapRange")
        layout.separator(factor=spacing)        
        add_node_type(layout, "ShaderNodeMix")
        add_node_type(layout, "ShaderNodeMath")
        add_node_type(layout, "FunctionNodeFloatToInt")

class NODE_MT_custom_add_menu_utilities(MenuBaseClass, SubmenuBaseClass):
    bl_label = "Utilities"
    bl_idname = "NODE_MT_custom_add_menu_utilities"

    items_compact = [
            NODE_MT_custom_add_menu_utilities_color,
            NODE_MT_custom_add_menu_utilities_string,
            NODE_MT_custom_add_menu_utilities_vector,
            "SeparateMenu",
            NODE_MT_custom_add_menu_utilities_fields,
            NODE_MT_custom_add_menu_utilities_rotation,
            NODE_MT_custom_add_menu_utilities_converter,
        ]

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'
        prefs = fetch_user_preferences()

        if prefs.ui_mode == "COMPACT":
            self.draw_compact(layout, items=self.items_compact)
        else:
            row = layout.row()
            col = row.column()
            col.label(text=NODE_MT_custom_add_menu_utilities_color.bl_label)
            col.separator(factor=spacing)
            col.menu_contents(NODE_MT_custom_add_menu_utilities_color.bl_idname)
            
            col.separator(factor=subcategory_spacing)
            col.label(text=NODE_MT_custom_add_menu_utilities_fields.bl_label)
            col.separator(factor=spacing)
            col.menu_contents(NODE_MT_custom_add_menu_utilities_fields.bl_idname)

            col = row.column()
            col.label(text=NODE_MT_custom_add_menu_utilities_string.bl_label)
            col.separator(factor=spacing)
            col.menu_contents(NODE_MT_custom_add_menu_utilities_string.bl_idname)

            col = row.column()
            col.label(text=NODE_MT_custom_add_menu_utilities_vector.bl_label)
            col.separator(factor=spacing)
            col.menu_contents(NODE_MT_custom_add_menu_utilities_vector.bl_idname)
            
            col.separator(factor=subcategory_spacing)
            col.label(text=NODE_MT_custom_add_menu_utilities_rotation.bl_label)
            col.separator(factor=spacing)
            col.menu_contents(NODE_MT_custom_add_menu_utilities_rotation.bl_idname)

            col = row.column()
            col.label(text=NODE_MT_custom_add_menu_utilities_converter.bl_label)
            col.separator(factor=spacing)
            col.menu_contents(NODE_MT_custom_add_menu_utilities_converter.bl_idname)

        draw_assets_for_catalog(layout, catalog_path=self.bl_label)

class NODE_MT_custom_add_menu_UV(MenuBaseClass):
    bl_idname = "NODE_MT_custom_add_menu_UV"
    bl_label = "UV"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeUVPackIslands")
        add_node_type(layout, "GeometryNodeUVUnwrap")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)
        
class NODE_MT_custom_add_menu_group(MenuBaseClass):
    bl_idname = "NODE_MT_custom_add_menu_group"
    bl_label = "Group"

    def draw(self, context):
        layout = self.layout
        node_add_menu.draw_node_group_add_menu(context, layout)
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)
        
class NODE_MT_custom_add_menu_layout(MenuBaseClass):
    bl_idname = "NODE_MT_custom_add_menu_layout"
    bl_label = "Layout"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "NodeFrame")
        add_node_type(layout, "NodeReroute")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)

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

classes = (
        NODE_MT_custom_add_menu,
        NODE_MT_custom_add_menu_attribute,
        NODE_MT_custom_add_menu_input,
        NODE_MT_custom_add_menu_input_scene,
        NODE_MT_custom_add_menu_input_fields,
        NODE_MT_custom_add_menu_input_constants,
        NODE_MT_custom_add_menu_output,
        NODE_MT_custom_add_menu_geometry,
        NODE_MT_custom_add_menu_mesh,
        NODE_MT_custom_add_menu_mesh_data,
        NODE_MT_custom_add_menu_mesh_operations,
        NODE_MT_custom_add_menu_mesh_setters,
        NODE_MT_custom_add_menu_mesh_primitives,
        NODE_MT_custom_add_menu_mesh_topology,
        NODE_MT_custom_add_menu_curve,
        NODE_MT_custom_add_menu_curve_data,
        NODE_MT_custom_add_menu_curve_operations,
        NODE_MT_custom_add_menu_curve_setters,
        NODE_MT_custom_add_menu_curve_primitives,
        NODE_MT_custom_add_menu_curve_topology,
        NODE_MT_custom_add_menu_instance,
        NODE_MT_custom_add_menu_point,
        NODE_MT_custom_add_menu_volume,
        NODE_MT_custom_add_menu_material,
        NODE_MT_custom_add_menu_texture,
        NODE_MT_custom_add_menu_utilities,
        NODE_MT_custom_add_menu_utilities_color,
        NODE_MT_custom_add_menu_utilities_string,
        NODE_MT_custom_add_menu_utilities_vector,
        NODE_MT_custom_add_menu_utilities_fields,
        NODE_MT_custom_add_menu_utilities_rotation,
        NODE_MT_custom_add_menu_utilities_converter,
        NODE_MT_custom_add_menu_UV,
        NODE_MT_custom_add_menu_group,
        NODE_MT_custom_add_menu_layout,
        NODE_OT_INVOKE_MENU,
        )

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


