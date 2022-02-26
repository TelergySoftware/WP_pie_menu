# Add all classes from wpm_main_panel.py here.
from .wpm_main_panel import WPM_PT_Main_Panel
# Add all classes from wpm_brushes_subpanel.py here.
from .wpm_brushes_subpanel import WPM_PT_Brushes_Subpanel, WPM_UL_Brushes_List

__all__ = [
    # Main Panel
    WPM_PT_Main_Panel,
    # Brushes Subpanel
    WPM_PT_Brushes_Subpanel,
    WPM_UL_Brushes_List,
]