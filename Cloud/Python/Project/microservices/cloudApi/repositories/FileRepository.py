from os import listdir
from os.path import isfile

class FileRepository(object):
    def __init__(self):
        self.files = []
        self.dirs = []

    def getAllData(self, path):
        self.files = [ file for file in listdir(path) if isfile(file) ]
        self.dirs = [ file for file in listdir(path) if not isfile(file) ]
        return (self.files, self.dirs)