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
from headers.EncryptionKey import EncryptionKey
from headers.CommunicationManager import CommunicationManager

from src.ServerCommunicationManager import ServerCommunicationManager


class MessageDeliveryServer(CommunicatingAgent):

    communication_manager: CommunicationManager

    def __init__(self, address: str):
        """
        Initialize class to prepare for communication.

        Args:
            address: network address of communicating agent. In IP:port format.
        """
        self.communication_manager = ServerCommunicationManager(self, address)


    def updateKey(self, serviceID: str, key: EncryptionKey):
        """
        Update encryptionkey for use with other agents

        Args:
            ServiceID: ID of service associated with encryptionKey
        """


    def getKey(self, serviceID: str) -> EncryptionKey:
        """
        returns EncryptionKey stored for a given service

        Args:
            ServiceID: ID of service associated with encryptionKey
        """


    def sendData(self, address: str, data: object, key: EncryptionKey):
        """
        Send data to indicated address

        Args:
            address: network address of recipient In IP:port format.
            data: data to send to recipient
            key: encryption key used to encrypt data

        """

    def recvData(self, data:object):
        """
        Recv data from indicated address

        Args:
            address: network address of sending agent In IP:port format.
            data: recved object

        Return:
            
        """
        print(data)
        sender,targets,content = self.__parse_string_message(data)
        self.sendMessage(content, sender, targets)

    def __parse_string_message(self, msg: str):
        sender = msg.split(";")[0]
        targets = msg.split(";")[1].strip('[]').replace("\'", "").split(", ")
        content = msg.split(";")[2]
        return [sender,targets,content]

    def sendMessage(self, message:object, sender: str, targets: list[str]):
        """
        Route message to intended recipients

        Args:
            message: message received by sender to send to targets
            sender: clientID of sender
            targets: clientIDs of receivers
        Return:
            
        """

        # store message
        for target in targets:
            if sender != target:
                self.communication_manager.sendData(target, f"({sender}):{message}")


        