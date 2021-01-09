from os import listdir, scandir, environ
from os.path import isfile
from pathlib import Path
from shutil import rmtree

path = "../Project/microservices/DB/FileUsers/sebas.reyes/Python"
directories = Path(path)
def obtainFiles(): return [ file.name for file in directories.iterdir() if file.is_file() ]
def obtainDir(): return [ file.name for file in directories.iterdir() if file.is_dir() ]
def removeDir(): 
    ans, directory = False, Path(path)
    ans = directory.is_dir()
    if ans: rmtree(path)
    return ans

print("Files: {0}".format(obtainFiles()))
print("Directories: {0}".format(obtainDir()))
print("It's directory {0}".format(directories.is_dir()))
print("It is remove? {0}".format(removeDir()))
#print("Environ {0}".format(environ))