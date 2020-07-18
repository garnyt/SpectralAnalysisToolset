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
# Filename            : interface_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
import pdb

class Interface_Frame(Gui_Label_Frame):

    # connection Frame constructor
    def __init__(self, root, master):

        Gui_Label_Frame.__init__(self, root, master, "interface_frame", "Device Interface")
        self.create_interface_frame(master)


    # Create the actual frame as a separate window
    def create_interface_frame(self, master):

        self.interface_selection = StringVar()
        # self.interface_selection.set('serial')

        # Add Radio button for Serial connection
        ttk.Radiobutton(
                master.frames[self.frame_name],
                text = 'Serial',
                variable = self.interface_selection,
                value = 'serial',
                width = 10,
                command = lambda: self.toggle_active_selection(master, self.interface_selection)).grid(
                        row = 0,
                        column = 0
        )

        # Add Radio button for GPIB connection
        ttk.Radiobutton(
                master.frames[self.frame_name],
                text = 'GPIB',
                variable = self.interface_selection,
                value = 'gpib',
                width = 10,
                command = lambda: self.toggle_active_selection(master, self.interface_selection)).grid(
                        row = 0,
                        column = 1)

        if ('connection' in self.root.preferences.keys() and
            'interface' in self.root.preferences['connection'].keys()):
                self.interface_selection.set(self.root.preferences['connection']['interface'])
        else:
            self.interface_selection.set('serial')

            self.build_structure()

            self.root.preferences['connection']['interface'] = self.interface_selection.get()

        master.frames[self.frame_name].pack(side=TOP, fill=BOTH, expand=True, anchor = 'w', padx = 10, pady = (20, 0))


    def toggle_active_selection(self, master, selection):

        if ('connection' in self.root.preferences.keys() and
            'interface' in self.root.preferences['connection'].keys()):
                self.root.preferences['connection']['interface'] = selection.get()
        else:
            self.build_structure()

            self.root.preferences['connection']['interface'] = selection.get()

        self.update_selectible()


    def build_structure(self):

        if 'connection' not in self.root.preferences.keys():
            self.root.preferences['connection'] = {}

        if 'interface' not in self.root.preferences['connection'].keys():
            self.root.preferences['connection']['interface'] = ''


    def update_selectible(self):

        if self.root.preferences['connection']['interface'] == 'serial':
            for child in self.root.frames['gpib_address_frame'].winfo_children():
                child.configure(state='disable')

            for child in self.root.frames['com_port_frame'].winfo_children():
                child.configure(state='enable')
        elif self.root.preferences['connection']['interface'] == 'gpib':
            for child in self.root.frames['gpib_address_frame'].winfo_children():
                child.configure(state='enable')

            for child in self.root.frames['com_port_frame'].winfo_children():
                child.configure(state='disable')