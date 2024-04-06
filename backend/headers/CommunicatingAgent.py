"""
Interface for Communicating agents

@Author: Kyle McMaster
@Date: 2024-04-02

ATTRIBUTES:

TODO:

"""

from headers.CommunicationManager import CommunicationManager


from abc import ABC, abstractmethod

class CommunicatingAgent(ABC):
    
    @abstractmethod
    def __init__(self, serverID: str, communicationManager: CommunicationManager):
        """
        initialize server

        """

    @abstractmethod
    def registerActions(self):
        """
        registers actions with the communication manager so that requests can be forwarded correctly.

        """
