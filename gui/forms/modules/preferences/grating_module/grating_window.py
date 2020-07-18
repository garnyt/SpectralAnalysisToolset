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
# Filename            : grating_window.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_window import Gui_Window
from gui.forms.modules.preferences.grating_module.grating_frame.grating_frame import Grating_Frame
import pdb

class Grating_Window(Gui_Window):

    # template Window constructor
    def __init__(self, root, master):

        Gui_Window.__init__(self, root, master, "grating_window", "Setup Gratings")
        self.create_grating_window(master)


    # Create the actual window as a separate window
    def create_grating_window(self, master):

        master.windows[self.window_name].protocol("WM_DELETE_WINDOW", lambda: self.on_closing(master))

        # Add the template frame to the window
        Grating_Frame(self.root, master.windows[self.window_name])


    # Action to perform when template window is closed
    def on_closing(self, master):

        master.windows[self.window_name].destroy()