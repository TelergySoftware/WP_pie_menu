# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy

# Import all UI classes
from .ui import WPM_MT_Pie_Menu, WPM_MT_Brush_Options_Pie_Menu, WPM_MT_Options_Pie_Menu
from .ui import WPM_PT_Main_Panel, WPM_PT_Brushes_Subpanel, WPM_UL_Brushes_List
# Import all operator classes
from .operators import (
    # Draw Brushes
    WPM_OT_Reset_Brushes,
    WPM_OT_Set_Brush,
    # Options
    WPM_OT_Toggle_Bone_Visibility,
    # Brushes List
    WPM_OT_Brushes_Add,
    WPM_OT_Brushes_Remove,
    WPM_OT_Move_Brush_Down,
    WPM_OT_Move_Brush_Up
)
# Import all property classes
from .properties import WPM_Properties, WPM_Brushes_Properties

# Add imported classes to classes to register
CLASSES_TO_REGISTER = [
    # UI classes
    WPM_MT_Pie_Menu,
    WPM_MT_Brush_Options_Pie_Menu,
    WPM_MT_Options_Pie_Menu,
    WPM_PT_Main_Panel,
    WPM_PT_Brushes_Subpanel,
    WPM_UL_Brushes_List,
    # Operator classes
    WPM_OT_Brushes_Add,
    WPM_OT_Brushes_Remove,
    WPM_OT_Move_Brush_Down,
    WPM_OT_Move_Brush_Up,
    WPM_OT_Reset_Brushes,
    WPM_OT_Set_Brush,
    WPM_OT_Toggle_Bone_Visibility,
    # Property classes
    WPM_Brushes_Properties,
    WPM_Properties,
]

bl_info = {
    "name" : "Weight Paint Pie Menu",
    "author" : "Telergy Studio",
    "description" : """A bundle of tools to make Weight Painting more efficient.""",
    "blender" : (3, 0, 0),
    "version" : (1, 0, 0),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

# Keymap references
keymaps = []

def register():
    # Register classes
    for cls in CLASSES_TO_REGISTER:
        bpy.utils.register_class(cls)
        
    # Register properties to scene
    bpy.types.Scene.wpm_properties = bpy.props.PointerProperty(type=WPM_Properties)
    bpy.types.Scene.wpm_brushes = bpy.props.CollectionProperty(type=WPM_Brushes_Properties)
    bpy.types.Scene.wpm_brushes_index = bpy.props.IntProperty(name="Brush Index", default=0)
        
    # Add keymaps
    wm = bpy.context.window_manager
    # Add new Keymap
    km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
    # Add new Keymap items to call the WPM_MT_Pie_Menu
    kmi = km.keymap_items.new('wm.call_menu_pie', 'D', 'PRESS')
    kmi.properties.name = 'WPM_MT_Pie_Menu'
    kmi.active = True
    keymaps.append((km, kmi))
    
    km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = km.keymap_items.new('wm.call_menu_pie', 'D', 'PRESS', shift=True)
    kmi.properties.name = 'WPM_MT_Brush_Options_Pie_Menu'
    kmi.active = True
    keymaps.append((km, kmi))
    
    km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = km.keymap_items.new('wm.call_menu_pie', 'X', 'PRESS')
    kmi.properties.name = 'WPM_MT_Options_Pie_Menu'
    kmi.active = True
    keymaps.append((km, kmi))

def unregister():
    # Unregister properties from scene
    del bpy.types.Scene.wpm_brushes_index
    del bpy.types.Scene.wpm_brushes
    del bpy.types.Scene.wpm_properties

     # Clear keymaps
    for km, kmi in keymaps:
        km.keymap_items.remove(kmi)
    keymaps.clear()
    
    # Unregister classes
    for cls in CLASSES_TO_REGISTER:
        bpy.utils.unregister_class(cls)
