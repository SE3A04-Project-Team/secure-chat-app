"""
For encrpyting and decrypting in the demo

@author Kyle McMaster
@date 2024-04-09

"""

from src.AESEncryptionFunction import AESEncryptionFunction
from src.Hashing32Bit import Hashin32Bit
import base64
import json

e = AESEncryptionFunction()
h = Hashin32Bit

def hash(password: str):
    print(h.hash(password))

def encrypt(data: str, key):
    encoded_data = data.encode()
    encrypted_data = e.encrypt(encoded_data, key)
    print(base64.b64encode(encrypted_data))


def decrypt_key(data: str, key):
    decoded_data = base64.b64decode(data)
    decrypted_data = e.decrypt(decoded_data, key)
    print(f"decrypted_key: {decrypted_data}")

def decrypt_message():
    decoded_data = base64.b64decode(data)
    decrypted_data = e.decrypt(decoded_data, key)
    print(f"decrypted_message: {decrypted_data.decode()}")




while True:
    i = input()
    count = 0
    if i == "hash":
        password = input("password:")
        hash(password)

    elif i == "encrypt":
        data = input("data: ")
        key = input("key: ")
        dic = {
    "client_details": {
        "clientID": "fURjH98QX4A0Ro6swlVb",
        "timestamp": 10000000
    }
        }
        data = json.dumps(dic)

        key = b'\x80L-FI\x0ev\xae\x1f\xe6C\xe5\xcd\x04\xc3\x9e'
        encrypt(data, key)

    elif i == "decrypt key":
        data = input("data: ")
        key = input("key: ")
        
        key = b'$O(\xce6\x85\x16wE\xad:\x7f\x17`\xfdD'
        decrypt_key(data, key)

    elif i == "decrypt msg":
        data = input("data: ")
        key = input("key: ")



    
