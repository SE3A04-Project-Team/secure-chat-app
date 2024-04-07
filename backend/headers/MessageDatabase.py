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

        @staticmethod
        @abstractmethod
        def create_room(room: dict) -> dict:
            """
            Create a new room in the database
            """
        
        @staticmethod
        @abstractmethod
        def get_rooms(user_id: str) -> list[str, list[str]]:
            """
            Get list of rooms a client can communicate in
            """

        @staticmethod
        @abstractmethod
        def join_room(user_id: str, roomID: str):
            """
            add client to room
            """   

        @staticmethod
        @abstractmethod
        def leave_room(user_id: str, roomID: str):
            """
            Remove client from room
            """

    class DatabaseMessageFunctions(ABC):

        @staticmethod
        @abstractmethod
        def get_message_history(room_id: str) -> dict:
            """
            Get a list of messages from the indicated room, starting from the most recent = 0
            """
        
        @staticmethod
        @abstractmethod
        def store_message(room_id: str, user_id: str, message: list[str]):
            """
            Add a message to the room chat log
            """

    class DatabaseUserFunctions(ABC):
        
        @staticmethod
        @abstractmethod
        def create_user(user: dict) -> dict:
            """
            Create a new user in the database
            """
        
        @staticmethod
        @abstractmethod
        def get_user(user_id: str) -> dict:
            """
            Get a user from the database
            """
        
        @staticmethod
        @abstractmethod
        def delete_user(user_id: str) -> dict:
            """
            Delete a user from the database
            """

    class DatabaseContactFunctions(ABC):

        @staticmethod
        @abstractmethod
        def add_contact(user_id: str, contact_id: str) -> dict:
            """
            Add a contact to a user's contact list
            """
        
        @staticmethod
        @abstractmethod
        def remove_contact(user_id: str, contact_id: str) -> dict:
            """
            Remove a contact from a user's contact list
            """
