from controller import MainController
from model import Student
from view import student_view_constants as constants

class StudentController(MainController):

    def __init__(self, parent_controller):
        self.__students = {}
        self.__parent_controller = parent_controller

    def create(self):
        title = constants.Create.ACTION.name
        student_name = self.prompt(constants.PROMPT.name, title)
        parent_name = self.prompt(constants.PROMPT_PARENT.name, title)
        if self.fetch_by_name(student_name):
            self.view.bottom_panel(constants.Update.FAILURE.name, title)
            return None

        new_student = Student(student_name, parent_name)
        self.__students.append(new_student)
        self.__parent_controller.add(new_student.parent)
        self.view.right_panel(self.stringify(self.__students), constants.List.ACTION.name)
        self.view.bottom_panel(constants.Create.ACTION.name, title)

    def list(self):
        class_list = self.stringify(self.__students)
        self.view.right_panel(class_list, constants.List.ACTION.name)

    def delete(self, index):
        title = constants.Delete.ACTION.name
        del(self.__students[index])
        self.view.right_panel(self.stringify(self.__students), constants.List.ACTION.name)
        self.view.bottom_panel(constants.Delete.ACTION.name, title)

    def fetch_by_name(self, name):
        return [_class for _class in self.__students.values() if _class.name == name][0]

