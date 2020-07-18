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
# Filename            : connection_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
from gui.forms.modules.preferences.connection_module.connection_frame.connection_sub_frames.interface_frame import Interface_Frame
from gui.forms.modules.preferences.connection_module.connection_frame.connection_sub_frames.com_port_frame import COM_Port_Frame
from gui.forms.modules.preferences.connection_module.connection_frame.connection_sub_frames.gpib_address_frame import GPIB_Address_Frame
import pdb

class Connection_Frame(Gui_Label_Frame):

    # connection Frame constructor
    def __init__(self, root, master):

        Gui_Label_Frame.__init__(self, root, master, "connection_frame", "OL-750 Connection Properties")
        self.create_connection_frame(master)


    # Create the actual frame as a separate window
    def create_connection_frame(self, master):

        # Add the Interface Frame to the notebook
        Interface_Frame(self.root, master.frames[self.frame_name])

        # Add the COM port Frame to the notebook
        COM_Port_Frame(self.root, master.frames[self.frame_name])

        # Add the GPIB Address Frame to the notebook
        GPIB_Address_Frame(self.root, master.frames[self.frame_name])

        master.frames[self.frame_name].pack(anchor='w', fill=BOTH, expand=True, padx=10, pady=10)