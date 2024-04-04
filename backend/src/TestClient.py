"""
Simple Client for testing message delivery server

@Author: Kyle McMaster
@Date: 2024-04-02

ATTRIBUTES:

TODO:
Complete Doc-string
Develop functions
Flesh out __init__ with remaining agents
add functionality to obtain key

"""

import socket
import threading


class TestClient:

    def run_client(self, address: str, clientID:str):
        HOST: str
        PORT: int

        try:
            HOST = address.split(":")[0]
            PORT = int(address.split(":")[1])

        except IndexError:
            print("invalid format. address should be in form IP:PORT")
        except ValueError:
            print("Ensure port is an int")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((HOST, PORT))
                s.send(bytes(clientID, 'utf-8'))
            except ConnectionError:
                print(f"Connection refused. Check address of server (current address {HOST}:{PORT})")

            msg_listener = threading.Thread(target=self.recv_msg, args=(s,))
            msg_listener.start()

            while True:
                targets = ["USER1","USER2","USER3"]
                msg = input()
                msg = (f"{clientID};{targets};{msg}")
                s.send(bytes(msg, 'utf-8'))

    def recv_msg(self, socket: socket.socket):
        print("listening")
        while True:
            data = socket.recv(1024)
            if not data:
                break
            print(str(data,'utf-8'))
        socket.close()
