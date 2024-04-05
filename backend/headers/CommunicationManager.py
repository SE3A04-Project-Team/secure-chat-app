"""
Interface for Managing Communication between communicating agents

@Author: Kyle McMaster
@Date: 2024-04-02

ATTRIBUTES:

TODO:

"""
from headers.EncryptionKey import EncryptionKey
from headers.EncryptionFunction import EncryptionFunction
from headers.RequestBroker import RequestBroker
from headers.Serializer import Serializer
from headers.AuthenticationManager import AuthenticationManager

import json
from abc import ABC, abstractmethod


class CommunicationManager(ABC):
    
    @abstractmethod
    def __init__(self, 
                 broker: RequestBroker, 
                 encryptionFunction: EncryptionFunction,
                 serializer: Serializer,
                 authenticationManager: AuthenticationManager):
        """
        initialize manager

        """

    @abstractmethod
    def registerActions(self, names: str, handlers: list[function]):
        """
        registers actions with the broker so that requests can be forwarded correctly.

        """

    @abstractmethod
    def updateKey(self, serviceID: str, key: EncryptionKey):
        """
        Update encryptionkey for use with other agents

        Args:
            ServiceID: ID of service associated with encryptionKey
        """

    @abstractmethod
    def authenticateUser(self, message: json) -> json:
        """
        authenticates user for communication with the server
        """