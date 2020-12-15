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
        resp = jsonify({'files': files, 'directiores': dirs})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)