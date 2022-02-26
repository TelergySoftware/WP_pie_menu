import bpy


class WPM_OT_Toggle_Bone_Visibility(bpy.types.Operator):
    """Toggle bone visibility"""
    bl_idname = "wpm.toggle_bone_visibility"
    bl_label = "Toggle Bone Visibility"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Toggle bone visibility
        context.space_data.show_object_viewport_armature = not context.space_data.show_object_viewport_armature
        return {'FINISHED'}