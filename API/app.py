from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
import pandas as pd
import ast
import urllib
from pred import Prediccion

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

class Result(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', required=True, type=str)
        args = parser.parse_args()
        url = args['url']
        print(url)
        pred = Prediccion(url)
        return {
            'url': url,
            'result': pred
        },200
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', required=True, type=str)
        args = parser.parse_args()
        url = args['url']
        print(url)
        pred = Prediccion(url)
        return {
            'url': url,
            'result': pred
        },200

api.add_resource(Result, '/result')
if __name__ == "__main__":
    app.run()