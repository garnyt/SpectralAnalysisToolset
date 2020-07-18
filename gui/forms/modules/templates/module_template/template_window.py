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
# Filename            : template_window.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_window import Gui_Window
from gui.forms.modules.templates.module_template.template_frame.template_frame import Template_Frame
import pdb

class Template_Window(Gui_Window):

    # template Window constructor
    def __init__(self, root, master):

        Gui_Window.__init__(self, root, master, "template_window", "Template")
        self.create_template_window(master)


    # Create the actual window as a separate window
    def create_template_window(self, master):

        master.windows[self.window_name].protocol("WM_DELETE_WINDOW", lambda: self.on_closing(master))

        # Add the template frame to the window
        Template_Frame(self.root, master.windows[self.window_name])


    # Save changes made to template
    def save_changes(self, master):

        pass
        master.windows[self.window_name].destroy()

    # Action to perform when template window is closed
    def on_closing(self, master):

        if messagebox.askyesno("Save Preferences", "Do you wish to save your changes?"):
            self.save_changes(master)
        else:
            master.windows[self.window_name].destroy()