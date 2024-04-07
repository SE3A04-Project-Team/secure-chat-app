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


import json
from flask_socketio import SocketIO, join_room, emit


class MessageDeliveryServer(CommunicatingAgent):

    

    def __init__(self, serverID: str, communicationManager: CommunicationManager):
        """
        initialize server

        """
        self.serverID = serverID
        self.communicationManager = communicationManager
        self.rooms = dict[str, list[str]]

        self.event_names = [
            "join_room"
        ]
        self.event_functions = [
            self.join_room
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


    def create_room(self, data: str) -> str:
        """
        creates new room for messaging
        Args: roomID
        """
        print(f"RECEIVED ARGS BY SERVER: {data}")
        room = "14"
        return f"created room: {room}"

    def remove_room(self, roomID: str):
        """
        SOCKET EVENT
        deletes room only if there are no more users registered to that room
        """

    def join_room(self, data) -> str:
        """
        SOCKET EVENT
        adds a client to a room
        """
        data = json.dumps(data)
        print(f"RECEIVED ARGS BY SERVER: {data}")
        
        room = "14"
        join_room("14")
        emit("send_message", f"Welcome")
        return f"joined room: {room}"
        # add create room function
        return f"joined room"
        if roomID not in self.rooms.keys:
            self.create_room(roomID)
        
        if clientID not in self.rooms.get(roomID):
            self.rooms.get(roomID).append(clientID)

        # get old messages
        
        return f"joined room {roomID}"

    
    def leave_room(self, clientID: str, roomID: str):
        """
        removes a client from a room
        """