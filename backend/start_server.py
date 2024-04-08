from src.MessageDeliveryServer import MessageDeliveryServer
from src.FlaskRequestBroker import FlaskRequestBroker
from src.ServerCommunicationManager import ServerCommunicationManager
from src.NoneEncryptor import NoneEncryptor
from src.JSONSerializer import JSONSerializer
from src.KerberosServerAuthManager import KerberosServerAuthManager
from src.KerberosAuthServer import KerberosAuthServer
from src.KerberosTicketServer import KerberosTicketServer
from src.AESEncryptionFunction import AESEncryptionFunction
from src.AESKeyGenerator import AESKeyGenerator

import base64
import json

'''s = KerberosAuthServer("t", None)
data = dict({"clientIDs": "sample"})
json_data = json.dumps(data)

print(s.login(json_data))'''

a = AESKeyGenerator()
print(a.generateKey())
k = b'\x81\xc9\x1cy{\xddmL\x86\x93\xc9W\x92\xd7\x93x'

print(f"K = {k.hex()}")
ab = AESEncryptionFunction()
dic = {
    "clientIDs": ["TESTID", "TESTID2"]
}
msg = json.dumps(dic)

msg = ab.encrypt(msg.encode(), k)
msg = base64.b64encode(msg)
print(f"msg= {msg}")
msg = ab.decrypt(base64.b64decode(msg), k)
print(msg)

broker = FlaskRequestBroker()
message_server_communication_manager = ServerCommunicationManager(
    'message_server',
    broker,
    AESEncryptionFunction(),
    JSONSerializer(),
    KerberosServerAuthManager()
)
auth_server_communication_manager = ServerCommunicationManager(
    'login_server',
    broker,
    NoneEncryptor(),
    JSONSerializer(),
    KerberosServerAuthManager() # think about how to handle this a little better, unnecessary to have for this server
)
ticket_server_communication_manager = ServerCommunicationManager(
    'ticket_server',
    broker,
    NoneEncryptor(),
    JSONSerializer(),
    KerberosServerAuthManager() 
)



s = MessageDeliveryServer("message_server", message_server_communication_manager)
a = KerberosAuthServer("login_server", auth_server_communication_manager)
t = KerberosTicketServer("ticket_server", ticket_server_communication_manager)

broker.start()



