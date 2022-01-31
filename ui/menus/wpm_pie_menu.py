import bpy


class WPM_MT_Pie_Menu(bpy.types.Menu):
    bl_idname = "WPM_MT_Pie_Menu"
    bl_label = "WPM Pie Menu"
    
    # This menu is only visible in 'PAINT_WEIGHT' mode
    @classmethod
    def poll(cls, context):
        is_weight_paint = context.mode == 'PAINT_WEIGHT'
        return is_weight_paint

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("wpm.set_brush_draw", text="Draw", icon='GREASEPENCIL')
        pie.operator("wpm.set_brush_add", text="Add", icon='ADD')
        pie.operator("wpm.set_brush_blur", text="Blur", icon='MATFLUID')
        pie.operator("wpm.set_brush_subtract", text="Subtract", icon='REMOVE')
        pie.operator("wpm.set_brush_darken", text="Darken", icon='MESH_CIRCLE')
        pie.operator("wpm.set_brush_lighten", text="Lighten", icon='SHADING_SOLID')
        pie.operator("wpm.set_brush_multiply", text="Multiply", icon='PANEL_CLOSE')
        pie.operator("wpm.set_brush_average", text="Average", icon='CLIPUV_HLT')