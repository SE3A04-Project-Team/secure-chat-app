"""
Weakest Encryptor for testing and dev purposes

@Author: Kyle McMaster
@Date: 2024-04-02

ATTRIBUTES:

TODO:
Complete Doc-string
Develop functions

"""
from headers.EncryptionFunction import EncryptionFunction
from headers.EncryptionKey import EncryptionKey


class NoneEncryptor(EncryptionFunction):

    @staticmethod
    def encrypt(data: bytes, key: EncryptionKey) -> bytes:
        """
        encrypt bytes

        Args:
            data: bytes to be encrypted
            key: encrpytion key to be used for encryption

        Return:
            returns encrpyted bytes

        """
        return data

    @staticmethod
    def decrypt(data: bytes, key: EncryptionKey) -> bytes:
        """
        decrypt bytes

        Args:
            data: bytes to be decrypted
            key: encrpytion key to be used for decryption

        Return:
            returns decrpyted bytes

        """
        return data