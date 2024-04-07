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
from flask_socketio import SocketIO
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
        self.socketio.on_event(event_name, EventAction(handler))
        print(f"registered {event_name}")


    def start(self, host:str='0.0.0.0', port:int=5050):
        """
        Host Server
        """
        self.socketio.run(self.app, host=host, port=port)

    

class EventAction(object):
    def __init__(self, action):

        self.action = action
        
    def __call__(self, *args):
        # JANKY - should fix
        print(args)
        self.action(args)
        


class EndpointAction(object):

    def __init__(self, action):
        self.action = action
        self.response = Response(status=200, headers={})

    def __call__(self, *args):
        #print("Received args by endpoint:", args)
        # Access JSON data from Flask request object
        
        json_data = request.json # comes in as json dict type
        print("Received JSON data by endpoint:", json_data)

        resp = self.action(json_data)

        print(f"Response recv by broker:{resp}") #consider jsonifying
        self.response.set_data(resp) # set to a string to return
        print(self.response)
        return self.response
