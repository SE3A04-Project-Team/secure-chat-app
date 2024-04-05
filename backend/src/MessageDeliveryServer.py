"""
Responsible for receiving and forwarding messages between clients

Connects to message storage server to store incoming messages

@Author: Kyle McMaster
@Date: 2024-04-02

ATTRIBUTES:

TODO:
finish set up

"""
from headers.CommunicatingAgent import CommunicatingAgent
from headers.CommunicationManager import CommunicationManager

from src.ServerCommunicationManager import ServerCommunicationManager

import json


class MessageDeliveryServer(CommunicatingAgent):

    

    def __init__(self, serverID: str, communicationManager: CommunicationManager):
        """
        initialize server

        """
        self.serverID = serverID
        self.communicationManager = communicationManager
        self.event_names = [

        ]
        self.event_functions = [

        ]
        self.endpoint_names = [
            "create_room"
        ]
        self.endpoint_functions = [
            self.create_room
        ]
        self.endpoint_methods = [
            ["POST"]
        ]
        self.registerActions()

    def registerActions(self):
        """
        registers actions with the communication manager so that requests can be forwarded correctly.
        """
        self.communicationManager.registerActions(self.endpoint_names, self.endpoint_functions, self.endpoint_methods, self.event_names, self.event_functions)


    def handle_message(self, message: json):
        """
        handles the storing and forwarding of messages in the following format
        {
	        “SenderID”: str,
	        “ChatID”: str,
	        “Timestamp”: str,
	        “Message”: str,
        }
        """

    def create_room(self, roomID: str):
        """
        creates new room for messaging
        """

    def remove_room(self, roomID: str):
        """
        deletes room only if there are no more users registered to that room
        """

    def join_room(self, clientID: str, roomID: str):
        """
        adds a client to a room
        """
    
    def leave_room(self, clientID: str, roomID: str):
        """
        removes a client from a room
        """