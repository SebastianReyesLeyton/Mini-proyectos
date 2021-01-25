from os import mkdir
from repositories.FileRepository import FileRepository
from flask import send_from_directory

class FileService(object):
    def __init__(self):
        self.filesRepository = FileRepository()

    def getAllFiles(self, route):
        ans = [[], []]
        tmp = route.split('/')
        if len(tmp): 
            route = '../../db/{0}'.format(route)
            ans = self.filesRepository.getAllData(route)
        return ans

    def saveFile(self, file, route, filename):
        file.save('../../db/{0}/{1}'.format(route, filename))

    def removeFile(self, route):
        route = '../../db/{0}'.format(route)
        return self.filesRepository.deleteFile(route)

    def removeDirectory(self, route):
        route = '../../db/{0}'.format(route)
        return self.filesRepository.deleteDir(route)

    def createDirectory(self, route):
        route = '../../db/{0}'.format(route)
        try:
            mkdir(route)
            return 'Ok'
        except Exception as e:
            return e
    
    def readFile(self, route):
        route = '../../db/{0}'.format(route)
        return self.filesRepository.readFile(route)