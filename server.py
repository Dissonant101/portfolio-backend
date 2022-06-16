from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from http import HTTPStatus


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self._initialize_api()

    def _initialize_api(self):
        self.api = Api(self.app)
        self.base_url = "/api"
        self.endpoint_map = [(Stylesheet, f"{self.base_url}/stylesheet/<string:stylesheet_name>"),
                             (Layout, f"{self.base_url}/layout/<string:layout_name>")]
        for resource, endpoint in self.endpoint_map:
            self.api.add_resource(resource, endpoint)

    def start(self):
        self.app.run(debug=True)


class Stylesheet(Resource):
    def get(self, stylesheet_name: str):
        return {"message": stylesheet_name}, HTTPStatus.OK


class Layout(Resource):
    def get(self, layout_name: str):
        return {"message": layout_name}, HTTPStatus.OK


if __name__ == "__main__":
    server = Server()
    server.start()