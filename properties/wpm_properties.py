from cgitb import text
import bpy


class WPM_Brushes_Properties(bpy.types.PropertyGroup):
    """Brushes Properties"""
    name: bpy.props.StringProperty(name="Brush Name", default="Brush")
    icon: bpy.props.StringProperty(name="Brush Icon", default="GREASEPENCIL")
    brush: bpy.props.PointerProperty(type=bpy.types.Brush)


class WPM_Properties(bpy.types.PropertyGroup):
    
    auto_normalize: bpy.props.BoolProperty(name="Auto Normalize", default=False)
    