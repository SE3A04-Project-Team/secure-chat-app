"""
Responible for hashing data to 32 bit hash

@Author: Aidan Froggatt
@Date: 2024-04-07

ATTRIBUTES:

"""
from Hasher import Hasher
from Crypto.Hash import SHA256

class Hashin32Bit(Hasher):

    def hash(data: object) -> bytes:
        # Create a SHA-256 hash object
        hasher = SHA256.new()
        
        # Update the hash object with the data bytes
        hasher.update(data.encode('utf-8'))
        
        # Get the full 256-bit hash
        full_hash = hasher.digest()
        
        # Truncate the hash to 32 bits (4 bytes)
        truncated_hash = full_hash[:4]
        
        # Return the 32-bit key as bytes
        return truncated_hash
    