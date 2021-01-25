from pathlib import Path
import os
from os import remove
from shutil import rmtree

class FileRepository(object):
    def __init__(self):
        self.files = []
        self.dirs = []

    def getAllData(self, path):
        directory = Path(path)
        self.files = [ file.name for file in directory.iterdir() if file.is_file() ]
        self.dirs = [ file.name for file in directory.iterdir() if file.is_dir() ]
        return (self.files, self.dirs)

    def deleteFile(self, path):
        ans = True
        if os.path.exists(path): remove(path)
        else: ans = False
        return ans

    def deleteDir(self, path):
        ans, directory = False, Path(path)
        ans = directory.is_dir()
        if ans: rmtree(path)
        return ans

    def readFile(self, path):
        return open(path, 'rb')
        