"""
Responsible for storing encryption keys to database

@Author: Daniel Franzé-Da Silva
@Date: 2024-04-08

"""
from headers.KeyStorage import KeyStorage
from headers.EncryptionKey import EncryptionKey


import firebase_admin
from firebase_admin import credentials, firestore


class KeyStorageFirebase(KeyStorage):
    pass

    def __init__(self):
        # Initialize firebase admin ADK
        cred = credentials.Certificate("backend/firebase.json")
        app = firebase_admin.initialize_app(cred, name="key_database")
        self.db = firestore.client(app)

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
        self.db.collection("encryptionKeys").document(id).update(
            {'value': key}
        )
        return key

    def getInfo(self) -> dict:
        """
        retrieves encryption keys from the database

        """
        try:
            docs = self.db.collection("encryptionKeys").stream()
            doc_dict = dict()

            for doc in docs:
                key = doc.to_dict().get('value')
                doc_dict.update({doc.id: key})

            return doc_dict
        
        except:
            return "error"
