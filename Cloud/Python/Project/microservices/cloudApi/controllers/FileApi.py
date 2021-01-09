from flask import Blueprint
from app import app
from flask import jsonify
from flask import flash, request
from services.FileService import FileService

file_api = Blueprint('file_api', __name__)
fileService = FileService()

@file_api.route('/files/<string:path>/', methods=['GET'])
def obtainFiles(path):
    try:
        print('/'.join(path.split('-')))
        files, dirs = fileService.getAllFiles('{0}'.format('/'.join(path.split('-'))))
        resp = jsonify({'directories': dirs, 'files': files})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@file_api.route('/saveFile/<string:path>/', methods=['POST'])
def saveFile(path):
    try:
        if 'file' not in request.files:
            resp = jsonify({'message': 'Param is not found'})
            resp.status_code = 404
            return resp
        f = request.files['file']
        fileService.saveFile(f, '/'.join(path.split('-')), f.filename)
        resp = jsonify({'message': 'Ok'})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@file_api.route('/removeFile/<string:path>', methods=['POST'])
def removeFile(path):
    try:
        resp = None
        name = request.json['filename']
        path = '/'.join(path.split('-'))
        path = '{0}/{1}'.format(path, name)
        if fileService.removeFile(path):
            resp = jsonify({'message': 'Ok'})
            resp.status_code = 200
        else:
            name = path.split('/')[-1]
            route = path.split('/')[1:-1]
            route = '/'.join(route)
            resp = jsonify({'message': 'Doesn\'t exist a file with name {0} in the route: {1}'.format(name, route)})
            resp.status_code = 406
        return resp
    except Exception as e:
        print(e)

@file_api.route('/removeDirectory/<string:path>', methods=['POST'])
def removeDirectory(path):
    try:
        resp = None
        path = '/'.join(path.split('-'))
        if fileService.removeDirectory(path):
            resp = jsonify({'message': 'Ok'})
            resp.status_code = 200
        else:
            name = path.split('/')[-1]
            route = '/'.join(path.split('/')[1:-1])
            resp = jsonify({'message': 'Doesn\'t exist a directory with name {0} in the route: {1}'.format(name, route)})
            resp.status_code = 406
        return resp
    except Exception as e:
        print(e)

@file_api.route('/createDirectory/<string:path>', methods=['POST'])
def createDirectory(path):
    try:
        path = '/'.join(path.split('-'))
        message = {'message': fileService.createDirectory(path)}
        resp = jsonify(message)
        if message['message'] == 'Ok': resp.status_code = 200
        else: resp.status_code = 400
        return resp
    except Exception as e:
        print(e)

@file_api.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp