"""
Responsible for encrypting and decrypting incoming bytes. Implements the EncryptionFunction interface using AES encryption.

@Author: Daniel Franze-Da Silva
@Date: 2024-04-03

"""

from backend.headers.EncryptionKey import EncryptionKey
from backend.headers.EncryptionFunction import EncryptionFunction
from backend.src.PythonSerializer import PythonSerializer

from Crypto.Cipher import AES


class AESEncryptionFunction(EncryptionFunction):

    def encrypt(data: bytes, key: EncryptionKey) -> tuple[bytes, bytes, bytes]:
        """
        encrypt bytes

        Args:
            data: bytes to be encrypted
            key: encryption key to be used for encryption

        Return:
            returns a tuple containing (in this order) the encrypted bytes of the data, the reference tag, and a nonce value (number used once)

        """
        serialized_key = PythonSerializer.serialize(key)
        cipher = AES.new(serialized_key, AES.MODE_EAX)
        cipher_data, tag = cipher.encrypt_and_digest(data)
        nonce = cipher.nonce
        return cipher_data, tag, nonce

    def decrypt(data: bytes, key: EncryptionKey, tag: bytes, nonce: bytes) -> bytes:
        """
        decrypt bytes

        Args:
            data: bytes to be decrypted
            key: encryption key to be used for decryption
            tag: reference tag that is used to match the encrypted data with the correct cipher
            nonce: an initialization vector used for decryption

        Return:
            returns decrypted bytes

        """
        serialized_key = PythonSerializer.serialize(key)
        cipher = AES.new(serialized_key, AES.MODE_EAX, nonce)
        plain_data = cipher.decrypt_and_verify(data, tag)
        return plain_data


### Testing
# test_key = "ABCDEFGHIJKLMNOPQ"
# encrypted_data, tag, nonce = AESEncryptionFunction.encrypt(b'\x80\x04\x95\x08\x00\x00\x00\x00\x00\x00\x00\x8c\x04Test\x94.', test_key)
# print(AESEncryptionFunction.decrypt(encrypted_data, test_key, tag, nonce))