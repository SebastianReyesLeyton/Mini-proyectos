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

