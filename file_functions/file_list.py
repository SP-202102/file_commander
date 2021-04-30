# list of file objects
from pathlib import Path

class file_list:
    #todo: move to main -> in constructor
    def __init__(self, initpath):
        self.basepath = initpath

    def get_file_objects(self):
        return Path(self.basepath).iterdir() 
