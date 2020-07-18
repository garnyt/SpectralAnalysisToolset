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
# Filename            : current_grating_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
import pdb

class Current_Grating_Frame(Gui_Label_Frame):

    # connection Frame constructor
    def __init__(self, root, master):

        Gui_Label_Frame.__init__(self, root, master, "current_grating_frame", "Current Grating")

        self.master = master

        self.create_current_grating_frame(master)


    # Create the actual frame as a separate window
    def create_current_grating_frame(self, master):

        self.current_grating_selection = StringVar()
        self.current_grating_selection.set('grating_1')
        self.root.preferences['gratings']['current_grating'] = self.current_grating_selection.get()

        # Add Radio button for Turret 1 selection
        ttk.Radiobutton(
                master.frames[self.frame_name],
                text = 'Grating 1',
                variable = self.current_grating_selection,
                value = 'grating_1',
                width = 10,
                command = lambda: self.toggle_active_selection(master, self.current_grating_selection)).grid(
                        row = 0,
                        rowspan = 1,
                        pady = 5,
                        column = 0
        )

        # Add Radio button for Turret 2 selection
        ttk.Radiobutton(
                master.frames[self.frame_name],
                text = 'Grating 2',
                variable = self.current_grating_selection,
                value = 'grating_2',
                width = 10,
                command = lambda: self.toggle_active_selection(master, self.current_grating_selection)).grid(
                        row = 1,
                        rowspan = 1,
                        pady = 5,
                        column = 0
        )

        # Add Radio button for Turret 13selection
        ttk.Radiobutton(
                master.frames[self.frame_name],
                text = 'Grating 3',
                variable = self.current_grating_selection,
                value = 'grating_3',
                width = 10,
                command = lambda: self.toggle_active_selection(master, self.current_grating_selection)).grid(
                        row = 2,
                        rowspan = 1,
                        pady = 5,
                        column = 0
        )


        master.frames[self.frame_name].grid(
            row = 1,
            column = 0,
            rowspan = 1,
            columnspan = 2,
            padx = 10,
            pady = 10,
            sticky = 'nsew'
        )



    def toggle_active_selection(self, master, selection):

        self.root.classes['grating_frame'].save_current_values()

        self.root.preferences['gratings']['current_grating'] = selection.get()

        self.root.classes['grating_frame'].load_current_values()