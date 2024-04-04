"""
Interface for Communicating agents

@Author: Kyle McMaster
@Date: 2024-04-02

ATTRIBUTES:

TODO:

"""

from headers.EncryptionKey import EncryptionKey
from headers.CommunicationManager import CommunicationManager


from abc import ABC, abstractmethod

class CommunicatingAgent(ABC):
    

    @abstractmethod
    def updateKey(self, serviceID: str, key: EncryptionKey):
        """
        Update encryptionkey for use with other agents

        Args:
            ServiceID: ID of service associated with encryptionKey
        """

    @abstractmethod
    def getKey(self, serviceID: str) -> EncryptionKey:
        """
        returns EncryptionKey stored for a given service

        Args:
            ServiceID: ID of service associated with encryptionKey
        """

    @abstractmethod
    def sendData(self, address: str, data: object, key: EncryptionKey):
        """
        Send data to indicated address

        Args:
            address: network address of recipient In IP:port format.
            data: data to send to recipient
            key: encryption key used to encrypt data

        """

    @abstractmethod
    def recvData(self, data:object):
        """
        Recv data from indicated address

        Args:
            address: network address of sending agent In IP:port format.
            data: recved object

        Return:
            

        """