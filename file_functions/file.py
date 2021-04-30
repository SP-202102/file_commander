# basic file objects - mostly used in file_list class
# leave it, probably we will not need it

import os

class file:
    filename = ""
    filetype = ""
    
    def __init__(self, name):
        self.filename = name
