"""
Responsible for handling encryption key distribution, and periodically refreshing keys

@Author: Daniel Franzé-Da Silva
@Date: 2024-04-07

ATTRIBUTES:
    keyGenerator: a generator used to generate new keys

"""

from abc import ABC, abstractmethod

from EncryptionKey import EncryptionKey


class KeyDistributionManager(ABC):

    @staticmethod
    @abstractmethod
    def __init__(self):
        keyGenerator: KeyGenerator
        keys = []

    @staticmethod
    @abstractmethod
    def refreshKeys(self) -> None:
        """
        refresh the stored keys to be distributed

        """

    @staticmethod
    @abstractmethod
    def getKey(self, agentID: str, serviceID: str) -> EncryptionKey:
        """
        distributes key to communicating agents

        Args:
            agentID: the ID of the desired communicating agent
            serviceID: the ID of the communicating session

        Return:
            returns an encryption key to a communicating agent for their specified session

        """
