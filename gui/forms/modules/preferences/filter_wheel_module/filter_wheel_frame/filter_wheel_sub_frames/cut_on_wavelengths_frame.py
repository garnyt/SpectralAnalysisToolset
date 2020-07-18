###
#
#
#
# Program Description :
# Created By          : Benjamin Kleynhans
# Creation Date       : March 1, 2020
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : February 18, 2020
# Filename            : cut_on_wavelengths_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
import pdb

class Cut_On_Wavelengths_Frame(Gui_Label_Frame):

    # connection Frame constructor
    def __init__(self, root, master):

        Gui_Label_Frame.__init__(self, root, master, "cut_on_wavelengths_frame", "Cut-On Wavelengths (nm)")

        self.create_filter_wheel_frame(master)


    # Create the actual frame as a separate window
    def create_filter_wheel_frame(self, master):

        self.build_structure()

        for i in range(11):

            filter_text = 'Filter ' + str(i)
            filter_index = 'filter' + str(i)

            ttk.Label(
                master.frames[self.frame_name],
                text = filter_text,
                width = 20).grid(
                    row = i,
                    column = 0,
                    padx = 10,
                    pady = 10,
                    sticky = 'nsew'
                )

            master.frames[self.frame_name].widgets[filter_index] = ttk.Entry(master.frames[self.frame_name], width = 80)
            master.frames[self.frame_name].widgets[filter_index].grid(
                row = i,
                column = 1,
                columnspan = 2,
                padx = 10,
                pady = 10,
                sticky = 'nsew'
            )

            if ((len(self.root.preferences['fw_cut-on_wavelengths']) - 1) >= i):
                master.frames[self.frame_name].widgets[filter_index].insert(0, self.root.preferences['fw_cut-on_wavelengths'][i])

        master.frames[self.frame_name].pack(side=TOP, fill=BOTH, expand=True, anchor = 'w', padx = 10, pady = (20, 0))

    def build_structure(self):

        if 'fw_cut-on_wavelengths' not in self.root.preferences.keys():
            self.root.preferences['fw_cut-on_wavelengths'] = []