from repositories.FileRepository import FileRepository

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