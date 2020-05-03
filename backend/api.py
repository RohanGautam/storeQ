from flask import Flask
from flask_restful import Resource, Api
import sys
sys.path.insert(1, '/home/rohan/Desktop/Python_files/quantumExploring/backend/storeQ')
import quantumStorage as qs

app = Flask(__name__)
api = Api(app)


class startUpload(Resource):
    def get(self):
        print(f'[GET] starting upload...')
        qs.startUpload()
        return {'startUpload': True,},200, {'Access-Control-Allow-Origin': '*'}

class startDownload(Resource):
    def get(self):
        print(f'[GET] starting download...')
        qs.startDownload()
        return {'startDownload': True,},200, {'Access-Control-Allow-Origin': '*'}


api.add_resource(startUpload, '/startUpload')
api.add_resource(startDownload, '/startDownload')

if __name__ == '__main__':
    app.run(debug=True)