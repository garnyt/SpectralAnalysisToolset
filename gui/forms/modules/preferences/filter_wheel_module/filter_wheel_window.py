###
#
#
#
# Program Description :
# Created By          : Benjamin Kleynhans
# Creation Date       : March 1, 2020
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : November 18, 2019
# Filename            : filter_wheel_window.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_window import Gui_Window
from gui.forms.modules.preferences.filter_wheel_module.filter_wheel_frame.filter_wheel_frame import Filter_Wheel_Frame
from gui.tools.save_file import Save_File
import pdb

class Filter_Wheel_Window(Gui_Window):

    # filter_wheel Window constructor
    def __init__(self, root, master):

        Gui_Window.__init__(self, root, master, "filter_wheel_window", "Filter_Wheel")
        self.create_filter_wheel_window(master)


    # Create the actual window as a separate window
    def create_filter_wheel_window(self, master):

        master.windows[self.window_name].protocol("WM_DELETE_WINDOW", lambda: self.on_closing(master))

        # Add the filter_wheel frame to the window
        Filter_Wheel_Frame(self.root, master.windows[self.window_name])


    # Save changes made to connection
    def save_changes(self, master):

        Save_File(self.root, master, 'config')

        master.windows[self.window_name].destroy()


    # Action to perform when connection window is closed
    def on_closing(self, master):

        if messagebox.askyesno("Save Preferences", "Do you wish to save your changes?"):
            self.save_changes(master)
        else:
            master.windows[self.window_name].destroy()