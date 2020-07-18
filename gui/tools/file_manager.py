# Imports
import json
import os

from tkinter import *
from tkinter import messagebox


class File_Manager:

    def __init__(self, root, master, data_dictionary, filepath):

        self.master = master
        
        
    def save_file(self):
        
        json_data = json.dumps(self.data)

        filehandle = open(self.save_location, 'w')
        filehandle.writelines(json_data)
        filehandle.close()
    
    
    def load_file(self):
        
        self.data = {}

        with open(file) as json_file:
            self.data = json.load(json_file)

        return self.data