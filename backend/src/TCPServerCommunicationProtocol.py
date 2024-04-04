"""
Communicates with clients over TCP

@Author: Kyle McMaster
@Date: 2024-04-02

ATTRIBUTES:
server_socket (socket.socket): socket for accepting incoming connections
communication_manager (CommunicationManager): manager for receiving data

TODO:
Complete Doc-string
Develop functions

"""
from headers.CommunicationProtocol import CommunicationProtocol
from headers.CommunicationManager import CommunicationManager

import socket
import threading

class TCPServerCommunicationProtocol(CommunicationProtocol):

    mutex = threading.Lock()
    communication_manager: CommunicationManager
    client_return_addresses: dict[str, socket.socket]
    


    def initialize(self, address: str, manager: CommunicationManager):
        """
        Initialize class to prepare for communication and listen for connections.
        Makes a new thread for each incoming connection.

        Args:
            address: network address of communicating agent. In IP:port format. 
        """
        self.communication_manager = manager
        self.client_return_addresses = dict()

        HOST: str
        PORT: int

        try:
            HOST = address.split(":")[0]
            PORT = int(address.split(":")[1])

        except IndexError:
            print("invalid format. address should be in form IP:PORT")
        except ValueError:
            print("Ensure port is an int")
        
        if PORT <= 1023:
            raise ValueError("Port must be greater than 1023.")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(4)
            host, port = s.getsockname()
            print(f"Server listening on {host}:{port}")

            while True:
                client_socket, addr = s.accept()
                print(f"accepted connection at {addr}")
                client_handler = threading.Thread(target=self.__acceptConnection, args=(client_socket,))
                client_handler.start()




    def __acceptConnection(self, client: socket.socket):
        clientID = str(client.recv(1024), 'utf-8')
        with self.mutex:
                self.client_return_addresses.update({clientID: client})
                self.communication_manager.registerAgent(clientID)
        while True:
            data = client.recv(1024)
            if not data:
                break
            # address = client.getsockname()[0] + ":" + str(client.getsockname()[1])

            with self.mutex:
                self.communication_manager.recvData(clientID, data)

            # send response
        
        with self.mutex:
            self.client_return_addresses.update({clientID: None})
            self.communication_manager.unregisterAgent(clientID)
        client.close()
        


    def sendData(self, send_address: str, recv_address:str, data: bytes):
        """
        Send data to indicated address. For security, data should be encrypted before sending

        Args:
            send_address: network address of recipient In IP:port format.
            recv_address: network address of sending agent In IP:port format.
            data: data to send to recipient

        """
        client = self.client_return_addresses.get(send_address)
        print("sending")
        client.send(data)
        print("sent")
    

    def recvData(self, send_address: str, recv_address:str, size: int) -> object:
        """
        Recv data from indicated address

        Args:
            send_address: network address of recipient In IP:port format.
            recv_address: network address of sending agent In IP:port format.
            size: size of data to accept in bytes

        Return:
            returns received object

        """


