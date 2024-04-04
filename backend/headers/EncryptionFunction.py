"""
Responsible for encrypting and decrypting incoming bytes

@Author: Kyle McMaster
@Date: 2024-04-02

ATTRIBUTES:

TODO:

"""
from headers.EncryptionKey import EncryptionKey

from abc import ABC, abstractstaticmethod

class EncryptionFunction(ABC):

    @abstractstaticmethod
    def encrypt(data: bytes, key: EncryptionKey) -> bytes:
        """
        encrypt bytes

        Args:
            data: bytes to be encrypted
            key: encrpytion key to be used for encryption

        Return:
            returns encrpyted bytes

        """

    @abstractstaticmethod
    def decrypt(data: bytes, key: EncryptionKey) -> bytes:
        """
        decrypt bytes

        Args:
            data: bytes to be decrypted
            key: encrpytion key to be used for decryption

        Return:
            returns decrpyted bytes

        """