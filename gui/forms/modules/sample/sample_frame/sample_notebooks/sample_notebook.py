# ###
# #
# #
# #
# # Program Description :
# # Module Description  :
# #
# # Created By          : Benjamin Kleynhans
# # Creation Date       : February 15, 2020
# # Authors             : Benjamin Kleynhans
# #
# # Last Modified By    : Benjamin Kleynhans
# # Last Modified Date  : February 18, 2020
# # Filename            : sample_notebook.py
# #
# ###

# # Imports
# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
# from gui.forms.base_classes.gui_notebook import Gui_Notebook
# from gui.forms.modules.sample.sample_frame.sample_notebooks.sample_sub_frames.sample1_frame import Sample1_Frame
# from gui.forms.modules.sample.sample_frame.sample_notebooks.sample_sub_frames.sample2_frame import Sample2_Frame
# from gui.forms.modules.sample.sample_frame.sample_notebooks.sample_sub_frames.sample3_frame import Sample3_Frame
# import pdb

# class Sample_Notebook(Gui_Notebook):

#     # Sample Notebook constructor
#     def __init__(self, root, master):

#         Gui_Notebook.__init__(self, root, master, "sample_notebook")

#         self.create_sample_notebook(master)


#     # Create the sample_notebook object that will contain all the tabs
#     def create_sample_notebook(self, master):

#         # Add the Interface Frame to the notebook
#         Sample1_Frame(self.root, master.notebooks[self.notebook_name])

#         # # Add the COM port Frame to the notebook
#         # Sample2_Frame(self.root, master.notebooks[self.notebook_name])

#         # # Add the GPIB Address Frame to the notebook
#         # Sample3_Frame(self.root, master.notebooks[self.notebook_name])

#         master.notebooks[self.notebook_name].pack(anchor = 'w', fill = BOTH, expand = True, padx = 10, pady = 10)