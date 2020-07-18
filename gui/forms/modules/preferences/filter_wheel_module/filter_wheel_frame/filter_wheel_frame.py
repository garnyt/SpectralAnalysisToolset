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
# Filename            : filter_wheel_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
from gui.forms.modules.preferences.filter_wheel_module.filter_wheel_frame.filter_wheel_sub_frames.cut_on_wavelengths_frame import Cut_On_Wavelengths_Frame
from gui.tools.save_file import Save_File
import pdb

class Filter_Wheel_Frame(Gui_Label_Frame):

    # filter_wheel Frame constructor
    def __init__(self, root, master):

        Gui_Label_Frame.__init__(self, root, master, "filter_wheel_frame", "Filter Wheel Cut-On Wavelength Setup")

        self.create_filter_wheel_frame(master)


    # Create the actual frame as a separate window
    def create_filter_wheel_frame(self, master):

        # Add the Filter_Wheel1 Frame to the notebook
        Cut_On_Wavelengths_Frame(self.root, master.frames[self.frame_name])

        master.frames[self.frame_name].pack(anchor = 'w', fill = BOTH, expand = True, padx = 10, pady = 10)

        self.add_buttons(master)


    # Add OK and Cancel Buttons
    def add_buttons(self, master):

        # Instantiate a start/pause button
        self.ok_button = ttk.Button(
            master.frames[self.frame_name],
            text = "OK",
            command = lambda: self.process_ok_button(master)
        )
        # Pack the button as a seperate process in order to access its value
        self.ok_button.pack(
                anchor='w',
                side=LEFT,
                fill=BOTH,
                expand=True,
                padx=10,
                pady=10
        )

        # Instantiate a stop button
        self.cancel_button = ttk.Button(
            master.frames[self.frame_name],
            text = "Cancel",
            command = lambda: self.process_cancel_button(master)
        )
        # Pack the button as a seperate process in order to access its value
        self.cancel_button.pack(
                anchor='w',
                side=RIGHT,
                fill=BOTH,
                expand=True,
                padx=10,
                pady=10
        )


    # Process OK Button
    def process_ok_button(self, master):

        for child in self.root.frames['cut_on_wavelengths_frame'].widgets:
            if child[:6] == 'filter':
                wl_idx = int(child[child.find('r') + 1:])

                if ((len(self.root.preferences['fw_cut-on_wavelengths']) - 1) >= wl_idx):
                    self.root.preferences['fw_cut-on_wavelengths'][wl_idx] = self.root.frames['cut_on_wavelengths_frame'].widgets[child].get()
                else:
                    self.root.preferences['fw_cut-on_wavelengths'].append(self.root.frames['cut_on_wavelengths_frame'].widgets[child].get())

        Save_File(self.root, master, 'config')

        self.root.windows['filter_wheel_window'].destroy()


    # Process the Cancel button
    def process_cancel_button(self, master):

        self.root.windows['filter_wheel_window'].destroy()