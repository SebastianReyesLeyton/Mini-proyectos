from app import app
from flask import jsonify, request
from controllers.FileApi import file_api

# Register each api here
app.register_blueprint(file_api)

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found {0}'.format(request.url),
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)