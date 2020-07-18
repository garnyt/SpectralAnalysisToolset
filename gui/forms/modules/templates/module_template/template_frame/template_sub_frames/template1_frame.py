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
# Filename            : template1_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
import pdb

class Template1_Frame(Gui_Label_Frame):

    # connection Frame constructor
    def __init__(self, root, master):

        Gui_Label_Frame.__init__(self, root, master, "template1_frame", "Frame Title")
        self.create_template1_frame(master)


    # Create the actual frame as a separate window
    def create_template1_frame(self, master):

        self.template1_selection = StringVar()
        self.template1_selection.set('serial')

        # Add Radio button for Serial connection
        ttk.Radiobutton(
                master.frames[self.frame_name],
                text = 'Serial',
                variable = self.template1_selection,
                value = 'serial',
                width = 10,
                command = lambda: self.toggle_active_selection(master, self.template1_selection)).grid(
                        row = 0,
                        column = 0
        )

        # Add Radio button for GPIB connection
        ttk.Radiobutton(
                master.frames[self.frame_name],
                text = 'GPIB',
                variable = self.template1_selection,
                value = 'gpib',
                width = 10,
                command = lambda: self.toggle_active_selection(master, self.template1_selection)).grid(
                        row = 0,
                        column = 1)


        master.frames[self.frame_name].pack(side=TOP, fill=BOTH, expand=True, anchor = 'w', padx = 10, pady = (20, 0))

    def toggle_active_selection(self, master, selection):

        self.root.preferences['connection']['template1'] = selection.get()