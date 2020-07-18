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
# Filename            : sample3_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
import pdb

class Sample3_Frame(Gui_Label_Frame):

    # connection Frame constructor
    def __init__(self, root, master):

        Gui_Label_Frame.__init__(self, root, master, "sample3_frame", "Sample3 Title")

        self.create_sample3_frame(master)


    # Create the actual frame as a separate window
    def create_sample3_frame(self, master):

        self.build_controller_combobox(master)
        self.build_750_device_combobox(master)

        master.frames[self.frame_name].pack(side=RIGHT, fill=BOTH, expand=True, anchor='e', padx=10, pady=(20, 20))


    def build_controller_combobox(self, master):

        labelTop = ttk.Label(master.frames[self.frame_name], text = "PC Controller")
        labelTop.grid(column = 0, row = 0)

        labelTop = ttk.Label(master.frames[self.frame_name], text = "(0 to 31)")
        labelTop.grid(column = 0, row = 1)

        pc_controller = ttk.Combobox(
            master.frames[self.frame_name],
            values = [
                "GPIB.00", "GPIB.01", "GPIB.02", "GPIB.03", "GPIB.04", "GPIB.05", "GPIB.06", "GPIB.07", "GPIB.08", "GPIB.09",
                "GPIB.10", "GPIB.11", "GPIB.12", "GPIB.13", "GPIB.14", "GPIB.15", "GPIB.16", "GPIB.17", "GPIB.18", "GPIB.19",
                "GPIB.20", "GPIB.21", "GPIB.22", "GPIB.23", "GPIB.24", "GPIB.25", "GPIB.26", "GPIB.27", "GPIB.28", "GPIB.29",
                "GPIB.30", "GPIB.31"
            ]
        )
        pc_controller.grid(column = 1, row = 1)
        pc_controller.current(0)

        pc_controller.bind("<<ComboboxSelected>>", self.update_pc_controller)


    def build_750_device_combobox(self, master):

        labelTop = ttk.Label(master.frames[self.frame_name], text = "750 Device")
        labelTop.grid(column = 0, row = 3)

        labelTop = ttk.Label(master.frames[self.frame_name], text = "(0 to 7)")
        labelTop.grid(column = 0, row = 4)

        m750_device = ttk.Combobox(
            master.frames[self.frame_name],
            values = ["GPIB.00", "GPIB.01", "GPIB.02", "GPIB.03", "GPIB.04", "GPIB.05", "GPIB.06", "GPIB.07"]
        )
        m750_device.grid(column = 1, row = 4)
        m750_device.current(3)

        m750_device.bind("<<ComboboxSelected>>", self.update_m750_device)


    def update_pc_controller(self, event):

        self.root.preferences['connection']['gpib']['pc_controller'] = event.widget.get()


    def update_m750_device(self, event):

        self.root.preferences['connection']['gpib']['m750_device'] = event.widget.get()