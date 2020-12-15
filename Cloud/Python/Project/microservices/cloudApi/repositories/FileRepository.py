from pathlib import Path
class FileRepository(object):
    def __init__(self):
        self.files = []
        self.dirs = []

    def getAllData(self, path):
        directory = Path(path)
        self.files = [ file.name for file in directory.iterdir() if file.is_file() ]
        self.dirs = [ file.name for file in directory.iterdir() if file.is_dir() ]
        return (self.files, self.dirs)