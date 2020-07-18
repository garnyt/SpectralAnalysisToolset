###
#
#
#
# Program Description : Base class for all Label Frames in the GUI
# Created By          : Benjamin Kleynhans
# Creation Date       : May 28, 2019
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : August 29, 2019
# Filename            : gui_label_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
import pdb

class Gui_Label_Frame():

    # Main Gui Frame constructor
    def __init__(self, root, master, frame_name, frame_title):

        self.root = root

        self.frame_name = frame_name
        self.frame_title = frame_title

        self.create_gui_label_frame(master)


    # Create the actual Frame
    def create_gui_label_frame(self, master):

        self.gui_label_frame = ttk.LabelFrame(master, text = self.frame_title)

        # Create notebook container to easily access notebooks from other areas in the gui
        self.notebooks = {}
        self.gui_label_frame.notebooks = self.notebooks

        # Create frame container to easily access frames from other areas in the gui
        self.frames = {}
        self.gui_label_frame.frames = self.frames

        # Create widgets container to easily access widgets from other areas in the gui
        self.widgets = {}
        self.gui_label_frame.widgets = self.widgets

         # Create widgets container to easily access widgets from other areas in the gui
        self.canvases = {}
        self.gui_label_frame.canvases = self.canvases

        # Create toolbar container to easily access toolbars from other areas in the gui
        self.toolbars = {}
        self.gui_label_frame.toolbars = self.toolbars

        # Create window container to easily access windows from other areas in the gui
        self.windows = {}
        self.gui_label_frame.windows = self.windows

        self.root.classes[self.frame_name] = self
        self.root.frames[self.frame_name] = self.gui_label_frame
        master.frames[self.frame_name] = self.gui_label_frame