from src.MessageDeliveryServer import MessageDeliveryServer
from src.FlaskRequestBroker import FlaskRequestBroker
from src.ServerCommunicationManager import ServerCommunicationManager
from src.NoneEncryptor import NoneEncryptor
from src.JSONSerializer import JSONSerializer
from src.KerberosServerAuthManager import KerberosServerAuthManager

import sys


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



