"""
Interface for Managing Communication between communicating agents

@Author: Kyle McMaster
@Date: 2024-04-02

ATTRIBUTES:

TODO:

"""
from headers.EncryptionKey import EncryptionKey
# from headers.CommunicatingAgent import CommunicatingAgent


from abc import ABC, abstractmethod

class CommunicationManager(ABC):
        

    @abstractmethod
    def sendData(self, address: str, data: object):
        """
        Send data to indicated address. For security, data should be encrypted before sending

        Args:
            address: network address of recipient In IP:port format.
            data: data to send to recipient
            key: encryption key used to encrypt data

        """
    
    @abstractmethod
    def registerAgent(self, clientID: str):
        """
        Add agent to list of currently connected agents

        Args:
            address: network address of communicating agent. In IP:port format. 
        """
        
    @abstractmethod
    def unregisterAgent(self, clientID: str):
        """
        remove agent from list of currently connected agents

        Args:
            address: network address of communicating agent. In IP:port format. 
        """

    @abstractmethod
    def recvData(self, address: str, data:bytes):
        """
        Recv data from indicated address

        Args:
            address: network address of sending agent In IP:port format.
            size: size of data to accept in bytes

        Return:
            returns received object

        """

    @abstractmethod
    def updateKey(self, serviceID: str, key: EncryptionKey):
        """
        Update encryptionkey for use with other agents

        Args:
            ServiceID: ID of service associated with encryptionKey
        """
        