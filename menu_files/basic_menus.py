import bpy
import json
from pathlib import Path
from bl_ui import node_add_menu
from bpy.app.translations import (
    pgettext_iface as iface_,
    contexts as i18n_contexts,
)

from .__baseclasses import BaseMenu
from .__globals import (
    draw_assets_for_catalog,
    add_node_type,
    spacing,
)


class NODE_MT_custom_add_menu_attribute(BaseMenu):
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

class NODE_MT_custom_add_menu_input_scene(BaseMenu):
    bl_label = "Scene"
    bl_idname = "NODE_MT_custom_add_menu_input_scene"

    def draw(self, context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeCollectionInfo")
        add_node_type(layout, "GeometryNodeObjectInfo")
        add_node_type(layout, "GeometryNodeSelfObject")
        add_node_type(layout, "GeometryNodeIsViewport")
        add_node_type(layout, "GeometryNodeInputSceneTime")

class NODE_MT_custom_add_menu_input_fields(BaseMenu):
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

class NODE_MT_custom_add_menu_input_constants(BaseMenu):
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

class NODE_MT_custom_add_menu_output(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_output"
    bl_label = "Output"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeViewer")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)
        
class NODE_MT_custom_add_menu_geometry(BaseMenu):
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
        
class NODE_MT_custom_add_menu_mesh_data(BaseMenu):
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

class NODE_MT_custom_add_menu_mesh_operations(BaseMenu):
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

class NODE_MT_custom_add_menu_mesh_setters(BaseMenu):
    bl_label = "Set Mesh Data"
    bl_idname = "NODE_MT_custom_add_menu_mesh_setters"

    def draw(self, context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeSetShadeSmooth")

class NODE_MT_custom_add_menu_mesh_primitives(BaseMenu):
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
        
class NODE_MT_custom_add_menu_mesh_topology(BaseMenu):
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

class NODE_MT_custom_add_menu_curve_data(BaseMenu):
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

class NODE_MT_custom_add_menu_curve_operations(BaseMenu):
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

class NODE_MT_custom_add_menu_curve_setters(BaseMenu):
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

class NODE_MT_custom_add_menu_curve_primitives(BaseMenu):
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
        
class NODE_MT_custom_add_menu_curve_topology(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_curve_topology"
    bl_label = "Curve Topology"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeOffsetPointInCurve")
        add_node_type(layout, "GeometryNodeCurveOfPoint")
        add_node_type(layout, "GeometryNodePointsOfCurve")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)

class NODE_MT_custom_add_menu_instance(BaseMenu):
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
        
class NODE_MT_custom_add_menu_point(BaseMenu):
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
        
class NODE_MT_custom_add_menu_volume(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_volume"
    bl_label = "Volume"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeVolumeCube")
        add_node_type(layout, "GeometryNodeVolumeToMesh")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)
        
class NODE_MT_custom_add_menu_material(BaseMenu):
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
        
class NODE_MT_custom_add_menu_texture(BaseMenu):
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
        
class NODE_MT_custom_add_menu_utilities_color(BaseMenu):
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
        
class NODE_MT_custom_add_menu_utilities_string(BaseMenu):
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

class NODE_MT_custom_add_menu_utilities_vector(BaseMenu):
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
               
class NODE_MT_custom_add_menu_utilities_fields(BaseMenu):
    bl_label = "Fields"
    bl_idname = "NODE_MT_custom_add_menu_utilities_fields"

    def draw(self, context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeAccumulateField")
        add_node_type(layout, "GeometryNodeFieldAtIndex")
        add_node_type(layout, "GeometryNodeFieldOnDomain")
        add_node_type(layout, "FunctionNodeRandomValue")

class NODE_MT_custom_add_menu_utilities_rotation(BaseMenu):
    bl_label = "Rotation"
    bl_idname = "NODE_MT_custom_add_menu_utilities_rotation"

    def draw(self, context):
        layout = self.layout
        add_node_type(layout, "FunctionNodeAlignEulerToVector")
        add_node_type(layout, "FunctionNodeRotateEuler")

class NODE_MT_custom_add_menu_utilities_converter(BaseMenu):
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

class NODE_MT_custom_add_menu_UV(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_UV"
    bl_label = "UV"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "GeometryNodeUVPackIslands")
        add_node_type(layout, "GeometryNodeUVUnwrap")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)
        
class NODE_MT_custom_add_menu_group(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_group"
    bl_label = "Group"

    def draw(self, context):
        layout = self.layout
        node_add_menu.draw_node_group_add_menu(context, layout)
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)
        
class NODE_MT_custom_add_menu_layout(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_layout"
    bl_label = "Layout"

    def draw(self, _context):
        layout = self.layout
        add_node_type(layout, "NodeFrame")
        add_node_type(layout, "NodeReroute")
        draw_assets_for_catalog(layout, catalog_path=self.bl_label)

classes = (
        NODE_MT_custom_add_menu_attribute,
        NODE_MT_custom_add_menu_input_scene,
        NODE_MT_custom_add_menu_input_fields,
        NODE_MT_custom_add_menu_input_constants,
        NODE_MT_custom_add_menu_output,
        NODE_MT_custom_add_menu_geometry,
        NODE_MT_custom_add_menu_mesh_data,
        NODE_MT_custom_add_menu_mesh_operations,
        NODE_MT_custom_add_menu_mesh_setters,
        NODE_MT_custom_add_menu_mesh_primitives,
        NODE_MT_custom_add_menu_mesh_topology,
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
        NODE_MT_custom_add_menu_utilities_color,
        NODE_MT_custom_add_menu_utilities_string,
        NODE_MT_custom_add_menu_utilities_vector,
        NODE_MT_custom_add_menu_utilities_fields,
        NODE_MT_custom_add_menu_utilities_rotation,
        NODE_MT_custom_add_menu_utilities_converter,
        NODE_MT_custom_add_menu_UV,
        NODE_MT_custom_add_menu_group,
        NODE_MT_custom_add_menu_layout,
        )

def register():  
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
