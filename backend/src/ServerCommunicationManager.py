"""
Manages communication with other agents for agents filling the role of a server

@Author: Kyle McMaster
@Date: 2024-04-02

ATTRIBUTES:

TODO:
Complete Doc-string
Develop functions
Flesh out __init__ with remaining agents
add functionality to obtain key

"""
from headers.CommunicationManager import CommunicationManager
from headers.EncryptionKey import EncryptionKey
from headers.CommunicationProtocol import CommunicationProtocol
from headers.EncryptionFunction import EncryptionFunction
from headers.Serializer import Serializer
from headers.CommunicatingAgent import CommunicatingAgent

from src.TCPServerCommunicationProtocol import TCPServerCommunicationProtocol
from src.NoneEncryptor import NoneEncryptor


import threading


class ServerCommunicationManager(CommunicationManager):

    protocol: CommunicationProtocol
    encryptor: EncryptionFunction
    serializer: Serializer
    agent: CommunicatingAgent
    keys: dict[str: EncryptionKey]
    registered_agents: list[str]

    def __init__(self, agent: CommunicatingAgent, address: str) -> None:
        """
        Initialize class to prepare for communication

        Args:
            address: network address of communicating agent. In IP:port format. 
        """
        self.agent = agent

        self.protocol = TCPServerCommunicationProtocol()
        self.encryptor = NoneEncryptor()
        

        self.keys = dict()
        self.registered_agents = list()

        protocol_handler = threading.Thread(target=self.protocol.initialize, args=(address,self))
        protocol_handler.start()
      


    def registerAgent(self, clientID: str):
        """
        Add agent to list of currently connected agents

        Args:
            address: network address of communicating agent. In IP:port format. 
        """
        self.registered_agents.append(clientID)
        print(f"registered {clientID}")


    def unregisterAgent(self, clientID: str):
        """
        remove agent from list of currently connected agents

        Args:
            address: network address of communicating agent. In IP:port format. 
        """
        try:
            self.registered_agents.remove(clientID)
        except:
            pass


    
        
    def sendData(self, address: str, data: object):
        """
        Send data to indicated address. For security, data should be encrypted before sending

        Args:
            address: network address of recipient In IP:port format.
            data: data to send to recipient
            key: encryption key used to encrypt data

        """
        # check if client is connected, if not add to backlog

        # serialize
        # encrypt
        # send IF client is open

        if address not in self.registered_agents:
            #add to message backlog
            return
        
        message = bytes(data, 'utf-8')
        self.protocol.sendData(address, None, message)
        


    
    def recvData(self, address: str, data: bytes):
        """
        Recv data from indicated address

        Args:
            address: network address of sending agent In IP:port format.
            size: size of data to accept in bytes


        Return:
            returns received object

        """
        
        # decrypted_data = self.encryptor.decrypt(data, self.keys.get(address))
        # message = self.serializer.deserialize(decrypted_data)
        message = str(data, 'utf-8')
        self.agent.recvData(message)


    def updateKey(self, serviceID: str, key: EncryptionKey):
        """
        Update encryptionkey for use with other agents

        Args:
            ServiceID: ID of service associated with encryptionKey
        """
        self.keys.update({serviceID: key})


