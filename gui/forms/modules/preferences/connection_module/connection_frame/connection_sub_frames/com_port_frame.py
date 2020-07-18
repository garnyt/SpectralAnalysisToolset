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
# Filename            : com_port_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
import pdb

class COM_Port_Frame(Gui_Label_Frame):

    # connection Frame constructor
    def __init__(self, root, master):

        Gui_Label_Frame.__init__(self, root, master, "com_port_frame", "COM")

        self.master = master

        self.create_com_port_frame(master)


    # Create the actual frame as a separate window
    def create_com_port_frame(self, master):

        com_port_values = [
                "COM01", "COM02", "COM03", "COM04", "COM05", "COM06", "COM07", "COM08",
                "COM09", "COM10", "COM11", "COM12", "COM13", "COM14", "COM15"
            ]

        labelTop = ttk.Label(master.frames[self.frame_name], text = "(1 to 15)")
        labelTop.grid(column = 0, row = 0)

        port_combobox = ttk.Combobox(
            master.frames[self.frame_name],
            values = com_port_values
        )

        port_combobox.grid(column = 0, row = 1)

        if ('connection' in self.root.preferences.keys() and
            'port' in self.root.preferences['connection'].keys()):
                port_combobox.current(com_port_values.index(self.root.preferences['connection']['port']))
        else:
            port_combobox.current(6)

            self.build_structure()

            self.root.preferences['connection']['port'] = port_combobox.get()


        port_combobox.bind("<<ComboboxSelected>>", self.update_selection)

        master.frames[self.frame_name].pack(side=LEFT, fill=BOTH, expand=True, anchor = 'w', padx = 10, pady = (20, 20))


    def update_selection(self, event):

        if ('connection' in self.root.preferences.keys() and
            'port' in self.root.preferences['connection'].keys()):
                self.root.preferences['connection']['port'] = event.widget.get()
        else:
            self.build_structure

            self.root.preferences['connection']['port'] = event.widget.get()


    def build_structure(self):

        if 'connection' not in self.root.preferences.keys():
            self.root.preferences['connection'] = {}

        if 'port' not in self.root.preferences['connection'].keys():
            self.root.preferences['connection']['port'] = ''