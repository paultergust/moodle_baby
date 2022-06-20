from controller import MainController
from model.abstract import Task
from model import Dependency, Event, Homework
from view import task_view_constants as constants


class TaskController(MainController):

    def __init__(self):
        self.__tasks = {}

    def create(self):
        title = constants.Create.ACTION.name
        task_desc = self.prompt(constants.PROMPT.name, title)
        if self.fetch_by_name(task_desc):
            sef.view.bottom_panel(constants.Update.FAILURE.name, title)
            return None

        choice = self.check_type()
        new_task = self.build_by_choice(choice, task_desc)
        self.__tasks.append(new_task)
        self.view.right_panel(self.stringify(self.__tasks), constants.List.ACTION.name)
        self.view.bottom_panel(constants.Create.ACTION.name, title)

    def list(self):
        class_list = self.stringify(self.__tasks)
        self.view.right_panel(class_list, constants.List.ACTION.name)

    def delete(self, index):
        title = constants.Delete.ACTION.name
        del(self.__tasks[index])
        self.view.right_panel(self.stringify(self.__tasks), constants.List.ACTION.name)
        self.view.bottom_panel(constants.Delete.ACTION.name, title)

    def fetch_by_name(self, name):
        return [_class for _class in self.__tasks.values() if _class.name == name][0]

    def check_type(self):
        options = self.stringify(constants.List.types())
        choice = self.prompt(options, constants.Create.PROMPT_TYPE.name)
        return choice

    def build_by_choice(self, choice, desc):
        builds = {
                '0': Dependency,
                '1': Event,
                '2': Homework,
                }
        return builds[choice](desc)

