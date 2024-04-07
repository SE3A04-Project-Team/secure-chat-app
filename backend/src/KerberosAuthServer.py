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



class KerberosAuthServer(CommunicatingAgent):


    def __init__(self, serverID: str, communicationManager: CommunicationManager):
        """
        initialize server

        """
        self.serverID = serverID
        self.communicationManager = communicationManager
        self.TGS_Key = "ABCDEFG"
        self.credentials = dict(
            {}
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
        # self.registerActions()

    
    def registerActions(self):
        """
        registers actions with the communication manager so that requests can be forwarded correctly.

        """
        self.communicationManager.registerActions(self.endpoint_names, self.endpoint_functions, self.endpoint_methods, self.event_names, self.event_functions)

    def login(self, data: str) -> str:
        """
        returns a session_key and TicketGrantingTicket
        Session Key is encrypted using the stored password for the user and TicketGrantingTicket is encrypted using the Ticket_Server_Key
        """
        try:
            json_data = json.loads(data)
            #print(json_data)
        except json.decoder.JSONDecodeError:
            return "Incorrect JSON format"

        try:
            clientID = json_data['clientID']
            print(clientID)
        except KeyError:
            return "missing field: clientID"
        

            


        

