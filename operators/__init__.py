# Add all classes from  wpm_set_brush_operators.py here.
from .wpm_set_brush_operators import (
    # Draw Brushes
    WPM_OT_Set_Brush,
    WPM_OT_Reset_Brushes,
)
# Add all classes from  wpm_set_options.py here.
from .wpm_set_options import (
    WPM_OT_Toggle_Bone_Visibility,
)

# Add all classes from wpm_brushes_list_operators.py here.
from .wpm_brushes_list_operators import (
    WPM_OT_Brushes_Add,
    WPM_OT_Brushes_Remove,
    WPM_OT_Move_Brush_Down,
    WPM_OT_Move_Brush_Up,
)

__all__ = [
    # Set Brush Operators
    WPM_OT_Set_Brush,
    # Brushes List Operators
    WPM_OT_Brushes_Add,
    WPM_OT_Brushes_Remove,
    WPM_OT_Move_Brush_Down,
    WPM_OT_Move_Brush_Up,
    WPM_OT_Reset_Brushes,
    # Options
    WPM_OT_Toggle_Bone_Visibility,
]