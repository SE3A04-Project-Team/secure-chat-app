"""
Responsible for storing encryption keys to database

@Author: Daniel Franzé-Da Silva
@Date: 2024-04-08

"""

from headers.EncryptionKey import EncryptionKey
from headers.KeyStorage import KeyStorage

import firebase_admin
from firebase_admin import credentials, firestore


class KeyStorageFirebase(KeyStorage):
    def __init__(self):
        # Initialize firebase admin ADK
        cred = credentials.Certificate("backend/firebase.json")
        firebase_admin.initialize_app(cred, name="key_database")
        self.db = firestore.client()

    def addEntry(self, id: str, key: EncryptionKey) -> None:
        """
        stores a new encryption key

        Args:
            id: the ID associated with the session key
            key: the encryption key used in a session

        """

        # Add a new key to the firestore
        self.db.collection("encryptionKeys").document(id).set(
            {'value': key}
        )

    def updateEntry(self, id: str, key: EncryptionKey) -> None:
        """
        updates an encryption key in the database

        Args:
            id: the ID associated with the session key
            key: the new encryption key to be used in a session

        """
        data = {id: key}

        # Add a new key to the firestore
        db_ref = self.db.collection("encryptionKeys").document(id).update(
            {'value': key}
        )

    def getInfo(self) -> dict:
        """
        retrieves encryption keys from the database

        """
        doc = self.db.collection("encryptionKeys")
        return doc.get().to_dict()
