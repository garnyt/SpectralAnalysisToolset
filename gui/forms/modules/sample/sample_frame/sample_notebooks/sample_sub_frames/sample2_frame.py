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
# Filename            : sample2_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
import pdb

class Sample2_Frame(Gui_Label_Frame):

    # connection Frame constructor
    def __init__(self, root, master):

        Gui_Label_Frame.__init__(self, root, master, "sample2_frame", "Sample2 Title")

        self.create_sample2_frame(master)


    # Create the actual frame as a separate window
    def create_sample2_frame(self, master):

        labelTop = ttk.Label(master.frames[self.frame_name], text = "(1 to 15)")
        labelTop.grid(column = 0, row = 0)

        port_combobox = ttk.Combobox(
            master.frames[self.frame_name],
            values = [
                "COM01", "COM02", "COM03", "COM04", "COM05", "COM06", "COM07", "COM08",
                "COM09", "COM10", "COM11", "COM12", "COM13", "COM14", "COM15"
            ]
        )
        port_combobox.grid(column = 0, row = 1)
        port_combobox.current(6)

        port_combobox.bind("<<ComboboxSelected>>", self.update_selection)

        master.frames[self.frame_name].pack(anchor = 'w', fill = BOTH, expand = True, padx = 10, pady = 10)


    def update_selection(self, event):

        self.root.preferences['connection']['com'] = event.widget.get()