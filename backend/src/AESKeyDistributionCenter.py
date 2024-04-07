"""
Responsible for handling encryption key distribution, and periodically refreshing keys. Implements the KeyDistributionManager

@Author: Daniel Franzé-Da Silva
@Date: 2024-04-07

ATTRIBUTES:
    keyGenerator: a generator used to generate new keys
    encryptionKeys: a dictionary that holds the keys for a communicating agent for each session

"""

from headers.EncryptionKey import EncryptionKey
from headers.KeyDistributionManager import KeyDistributionManager
from src.AESKeyGenerator import AESKeyGenerator


class AESKeyDistributionCenter(KeyDistributionManager):

    def __init__(self):
        self.keyGenerator = AESKeyGenerator()
        self.encryptionKeys = {}

    def refreshKeys(self) -> None:
        """
        refresh the stored keys to be distributed

        """
        for id in self.encryptionKeys.keys():
            self.encryptionKeys[id] = self.keyGenerator.generateKey()

    def getKey(self, agentID: str, serviceID: str) -> EncryptionKey:
        """
        distributes key to communicating agents

        Args:
            agentID: the ID of the desired communicating agent
            serviceID: the ID of the communicating session

        Return:
            returns an encryption key to a communicating agent for their specified session

        """
        id = agentID + serviceID

        # Session key does not already exist
        if self.encryptionKeys.get(id) is None:
            self.encryptionKeys[id] = self.keyGenerator.generateKey()
        else:
            return self.encryptionKeys.get(id)


### Testing
# kdc = AESKeyDistributionCenter()
# kdc.getKey("0", "1",)
# kdc.getKey("1", "1",)
# kdc.getKey("2", "2",)
# kdc.getKey("3", "2",)
# kdc.getKey("4", "3",)
#
# for i in kdc.encryptionKeys.values():
#     print(i)
#
# kdc.refreshKeys()
#
# print("*******************************")
# for j in kdc.encryptionKeys.values():
#     print(j)

