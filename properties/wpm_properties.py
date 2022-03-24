import bpy


def update_brush(self, context):
    """Update the brush"""
    # TODO: This needs a better place to be stored.
    default_icons = {'Draw': 'GREASEPENCIL',
                     'Add': 'ADD',
                     'Blur': 'MATFLUID',
                     'Subtract': 'REMOVE',
                     'Darken': 'RADIOBUT_OFF',
                     'Lighten': 'RADIOBUT_ON',
                     'Multiply': 'PANEL_CLOSE',
                     'Average': 'CLIPUV_HLT'}
    
    wpm_brushes = context.scene.wpm_brushes
    wpm_brushes[context.scene.wpm_brushes_index].brush = bpy.data.brushes[self.name]
    wpm_brushes[context.scene.wpm_brushes_index].icon = default_icons[self.name] if self.name in default_icons else 'BRUSH_DATA'


class WPM_Brushes_Properties(bpy.types.PropertyGroup):
    """Brushes Properties"""
    name: bpy.props.StringProperty(name="Brush Name", default="Brush", update=update_brush)
    icon: bpy.props.StringProperty(name="Brush Icon", default="GREASEPENCIL")
    brush: bpy.props.PointerProperty(type=bpy.types.Brush, name="Brush")


class WPM_Properties(bpy.types.PropertyGroup):
    
    auto_normalize: bpy.props.BoolProperty(name="Auto Normalize", default=False)
    