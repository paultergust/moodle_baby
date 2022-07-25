from controller import MainController
from daos.studentDAO import StudentDAO
from model import Student
from view import student_view_constants as constants

class StudentController(MainController):

    def __init__(self, parent_controller):
        self.__dao = StudentDAO()
        self.__parent_controller = parent_controller

    def create(self):
        title = constants.Create.ACTION.name
        student_name = self.prompt(constants.PROMPT.name, title)
        parent_name = self.prompt(constants.PROMPT_PARENT.name, title)
        if self.fetch_by_name(student_name):
            return None

        new_student = Student(student_name, parent_name)
        self.__dao.add(new_student.id, new_student)

        self.__students.append(new_student)
        self.__parent_controller.add(new_student.parent)


    def list(self):
        class_list = self.__dao.get_all()

    def delete(self, student):
        self.__dao.delete(student)


    def fetch_by_name(self, name):
        return [_class for _class in self.__students.values() if _class.name == name][0]

