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

from src.FirebaseMessageDatabase import FirebaseMessageDatabase


import json
from flask_socketio import join_room, emit


class MessageDeliveryServer(CommunicatingAgent):

    

    def __init__(self, serverID: str, communicationManager: CommunicationManager):
        """
        initialize server

        """
        self.serverID = serverID
        self.communicationManager = communicationManager
        self.rooms = dict[str, list[str]]
        self.databaseManager = FirebaseMessageDatabase()


        self.event_names = [
            "join_room",
            "send_message"

        ]
        self.event_functions = [
            self.join_room,
            self.handle_message
            
        ]
        self.endpoint_names = [
            "get_rooms",
            "create_room",
            "message_history"
        ]
        self.endpoint_functions = [
            self.get_rooms,
            self.create_room,
            self.get_message_history
        ]
        self.endpoint_methods = [
            ["POST"],
            ["POST"],
            ["POST"]
        ]
        self.registerActions()

    def registerActions(self):
        """
        registers actions with the communication manager so that requests can be forwarded correctly.
        """
        self.communicationManager.registerActions(self.endpoint_names, self.endpoint_functions, self.endpoint_methods, self.event_names, self.event_functions)


    def handle_message(self, args: json):
        """
        handles the storing and forwarding of messages in the following format
        {
	        “SenderID”: str,
	        “ChatID”: str,
	        “Timestamp”: int,
	        “Message”: str,
        }
        arg1: senderID
        arg2: roomID,
        arg3: timestamp
        arg4: message
        """
        print(args)
        if len(args) < 4:
            raise ValueError("Bad Message Format")
        
        senderID = args[0]
        roomID = args[1]
        timestamp = args[2]
        message = args[3]
        
        # store message
        self.databaseManager.store_message(
            user_id=senderID,
            room_id=roomID,
            timestamp=timestamp,
            message_content=message
        )

        # emit to connected clients
        # TODO: add room=roomID when rooms are set up
        emit('receive_message', 
             {
            "senderID": senderID, 
            "timestamp": timestamp,
            "message_content": message
            }
            )


    def get_message_history(self, data: json) ->str:
        try:
            roomID = data['roomID']
            print(roomID)
        except KeyError:
            return "Bad Request: args: (roomID)"
        
        msg_history = self.databaseManager.get_message_history(roomID)
        return json.dumps(msg_history)


    def get_rooms(self, data: json) -> str:
        try:
            clientID = data['clientID']
            print(clientID)
        except KeyError:
            return "Bad Request: args: (clientID)"
        
        rooms = self.databaseManager.get_chat_selection(clientID)
        if not rooms:
            return "No rooms found"
        # rooms_obj = json.loads(rooms)
        print(f"result: {rooms}")

        return_msg = {
            "rooms": rooms
        }
        return json.dumps(return_msg)


    def create_room(self, data: json) -> str:
        """
        creates new room for messaging
        Args: list of clientIDs
        """
        try:
            data['clientIDs']
        except KeyError:
            return "Bad Request: args: (clientIDs)"
        
        return self.databaseManager.create_room(data)


    def remove_room(self, roomID: json):
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
        emit("send_message", f"Welcome", room=room)
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