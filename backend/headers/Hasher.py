"""
Responsible for hashing incoming bytes

@Author: Aidan Froggatt
@Date: 2024-04-07

ATTRIBUTES:

"""

from abc import ABC, abstractmethod

class Hasher(ABC):


    @staticmethod
    @abstractmethod
    def hash(data: object) -> bytes:
        """
        Convert object to bytes

        Args:
            data: object to be converted

        Return:
            returns bytes representing object

        """
