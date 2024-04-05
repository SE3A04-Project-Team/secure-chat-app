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


from flask import Flask
from flask_socketio import SocketIO, emit


class FlaskRequestBroker(RequestBroker):
    
    def initialize(self):
        """
        Initialize class to prepare for communication
        """

        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret!'
        self.socketio = SocketIO(self.app)


    def add_endpoint(self, endpoint: str, name: str, handler: callable):
        """
        Add API endpoint for HTTP requests to the server

        Args:  
        """
        self.app.add_url_rule(endpoint, name, handler)


    def add_event(self, event_name: str, handler: callable):
        """
        Add listener for Socket Events

        Args:
        """
        self.socketio.on_event(event_name, handler)


    def run(self):
        """
        Host Server
        """
        self.socketio.run(self.app)

'''


    def index(self):
        return "index_test"
    
    def message_server(self):
        return "Message"

    def handle_message(self, message):
        # self.manager.recvData(message)
        emit('message', message)

'''
