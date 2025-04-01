import bpy


class WPM_PT_Base_Panel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'WPM'
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Ensure the brushes list is initialized
        brushes = bpy.context.scene.wpm_brushes
        if len(brushes) == 0:
            bpy.ops.wpm.reset_brushes()
    
    @classmethod
    def poll(self, context):
        is_weight_paint = context.mode == 'PAINT_WEIGHT'
        return is_weight_paint

class WPM_PT_Main_Panel(WPM_PT_Base_Panel):
    """Panel for WPM"""
    bl_idname = "WPM_PT_Main_Panel"
    bl_label = "WPM"
    
    @classmethod
    def poll(self, context):
        is_weight_paint = context.mode == 'PAINT_WEIGHT'
        return is_weight_paint
    
    def draw(self, context):
        """Draw Subpanels"""
