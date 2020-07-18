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
# Filename            : sample_definition_frame.py
#
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gui.forms.base_classes.gui_label_frame import Gui_Label_Frame
import pdb

class Sample_Definition_Frame(Gui_Label_Frame):

    # connection Frame constructor
    def __init__(self, root, master):

        Gui_Label_Frame.__init__(self, root, master, "sample_definition_frame", "Sample Definition")

        self.create_sample1_frame(master)


    # Create the actual frame as a separate window
    def create_sample1_frame(self, master):

        # Read in the starting wavelength
        ttk.Label(
            master.frames[self.frame_name],
            text = u"Starting \u03bb (nm)", #unicode for lamda
            width = 20).grid(
                row = 0,
                column = 0,
                padx = 10,
                pady = 10,
                sticky = 'nsew'
            )

        master.frames[self.frame_name].widgets['starting_wavelength'] = ttk.Entry(master.frames[self.frame_name], width = 20)
        master.frames[self.frame_name].widgets['starting_wavelength'].grid(
            row = 0,
            column = 1,
            # columnspan = 3,
            padx = 10,
            pady = 10,
            sticky = 'nsew'
        )

        # Read in the ending wavelength
        ttk.Label(
            master.frames[self.frame_name],
            text = u"Ending \u03bb (nm)", #unicode for lamda
            width = 20).grid(
                row = 1,
                column = 0,
                padx = 10,
                pady = 10,
                sticky = 'nsew'
            )

        master.frames[self.frame_name].widgets['ending_wavelength'] = ttk.Entry(master.frames[self.frame_name], width = 20)
        master.frames[self.frame_name].widgets['ending_wavelength'].grid(
            row = 1,
            column = 1,
            # columnspan = 3,
            padx = 10,
            pady = 10,
            sticky = 'nsew'
        )

        # Read in the change in wavelength
        ttk.Label(
            master.frames[self.frame_name],
            text = u"\u0394 \u03bb (nm)", #unicode for lamda #unicode for delta u0394
            width = 20).grid(
                row = 2,
                column = 0,
                padx = 10,
                pady = 10,
                sticky = 'nsew'
            )

        master.frames[self.frame_name].widgets['change_in_wavelength'] = ttk.Entry(master.frames[self.frame_name], width = 20)
        master.frames[self.frame_name].widgets['change_in_wavelength'].grid(
            row = 2,
            column = 1,
            # columnspan = 3,
            padx = 10,
            pady = 10,
            sticky = 'nsew'
        )

        # Read in the time of illumination
        ttk.Label(
            master.frames[self.frame_name],
            text = u"\u0394 time (s)", #unicode for lamda #unicode for delta u0394
            width = 20).grid(
                row = 3,
                column = 0,
                padx = 10,
                pady = 10,
                sticky = 'nsew'
            )

        master.frames[self.frame_name].widgets['time_between_wavelengths'] = ttk.Entry(master.frames[self.frame_name], width = 20)
        master.frames[self.frame_name].widgets['time_between_wavelengths'].grid(
            row = 3,
            column = 1,
            # columnspan = 3,
            padx = 10,
            pady = 10,
            sticky = 'nsew'
        )

        master.frames[self.frame_name].pack(anchor = 'w', fill = BOTH, expand = True, padx = 10, pady = 10)