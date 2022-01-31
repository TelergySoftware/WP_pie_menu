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
from .ui import WPM_MT_Pie_Menu
# Import all operator classes
from .operators import (
    # Draw Brushes
    WPM_OT_Set_Brush_Draw,
    WPM_OT_Set_Brush_Add,
    WPM_OT_Set_Brush_Subtract,
    WPM_OT_Set_Brush_Multiply,
    WPM_OT_Set_Brush_Darken,
    WPM_OT_Set_Brush_Lighten,
    WPM_OT_Set_Brush_Blur,
    WPM_OT_Set_Brush_Average,
)

# Add imported classes to classes to register
CLASSES_TO_REGISTER = [
    # UI classes
    WPM_MT_Pie_Menu,
    # Operator classes
    WPM_OT_Set_Brush_Draw,
    WPM_OT_Set_Brush_Add,
    WPM_OT_Set_Brush_Subtract,
    WPM_OT_Set_Brush_Multiply,
    WPM_OT_Set_Brush_Darken,
    WPM_OT_Set_Brush_Lighten,
    WPM_OT_Set_Brush_Average,
    WPM_OT_Set_Brush_Blur,
]

bl_info = {
    "name" : "Weight Paint Pie Menu",
    "author" : "Telergy Studio",
    "description" : "",
    "blender" : (3, 0, 0),
    "version" : (0, 0, 1),
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
        
    # Add keymaps
    wm = bpy.context.window_manager
    # Add new Keymap
    km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
    # Add new Keymap items to call the WPM_MT_Pie_Menu
    kmi = km.keymap_items.new('wm.call_menu_pie', 'D', 'PRESS')
    kmi.properties.name = 'WPM_MT_Pie_Menu'
    kmi.active = True
    keymaps.append((km, kmi))

def unregister():
     # Clear keymaps
    for km, kmi in keymaps:
        km.keymap_items.remove(kmi)
    keymaps.clear()
    
    # Unregister classes
    for cls in CLASSES_TO_REGISTER:
        bpy.utils.unregister_class(cls)
