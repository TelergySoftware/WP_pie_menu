from .wpm_main_panel import *


class WPM_UL_Brushes_List(bpy.types.UIList):
    """List of Brushes"""
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=item.name, translate=False, icon_value=182)
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=icon)


class WPM_PT_Brushes_Subpanel(WPM_PT_Base_Panel):
    """ Subpanel to organize the brushes in the pie menu """
    bl_idname = "WPM_PT_Brushes_Subpanel"
    bl_label = "Brushes"
    bl_parent_id = "WPM_PT_Main_Panel"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Brushes:")
        
        row = layout.row()
        
        col = row.column()
        col.template_list("WPM_UL_Brushes_List", "", bpy.context.scene, "wpm_brushes", bpy.context.scene, "wpm_brushes_index", rows=8, maxrows=8)
        
        col = row.column()
        col_item = col.column(align=True)
        col_item.operator("wpm.brushes_add", icon='ADD', text="")
        
        col_item = col.column(align=True)
        col_item.operator("wpm.brushes_remove", icon='REMOVE', text="")
        
        col_item = col.column(align=True)
        col_item.separator()
        
        col_item = col.column(align=True)
        col_item.operator("wpm.move_brush_up", icon='TRIA_UP', text="")
        
        col_item = col.column(align=True)
        col_item.operator("wpm.move_brush_down", icon='TRIA_DOWN', text="")
        