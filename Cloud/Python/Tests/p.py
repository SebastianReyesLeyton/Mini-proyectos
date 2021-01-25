from os import listdir, scandir, environ
from os.path import isfile
from pathlib import Path
from shutil import rmtree

path = "../Project/microservices/DB/FileUsers/sebas.reyes/7edcf83a5ec1e8cbd9570b60e7779ceb.jpg"
directories = Path(path)
def obtainFiles(): return [ file.name for file in directories.iterdir() if file.is_file() ]
def obtainDir(): return [ file.name for file in directories.iterdir() if file.is_dir() ]
def removeDir(): 
    ans, directory = False, Path(path)
    ans = directory.is_dir()
    if ans: rmtree(path)
    return ans
def readFile(path):
    f = open(path, 'rb')
    return {'f': f.name}

#print("Files: {0}".format(obtainFiles()))
#print("Directories: {0}".format(obtainDir()))
#print("It's directory {0}".format(directories.is_dir()))
#print("It is remove? {0}".format(removeDir()))
print(readFile(path))
#print("Environ {0}".format(environ))