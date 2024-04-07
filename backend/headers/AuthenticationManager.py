"""
Interface for Authenticating incoming requests

@Author: Kyle McMaster
@Date: 2024-04-02

ATTRIBUTES:

TODO:
"""
from headers.EncryptionKey import EncryptionKey

from abc import ABC, abstractmethod
import json


class AuthenticationManager(ABC):
    
    @abstractmethod
    def __init__(self, args: list[object]=None):
        """
        initialize manager

        """

    @abstractmethod
    def authenticateUser(self, data: json) -> str:
        """
        authenticates user for communication with the server

        RETURN:
            EncryptionKey: to be used with the requesting agent
            return message: to be sent back to requesting agent
        """