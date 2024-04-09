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
from src.AESKeyDistributionCenter import AESKeyDistributionCenter
from src.KeyStorageFirebase import KeyStorageFirebase

import base64
import json
import time


data = dict({"clientIDs": "sample"})
json_data = json.dumps(data)



a = AESKeyGenerator()
print(a.generateKey())
k = b'\x80L-FI\x0ev\xae\x1f\xe6C\xe5\xcd\x04\xc3\x9e'
k = base64.b64encode(k)
k = b'gEwtRkkOdq4f5kPlzQTDng=='
print(f"k = {k}")
ab = AESEncryptionFunction()
dic = {
    "client_details": {
        "clientID": "fURjH98QX4A0Ro6swlVb",
        "timestamp": time.time()
    }
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
s = MessageDeliveryServer("message_server", message_server_communication_manager)


key_database = KeyStorageFirebase()
KDC = AESKeyDistributionCenter(key_database)


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


a = KerberosAuthServer("login_server", auth_server_communication_manager, KDC)
t = KerberosTicketServer("ticket_server", ticket_server_communication_manager, KDC)

broker.start()



