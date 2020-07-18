###
#
#
#
# Program Description : Base class for all Frames in the GUI
# Created By          : Benjamin Kleynhans
# Creation Date       : May 28, 2019
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : August 29, 2019
# Filename            : gui_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
import pdb

class Gui_Frame():

    # Main Gui Frame constructor
    def __init__(self, root, master, frame_name):

        self.root = root

        self.frame_name = frame_name

        self.create_gui_frame(master)


    # Create the actual Frame
    def create_gui_frame(self, master):

        self.gui_frame = ttk.Frame(master)

        # Create notebook container to easily access notebooks from other areas in the gui
        self.notebooks = {}
        self.gui_frame.notebooks = self.notebooks

        # Create frame container to easily access frames from other areas in the gui
        self.frames = {}
        self.gui_frame.frames = self.frames

        # Create widgets container to easily access widgets from other areas in the gui
        self.widgets = {}
        self.gui_frame.widgets = self.widgets

         # Create widgets container to easily access widgets from other areas in the gui
        self.canvases = {}
        self.gui_frame.canvases = self.canvases

        # Create toolbar container to easily access toolbars from other areas in the gui
        self.toolbars = {}
        self.gui_frame.toolbars = self.toolbars

        # Create window container to easily access windows from other areas in the gui
        self.windows = {}
        self.gui_frame.windows = self.windows

        self.root.classes[self.frame_name] = self
        self.root.frames[self.frame_name] = self.gui_frame
        master.frames[self.frame_name] = self.gui_frame