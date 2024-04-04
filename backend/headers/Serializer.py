"""
Responsible for converting objects to bytes and back again.

@Author: Kyle McMaster
@Date: 2024-04-02

ATTRIBUTES:

"""

from abc import ABC, abstractstaticmethod

class Serializer(ABC):

    @abstractstaticmethod
    def serialize(data: object) -> bytes:
        """
        Convert object to bytes

        Args:
            data: object to be converted

        Return:
            returns bytes representing object

        """
        
    @abstractstaticmethod
    def deserialize(data: bytes) -> object:
        """
        Convert bytes to object

        Args:
            data: bytes to be converted

        Return:
            returns object obtained from bytes

        """
