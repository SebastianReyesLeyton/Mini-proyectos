from os import listdir, scandir, environ
from os.path import isfile

def obtainFiles(path='.'): return [ file for file in listdir(path) if isfile(file) ]
def obtainDir(path='.'): return [ file for file in listdir(path) if not isfile(file) ]

print("Directories: {0}".format(obtainDir("../")))
print("File: {0}".format(obtainFiles("../")))
print("Environ {0}".format(environ))