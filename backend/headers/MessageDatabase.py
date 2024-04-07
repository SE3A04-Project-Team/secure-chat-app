"""
Interface for Storing messages and chat rooms

@Author: Kyle McMaster
@Date: 2024-04-06

ATTRIBUTES:

TODO:
"""
from abc import ABC , abstractmethod

class MessageDatabase(ABC):

    @abstractmethod
    def __init__(self) -> None:
        """
        Initialize database for communication
        """
    @abstractmethod
    def get_rooms(self, clientID: str) -> list[str, list[str]]:
        """
        Get list of rooms a client can communicate in
        """
    @abstractmethod
    def join_room(self, clientID: str, roomID: str):
        """
        add client to room
        """    
    @abstractmethod
    def leave_room(self, clientID: str, roomID: str):
        """
        Remove client from room
        """
    @abstractmethod
    def get_message_history(self, roomID: str, start: int, end: int) -> list[list[str]]:
        """
        Get a list of messages from the indicated room, starting from the most recent = 0
        """
    @abstractmethod
    def store_message(self, roomID: str, message: list[str]):
        """
        Add a message to the room chat log
        """




