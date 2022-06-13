from model import Teacher

class Classroom:

    def __init__(self, name: str, teacher: Teacher):
        self.__name = name
        self.__teacher = teacher


    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

