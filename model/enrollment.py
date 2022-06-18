from model import Student
from model import Classroom


class Enrollment:

    def __init__(self, student: Student, classroom: Classroom):
        self.__sudent = student
        self.__classroom = classroom

    @property
    def student(self) -> str:
        return self.__sudent

    @property
    def classroom(self) -> str:
        return self.__classroom

