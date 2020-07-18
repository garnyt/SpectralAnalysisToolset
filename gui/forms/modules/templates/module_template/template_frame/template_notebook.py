###
#
#
#
# Program Description :
# Module Description  :
#
# Created By          : Benjamin Kleynhans
# Creation Date       : February 15, 2020
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : February 18, 2020
# Filename            : template_notebook.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from gui.forms.base_classes.gui_notebook import Gui_Notebook
import pdb

class Template_Notebook(Gui_Notebook):

    # Template Notebook constructor
    def __init__(self, root, master):

        Gui_Notebook.__init__(self, root, master, "template_notebook")

        self.create_template_notebook(master)


    # Create the template_notebook object that will contain all the tabs
    def create_template_notebook(self, master):

        # Add the template notebook to the frame
        Template_Notebook(self.root, master.frames[self.frame_name])

        master.notebooks[self.notebook_name].pack(anchor = 'w', fill = BOTH, expand = True, padx = 10, pady = 10)