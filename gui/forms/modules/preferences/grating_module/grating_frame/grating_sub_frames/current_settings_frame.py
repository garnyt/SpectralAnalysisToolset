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
# Filename            : current_settings_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
import pdb

class Current_Settings_Frame(Gui_Label_Frame):

    # connection Frame constructor
    def __init__(self, root, master):

        Gui_Label_Frame.__init__(self, root, master, "current_settings_frame", "Current Settings")

        self.master = master

        self.create_current_settings_frame(master)


    # Create the actual frame as a separate window
    def create_current_settings_frame(self, master):

        # Lower Effective Wavelength
        ttk.Label(
            master.frames[self.frame_name],
            text = 'Lower Effective Wavelength',
            width = 30).grid(
                row = 0,
                column = 0,
                padx = 10,
                pady = 5,
                sticky = 'nsew'
            )

        master.frames[self.frame_name].widgets['lower_effective_wavelength'] = ttk.Entry(master.frames[self.frame_name], width = 20)
        master.frames[self.frame_name].widgets['lower_effective_wavelength'].grid(
            row = 0,
            column = 1,
            columnspan = 2,
            padx = 10,
            pady = 5,
            sticky = 'nsew'
        )

        # Upper Effective Wavelength
        ttk.Label(
            master.frames[self.frame_name],
            text = 'Upper Effective Wavelength',
            width = 30).grid(
                row = 1,
                column = 0,
                padx = 10,
                pady = 5,
                sticky = 'nsew'
            )

        master.frames[self.frame_name].widgets['upper_effective_wavelength'] = ttk.Entry(master.frames[self.frame_name], width = 20)
        master.frames[self.frame_name].widgets['upper_effective_wavelength'].grid(
            row = 1,
            column = 1,
            columnspan = 2,
            padx = 10,
            pady = 5,
            sticky = 'nsew'
        )

        # Grating Alignment Factor
        ttk.Label(
            master.frames[self.frame_name],
            text = 'Grating Alignment Factor',
            width = 30).grid(
                row = 2,
                column = 0,
                padx = 10,
                pady = 5,
                sticky = 'nsew'
            )

        master.frames[self.frame_name].widgets['grating_alignment_factor'] = ttk.Entry(master.frames[self.frame_name], width = 20)
        master.frames[self.frame_name].widgets['grating_alignment_factor'].grid(
            row = 2,
            column = 1,
            columnspan = 2,
            padx = 10,
            pady = 5,
            sticky = 'nsew'
        )

        # Gracting Alignment Angle
        ttk.Label(
            master.frames[self.frame_name],
            text = 'Grating Alignment Angle',
            width = 30).grid(
                row = 3,
                column = 0,
                padx = 10,
                pady = 5,
                sticky = 'nsew'
            )

        master.frames[self.frame_name].widgets['grating_alignment_angle'] = ttk.Entry(master.frames[self.frame_name], width = 20)
        master.frames[self.frame_name].widgets['grating_alignment_angle'].grid(
            row = 3,
            column = 1,
            columnspan = 2,
            padx = 10,
            pady = 5,
            sticky = 'nsew'
        )

        # Cut-On Wavelength
        ttk.Label(
            master.frames[self.frame_name],
            text = 'Cut-On Wavelength',
            width = 30).grid(
                row = 4,
                column = 0,
                padx = 10,
                pady = 5,
                sticky = 'nsew'
            )

        master.frames[self.frame_name].widgets['cut_on_wavelength'] = ttk.Entry(master.frames[self.frame_name], width = 20)
        master.frames[self.frame_name].widgets['cut_on_wavelength'].grid(
            row = 4,
            column = 1,
            columnspan = 2,
            padx = 10,
            pady = 5,
            sticky = 'nsew'
        )

        # Blaze Wavelength
        ttk.Label(
            master.frames[self.frame_name],
            text = 'Blaze Wavelength',
            width = 30).grid(
                row = 5,
                column = 0,
                padx = 10,
                pady = 5,
                sticky = 'nsew'
            )

        master.frames[self.frame_name].widgets['blaze_wavelength'] = ttk.Entry(master.frames[self.frame_name], width = 20)
        master.frames[self.frame_name].widgets['blaze_wavelength'].grid(
            row = 5,
            column = 1,
            columnspan = 2,
            padx = 10,
            pady = 5,
            sticky = 'nsew'
        )

        # Grooves Per Millimeter
        ttk.Label(
            master.frames[self.frame_name],
            text = 'Grooves Per Millimeter',
            width = 30).grid(
                row = 6,
                column = 0,
                padx = 10,
                pady = 5,
                sticky = 'nsew'
            )

        master.frames[self.frame_name].widgets['grooves_per_millimeter'] = ttk.Entry(master.frames[self.frame_name], width = 20)
        master.frames[self.frame_name].widgets['grooves_per_millimeter'].grid(
            row = 6,
            column = 1,
            columnspan = 2,
            padx = 10,
            pady = 5,
            sticky = 'nsew'
        )


        master.frames[self.frame_name].grid(
            row = 0,
            column = 2,
            rowspan = 2,
            columnspan = 4,
            padx = 10,
            pady = 10,
            sticky = 'nsew'
        )