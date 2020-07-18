###
#
#
#
# Program Description : Base class for all Canvases in the GUI
# Created By          : Benjamin Kleynhans
# Creation Date       : February 22, 2020
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : February 22, 2020
# Filename            : gui_canvas.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
import pdb

class Gui_Canvas():

    # Main Canvas constructor
    def __init__(self, root, master, canvas_name):

        self.root = root

        self.canvas_name = canvas_name

        self.create_gui_canvas(master)


    # Create the actual Canvas
    def create_gui_canvas(self, master):

        self.gui_canvas = Canvas(master, width=450, height=300, bg="white")

        # Create notebook container to easily access notebooks from other areas in the gui
        self.notebooks = {}
        self.gui_canvas.notebooks = self.notebooks

        # Create frame container to easily access frames from other areas in the gui
        self.frames = {}
        self.gui_canvas.frames = self.frames

        # Create widgets container to easily access widgets from other areas in the gui
        self.widgets = {}
        self.gui_canvas.widgets = self.widgets

        # Create canvas container to easily access canvases from other areas in the gui
        self.canvases = {}
        self.gui_canvas.canvases = self.canvases

        # Create toolbar container to easily access toolbars from other areas in the gui
        self.toolbars = {}
        self.gui_canvas.toolbars = self.toolbars

        # Create window container to easily access windows from other areas in the gui
        self.windows = {}
        self.gui_canvas.windows = self.windows

        self.root.classes[self.canvas_name] = self
        self.root.canvases[self.canvas_name] = self.gui_canvas
        master.canvases[self.canvas_name] = self.gui_canvas