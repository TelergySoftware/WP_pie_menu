from cmath import pi
import bpy


class WPM_MT_Options_Pie_Menu(bpy.types.Menu):
    """Pie Menu for Options"""
    bl_idname = "WPM_MT_Options_Pie_Menu"
    bl_label = "WPM Options"
    
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
        pie = layout.menu_pie()
        # LEFT
        col = pie.column()
        col.prop(context.scene.tool_settings, "use_auto_normalize", text="Auto Normalize")
        col.prop(context.scene.tool_settings, "use_multipaint", text="Multi Paint")
        # RIGHT
        col = pie.column()
        col.prop(context.object.data, property="use_mirror_vertex_groups", text="Mirror Vertex Groups", toggle=True)
        col.prop(context.object, property="use_mesh_mirror_x", text="Mirror X", toggle=True)
        col.prop(context.object.data, property="use_mirror_topology", text="Mirror Topology", toggle=True)
        
        pie.separator()
        
        # TOP
        if context.space_data.show_object_viewport_armature:
            pie.operator("wpm.toggle_bone_visibility", text="Bone Visibility", icon='HIDE_ON')
        else:
            pie.operator("wpm.toggle_bone_visibility", text="Bone Visibility", icon='HIDE_OFF')


class WPM_MT_Brush_Options_Pie_Menu(bpy.types.Menu):
    """Pie Menu for Brush Options"""
    bl_idname = "WPM_MT_Brush_Options_Pie_Menu"
    bl_label = "WPM Brush Options"
    
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
        brush = context.tool_settings.weight_paint.brush
        options = context.tool_settings.unified_paint_settings
        
        layout = self.layout
        pie = layout.menu_pie()
        
        col = pie.column()
        
        col.prop(brush, property="use_accumulate", text="Accumulate")
        col.prop(brush, property="use_frontface", text="Frontface")
        
        col = pie.column()
        
        row = col.row()
        row.prop(options, property="weight", text="Weight", slider=True)

        row = col.row()
        row.prop(brush, property="strength", text="Strength", slider=True)
        row.prop(brush, property="use_pressure_strength", text="", icon='STYLUS_PRESSURE')