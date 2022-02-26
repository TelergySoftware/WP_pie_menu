import bpy


class WPM_OT_Brushes_Add(bpy.types.Operator):
    """Add a new brush"""
    bl_idname = "wpm.brushes_add"
    bl_label = "Add Brush"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        is_full = len(context.scene.wpm_brushes) >= 8
        return not is_full

    def execute(self, context):
        brushes = context.scene.wpm_brushes
        new_brush = brushes.add()
        new_brush.name = "Draw"
        new_brush.icon = "GREASEPENCIL"
        new_brush.brush = bpy.data.brushes.new(name=new_brush.name)
        return {'FINISHED'}


class WPM_OT_Brushes_Remove(bpy.types.Operator):
    """Remove a brush"""
    bl_idname = "wpm.brushes_remove"
    bl_label = "Remove Brush"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        is_empty = len(context.scene.wpm_brushes) == 0
        return not is_empty

    def execute(self, context):
        brushes = context.scene.wpm_brushes
        index = context.scene.wpm_brushes_index
        brushes.remove(index)
        context.scene.wpm_brushes_index = min(max(0, index - 1), len(brushes) - 1)
        return {'FINISHED'}


class WPM_OT_Move_Brush_Up(bpy.types.Operator):
    """Move the selected brush up"""
    bl_idname = "wpm.move_brush_up"
    bl_label = "Move Brush Up"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        is_empty = len(context.scene.wpm_brushes) == 0
        return not is_empty

    def execute(self, context):
        brushes = context.scene.wpm_brushes
        index = context.scene.wpm_brushes_index
        if index > 0:
            brushes[index].name, brushes[index - 1].name = brushes[index - 1].name, brushes[index].name
            brushes[index].brush, brushes[index - 1].brush = brushes[index - 1].brush, brushes[index].brush
            context.scene.wpm_brushes_index = index - 1
        return {'FINISHED'}


class WPM_OT_Move_Brush_Down(bpy.types.Operator):
    """Move the selected brush down"""
    bl_idname = "wpm.move_brush_down"
    bl_label = "Move Brush Down"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        is_empty = len(context.scene.wpm_brushes) == 0
        return not is_empty

    def execute(self, context):
        brushes = context.scene.wpm_brushes
        index = context.scene.wpm_brushes_index
        if index < len(brushes) - 1:
            brushes[index].name, brushes[index + 1].name = brushes[index + 1].name, brushes[index].name
            brushes[index].brush, brushes[index + 1].brush = brushes[index + 1].brush, brushes[index].brush
            context.scene.wpm_brushes_index = index + 1
        return {'FINISHED'}