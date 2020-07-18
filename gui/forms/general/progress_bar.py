###
#
# CIS Top of Atmosphere Radiance Calibration
#
# Program Description : This modules create a window with a continuously running progress bar
# Created By          : Benjamin Kleynhans
# Creation Date       : May 23, 2019
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : August 8, 2019
# Filename            : progress_bar.py
#
###Usage
# 
# Create a progress bar to show activity
#   self.progressbar = Progress_Bar(master, self, 'Processing... ')
#
#   Components:     master              Tk root object
#                   self                The calling class (used if you want to change button states)
#                   'Processing... '    The text to display in the progress window
#
# Start the progressbar
#   self.progressbar.start()
#
# Stop the progressbar
#   self.progressbar.stop()
# After process is complete, set the status to complete
#   
###

# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import time
import threading

import pdb

class Progress_Bar():
    
    # Progress Bar constructor
    def __init__(self, master, parent, progressbar_text):
        
        self.text = progressbar_text
        self.parent = parent
        
        self.create_progressbar_window(master)
        
    
    # Create the progress bar widow object
    def create_progressbar_window(self, master):
        
        # Create the progressbar object
        self.progressbar_window = Toplevel(master)                              # Create a progressbar toplevel window
        self.progressbar_window.protocol('WM_DELETE_WINDOW', 'do_nothing')      # Don't close the window on X
        master.progressbar_window = self.progressbar_window                     # Add the progressbar window to the master window as object variable
        master.progressbar_window.resizable(False, False)
                
        self.progressbar_label = ttk.Label(self.progressbar_window, text = self.text)
        self.progressbar_window.progressbar_label = self.progressbar_label
        
        self.progressbar_label.pack(anchor = 'sw', padx = 10, pady = (10, 0))
        
        self.progressbar = ttk.Progressbar(self.progressbar_window, orient = HORIZONTAL, length = 200)  # Create a progressbar
        self.progressbar_window.progressbar = self.progressbar                  # Add the progressbar to the progressbar window as object variable
        
        self.progressbar.config(mode = 'indeterminate')
        self.progressbar_thread = threading.Thread(target = self.step_progressbar)
                
        self.progressbar.pack(anchor = 'nw', fill = BOTH, expand = True, padx = 10, pady = (0, 10))
        
    
    # Start the progressbar
    def start(self):
        
        self.process_complete = False
        self.progressbar_thread.start()
        
        
    # Stop the progressbar
    def stop(self):
        
        self.process_complete = True        
        
    
    # Used to step the progressbar
    def step_progressbar(self):
                    
        while not self.process_complete:            
            self.progressbar.step()
            time.sleep(0.02)        
        
        self.progressbar_window.destroy()
        
        
    # Removes the ability to close the progress bar using the X button
    def do_nothing(self, master):
        
        pass