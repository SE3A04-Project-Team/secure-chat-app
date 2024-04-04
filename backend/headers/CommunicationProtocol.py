"""
Responsible for sending and receiving data from communicating agents

@Author: Kyle McMaster
@Date: 2024-04-02

ATTRIBUTES:

TODO:

"""
from abc import ABC, abstractmethod

class CommunicationProtocol(ABC):
    @abstractmethod
    def initialize(self, address: str):
        """
        Initialize class to prepare for communication

        Args:
            address: network address of communicating agent. In IP:port format. 
        """
        

    @abstractmethod
    def sendData(self, send_address: str, recv_address:str, data: bytes):
        """
        Send data to indicated address. For security, data should be encrypted before sending

        Args:
            send_address: network address of recipient In IP:port format.
            recv_address: network address of sending agent In IP:port format.
            data: data to send to recipient

        """
    

    @abstractmethod
    def recvData(self, send_address: str, recv_address:str, size: int) -> object:
        """
        Recv data from indicated address

        Args:
            send_address: network address of recipient In IP:port format.
            recv_address: network address of sending agent In IP:port format.
            size: size of data to accept in bytes

        Return:
            returns received object

        """