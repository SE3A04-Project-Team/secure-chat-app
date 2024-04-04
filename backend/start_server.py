from src.MessageDeliveryServer import MessageDeliveryServer

import sys

HOST = sys.argv[1]
PORT = sys.argv[2]

address = HOST + ":" + PORT

s = MessageDeliveryServer(address)



