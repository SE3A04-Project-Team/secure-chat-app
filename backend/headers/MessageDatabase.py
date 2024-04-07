"""
Interface for Storing messages and chat rooms

@Author: Kyle McMaster, Aidan Froggatt
@Date: 2024-04-07

ATTRIBUTES:

TODO:
"""
from abc import ABC, abstractmethod

class MessageDatabase(ABC):

    class DatabaseRoomFunctions(ABC):

        @abstractmethod
        def create_room(self, room: dict) -> dict:
            """
            Create a new room in the database
            """
        
        @abstractmethod
        def get_rooms(self, user_id: str) -> list[str, list[str]]:
            """
            Get list of rooms a client can communicate in
            """
        
        @abstractmethod
        def join_room(self, user_id: str, roomID: str):
            """
            add client to room
            """    
        
        @abstractmethod
        def leave_room(self, user_id: str, roomID: str):
            """
            Remove client from room
            """

    class DatabaseMessageFunctions(ABC):

        @abstractmethod
        def get_message_history(self, room_id: str) -> dict:
            """
            Get a list of messages from the indicated room, starting from the most recent = 0
            """
        
        @abstractmethod
        def store_message(self, room_id: str, user_id: str, message: list[str]):
            """
            Add a message to the room chat log
            """

    class DatabaseUserFunctions(ABC):
        
        @abstractmethod
        def create_user(self, user: dict) -> dict:
            """
            Create a new user in the database
            """
        
        @abstractmethod
        def get_user(self, user_id: str) -> dict:
            """
            Get a user from the database
            """
        
        @abstractmethod
        def delete_user(self, user_id: str) -> dict:
            """
            Delete a user from the database
            """

    class DatabaseContactFunctions(ABC):

        @abstractmethod
        def add_contact(self, user_id: str, contact_id: str) -> dict:
            """
            Add a contact to a user's contact list
            """
        
        @abstractmethod
        def remove_contact(self, user_id: str, contact_id: str) -> dict:
            """
            Remove a contact from a user's contact list
            """
