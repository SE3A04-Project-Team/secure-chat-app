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
import base64


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


        self.keys = dict({
            "TEST_USER" : b'\x81\xc9\x1cy{\xddmL\x86\x93\xc9W\x92\xd7\x93x',
        })




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
            self.broker.add_endpoint(f'/{self.serverName}/{endpoint}', f'/{self.serverName}/{endpoint}', ProxyMethod(self, endpoint_handlers[i]), endpoint_methods[i])
            
        
        for i, event in enumerate(event_names):
            self.broker.add_event(event, ProxyEvent(self, event_handlers[i]))

        


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

    def encrypt(self, clientID:str, data:json) -> bytes:
        """
        encrpyt message using given clientID
        """
        if clientID not in self.keys.keys():
            raise KeyError ("405: No Key found, please authenticate")
        
        key = self.keys.get(clientID)

        data = json.dumps(data)
        encoded_data = data.encode()
        encrypted_data = self.encryptionFunction.encrypt(encoded_data, key)
        return base64.b64encode(encrypted_data)

        

    def decrypt(self, clientID:str, data:bytes) -> json:
        """
        Decrypt message using given clientID
        """
        if clientID not in self.keys.keys():
            raise KeyError ("405: No Key found, please authenticate")
        
        key = self.keys.get(clientID)

        decoded_data = base64.b64decode(data)
        decrypted_data = self.encryptionFunction.decrypt(decoded_data, key)
        # print(f"decrypted_data: {decrypted_data}")
        # print(decrypted_data.decode())
        return json.loads(decrypted_data.decode())




class ProxyMethod(object):

    def __init__(self, manager: ServerCommunicationManager, action: Callable):
        self.action = action
        self.manager = manager

    def __call__(self, headers, json_data: json):
        """
        Handles the encryption and decryption of server calls
        Data is received in base 64, and decrypted using client Key
        unencrypted data is in 'utf-8', which is converted to string
        string is attempted to be converted to dict object
        """
        print("Received headers by proxy:", headers)
        print("Received args by proxy:", json_data)
        # Unpack args if needed, and pass them individually
        secure_message = True
        clientID = headers['clientID']
        try:
            data = json_data['secure_data']
        except KeyError:
            print("no secure data")
            secure_message = False
            unencrypted_data = json_data

        if secure_message:
            try:
                unencrypted_data = self.manager.decrypt(clientID, data)
                print(unencrypted_data)
            except KeyError:
                return ("405: No Key found, please authenticate")
            

        resp = self.action(unencrypted_data)
        print(resp)

        if secure_message:
            try:
                resp = self.manager.encrypt(clientID, resp)
            except KeyError:
                return ("405: No Key found, please authenticate")

        print(f"Response recv by proxy:{resp}") #consider jsonifying
        return resp
    
class ProxyEvent(object):
    def __init__(self, manager: ServerCommunicationManager, action: Callable):
        self.action = action
        self.manager = manager

    def __call__(self, data: json):
        print("Received args by proxy:", data)
        # Unpack args if needed, and pass them individually

        resp = self.action(data)
        print(f"Response recv by proxy:{resp}") #consider jsonifying
        return resp


