"""
Communicates with clients over HTTP
uses flask and socket IO to support bi-directional communication with clients

@Author: Kyle McMaster
@Date: 2024-04-02

ATTRIBUTES:


TODO:
Complete Doc-string
Develop functions

"""
from headers.RequestBroker import RequestBroker

from flask import Flask, Response, request
from flask_socketio import SocketIO, emit
import json


class FlaskRequestBroker(RequestBroker):
    
    def __init__(self):
        """
        Initialize class to prepare for communication
        """

        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret!'
        self.socketio = SocketIO(self.app)


    def add_endpoint(self, endpoint: str, name: str, handler: callable, allowed_methods: list[str]):
        """
        Add API endpoint for HTTP requests to the server

        Args:  
        """
        self.app.add_url_rule(endpoint, name, EndpointAction(handler), methods=allowed_methods)
        print(f"registered {endpoint}")


    def add_event(self, event_name: str, handler: callable):
        """
        Add listener for Socket Events

        Args:
        """
        self.socketio.on_event(event_name, handler)
        print(f"registered {event_name}")


    def start(self):
        """
        Host Server
        """
        self.socketio.run(self.app)


class EndpointAction(object):

    def __init__(self, action):
        self.action = action
        self.response = Response(status=200, headers={})

    def __call__(self, *args):
        # Unpack args if needed, and pass them individually
        # Access JSON data from Flask request object
        json_data = request.json
        print("Received JSON data:", json_data)
        resp = self.action(json_data)

        self.response.set_data(json.dumps(json_data))
        return self.response
