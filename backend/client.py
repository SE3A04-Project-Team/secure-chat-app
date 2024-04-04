from src.TestClient import TestClient

import sys

HOST = sys.argv[1]
PORT = sys.argv[2]
clientID = sys.argv[3]

address = HOST + ":" + PORT

c = TestClient()

c.run_client(address, clientID)