from uuid import uuid4, UUID
from model.parent import Parent


class Student:

    def __init__(self, name: str, parent_name: str):
        self.__id = uuid4()
        self.__name = name
        self.__parent = Parent(parent_name)

    @property
    def id(self) -> UUID:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def parent(self) -> Parent:
        return self.__parent

    @parent.setter
    def parent(self, parent: Parent):
        self.__parent = parent

    def __str__(self):
        return self.name

