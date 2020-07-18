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
# Filename            : grating_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
# from gui.forms.modules.preferences.grating_module.grating_frame.grating_notebook import Grating_Notebook
from gui.forms.modules.preferences.grating_module.grating_frame.grating_sub_frames.current_turret_frame import Current_Turret_Frame
from gui.forms.modules.preferences.grating_module.grating_frame.grating_sub_frames.current_grating_frame import Current_Grating_Frame
from gui.forms.modules.preferences.grating_module.grating_frame.grating_sub_frames.current_settings_frame import Current_Settings_Frame
from gui.tools.save_file import Save_File
import pdb

class Grating_Frame(Gui_Label_Frame):

    # template Frame constructor
    def __init__(self, root, master):

        Gui_Label_Frame.__init__(self, root, master, "grating_frame", "OL-750 Template Properties")

        self.preferences_dictionary = [
            'lower_effective_wavelength', 'upper_effective_wavelength', 'grating_alignment_factor',
            'grating_alignment_angle', 'cut_on_wavelength', 'blaze_wavelength', 'grooves_per_millimeter'
        ]

        self.create_grating_frame(master)


    # Create the actual frame as a separate window
    def create_grating_frame(self, master):

        self.build_structure()

        # # Add the template notebook to the frame
        # Grating_Notebook(self.root, master.frames[self.frame_name])

        # Add the Template1 Frame to the notebook
        Current_Turret_Frame(self.root, master.frames[self.frame_name])

        # Add the Template2 Frame to the notebook
        Current_Grating_Frame(self.root, master.frames[self.frame_name])

        # Add the Template3 Frame to the notebook
        Current_Settings_Frame(self.root, master.frames[self.frame_name])

        self.load_current_values()

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
        # Grid the button as a seperate process in order to access its value
        self.ok_button.grid(
            row = 2,
            column = 4,
            rowspan = 1,
            columnspan = 1,
            padx = 10,
            pady = 10,
            sticky = 'nsew'
        )

        # Instantiate a stop button
        self.cancel_button = ttk.Button(
            master.frames[self.frame_name],
            text = "Cancel",
            command = lambda: self.process_cancel_button(master)
        )
        # Grid the button as a seperate process in order to access its value
        self.cancel_button.grid(
            row = 2,
            column = 5,
            rowspan = 1,
            columnspan = 1,
            padx = 10,
            pady = 10,
            sticky = 'nsew'
        )


    # Build the dictionary structure to save the grating values
    def build_structure(self):

        if 'gratings' not in self.root.preferences.keys():
            self.root.preferences['gratings'] = {}

        for idx in range(1, 4):
            turret = 'turret_' + str(idx)

            if turret not in self.root.preferences['gratings'].keys():
                    self.root.preferences['gratings'][turret] = {}

            for idx0 in range(1, 4):
                grating = 'grating_' + str(idx0)

                if grating not in self.root.preferences['gratings'][turret].keys():
                    self.root.preferences['gratings'][turret][grating] = {}


    # Save the values when the radio button is changed
    def save_current_values(self):

        current_turret = self.root.preferences['gratings']['current_turret']
        current_grating = self.root.preferences['gratings']['current_grating']
        current_frame = self.root.frames['current_settings_frame']

        saved_preferences = self.root.preferences['gratings'][current_turret][current_grating]

        for idx in self.preferences_dictionary:
            saved_preferences[idx] = current_frame.widgets[idx].get()


    def set_text(self, widget, value):

        widget.delete(0, END)
        widget.insert(0, value)


    # Populate the current_settings_frame with the current data in the dictionary
    def load_current_values(self):

        current_turret = self.root.preferences['gratings']['current_turret']
        current_grating = self.root.preferences['gratings']['current_grating']
        current_frame = self.root.frames['current_settings_frame']

        saved_preferences = self.root.preferences['gratings'][current_turret][current_grating]

        for idx in self.preferences_dictionary:
            if idx in saved_preferences.keys():
                if saved_preferences[idx] != '':
                    self.set_text(current_frame.widgets[idx], saved_preferences[idx])
                else:
                    self.set_text(current_frame.widgets[idx], 0)
            else:
                self.set_text(current_frame.widgets[idx], 0)


    # Process OK Button
    def process_ok_button(self, master):

        self.save_current_values()

        Save_File(self.root, master, 'config')

        self.root.windows['grating_window'].destroy()


    # Process the Cancel button
    def process_cancel_button(self, master):

        self.root.windows['grating_window'].destroy()
