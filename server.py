from flask import Flask
from flask_restful import Resource, Api
from http import HTTPStatus
from s3_dao import ResumeDAO
from flask_cors import CORS


class Server:
    """ Flask server for API.

    Wraps Flask server for better maintability.
    """

    def __init__(self):
        """Constructor for Server class."""
        self.app = Flask(__name__)
        self.cors = CORS(self.app)
        self._initialize_api()

    def create_app(self):
        """Returns the Flask app."""
        return self.app

    def _initialize_api(self):
        """Initialize API endpoints."""
        self.api = Api(self.app)
        self.base_url = "/api"
        self.endpoint_map = [(Resume, f"{self.base_url}/resume/<string:resume_name>"), (Stylesheet,
                                                                                        f"{self.base_url}/stylesheet/<string:stylesheet_name>"), (Layout, f"{self.base_url}/layout/<string:layout_name>")]
        for resource, endpoint in self.endpoint_map:
            self.api.add_resource(resource, endpoint)

    def start(self):
        """Starts server."""
        self.app.run(debug=True)


class Resume(Resource):
    """Resume resource.

    API resource for /resume endpoint.
    """

    def get(self, resume_name: str):
        """Makes call to DAO."""
        return ResumeDAO.get_resume(resume_name), HTTPStatus.OK


class Stylesheet(Resource):
    """Stylesheet resource.

    API resource for /stylesheet endpoint.
    """

    def get(self, stylesheet_name: str):
        """Makes call to DAO."""
        return ResumeDAO.get_stylesheet(stylesheet_name), HTTPStatus.OK


class Layout(Resource):
    """Layout resource.

    API resource for /layout endpoint.
    """

    def get(self, layout_name: str):
        """Makes call to DAO."""
        return ResumeDAO.get_layout(layout_name), HTTPStatus.OK


server = Server()
gunicorn_server = server.create_app()
