from flask import Flask
from flask_restful import Resource, Api
import backend.storeQ.quantumStorage as qs

app = Flask(__name__)
api = Api(app)


class startUpload(Resource):
    def get(self):
        print(f'[GET] starting upload...')
        
        return {
            'startUpload': True,
        }

class startDownload(Resource):
    def get(self):
        print(f'[GET] starting download...')
        return {
            'startDownload': True,
        }


api.add_resource(startUpload, '/startUpload')
api.add_resource(startDownload, '/startDownload')

if __name__ == '__main__':
    app.run(debug=True)