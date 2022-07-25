import uuid
from abc import ABC, abstractclassmethod

class User(ABC):

    @abstractclassmethod
    def __init__(self, name) -> None:
        self.__id = uuid.uuid4()
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    @property
    def id(self) -> uuid.UUID:
        return self.__id
    
    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return self.name

