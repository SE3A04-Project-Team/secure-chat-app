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

import json
import time


class KerberosAuthServer(CommunicatingAgent):


    def __init__(self, serverID: str, communicationManager: CommunicationManager):
        """
        initialize server

        """
        self.serverID = serverID
        self.communicationManager = communicationManager
        self.TGS_Key = "TGS_KEY"
        self.VALID_PERIOD = 10000000
        self.credentials = dict(
            {"USER1": "PASSWORD1"}
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

        Session_Key = "TEST_KEY"
        Timestamp = time.time()
        Validity_Period = time.time()+self.VALID_PERIOD

        Ticket_Granting_Ticket = {
            "session_key": Session_Key,
            "clientID": clientID,
            "timestamp": Timestamp,
            "timeout_date": Validity_Period
            }
        

        #Encrypt Session_Key with Hashed_Password
        encrypted_session_key = Session_Key
        # encrypt TGT with TGS_KEY
        encrypted_TGT = Ticket_Granting_Ticket

        return_message = {
            "session_key": encrypted_session_key,
            "ticket_granting_ticket": encrypted_TGT
        }
        
        return json.dumps(return_message)

    def __get_credential(self, clientID:str): 
        if clientID not in self.credentials.keys():
            raise KeyError("Client not registered")
        return self.credentials.get(clientID)
        
        

            


        

