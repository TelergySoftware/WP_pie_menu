import bpy


class WPM_OT_Base_Operator(bpy.types.Operator):
    
    @classmethod
    def poll(cls, context):
        is_weight_paint = context.mode == 'PAINT_WEIGHT'
        is_view3d = context.area.type == 'VIEW_3D'
        return is_weight_paint and is_view3d
 

class WPM_OT_Set_Brush_Draw(WPM_OT_Base_Operator, bpy.types.Operator):
    bl_idname = "wpm.set_brush_draw"
    bl_label = "Set Draw"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        # Set brush to draw mode
        context.tool_settings.weight_paint.brush = bpy.data.brushes['Draw']
        return {'FINISHED'}


class WPM_OT_Set_Brush_Add(WPM_OT_Base_Operator):
    """Set brush to add mode"""
    bl_idname = "wpm.set_brush_add"
    bl_label = "Set Add"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Set brush to add mode
        context.tool_settings.weight_paint.brush = bpy.data.brushes['Add']
        return {'FINISHED'}


class WPM_OT_Set_Brush_Subtract(WPM_OT_Base_Operator):
    """Set brush to subtract mode"""
    bl_idname = "wpm.set_brush_subtract"
    bl_label = "Set Subtract"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Set brush to subtract mode
        context.tool_settings.weight_paint.brush = bpy.data.brushes['Subtract']
        return {'FINISHED'}

class WPM_OT_Set_Brush_Multiply(WPM_OT_Base_Operator):
    """Set brush to multiply mode"""
    bl_idname = "wpm.set_brush_multiply"
    bl_label = "Set Multiply"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Set brush to multiply mode
        context.tool_settings.weight_paint.brush = bpy.data.brushes['Multiply']
        return {'FINISHED'}


class WPM_OT_Set_Brush_Lighten(WPM_OT_Base_Operator):
    """Set brush to lighten mode"""
    bl_idname = "wpm.set_brush_lighten"
    bl_label = "Set Lighten"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Set brush to lighten mode
        context.tool_settings.weight_paint.brush = bpy.data.brushes['Lighten']
        return {'FINISHED'}


class WPM_OT_Set_Brush_Darken(WPM_OT_Base_Operator):
    """Set brush to darken mode"""
    bl_idname = "wpm.set_brush_darken"
    bl_label = "Set Darken"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Set brush to darken mode
        context.tool_settings.weight_paint.brush = bpy.data.brushes['Darken']
        return {'FINISHED'}
    

class WPM_OT_Set_Brush_Blur(WPM_OT_Base_Operator):
    """Set brush to Blur"""
    bl_idname = "wpm.set_brush_blur"
    bl_label = "Set Blur"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Set brush to Blur
        context.tool_settings.weight_paint.brush = bpy.data.brushes['Blur']
        return {'FINISHED'}


class WPM_OT_Set_Brush_Average(WPM_OT_Base_Operator):
    """Set brush to Average"""
    bl_idname = "wpm.set_brush_average"
    bl_label = "Set Average"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Set brush to Average
        context.tool_settings.weight_paint.brush = bpy.data.brushes['Average']
        return {'FINISHED'}
