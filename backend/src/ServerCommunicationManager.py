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
from headers.EncryptionFunction import EncryptionFunction
from headers.RequestBroker import RequestBroker
from headers.Serializer import Serializer
from headers.AuthenticationManager import AuthenticationManager

from typing import Callable
import json
import threading


class ServerCommunicationManager(CommunicationManager):

    keys: dict[str: EncryptionKey]

    def __init__(self, 
                 serverName: str,
                 broker: RequestBroker, 
                 encryptionFunction: EncryptionFunction,
                 serializer: Serializer,
                 authenticationManager: AuthenticationManager):
        """
        initialize manager
        """
        self.serverName = serverName
        self.broker = broker
        self.encryptionFunction = encryptionFunction
        self.serializer = serializer
        self.authenticationManager = authenticationManager


        self.keys = dict()




    def processData(self, *args) -> object:
        """
        prepares incoming data before passing to server for processing then
        prepares data from server for sending 
        """
        print(f"process_data {args}")
        """
        key = self.keys.get(senderID)
        if not key:
            return f"401: user not authenticated. poll {self.serverName}/auth"

        decrypted_data = self.encryptionFunction.decrypt(data, key)
        deserialized_data = self.serializer.deserialize(decrypted_data)

        response = handler(deserialized_data)

        serialized_response = self.serializer.serialize(response)
        encrypted_response = self.encryptionFunction.encrypt(serialized_response, key)
        return encrypted_response
    """


    def registerActions(self, endpoint_names: list[str], endpoint_handlers: list[Callable], endpoint_methods:list[str], event_names: list[str], event_handlers: list[Callable]):
        """
        registers actions with the broker so that requests can be forwarded correctly.

        """
        self.broker.add_endpoint(f'/{self.serverName}/auth', f'/{self.serverName}/auth', self.authenticateUser, ["GET", "POST"])

        for i, endpoint in enumerate(endpoint_names):
            self.broker.add_endpoint(f'/{self.serverName}/{endpoint}', f'/{self.serverName}/{endpoint}', ProxyMethod(endpoint_handlers[i]), endpoint_methods[i])
            
        
        for i, event in enumerate(event_names):
            self.broker.add_event(event, ProxyEvent(event_handlers[i]))

        


    def updateKey(self, serviceID: str, key: EncryptionKey):
        """
        Update encryptionkey for use with other agents

        Args:
            ServiceID: ID of service associated with encryptionKey
        """

    def dump_keys(self):
        """
        Remove all session keys on event of refresh
        """

    def authenticateUser(self, message: json) -> str:
        """
        authenticates user for communication with the server
        """
        #print(message)
        auth_response = self.authenticationManager.authenticateUser(message)
        try: 
            auth_data = json.loads(auth_response)
        except:
            return auth_response
        print(f"auth_data: {auth_data}")
        try:
            key = auth_data['key']
            clientID = auth_data['clientID']
            message = auth_data['message']
        except KeyError:
            return auth_response
        
        self.updateKey(clientID, key)
        return message

      


class ProxyMethod(object):

    def __init__(self, action: Callable):
        self.action = action

    def __call__(self, data: json):
        print("Received args by proxy:", data)
        # Unpack args if needed, and pass them individually

        resp = self.action(data)
        print(f"Response recv by proxy:{resp}") #consider jsonifying
        return resp
    
class ProxyEvent(object):
    def __init__(self, action: Callable):
        self.action = action

    def __call__(self, data: json):
        print("Received args by proxy:", data)
        # Unpack args if needed, and pass them individually

        resp = self.action(data)
        print(f"Response recv by proxy:{resp}") #consider jsonifying
        return resp


