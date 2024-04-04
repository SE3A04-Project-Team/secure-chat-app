"""
Data structure used for encrypting and decrypting messages. Key can be stored in any format but should be convertable to bytes for encryption.

@Author: Kyle McMaster
@Date: 2024-04-02

ATTRIBUTES:
    value (): the value of the key

TODO:

"""

from abc import ABC, abstractmethod

class EncryptionKey(ABC):

    @abstractmethod
    def getKey(self) -> bytes:
        """
        return the key as bytes
        """
    
