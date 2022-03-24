import bpy


class WPM_MT_Pie_Menu(bpy.types.Menu):
    bl_idname = "WPM_MT_Pie_Menu"
    bl_label = "WPM Brushes"
    
    def __init__(self) -> None:
        super().__init__()
        brushes = bpy.context.scene.wpm_brushes
        if len(brushes) == 0:
            bpy.ops.wpm.reset_brushes()
    
    # This menu is only visible in 'PAINT_WEIGHT' mode
    @classmethod
    def poll(cls, context):
        is_weight_paint = context.mode == 'PAINT_WEIGHT'
        return is_weight_paint

    def draw(self, context):
        layout = self.layout
        brushes = context.scene.wpm_brushes
        if len(brushes) == 0:
            bpy.ops.wpm.reset_brushes()
        pie = layout.menu_pie()
        for brush in brushes:
            pie.operator("wpm.set_brush", text=f"{brush.name}", icon=f"{brush.icon}").brush = brush.name