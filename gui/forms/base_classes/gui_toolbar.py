###
#
#
#
# Program Description : Base class for all Toolbars in the GUI
# Created By          : Benjamin Kleynhans
# Creation Date       : February 22, 2020
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : February 22, 2020
# Filename            : gui_toolbar.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
import pdb

class Gui_Toolbar():

    # Main Canvas constructor
    def __init__(self, root, master, toolbar_name):

        self.root = root

        self.toolbar_name = toolbar_name

        self.create_gui_toolbar(master)


    # Create the actual Canvas
    def create_gui_toolbar(self, master):

        self.gui_toolbar = ttk.Frame(master, borderwidth=1, relief=RAISED)

        # Create notebook container to easily access notebooks from other areas in the gui
        self.notebooks = {}
        self.gui_toolbar.notebooks = self.notebooks

        # Create toolbar container to easily access toolbars from other areas in the gui
        self.frames = {}
        self.gui_toolbar.frames = self.frames

        # Create widgets container to easily access widgets from other areas in the gui
        self.widgets = {}
        self.gui_toolbar.widgets = self.widgets

        # Create widgets container to easily access widgets from other areas in the gui
        self.canvases = {}
        self.gui_toolbar.canvases = self.canvases

        # Create widgets container to easily access widgets from other areas in the gui
        self.toolbars = {}
        self.gui_toolbar.toolbars = self.toolbars

        # Create window container to easily access windows from other areas in the gui
        self.windows = {}
        self.gui_toolbar.windows = self.windows

        self.root.classes[self.toolbar_name] = self
        self.root.toolbars[self.toolbar_name] = self.gui_toolbar
        master.toolbars[self.toolbar_name] = self.gui_toolbar