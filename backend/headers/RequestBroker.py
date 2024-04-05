"""
Responsible for managing requests from clients by routing them to the correct subsystem

@Author: Kyle McMaster
@Date: 2024-04-04

ATTRIBUTES:

TODO:

"""

from abc import ABC, abstractmethod

class RequestBroker(ABC):

    @abstractmethod
    def __init__(self):
        """
        Initialize class to prepare for communication
        """

    @abstractmethod
    def add_endpoint(self, endpoint: str, name: str, handler: callable):
        """
        Add API endpoint for HTTP requests to the server
        """

    @abstractmethod
    def add_event(self, event_name: str, handler: callable):
        """
        Add listener for Socket Events
        """
        
    @abstractmethod
    def run(self):
        """
        Host Server
        """
