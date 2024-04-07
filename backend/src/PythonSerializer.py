"""
Responsible for converting objects to bytes and back again. Implements the serializer interface using python.

@Author: Daniel Franze-Da Silva
@Date: 2024-04-03

ATTRIBUTES:

"""

from headers.Serializer import Serializer
import pickle


class PythonSerializer(Serializer):

    def serialize(data: object) -> bytes:
        """
        Convert object to bytes

        Args:
            data: object to be converted

        Return:
            returns bytes representing object

        """
        return pickle.dumps(data)

    def deserialize(data: bytes) -> object:
        """
        Convert bytes to object

        Args:
            data: bytes to be converted

        Return:
            returns object obtained from bytes

        """
        return pickle.loads(data)
