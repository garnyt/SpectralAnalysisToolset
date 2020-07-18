###
#
#
#
# Program Description :
# Created By          : Benjamin Kleynhans
# Creation Date       : February 18, 2020
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : February 18, 2020
# Filename            : template_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
from gui.forms.modules.templates.module_template.template_frame.template_notebook import Template_Notebook
from gui.forms.modules.templates.module_template.template_frame.template_sub_frames.template1_frame import Template1_Frame
from gui.forms.modules.templates.module_template.template_frame.template_sub_frames.template2_frame import Template2_Frame
from gui.forms.modules.templates.module_template.template_frame.template_sub_frames.template3_frame import Template3_Frame
import pdb

class Template_Frame(Gui_Label_Frame):

    # template Frame constructor
    def __init__(self, root, master):

        Gui_Label_Frame.__init__(self, root, master, "template_frame", "OL-750 Template Properties")
        self.create_template_frame(master)


    # Create the actual frame as a separate window
    def create_template_frame(self, master):

        # # Add the template notebook to the frame
        # Template_Notebook(self.root, master.frames[self.frame_name])

        # Add the Template1 Frame to the notebook
        Template1_Frame(self.root, master.frames[self.frame_name])

        # Add the Template2 Frame to the notebook
        Template2_Frame(self.root, master.frames[self.frame_name])

        # Add the Template3 Frame to the notebook
        Template3_Frame(self.root, master.frames[self.frame_name])

        master.frames[self.frame_name].pack(anchor = 'w', fill = BOTH, expand = True, padx = 10, pady = 10)
