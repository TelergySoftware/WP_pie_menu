from email.policy import default
import re
import bpy


class WPM_OT_Base_Operator(bpy.types.Operator):
    
    @classmethod
    def poll(cls, context):
        is_weight_paint = context.mode == 'PAINT_WEIGHT'
        is_view3d = context.area.type == 'VIEW_3D'
        return is_weight_paint and is_view3d
 

class WPM_OT_Set_Brush(WPM_OT_Base_Operator):
    bl_idname = "wpm.set_brush"
    bl_label = "Set Brush"
    bl_options = {'REGISTER', 'UNDO'}
    
    brush: bpy.props.StringProperty(default="Draw")
    
    def execute(self, context):
        # Set brush
        context.tool_settings.weight_paint.brush = bpy.data.brushes[self.brush]
        return {'FINISHED'}

class WPM_OT_Reset_Brushes(WPM_OT_Base_Operator):
    """Reset all brushes to default"""
    bl_idname = "wpm.reset_brushes"
    bl_label = "Reset Brushes"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        is_weight_paint = context.mode == 'PAINT_WEIGHT'
        is_view3d = context.area.type == 'VIEW_3D'
        return is_weight_paint and is_view3d

    def execute(self, context):
        # Reset all brushes to default
        # Get the CollectionGroup of Brushes wpm_brushes
        brushes = context.scene.wpm_brushes
        
        # Clear the collection
        brushes.clear()
        # Add the default brushes
        for _ in range(8):
            brushes.add()
        
        brushes[0].name = 'Draw'
        brushes[0].icon = 'GREASEPENCIL'
        brushes[0].brush = bpy.data.brushes['Draw']
        brushes[1].name = 'Add'
        brushes[1].icon = 'ADD'
        brushes[1].brush = bpy.data.brushes['Add']
        brushes[2].name = 'Blur'
        brushes[2].icon = 'MATFLUID'
        brushes[2].brush = bpy.data.brushes['Blur']
        brushes[3].name = 'Subtract'
        brushes[3].icon = 'REMOVE'
        brushes[3].brush = bpy.data.brushes['Subtract']
        brushes[4].name = 'Darken'
        brushes[4].icon = 'RADIOBUT_OFF'
        brushes[4].brush = bpy.data.brushes['Darken']
        brushes[5].name = 'Lighten'
        brushes[5].icon = 'RADIOBUT_ON'
        brushes[5].brush = bpy.data.brushes['Lighten']
        brushes[6].name = 'Multiply'
        brushes[6].icon = 'PANEL_CLOSE'
        brushes[6].brush = bpy.data.brushes['Multiply']
        brushes[7].name = 'Average'
        brushes[7].icon = 'CLIPUV_HLT'
        brushes[7].brush = bpy.data.brushes['Average']
        
        return {'FINISHED'}
