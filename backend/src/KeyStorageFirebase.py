"""
Responsible for storing encryption keys to database

@Author: Daniel Franzé-Da Silva
@Date: 2024-04-07

"""

from backend.headers.EncryptionKey import EncryptionKey
from backend.headers.KeyStorage import KeyStorage

from backend.src import firebase_admin
from backend.src.firebase_admin import credentials, firestore


class KeyStorageFirebase(KeyStorage):
    def __init__(self):
        # Initialize firebase admin ADK
        cred = credentials.Certificate("./firebase.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def addEntry(self, id: str, key: EncryptionKey) -> None:
        """
        stores a new encryption key

        Args:
            id: the ID associated with the session key
            key: the encryption key used in a session

        """
        data = {id: key}

        # Add a new key to the firestore
        db_ref = self.db.collection("encryptionKeys").document("AESEncryptionKeys")
        db_ref.set(data, merge=True)

    def updateEntry(self, id: str, key: EncryptionKey) -> None:
        """
        updates an encryption key in the database

        Args:
            id: the ID associated with the session key
            key: the new encryption key to be used in a session

        """
        data = {id: key}

        # Add a new key to the firestore
        db_ref = self.db.collection("encryptionKeys").document("AESEncryptionKeys")
        db_ref.update({id: key})

    def getInfo(self) -> dict:
        """
        retrieves encryption keys from the database

        """
        doc = self.db.collection("encryptionKeys").document("AESEncryptionKeys")
        return doc.get().to_dict()
