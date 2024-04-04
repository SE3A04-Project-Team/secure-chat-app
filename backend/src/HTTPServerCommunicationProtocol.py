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
from headers.CommunicationProtocol import CommunicationProtocol

from flask import Flask
from flask_socketio import SocketIO, emit, join_room, leave_room


class HTTPServerCommunicationProtocol(CommunicationProtocol):

    

    app: Flask

    
    def initialize(self, address: str):
        """
        Initialize class to prepare for communication

        Args:
            address: network address of communicating agent. In IP:port format. 
        """
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret!'
        self.socketio = SocketIO(self.app)
        self.socketio.run(self.app)

    @app.route('/')
    def connect():
        """
        Handle initial connections to the server
        """
    
        return 'Success'
    
    @app.route('/chats')
    def show_chat(clientID: bytes):
        """
        Handle initial connections to the server
        """
    
        return 'Success'

    @app.route('/chats/<chatID>')
    def show_chat():
        """
        Handle initial connections to the server
        """
    
        return 'Success'
    

        

    
    def sendData(self, send_address: str, recv_address:str, data: bytes):
        """
        Send data to indicated address. For security, data should be encrypted before sending

        Args:
            send_address: network address of recipient In IP:port format.
            recv_address: network address of sending agent In IP:port format.
            data: data to send to recipient

        """
    

    
    def recvData(self, send_address: str, recv_address:str, size: int) -> object:
        """
        Recv data from indicated address

        Args:
            send_address: network address of recipient In IP:port format.
            recv_address: network address of sending agent In IP:port format.
            size: size of data to accept in bytes

        Return:
            returns received object

        """