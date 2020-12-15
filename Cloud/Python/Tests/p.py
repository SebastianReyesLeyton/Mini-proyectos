from os import listdir, scandir, environ
from os.path import isfile
from pathlib import Path

path = "../Project/microservices/DB/FileUsers/sebas.reyes"
directories = Path(path)
def obtainFiles(): return [ file.name for file in directories.iterdir() if file.is_file() ]
def obtainDir(): return [ file.name for file in directories.iterdir() if file.is_dir() ]

print("Files: {0}".format(obtainFiles()))
print("Directories: {0}".format(obtainDir()))
#print("Environ {0}".format(environ))