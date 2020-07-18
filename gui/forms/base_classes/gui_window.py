###
#
#
#
# Program Description : Base class for all Windows in the GUI
# Created By          : Benjamin Kleynhans
# Creation Date       : May 30, 2019
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : August 30, 2019
# Filename            : gui_window.py
#
###

# Imports
from tkinter import *
from tkinter import ttk


class Gui_Window():

    # Settings Window constructor
    def __init__(self, root, master, window_name, window_title):

        self.root = root

        self.window_name = window_name
        self.window_title = window_title

        self.create_gui_window(master)


    # Create the actual window as a separate window
    def create_gui_window(self, master):

        self.gui_window = Toplevel(master)

        # Create frame container to easily access frames from other areas in the gui
        self.frames = {}
        self.gui_window.frames = self.frames

        # Create notebook container to easily access notebooks from other areas in the gui
        self.notebooks = {}
        self.gui_window_notebooks = self.notebooks

        # Create widgets container to easily access widgets from other areas in the gui
        self.widgets = {}
        self.gui_window.widgets = self.widgets

         # Create widgets container to easily access widgets from other areas in the gui
        self.canvases = {}
        self.gui_window.canvases = self.canvases

        # Create toolbar container to easily access toolbars from other areas in the gui
        self.toolbars = {}
        self.gui_window.toolbars = self.toolbars

        # Create window container to easily access windows from other areas in the gui
        self.windows = {}
        self.gui_window.windows = self.windows

        self.root.classes[self.window_name] = self
        self.root.windows[self.window_name] = self.gui_window
        master.windows[self.window_name] = self.gui_window