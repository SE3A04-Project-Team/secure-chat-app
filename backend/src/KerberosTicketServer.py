"""
Used to obtain server keys after client has been authenticated with Auth Server

@Author: Kyle McMaster
@Date: 2024-04-07

ATTRIBUTES:

TODO:

"""
from headers.CommunicatingAgent import CommunicatingAgent
from headers.CommunicationManager import CommunicationManager
from headers.KeyDistributionManager import KeyDistributionManager

from src.AESEncryptionFunction import AESEncryptionFunction


import json
import time
import base64

class KerberosTicketServer(CommunicatingAgent):
    

    def __init__(self, serverID: str, communicationManager: CommunicationManager, KDC: KeyDistributionManager):
        """
        initialize server

        """
        self.serverID = serverID
        self.communicationManager = communicationManager
        self.KDC = KDC
        self.TGS_Key = b'\xa8\xe9\xae\xa1\x99\x18\xa7R\xa3\x01Cg\xe4\x97\x86\xbf'
        self.VALID_PERIOD = 10000000
        self.encryptionFunction = AESEncryptionFunction()
        self.servers = dict(
            {"message_server": b'\xec\x12;\xd8\xdb\x18\xfcj|\xdd\xfaj\x08\x07{\xad'}
        )
        self.event_names = [

        ]
        self.event_functions = [

        ]
        self.endpoint_names = [
            "get_ticket"
        ]
        self.endpoint_functions = [
            self.get_ticket
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


    def get_ticket(self, data: json) -> str:
        """
        Grants access to server
        """
        try:
            TGT = data['ticket_granting_ticket']
            print(TGT)
        except KeyError:
            return "missing field: ticket_granting_ticket"
        
        try:
            serviceID = data['serviceID']
            print(serviceID)
        except KeyError:
            return "missing field: serviceID"
        
        try:
            client_details = data['client_details']
            print(client_details)
        except KeyError:
            return "missing field: client_details"
        

        # TODO: decrypt TGT fields
        TGT = base64.b64decode(TGT)
        TGT = self.encryptionFunction.decrypt(TGT, self.TGS_Key)
        TGT = TGT.decode()
        TGT = json.loads(TGT)
        try:
            session_key = TGT['session_key']
            TGT_clientID = TGT['clientID']
            TGT_timeout = TGT['timeout_date']
        except KeyError:
            return "Incorrect Ticket"
        
        print(session_key)
        print(TGT_clientID)
        print(TGT_timeout)
        
        # TODO: decrypt client_details using session_key----------

        try:
            clientID = client_details['clientID']
            timestamp = client_details['timestamp']
        except KeyError:
            return "incorrect client details"
        
        if TGT_clientID != clientID or timestamp > TGT_timeout:
            return "Authentication Failed"

        # TODO: GET Service_KEY
        service_key = "TEST_SERVICE_KEY"
        Timestamp = time.time()
        Validity_Period = time.time()+self.VALID_PERIOD

        Service_Granting_Ticket = {
            "service_key": service_key,
            "clientID": clientID,
            "serviceID": serviceID,
            "timestamp": Timestamp,
            "timeout_date": Validity_Period
            }
        
        # TODO: Encrypt serivce_key with Hashed_Password
        encrypted_session_key = service_key
        # TODO: encrypt TGT with TGS_KEY
        encrypted_TGT = Service_Granting_Ticket

        return_message = {
            "session_key": encrypted_session_key,
            "service_granting_ticket": encrypted_TGT
        }

        return json.dumps(return_message)


        



