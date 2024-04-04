"""
Responsible for converting objects to bytes and back again. Implements the serializer interface using python.

@Author: Daniel Franze-Da Silva
@Date: 2024-04-03

ATTRIBUTES:

"""

from headers.Serializer import Serializer
import pickle


class PythonSerializer(Serializer):

    def serialize(self, data: object) -> bytes:
        """
        Convert object to bytes

        Args:
            data: object to be converted

        Return:
            returns bytes representing object

        """
        ### Testing
        # print(data)
        # print(pickle.dumps(data))
        return pickle.dumps(data)

    def deserialize(self, data: bytes) -> object:
        """
        Convert bytes to object

        Args:
            data: bytes to be converted

        Return:
            returns object obtained from bytes

        """
        ### Testing
        # print(data)
        # print(pickle.loads(data))
        return pickle.loads(data)

### Testing
# Serializer.serialize("Test")
# Serializer.deserialize(b'\x80\x04\x95\x08\x00\x00\x00\x00\x00\x00\x00\x8c\x04Test\x94.')
