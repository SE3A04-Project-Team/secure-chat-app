"""
Responsible for encrypting and decrypting incoming bytes

@Author: Kyle McMaster, Daniel Franzé-Da Silva
@Date: 2024-04-02

"""
from headers.EncryptionKey import EncryptionKey


from abc import ABC, abstractmethod


class EncryptionFunction(ABC):

    @staticmethod 
    @abstractmethod
    def encrypt(data: bytes, key: EncryptionKey) -> bytes:
        """
        encrypt bytes

        Args:
            data: bytes to be encrypted
            key: encryption key to be used for encryption

        Return:
            returns a tuple containing (in this order) the encrypted bytes of the data, the reference tag, and a nonce value (number used once)

        """

    @staticmethod 
    @abstractmethod
    def decrypt(data: bytes, key: EncryptionKey, tag: bytes, nonce: bytes) -> bytes:
        """
        decrypt bytes

        Args:
            data: bytes to be decrypted
            key: encryption key to be used for decryption
            tag: reference tag that is used to match the encrypted data with the correct cipher
            nonce: an initialization vector used for decryption

        Return:
            returns decrypted bytes

        """