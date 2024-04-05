"""
Interface for Authenticating incoming requests
Uses Kerberos to verify a user is authenticated to connect to the requested server. Not to be used in the intial authentication steps

@Author: Kyle McMaster
@Date: 2024-04-02

ATTRIBUTES:

TODO:
"""
from headers.EncryptionKey import EncryptionKey
from headers.AuthenticationManager import AuthenticationManager


import json


class KerberosServerAuthManager(AuthenticationManager):
    

    def __init__(self, args: list[object]=None):
        """
        initialize manager

        """

    def authenticateUser(self, message: json) -> tuple[EncryptionKey, object]:
        """
        authenticates user for communication with the server

        RETURN:
            EncryptionKey: to be used with the requesting agent
            return message: to be sent back to requesting agent
        """