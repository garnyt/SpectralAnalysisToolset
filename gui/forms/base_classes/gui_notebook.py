###
#
#
#
# Program Description : Base class for all Notebooks in the GUI
# Created By          : Benjamin Kleynhans
# Creation Date       : May 28, 2019
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : August 29, 2019
# Filename            : gui_notebook.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
import pdb

class Gui_Notebook():

    # Main Gui Frame constructor
    def __init__(self, root, master, notebook_name):

        self.root = root

        self.notebook_name = notebook_name

        self.create_gui_notebook(master)


    # Create the actual Frame
    def create_gui_notebook(self, master):

        self.gui_notebook = ttk.Notebook(master)

        # Create notebook container to easily access notebooks from other areas in the gui
        self.notebooks = {}
        self.gui_notebook.notebooks = self.notebooks

        # Create frame container to easily access frames from other areas in the gui
        self.frames = {}
        self.gui_notebook.frames = self.frames

        # Create widgets container to easily access widgets from other areas in the gui
        self.widgets = {}
        self.gui_notebook.widgets = self.widgets

         # Create widgets container to easily access widgets from other areas in the gui
        self.canvases = {}
        self.gui_notebook.canvases = self.canvases

        # Create toolbar container to easily access toolbars from other areas in the gui
        self.toolbars = {}
        self.gui_notebook.toolbars = self.toolbars

        # Create window container to easily access windows from other areas in the gui
        self.windows = {}
        self.gui_notebook.windows = self.windows

        self.root.classes[self.notebook_name] = self
        self.root.notebooks[self.notebook_name] = self.gui_notebook
        master.notebooks[self.notebook_name] = self.gui_notebook