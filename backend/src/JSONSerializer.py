"""
Weakest Serializer for testing and dev purposes

@Author: Kyle McMaster
@Date: 2024-04-02

ATTRIBUTES:

TODO:
Complete Doc-string
Develop functions

"""
from headers.Serializer import Serializer

import json

class JSONSerializer(Serializer):


    @staticmethod
    def serialize(data: object) -> bytes:
        """
        Convert object to bytes

        Args:
            data: object to be converted

        Return:
            returns bytes representing object

        """
        data = json.dumps(data)
        data = bytes(data, 'utf-8')
        return  data
        

    @staticmethod
    def deserialize(data: bytes) -> object:
        """
        Convert bytes to object

        Args:
            data: bytes to be converted

        Return:
            returns object obtained from bytes

        """
        data = str(data, 'utf-8')
        return json.loads(data)
