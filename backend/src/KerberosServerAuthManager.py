"""
Interface for Authenticating incoming requests
Uses Kerberos to verify a user is authenticated to connect to the requested server. Not to be used in the intial authentication steps

@Author: Kyle McMaster
@Date: 2024-04-02

ATTRIBUTES:

TODO:
"""
from headers.EncryptionKey import EncryptionKey
from headers.AuthenticationManager import AuthenticationManager


import json


class KerberosServerAuthManager(AuthenticationManager):
    

    def __init__(self, args: list[object]=None):
        """
        initialize manager
        """
        self.SGT_KEY = "SGT_KEY"

    def authenticateUser(self, data: json) -> str:
        """
        authenticates user for communication with the server

        RETURN:
            EncryptionKey: to be used with the requesting agent
            return message: to be sent back to requesting agent
        """
        try:
            SGT = data['service_granting_ticket']
            print(SGT)
        except KeyError:
            return "missing field: service_granting_ticket"
                
        try:
            client_details = data['client_details']
            print(client_details)
        except KeyError:
            return "missing field: client_details"

        # TODO: decrypt SGT fields
 
        try:
            service_key = SGT['service_key']
            SGT_clientID = SGT['clientID']
            SGT_timeout = SGT['timeout_date']
        except KeyError:
            return "Incorrect Ticket"
        
        # TODO: decrypt client_details using session_key----------

        try:
            clientID = client_details['clientID']
            timestamp = client_details['timestamp']
        except KeyError:
            return "incorrect client details"
        
        if SGT_clientID != clientID or timestamp > SGT_timeout:
            return "Authentication Failed"
        
        response = {
            "clientID": clientID,
            "key": service_key,
            "message": "Authentication Success"
        }

        return json.dumps(response)