import bpy


class WPM_PT_Base_Panel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'WPM'
    
    @classmethod
    def polls(self, context):
        is_weight_paint = context.mode == 'PAINT_WEIGHT'
        return is_weight_paint


class WPM_PT_Main_Panel(WPM_PT_Base_Panel):
    """Panel for WPM"""
    bl_idname = "WPM_PT_Main_Panel"
    bl_label = "WPM"
    
    def __init__(self) -> None:
        super().__init__()
        brushes = bpy.context.scene.wpm_brushes
        if len(brushes) == 0:
            bpy.ops.wpm.reset_brushes()
    
    def draw(self, context):
        """Draw Subpanels"""
