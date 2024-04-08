"""
Responsible for generating AES encryption keys. Implements the KeyGenerator

@Author: Daniel Franzé-Da Silva
@Date: 2024-04-08

"""

from backend.headers.EncryptionKey import EncryptionKey
from backend.headers.KeyGenerator import KeyGenerator
from backend.src.Crypto.Random import get_random_bytes


class AESKeyGenerator(KeyGenerator):

    def generateKey(self, size=16) -> EncryptionKey:
        """
        generates encryption key

        Args:
            size: the key size in bytes

        Return:
            returns a newly generated encryption key

        """
        return get_random_bytes(size)
