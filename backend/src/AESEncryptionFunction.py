"""
Responsible for encrypting and decrypting incoming bytes. Implements the EncryptionFunction interface using AES encryption.

@Author: Daniel Franze-Da Silva
@Date: 2024-04-03

"""

from headers.EncryptionKey import EncryptionKey
from headers.EncryptionFunction import EncryptionFunction
from src.PythonSerializer import PythonSerializer

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

import base64

class AESEncryptionFunction(EncryptionFunction):

    @staticmethod
    def encrypt(data: str, key: bytes) -> bytes:
        """
        encrypt bytes

        Args:
            data: bytes to be encrypted
            key: encryption key to be used for encryption

        Return:
            returns a tuple containing (in this order) the encrypted bytes of the data, the reference tag, and a nonce value (number used once)

        """
        print(AES.block_size)
        iv = b'0000000000000000'
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_data = pad(data, AES.block_size)
        cipher_data = cipher.encrypt(padded_data)
        return cipher_data
        

    @staticmethod
    def decrypt(data: str, key: bytes) -> bytes:
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
        iv = b'0000000000000000'
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plain_data = cipher.decrypt(data)
        unpadded_data = unpad(plain_data, AES.block_size)
        return unpadded_data


### Testing
### test_key = "ABCDEFGHIJKLMNOPQ"
###encrypted_data, tag, nonce = AESEncryptionFunction.encrypt(b'\x80\x04\x95\x08\x00\x00\x00\x00\x00\x00\x00\x8c\x04Test\x94.', test_key)
# print(AESEncryptionFunction.decrypt(encrypted_data, test_key, tag, nonce))