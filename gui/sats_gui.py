#!/usr/bin/env python3
###
#
#
#
# Program Description :
# Created By          : Benjamin Kleynhans
# Creation Date       : May 23, 2019
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : September 8, 2019
# Filename            : sats_gui.py
#
###

# Imports
import json
import os
import pdb
import matplotlib.pyplot as plt

from tkinter import *
from tkinter import messagebox

from gui.tools.load_file import Load_File


class SATS_Gui:

    def __init__(self, master, args):

        self.root = master
        master.args = args

        # Import gui paths
        from forms.main_window.menu_bar import Menu_Bar
#        from forms.main_window.main_toolbar import Main_Toolbar
        from forms.main_window.main_frame import Main_Frame

        # Create the root Tkinter object
        master.title('Spectral Analysis Toolset')
        master.geometry('1024x768')
        master.resizable(True, True)

        # Ensure the master frame cannot be detached from the main program
        master.option_add('*tearOff', False)

        # Create class container to easily access class definitions from other areas in the gui
        classes = {}
        master.classes = classes

        # Create notebook container to easily access notebooks from other areas in the gui
        notebooks = {}
        master.notebooks = notebooks

        # Create frame container to easily access frames from other areas in the gui
        frames = {}
        master.frames = frames

        # Create widgets container to easily access widgets from other areas in the gui
        widgets = {}
        master.widgets = widgets

         # Create widgets container to easily access widgets from other areas in the gui
        canvases = {}
        master.canvases = canvases

        # Create toolbar container to easily access toolbars from other areas in the gui
        toolbars = {}
        master.toolbars = toolbars

        # Create window container to easily access windows from other areas in the gui
        windows = {}
        master.windows = windows

        # Create the Menubar - accessed via master.menu_bar
        Menu_Bar(self.root, master)

        # Create the Toolbar - accessed via master.menu_bar
#        Main_Toolbar(self.root, master)

        # Create the Header - accessed via master.header_frame
        Main_Frame(self.root, master)

#        # Build the path to the configuration file
#        source_file = os.path.join(args['project_root'], 'gui', 'etc', 'ol750.cfg')
#        
#        # Create an instance of a file loader/reader object
#        loader = Load_File(self.root, master)
#        
#        # Read the contents of the file into the global preferences file
#        master.preferences = loader.load(source_file)
#        
#        # Add the project root to the preferences dictionary
#        master.preferences['project_root'] = args['project_root']
#
#        # Create a dictionary to contain all the custom user settings
#        user_options = {
#            'sample_definition': {
#                'starting_wavelength': '',
#                'ending_wavelength': '',
#                'change_in_wavelength': '',
#                'time_between_wavelengths': ''
#            }
#        }
#        master.user_options = user_options


# Ask the user to confirm if they want to close the program
def on_closing(root):

    if messagebox.askyesno("Quit", "Do you really wish to quit?"):
        plt.close('all')
        root.destroy()


# Main entry to the GUI program
def main(project_root, args):

    root = Tk()

    # Move the GUI to the front of the display
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)

    root.project_root = project_root

    args['project_root'] = project_root
    # root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))

    sats_gui = SATS_Gui(root, args)

    root.mainloop()
