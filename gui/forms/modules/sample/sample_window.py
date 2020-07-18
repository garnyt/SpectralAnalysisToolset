###
#
#
#
# Program Description :
# Created By          : Benjamin Kleynhans
# Creation Date       : May 30, 2019
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : November 18, 2019
# Filename            : sample_window.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_window import Gui_Window
from gui.forms.modules.sample.sample_frame.sample_frame import Sample_Frame
from gui.tools.save_file import Save_File

import pdb

class Sample_Window(Gui_Window):

    # sample Window constructor
    def __init__(self, root, master):

        Gui_Window.__init__(self, root, master, "sample_window", "Sample")
        self.create_sample_window(master)


    # Create the actual window as a separate window
    def create_sample_window(self, master):

        master.windows[self.window_name].protocol("WM_DELETE_WINDOW", lambda: self.on_closing(master))

        # Add the sample frame to the window
        Sample_Frame(self.root, master.windows[self.window_name])


    # Save changes made to connection
    def save_changes(self, master):

        Save_File(self.root, master, 'config')

        master.windows[self.window_name].destroy()


    # Action to perform when connection window is closed
    def on_closing(self, master):

        self.save_changes(master)