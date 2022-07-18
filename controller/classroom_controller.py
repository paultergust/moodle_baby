from controller import MainController
from model import Classroom
from view import classroom_view_constants as constants

class ClassroomController(MainController):

    def __init__(self):
        self.__classrooms = {}

    def create(self):
        title = constants.Create.ACTION.name
        classroom_name = self.prompt(constants.PROMPT.name, title)
        if self.fetch_by_name(classroom_name):
            self.view.bottom_panel(constants.Update.FAILURE.name, title)
            return None

        new_classroom = Classroom(classroom_name, self.current_user)
        self.__classrooms.append(new_classroom)
        self.view.right_panel(self.stringify(self.__classrooms), constants.List.ACTION.name)
        self.view.bottom_panel(constants.Create.ACTION.name, title)

    def list(self):
        class_list = self.stringify(self.__classrooms)
        self.view.right_panel(class_list, constants.List.ACTION.name)

    def update(self, index):
        title = constants.Update.ACTION.name
        classroom_name = self.prompt(constants.PROMPT.name, title)
        if self.fetch_by_name(classroom_name):
            self.view.bottom_panel(constants.Update.FAILURE.name, title)
            return None

        classroom = self.__classrooms[index]
        classroom.name = classroom_name
        self.view.right_panel(self.stringify(self.__classrooms), constants.List.ACTION.name)
        self.view.bottom_panel(constants.Update.ACTION.name, title)

    def delete(self, index):
        title = constants.Delete.ACTION.name
        del(self.__classrooms[index])
        self.view.right_panel(self.stringify(self.__classrooms), constants.List.ACTION.name)
        self.view.bottom_panel(constants.Delete.ACTION.name, title)

    def fetch_by_name(self, name):
        return [_class for _class in self.__classrooms.values() if _class.name == name][0]

