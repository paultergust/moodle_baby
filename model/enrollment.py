import uuid
from model.student import Student
from model.classroom import Classroom


class Enrollment:

    def __init__(self, student: Student, classroom: Classroom):
        self.__id = uuid.uuid4()
        self.__sudent = student
        self.__classroom = classroom

    @property
    def id(self):
        return self.__id
        
    @property
    def student(self) -> str:
        return self.__sudent

    @property
    def classroom(self) -> str:
        return self.__classroom

