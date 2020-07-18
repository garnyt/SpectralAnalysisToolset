###
#
#
#
# Program Description :
# Created By          : Benjamin Kleynhans
# Creation Date       : February 22, 2020
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : February 22, 2020
# Filename            : main_toolbar.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from gui.forms.base_classes.gui_toolbar import Gui_Toolbar
from gui.forms.main_window.toolbar.main_toolbar_canvas import Main_Toolbar_Canvas
import pdb

class Main_Toolbar(Gui_Toolbar):

    # Toolbar constructor
    def __init__(self, root, master):

        Gui_Toolbar.__init__(self, root, master, "main_toolbar")
        self.create_toolbar(master)


    # Create header frame object
    def create_toolbar(self, master):

        # Add a toolbar canvas for graphical display
        Main_Toolbar_Canvas(self.root, master.toolbars[self.toolbar_name])

        master.toolbars[self.toolbar_name].pack(side = TOP, fill = X)

