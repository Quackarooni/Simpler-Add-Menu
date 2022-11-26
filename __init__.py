# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "Cleaner Add Menu",
    "author": "Quackers",
    "description": "Addon for a slightly more cleaner and organized geometry nodes add menu",
    "blender": (3, 4, 0),
    "version": (0, 1, 0),
    "location": "Shader Editor > Add",
    "category": "Node",
}

import bpy
import os
from bl_ui import node_add_menu
import json

menu_classes = []
addon_draw_funcs = []
dir_path = os.path.dirname(__file__)
spacing = 0.65

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


class NODE_MT_custom_add_menu(MenuBaseClass):
    bl_label = "Add"
    bl_idname = "NODE_MT_custom_add_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'

        props = layout.operator("node.add_search", text="Search...", icon='VIEWZOOM')
        props.use_transform = True
        layout.separator()

        layout.menu(bpy.types.NODE_MT_geometry_node_GEO_ATTRIBUTE.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_input.bl_idname)
        layout.menu(bpy.types.NODE_MT_category_GEO_OUTPUT.bl_idname)
        layout.separator(factor=spacing)

        layout.menu(bpy.types.NODE_MT_geometry_node_GEO_GEOMETRY.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_mesh.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_curves.bl_idname)
        layout.menu(bpy.types.NODE_MT_geometry_node_GEO_INSTANCE.bl_idname)
        layout.menu(bpy.types.NODE_MT_category_GEO_POINT.bl_idname)
        layout.menu(bpy.types.NODE_MT_category_GEO_VOLUME.bl_idname)
        layout.separator(factor=spacing)
        
        layout.menu(bpy.types.NODE_MT_geometry_node_GEO_MATERIAL.bl_idname)
        layout.menu(bpy.types.NODE_MT_category_GEO_TEXTURE.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_utilities.bl_idname)
        
        layout.menu(bpy.types.NODE_MT_category_GEO_UV.bl_idname)
        layout.separator(factor=spacing)
        layout.menu(bpy.types.NODE_MT_category_GEO_GROUP.bl_idname)
        layout.menu(bpy.types.NODE_MT_category_GEO_LAYOUT.bl_idname)


class NODE_MT_custom_add_menu_curve_operations(MenuBaseClass):
    bl_label = "Curve Operations"
    bl_idname = "NODE_MT_custom_add_menu_curve_operations"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeCurveLength")
        node_add_menu.add_node_type(layout, "GeometryNodeCurveToMesh")
        node_add_menu.add_node_type(layout, "GeometryNodeCurveToPoints")
        node_add_menu.add_node_type(layout, "GeometryNodeDeformCurvesOnSurface")
        node_add_menu.add_node_type(layout, "GeometryNodeFillCurve")
        node_add_menu.add_node_type(layout, "GeometryNodeFilletCurve")
        node_add_menu.add_node_type(layout, "GeometryNodeResampleCurve")
        node_add_menu.add_node_type(layout, "GeometryNodeReverseCurve")
        node_add_menu.add_node_type(layout, "GeometryNodeSampleCurve")
        node_add_menu.add_node_type(layout, "GeometryNodeSubdivideCurve")
        node_add_menu.add_node_type(layout, "GeometryNodeTrimCurve")


class NODE_MT_custom_add_menu_curve_data(MenuBaseClass):
    bl_label = "Curve Data"
    bl_idname = "NODE_MT_custom_add_menu_curve_data"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeInputCurveHandlePositions")
        node_add_menu.add_node_type(layout, "GeometryNodeInputTangent")
        node_add_menu.add_node_type(layout, "GeometryNodeInputCurveTilt")
        node_add_menu.add_node_type(layout, "GeometryNodeCurveEndpointSelection")
        node_add_menu.add_node_type(layout, "GeometryNodeCurveHandleTypeSelection")
        node_add_menu.add_node_type(layout, "GeometryNodeInputSplineCyclic")
        node_add_menu.add_node_type(layout, "GeometryNodeSplineLength")
        node_add_menu.add_node_type(layout, "GeometryNodeSplineParameter")
        node_add_menu.add_node_type(layout, "GeometryNodeInputSplineResolution")


class NODE_MT_custom_add_menu_curve_setters(MenuBaseClass):
    bl_label = "Curve Setters"
    bl_idname = "NODE_MT_custom_add_menu_curve_setters"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeSetCurveNormal")
        node_add_menu.add_node_type(layout, "GeometryNodeSetCurveRadius")
        node_add_menu.add_node_type(layout, "GeometryNodeSetCurveTilt")
        node_add_menu.add_node_type(layout, "GeometryNodeSetCurveHandlePositions")
        node_add_menu.add_node_type(layout, "GeometryNodeCurveSetHandles")
        node_add_menu.add_node_type(layout, "GeometryNodeSetSplineCyclic")
        node_add_menu.add_node_type(layout, "GeometryNodeSetSplineResolution")
        node_add_menu.add_node_type(layout, "GeometryNodeCurveSplineType")


class NODE_MT_custom_add_menu_curves(MenuBaseClass):
    bl_label = "Curve"
    bl_idname = "NODE_MT_custom_add_menu_curves"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'
        layout.menu(NODE_MT_custom_add_menu_curve_data.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_curve_operations.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_curve_setters.bl_idname)
        layout.menu(bpy.types.NODE_MT_geometry_node_GEO_PRIMITIVES_CURVE.bl_idname)
        layout.menu(bpy.types.NODE_MT_geometry_node_curve_topology.bl_idname)


class NODE_MT_custom_add_menu_input(MenuBaseClass):
    bl_label = "Input"
    bl_idname = "NODE_MT_custom_add_menu_input"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'
        layout.menu(NODE_MT_custom_add_menu_input_constants.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_input_fields.bl_idname)


class NODE_MT_custom_add_menu_input_constants(MenuBaseClass):
    bl_label = "Constants"
    bl_idname = "NODE_MT_custom_add_menu_input_constants"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeCollectionInfo")
        node_add_menu.add_node_type(layout, "GeometryNodeObjectInfo")
        node_add_menu.add_node_type(layout, "GeometryNodeSelfObject")
        node_add_menu.add_node_type(layout, "GeometryNodeIsViewport")
        node_add_menu.add_node_type(layout, "GeometryNodeInputSceneTime")
        layout.separator(factor=spacing)
        node_add_menu.add_node_type(layout, "FunctionNodeInputBool")
        node_add_menu.add_node_type(layout, "FunctionNodeInputColor")
        node_add_menu.add_node_type(layout, "FunctionNodeInputInt")
        node_add_menu.add_node_type(layout, "GeometryNodeInputMaterial")
        node_add_menu.add_node_type(layout, "FunctionNodeInputString")
        node_add_menu.add_node_type(layout, "ShaderNodeValue")
        node_add_menu.add_node_type(layout, "FunctionNodeInputVector")


class NODE_MT_custom_add_menu_input_fields(MenuBaseClass):
    bl_label = "Fields"
    bl_idname = "NODE_MT_custom_add_menu_input_fields"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeInputID")
        node_add_menu.add_node_type(layout, "GeometryNodeInputIndex")
        node_add_menu.add_node_type(layout, "GeometryNodeInputNamedAttribute")
        node_add_menu.add_node_type(layout, "GeometryNodeInputNormal")
        node_add_menu.add_node_type(layout, "GeometryNodeInputPosition")
        node_add_menu.add_node_type(layout, "GeometryNodeInputRadius")


class NODE_MT_custom_add_menu_mesh_operations(MenuBaseClass):
    bl_label = "Mesh Operations"
    bl_idname = "NODE_MT_custom_add_menu_mesh_operations"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeDualMesh")
        node_add_menu.add_node_type(layout, "GeometryNodeEdgePathsToCurves")
        node_add_menu.add_node_type(layout, "GeometryNodeEdgePathsToSelection")
        node_add_menu.add_node_type(layout, "GeometryNodeExtrudeMesh")
        node_add_menu.add_node_type(layout, "GeometryNodeFlipFaces")
        node_add_menu.add_node_type(layout, "GeometryNodeMeshBoolean")
        node_add_menu.add_node_type(layout, "GeometryNodeMeshToCurve")
        node_add_menu.add_node_type(layout, "GeometryNodeMeshToPoints")
        node_add_menu.add_node_type(layout, "GeometryNodeMeshToVolume")
        node_add_menu.add_node_type(layout, "GeometryNodeSampleNearestSurface")
        node_add_menu.add_node_type(layout, "GeometryNodeSampleUVSurface")
        node_add_menu.add_node_type(layout, "GeometryNodeScaleElements")
        node_add_menu.add_node_type(layout, "GeometryNodeSplitEdges")
        node_add_menu.add_node_type(layout, "GeometryNodeSubdivideMesh")
        node_add_menu.add_node_type(layout, "GeometryNodeSubdivisionSurface")
        node_add_menu.add_node_type(layout, "GeometryNodeTriangulate")


class NODE_MT_custom_add_menu_mesh_data(MenuBaseClass):
    bl_label = "Mesh Data"
    bl_idname = "NODE_MT_custom_add_menu_mesh_data"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeInputMeshEdgeAngle")
        node_add_menu.add_node_type(layout, "GeometryNodeInputMeshEdgeNeighbors")
        node_add_menu.add_node_type(layout, "GeometryNodeInputMeshEdgeVertices")
        node_add_menu.add_node_type(layout, "GeometryNodeInputMeshFaceArea")
        node_add_menu.add_node_type(layout, "GeometryNodeInputMeshFaceNeighbors")
        node_add_menu.add_node_type(layout, "GeometryNodeMeshFaceSetBoundaries")
        node_add_menu.add_node_type(layout, "GeometryNodeInputMeshFaceIsPlanar")
        node_add_menu.add_node_type(layout, "GeometryNodeInputShadeSmooth")
        node_add_menu.add_node_type(layout, "GeometryNodeInputMeshIsland")
        node_add_menu.add_node_type(layout, "GeometryNodeInputShortestEdgePaths")
        node_add_menu.add_node_type(layout, "GeometryNodeInputMeshVertexNeighbors")


class NODE_MT_custom_add_menu_mesh_setters(MenuBaseClass):
    bl_label = "Mesh Setters"
    bl_idname = "NODE_MT_custom_add_menu_mesh_setters"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeSetShadeSmooth")


class NODE_MT_custom_add_menu_mesh(MenuBaseClass):
    bl_label = "Mesh"
    bl_idname = "NODE_MT_custom_add_menu_mesh"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'
        layout.menu(NODE_MT_custom_add_menu_mesh_data.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_mesh_operations.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_mesh_setters.bl_idname)
        layout.menu(bpy.types.NODE_MT_category_PRIMITIVES_MESH.bl_idname)
        layout.menu(bpy.types.NODE_MT_geometry_node_mesh_topology.bl_idname)

class NODE_MT_custom_add_menu_utilities(MenuBaseClass):
    bl_label = "Utilities"
    bl_idname = "NODE_MT_custom_add_menu_utilities"

    def draw(self, context):
        layout = self.layout
        layout.menu(NODE_MT_custom_add_menu_utilities_converter.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_utilities_fields.bl_idname)
        layout.menu(NODE_MT_custom_add_menu_utilities_rotation.bl_idname)
        layout.separator(factor=spacing)
        layout.menu(bpy.types.NODE_MT_geometry_node_GEO_COLOR.bl_idname)
        layout.menu(bpy.types.NODE_MT_category_GEO_TEXT.bl_idname, text='String')
        layout.menu(bpy.types.NODE_MT_category_GEO_VECTOR.bl_idname)

class NODE_MT_custom_add_menu_utilities_fields(MenuBaseClass):
    bl_label = "Fields"
    bl_idname = "NODE_MT_custom_add_menu_utilities_fields"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "GeometryNodeAccumulateField")
        node_add_menu.add_node_type(layout, "GeometryNodeFieldAtIndex")
        node_add_menu.add_node_type(layout, "GeometryNodeFieldOnDomain")
        node_add_menu.add_node_type(layout, "FunctionNodeRandomValue")

class NODE_MT_custom_add_menu_utilities_rotation(MenuBaseClass):
    bl_label = "Rotation"
    bl_idname = "NODE_MT_custom_add_menu_utilities_rotation"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "FunctionNodeAlignEulerToVector")
        node_add_menu.add_node_type(layout, "FunctionNodeRotateEuler")

class NODE_MT_custom_add_menu_utilities_converter(MenuBaseClass):
    bl_label = "Converter"
    bl_idname = "NODE_MT_custom_add_menu_utilities_converter"

    def draw(self, context):
        layout = self.layout
        node_add_menu.add_node_type(layout, "FunctionNodeBooleanMath")
        node_add_menu.add_node_type(layout, "ShaderNodeClamp")
        node_add_menu.add_node_type(layout, "FunctionNodeCompare")
        node_add_menu.add_node_type(layout, "ShaderNodeFloatCurve")
        node_add_menu.add_node_type(layout, "FunctionNodeFloatToInt")
        node_add_menu.add_node_type(layout, "ShaderNodeMapRange")
        node_add_menu.add_node_type(layout, "ShaderNodeMath")
        node_add_menu.add_node_type(layout, "ShaderNodeMix")
        node_add_menu.add_node_type(layout, "GeometryNodeSwitch")

class NODE_OT_INVOKE_MENU(bpy.types.Operator):
    bl_label = "Invoke Menu"
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
        NODE_MT_custom_add_menu_curves,
        NODE_MT_custom_add_menu_curve_data,
        NODE_MT_custom_add_menu_curve_operations,
        NODE_MT_custom_add_menu_curve_setters,
        NODE_MT_custom_add_menu_input,
        NODE_MT_custom_add_menu_input_constants,
        NODE_MT_custom_add_menu_input_fields,
        NODE_MT_custom_add_menu_mesh,
        NODE_MT_custom_add_menu_mesh_data,
        NODE_MT_custom_add_menu_mesh_operations,
        NODE_MT_custom_add_menu_mesh_setters,
        NODE_MT_custom_add_menu_utilities,
        NODE_MT_custom_add_menu_utilities_fields,
        NODE_MT_custom_add_menu_utilities_rotation,
        NODE_MT_custom_add_menu_utilities_converter,
        NODE_OT_INVOKE_MENU,
        )

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    with open("addon_menus.json", "r") as f:
        addon_menus = json.loads(f.read())

    append_addon_menus(addon_menus)

def unregister():
    for draw_func in addon_draw_funcs:
        bpy.types.NODE_MT_custom_add_menu.remove(draw_func)

    for cls in classes:
        bpy.utils.unregister_class(cls)

