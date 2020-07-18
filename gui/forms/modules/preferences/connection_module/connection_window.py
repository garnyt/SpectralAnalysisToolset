###
#
#
#
# Program Description :
# Created By          : Benjamin Kleynhans
# Creation Date       : May 30, 2019
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : November 18, 2019
# Filename            : connection_window.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_window import Gui_Window
from gui.forms.modules.preferences.connection_module.connection_frame.connection_frame import Connection_Frame
from gui.tools.save_file import Save_File
import pdb

class Connection_Window(Gui_Window):

    # connection Window constructor
    def __init__(self, root, master):

        Gui_Window.__init__(self, root, master, "connection_window", "Connection")
        self.create_connection_window(master)


    # Create the actual window as a separate window
    def create_connection_window(self, master):

        # Add the connection frame to the window
        Connection_Frame(self.root, master.windows[self.window_name])

        close_button = ttk.Button(
            master.windows[self.window_name],
            text = "Close",
            command = lambda: self.on_closing(master))
        close_button.pack(side=RIGHT, padx=(0, 10), pady=(5, 20))

        master.windows[self.window_name].protocol("WM_DELETE_WINDOW", lambda: self.on_closing(master))

        self.update_selectible()


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


    # Save changes made to connection
    def save_changes(self, master):

        Save_File(self.root, master, 'config')

        master.windows[self.window_name].destroy()


    # Action to perform when connection window is closed
    def on_closing(self, master):

        self.save_changes(master)