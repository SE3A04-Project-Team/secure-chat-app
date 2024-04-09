"""
Responsible for handling encryption key distribution, and periodically refreshing keys. Implements the KeyDistributionManager

@Author: Daniel Franzé-Da Silva
@Date: 2024-04-08

ATTRIBUTES:
    keyGenerator: a generator used to generate new keys
    encryptionKeys: a dictionary that holds the keys for a communicating agent for each session

"""

from headers.EncryptionKey import EncryptionKey
from headers.KeyDistributionManager import KeyDistributionManager
from headers.KeyStorage import KeyStorage

from src.AESKeyGenerator import AESKeyGenerator
from src.KeyStorageFirebase import KeyStorageFirebase


class AESKeyDistributionCenter(KeyDistributionManager):

    def __init__(self, keyStore: KeyStorage ):
        self.keyGenerator = AESKeyGenerator()
        self.encryptionKeys = []
        self.keyStore = keyStore

    def refreshKeys(self) -> None:
        """
        refresh the stored keys to be distributed

        """
        # get latest keys stored on server
        self.encryptionKeys = self.keyStore.getInfo()

        # update keys
        for key in self.encryptionKeys:
            id = key.keys()[0]
            self.keyStore.updateEntry(id, self.keyGenerator.generateKey())

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

        # get latest keys stored on server
        # TODO: might be very inefficient ----- flag for optimization if slow
        self.encryptionKeys = self.keyStore.getInfo()
        print("keys", self.encryptionKeys)
        # Session key does not already exist
        if id not in self.encryptionKeys.keys():
            print("new Key")
            return self.keyStore.addEntry(id, self.keyGenerator.generateKey())
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

