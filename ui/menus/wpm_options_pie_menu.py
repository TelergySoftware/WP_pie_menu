import bpy


class WPM_MT_Options_Pie_Menu(bpy.types.Menu):
    """Pie Menu for Options"""
    bl_idname = "WPM_MT_Options_Pie_Menu"
    bl_label = "WPM Options"
    
    # This menu is only visible in 'PAINT_WEIGHT' mode
    @classmethod
    def poll(cls, context):
        is_weight_paint = context.mode == 'PAINT_WEIGHT'
        return is_weight_paint

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.separator()
        pie.separator()
        pie.separator()
        # 4 - LEFT
        if context.space_data.show_object_viewport_armature:
            pie.operator("wpm.toggle_bone_visibility", text="Bone Visibility", icon='HIDE_ON')
        else:
            pie.operator("wpm.toggle_bone_visibility", text="Bone Visibility", icon='HIDE_OFF')
        # # 6 - RIGHT
        # pie.operator("wpm.set_brush_add", text="Add", icon='ADD')
        # # 2 - BOTTOM
        # pie.operator("wpm.set_brush_subtract", text="Subtract", icon='SUBTRACT')
        # # 8 - TOP
        # pie.operator("wpm.set_brush_multiply", text="Multiply", icon='MULTIPLY')
        # # 7 - TOP - LEFT
        # pie.operator("wpm.set_brush_darken", text="Darken", icon='SOLID')
        # # 9 - TOP - RIGHT
        # pie.operator("wpm.set_brush_lighten", text="Lighten", icon='LIGHT_SUN')
        # # 1 - BOTTOM - LEFT
        # pie.operator("wpm.set_brush_blur", text="Blur", icon='BRUSH_BLUR')
        # # 3 - BOTTOM - RIGHT
        # pie.operator("wpm.set_brush_average", text="Average", icon='BRUSH_TEXDRAW')