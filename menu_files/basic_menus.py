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
    
    draw_assets = True
    items = [
        "GeometryNodeAttributeStatistic",
        "GeometryNodeAttributeDomainSize",
        "SeparateMenu",
        "GeometryNodeCaptureAttribute",
        "GeometryNodeStoreNamedAttribute",
        "GeometryNodeRemoveAttribute",
    ]

class NODE_MT_custom_add_menu_input_scene(BaseMenu):
    bl_label = "Scene"
    bl_idname = "NODE_MT_custom_add_menu_input_scene"

    items = [
        "GeometryNodeCollectionInfo",
        "GeometryNodeObjectInfo",
        "GeometryNodeSelfObject",
        "GeometryNodeIsViewport",
        "GeometryNodeInputSceneTime",
    ]

class NODE_MT_custom_add_menu_input_fields(BaseMenu):
    bl_label = "Fields"
    bl_idname = "NODE_MT_custom_add_menu_input_fields"

    items = [
        "GeometryNodeInputID",
        "GeometryNodeInputIndex",
        "GeometryNodeInputNamedAttribute",
        "GeometryNodeInputNormal",
        "GeometryNodeInputPosition",
        "GeometryNodeInputRadius",
    ]

class NODE_MT_custom_add_menu_input_constants(BaseMenu):
    bl_label = "Constants"
    bl_idname = "NODE_MT_custom_add_menu_input_constants"

    items = [
        "FunctionNodeInputBool",
        "FunctionNodeInputColor",
        "FunctionNodeInputInt",
        "GeometryNodeInputMaterial",
        "FunctionNodeInputString",
        "ShaderNodeValue",
        "FunctionNodeInputVector",
    ]
    
class NODE_MT_custom_add_menu_output(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_output"
    bl_label = "Output"

    draw_assets = True
    items = ["GeometryNodeViewer",]

class NODE_MT_custom_add_menu_geometry(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_geometry"
    bl_label = "Geometry"

    draw_assets = True
    items = [
        "GeometryNodeBoundBox",
        "GeometryNodeConvexHull",
        "GeometryNodeDeleteGeometry",
        "GeometryNodeDuplicateElements",
        "GeometryNodeMergeByDistance",
        "GeometryNodeTransform",
        "SeparateMenu",
        "GeometryNodeJoinGeometry",
        "GeometryNodeGeometryToInstance",
        "SeparateMenu",
        "GeometryNodeRaycast",
        {"GeometryNodeProximity": {"label": "Proximity"}},
        "GeometryNodeSampleIndex",
        "GeometryNodeSampleNearest",
        "SeparateMenu",
        "GeometryNodeSeparateComponents",
        "GeometryNodeSeparateGeometry",
        "SeparateMenu",
        "GeometryNodeSetID",
        "GeometryNodeSetPosition",
        ]

class NODE_MT_custom_add_menu_mesh_data(BaseMenu):
    bl_label = "Get Mesh Data"
    bl_idname = "NODE_MT_custom_add_menu_mesh_data"

    items = [
        "GeometryNodeInputMeshVertexNeighbors",
        "SeparateMenu",
        "GeometryNodeInputMeshEdgeAngle",
        "GeometryNodeInputMeshEdgeNeighbors",
        "GeometryNodeInputMeshEdgeVertices",
        "SeparateMenu",
        "GeometryNodeInputMeshFaceArea",
        "GeometryNodeInputMeshFaceNeighbors",
        "GeometryNodeMeshFaceSetBoundaries",
        "SeparateMenu",
        "GeometryNodeInputMeshFaceIsPlanar",
        "GeometryNodeInputShadeSmooth",
        "SeparateMenu",
        "GeometryNodeInputMeshIsland",
        "GeometryNodeInputShortestEdgePaths",
        ]

class NODE_MT_custom_add_menu_mesh_operations(BaseMenu):
    bl_label = "Mesh Operations"
    bl_idname = "NODE_MT_custom_add_menu_mesh_operations"

    items = [
        "GeometryNodeDualMesh",
        "GeometryNodeExtrudeMesh",
        "GeometryNodeFlipFaces",
        "GeometryNodeSplitEdges",
        "GeometryNodeScaleElements",
        "SeparateMenu",
        "GeometryNodeEdgePathsToCurves",
        "GeometryNodeEdgePathsToSelection",
        "SeparateMenu",
        "GeometryNodeMeshBoolean",
        "GeometryNodeMeshToCurve",
        "GeometryNodeMeshToPoints",
        "GeometryNodeMeshToVolume",
        "SeparateMenu",
        "GeometryNodeSampleNearestSurface",
        "GeometryNodeSampleUVSurface",
        "SeparateMenu",
        "GeometryNodeSubdivideMesh",
        "GeometryNodeSubdivisionSurface",
        "GeometryNodeTriangulate",
        ]

class NODE_MT_custom_add_menu_mesh_setters(BaseMenu):
    bl_label = "Set Mesh Data"
    bl_idname = "NODE_MT_custom_add_menu_mesh_setters"

    items = ["GeometryNodeSetShadeSmooth",]

class NODE_MT_custom_add_menu_mesh_primitives(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_mesh_primitives"
    bl_label = "Mesh Primitives"
    
    draw_assets = True
    items = [
        "GeometryNodeMeshCone",
        "GeometryNodeMeshCube",
        "GeometryNodeMeshCylinder",
        "GeometryNodeMeshGrid",
        "GeometryNodeMeshIcoSphere",
        "GeometryNodeMeshCircle",
        "GeometryNodeMeshLine",
        "GeometryNodeMeshUVSphere",
        ]
        
class NODE_MT_custom_add_menu_mesh_topology(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_mesh_topology"
    bl_label = "Mesh Topology"

    draw_assets = True
    items = [
        "GeometryNodeCornersOfFace",
        "GeometryNodeCornersOfVertex",
        "SeparateMenu",
        "GeometryNodeEdgesOfCorner",
        "GeometryNodeEdgesOfVertex",
        "SeparateMenu",
        "GeometryNodeFaceOfCorner",
        "GeometryNodeVertexOfCorner",
        "GeometryNodeOffsetCornerInFace",
        ]

class NODE_MT_custom_add_menu_curve_data(BaseMenu):
    bl_label = "Get Curve Data"
    bl_idname = "NODE_MT_custom_add_menu_curve_data"

    items = [
        "GeometryNodeInputCurveHandlePositions",
        "GeometryNodeInputTangent",
        "GeometryNodeInputCurveTilt",
        "SeparateMenu",
        "GeometryNodeCurveEndpointSelection",
        "GeometryNodeCurveHandleTypeSelection",
        "SeparateMenu",
        "GeometryNodeInputSplineCyclic",
        "GeometryNodeSplineLength",
        "GeometryNodeSplineParameter",
        "GeometryNodeInputSplineResolution",
        ]

class NODE_MT_custom_add_menu_curve_operations(BaseMenu):
    bl_label = "Curve Operations"
    bl_idname = "NODE_MT_custom_add_menu_curve_operations"

    items = [
        "GeometryNodeCurveToMesh",
        "GeometryNodeCurveToPoints",
        "SeparateMenu",
        "GeometryNodeFillCurve",
        "GeometryNodeFilletCurve",
        "GeometryNodeReverseCurve",
        "GeometryNodeTrimCurve",
        "SeparateMenu",
        "GeometryNodeSampleCurve",
        "GeometryNodeResampleCurve",
        "GeometryNodeSubdivideCurve",
        "SeparateMenu",
        "GeometryNodeCurveLength",
        "GeometryNodeDeformCurvesOnSurface",
    ]
    
class NODE_MT_custom_add_menu_curve_setters(BaseMenu):
    bl_label = "Set Curve Data"
    bl_idname = "NODE_MT_custom_add_menu_curve_setters"

    items = [
        "GeometryNodeSetCurveNormal",
        "GeometryNodeSetCurveRadius",
        "GeometryNodeSetCurveTilt",
        "SeparateMenu",
        "GeometryNodeSetCurveHandlePositions",
        "GeometryNodeCurveSetHandles",
        "SeparateMenu",
        "GeometryNodeSetSplineCyclic",
        "GeometryNodeSetSplineResolution",
        "GeometryNodeCurveSplineType",
    ]

class NODE_MT_custom_add_menu_curve_primitives(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_curve_primitives"
    bl_label = "Curve Primitives"

    draw_assets = True
    items = [
        "GeometryNodeCurveArc",
        "GeometryNodeCurvePrimitiveBezierSegment",
        "GeometryNodeCurvePrimitiveCircle",
        "GeometryNodeCurvePrimitiveLine",
        "GeometryNodeCurveSpiral",
        "GeometryNodeCurveQuadraticBezier",
        "GeometryNodeCurvePrimitiveQuadrilateral",
        "GeometryNodeCurveStar",
    ]
        
class NODE_MT_custom_add_menu_curve_topology(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_curve_topology"
    bl_label = "Curve Topology"

    draw_assets = True
    items = [
        "GeometryNodeOffsetPointInCurve",
        "GeometryNodeCurveOfPoint",
        "GeometryNodePointsOfCurve",
    ]

class NODE_MT_custom_add_menu_instance(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_instance"
    bl_label = "Instances"

    draw_assets = True
    items = [
        "GeometryNodeInstanceOnPoints",
        "GeometryNodeInstancesToPoints",
        "SeparateMenu",
        "GeometryNodeRealizeInstances",
        "GeometryNodeRotateInstances",
        "GeometryNodeScaleInstances",
        "GeometryNodeTranslateInstances",
        "SeparateMenu",
        "GeometryNodeInputInstanceRotation",
        "GeometryNodeInputInstanceScale",
        ]

class NODE_MT_custom_add_menu_point(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_point"
    bl_label = "Point"

    draw_assets = True
    items = [
        "GeometryNodeDistributePointsInVolume",
        "GeometryNodeDistributePointsOnFaces",
        "SeparateMenu",
        "GeometryNodePoints",
        "GeometryNodePointsToVertices",
        "GeometryNodePointsToVolume",
        "SeparateMenu",
        "GeometryNodeSetPointRadius",
    ]
        
class NODE_MT_custom_add_menu_volume(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_volume"
    bl_label = "Volume"

    draw_assets = True
    items = [
        "GeometryNodeVolumeCube",
        "GeometryNodeVolumeToMesh",
    ]
        
class NODE_MT_custom_add_menu_material(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_material"
    bl_label = "Material"

    draw_assets = True
    items = [
        "GeometryNodeReplaceMaterial",        
        "SeparateMenu",
        "GeometryNodeInputMaterialIndex",
        "GeometryNodeMaterialSelection",
        "SeparateMenu",
        "GeometryNodeSetMaterial",
        "GeometryNodeSetMaterialIndex",
    ]
        
class NODE_MT_custom_add_menu_texture(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_texture"
    bl_label = "Texture"

    draw_assets = True
    items = [
        "ShaderNodeTexBrick",
        "ShaderNodeTexChecker",
        "ShaderNodeTexGradient",
        "GeometryNodeImageTexture",
        "ShaderNodeTexMagic",
        "ShaderNodeTexMusgrave",
        "ShaderNodeTexNoise",
        "ShaderNodeTexVoronoi",
        "ShaderNodeTexWave",
        "ShaderNodeTexWhiteNoise",
    ]
        
class NODE_MT_custom_add_menu_utilities_color(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_utilities_color"
    bl_label = "Color"

    draw_assets = True
    items = [
        {"ShaderNodeValToRGB": {"label": "Color Ramp"}},
        "ShaderNodeRGBCurve",
        "SeparateMenu",
        {"ShaderNodeMix": {"label": iface_("Mix Color"), "props":{"name": "data_type", "value":"'RGBA'"}}},
        "FunctionNodeCombineColor",
        "FunctionNodeSeparateColor",
    ]

class NODE_MT_custom_add_menu_utilities_string(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_utilities_string"
    bl_label = "String"

    draw_assets = True
    items = [
        "GeometryNodeStringJoin",
        "FunctionNodeReplaceString",
        "FunctionNodeSliceString",
        "SeparateMenu",
        "FunctionNodeStringLength",
        "GeometryNodeStringToCurves",
        "FunctionNodeValueToString",
        "SeparateMenu",
        "FunctionNodeInputSpecialCharacters",
    ]
    
class NODE_MT_custom_add_menu_utilities_vector(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_utilities_vector"
    bl_label = "Vector"

    draw_assets = True
    items = [
        "ShaderNodeVectorCurve",
        "ShaderNodeVectorMath",
        "ShaderNodeVectorRotate",
        "SeparateMenu",
        {"ShaderNodeMix": {"label": iface_("Mix Vector"), "props":{"name": "data_type", "value":"'VECTOR'"}}},
        "ShaderNodeCombineXYZ",
        "ShaderNodeSeparateXYZ",
    ]
    
class NODE_MT_custom_add_menu_utilities_fields(BaseMenu):
    bl_label = "Fields"
    bl_idname = "NODE_MT_custom_add_menu_utilities_fields"

    items = [
        "GeometryNodeAccumulateField",
        "GeometryNodeFieldAtIndex",
        "GeometryNodeFieldOnDomain",
        "FunctionNodeRandomValue",
    ]

class NODE_MT_custom_add_menu_utilities_rotation(BaseMenu):
    bl_label = "Rotation"
    bl_idname = "NODE_MT_custom_add_menu_utilities_rotation"

    items = [
        "FunctionNodeAlignEulerToVector",
        "FunctionNodeRotateEuler",
    ]

class NODE_MT_custom_add_menu_utilities_converter(BaseMenu):
    bl_label = "Converter"
    bl_idname = "NODE_MT_custom_add_menu_utilities_converter"

    items = [
        "FunctionNodeBooleanMath",
        "GeometryNodeSwitch",
        "SeparateMenu",
        "ShaderNodeClamp",
        "FunctionNodeCompare",
        "ShaderNodeFloatCurve",
        "ShaderNodeMapRange",
        "SeparateMenu",
        "ShaderNodeMix",
        "ShaderNodeMath",
        "FunctionNodeFloatToInt",
    ]

class NODE_MT_custom_add_menu_UV(BaseMenu):
    bl_idname = "NODE_MT_custom_add_menu_UV"
    bl_label = "UV"

    draw_assets = True
    items = [
        "GeometryNodeUVPackIslands",
        "GeometryNodeUVUnwrap",
    ]
        
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

    draw_assets = True
    items = [
        "NodeFrame",
        "NodeReroute",
    ]

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
