from src.MessageDeliveryServer import MessageDeliveryServer
from src.FlaskRequestBroker import FlaskRequestBroker
from src.ServerCommunicationManager import ServerCommunicationManager
from src.NoneEncryptor import NoneEncryptor
from src.JSONSerializer import JSONSerializer
from src.KerberosServerAuthManager import KerberosServerAuthManager
from src.KerberosAuthServer import KerberosAuthServer

import json

s = KerberosAuthServer("t", None)
data = dict({"clientIDs": "sample"})
json_data = json.dumps(data)

print(s.login(json_data))


broker = FlaskRequestBroker()
ms_coms = ServerCommunicationManager(
    'message_server',
    broker,
    NoneEncryptor(),
    JSONSerializer(),
    KerberosServerAuthManager()
)



s = MessageDeliveryServer("message_server", ms_coms)

broker.start()



