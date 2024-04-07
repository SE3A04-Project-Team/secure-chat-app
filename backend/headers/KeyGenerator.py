"""
Responsible for generating encryption keys

@Author: Daniel Franzé-Da Silva
@Date: 2024-04-07

TODO
- DOC strings
"""

from abc import ABC, abstractmethod

from EncryptionKey import EncryptionKey


class KeyGenerator(ABC):

    @staticmethod
    @abstractmethod
    def generateKey(size: int) -> EncryptionKey:
        """
        generates encryption key

        Args:
            size: the key size in bits

        Return:
            returns a newly generated encryption key

        """
