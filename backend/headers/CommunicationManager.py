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

from abc import ABC, abstractmethod
from typing import Callable
import json


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
    def processData(self, data: bytes, handler: Callable) -> bytes:
        """
        prepares incoming data before passing to server for processing
        """

    @abstractmethod
    def registerActions(self, endpoint_names: list[str], endpoint_handlers: list[Callable], endpoint_methods:list[str], event_names: list[str], event_handlers: list[Callable]):
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
    def dump_keys(self):
        """
        Remove all session keys on event of refresh
        """

    @abstractmethod
    def authenticateUser(self, message: json) -> json:
        """
        authenticates user for communication with the server
        """