"""
Performs initial login authentication for user

@Author: Kyle McMaster
@Date: 2024-04-07

ATTRIBUTES:

TODO:
finish set up

"""
from headers.CommunicatingAgent import CommunicatingAgent
from headers.CommunicationManager import CommunicationManager
from headers.KeyDistributionManager import KeyDistributionManager
from headers.Hasher import Hasher

from src.AESKeyDistributionCenter import AESKeyDistributionCenter
from src.Hashing32Bit import Hashin32Bit
from src.AESEncryptionFunction import AESEncryptionFunction

import json
import time
import base64


class KerberosAuthServer(CommunicatingAgent):


    def __init__(self, serverID: str, communicationManager: CommunicationManager, KDC: KeyDistributionManager):
        """
        initialize server

        """
        self.serverID = serverID
        self.communicationManager = communicationManager
        self.passwordHasher = Hashin32Bit()
        self.KDC = KDC
        self.TGS_Key = b'\xa8\xe9\xae\xa1\x99\x18\xa7R\xa3\x01Cg\xe4\x97\x86\xbf'
        self.VALID_PERIOD = 10000000
        self.encryptionFunction = AESEncryptionFunction()
        self.credentials = dict(
            {"USER1": "PASSWORD1",
             "fURjH98QX4A0Ro6swlVb": "PASSWORD1"}
        )
        self.event_names = [

        ]
        self.event_functions = [

        ]
        self.endpoint_names = [
            "login"
        ]
        self.endpoint_functions = [
            self.login
        ]
        self.endpoint_methods = [
            ["POST"]
        ]
        self.registerActions()

    
    def registerActions(self):
        """
        registers actions with the communication manager so that requests can be forwarded correctly.

        """
        self.communicationManager.registerActions(self.endpoint_names, self.endpoint_functions, self.endpoint_methods, self.event_names, self.event_functions)

    def login(self, data: json) -> str:
        """
        returns a session_key and TicketGrantingTicket
        Session Key is encrypted using the stored password for the user and TicketGrantingTicket is encrypted using the Ticket_Server_Key
        """

        try:
            clientID = data['clientID']
            print(clientID)
        except KeyError:
            return "missing field: clientID"
        
        try:
            password = self.__get_credential(clientID)
        except KeyError:
            return "User not found"
        
        Hashed_Password = self.passwordHasher.hash(password)

        Session_Key = self.KDC.getKey(clientID, 'ticket_server')
        Timestamp = time.time()
        Validity_Period = time.time()+self.VALID_PERIOD

        Ticket_Granting_Ticket = {
            "session_key": str(base64.b64encode(Session_Key +b'==')),
            "clientID": clientID,
            "timestamp": Timestamp,
            "timeout_date": Validity_Period
            }
        
        print(Session_Key)
        #Encrypt Session_Key with Hashed_Password
        encrypted_session_key = self.encryptionFunction.encrypt(Session_Key, Hashed_Password)
        encrypted_session_key = str(base64.b64encode(encrypted_session_key)).lstrip('b').strip('\'')
        print("encrypted_session_key: ", str(encrypted_session_key) )
        # encrypt TGT with TGS_KEY
        Ticket_Granting_Ticket = json.dumps(Ticket_Granting_Ticket)
        Ticket_Granting_Ticket = Ticket_Granting_Ticket.encode()
        encrypted_TGT = self.encryptionFunction.encrypt(Ticket_Granting_Ticket, self.TGS_Key)
        encrypted_TGT = str(base64.b64encode(encrypted_TGT)).lstrip('b').strip('\'')

        return_message = {
            "session_key": encrypted_session_key,
            "ticket_granting_ticket": encrypted_TGT
        }
        
        return json.dumps(return_message)

    def __get_credential(self, clientID:str): 
        if clientID not in self.credentials.keys():
            raise KeyError("Client not registered")
        return self.credentials.get(clientID)
        
        

            


        

