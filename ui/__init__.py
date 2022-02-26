# Add all classes from the menus package here.
from .menus import WPM_MT_Pie_Menu, WPM_MT_Options_Pie_Menu
# Add all classes from the panels package here.
from .panels import WPM_PT_Main_Panel, WPM_PT_Brushes_Subpanel, WPM_UL_Brushes_List

__all__ = [
    # Menus    
    WPM_MT_Pie_Menu,
    WPM_MT_Options_Pie_Menu,
    # Panels
    WPM_PT_Main_Panel,
    WPM_PT_Brushes_Subpanel,
    WPM_UL_Brushes_List,
]