"""
Responsible for storing encryption keys to database

@Author: Daniel Franzé-Da Silva
@Date: 2024-04-08

"""

from abc import ABC, abstractmethod

from headers.EncryptionKey import EncryptionKey


class KeyStorage(ABC):

    @staticmethod
    @abstractmethod
    def addEntry(id: str, key: EncryptionKey) -> None:
        """
        stores a new encryption key

        Args:
            id: the ID associated with the session key
            key: the encryption key used in a session

        """

    @staticmethod
    @abstractmethod
    def updateEntry(id: str, key: EncryptionKey) -> None:
        """
        updates an encryption key in the database

        Args:
            id: the ID associated with the session key
            key: the new encryption key to be used in a session

        """

    @staticmethod
    @abstractmethod
    def getInfo() -> dict:
        """
        retrieves encryption keys from the database

        """
