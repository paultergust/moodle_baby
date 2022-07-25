from controller import MainController
from model.abstract.task import Task
from model import Dependency, Event, Homework
from view import task_view_constants as constants
from daos.taskDAO import TaskDAO


class TaskController(MainController):

    def __init__(self):
        self.__dao = TaskDAO()

    def create(self):
        title = constants.Create.ACTION.name
        task_desc = self.prompt(constants.PROMPT.name, title)
        if self.fetch_by_name(task_desc):
            return None

        choice = self.check_type()
        new_task = self.build_by_choice(choice, task_desc)

        self.__dao.add(new_task.id, new_task)

    def list(self):
        class_list = self.__dao.get_all()

    def delete(self, task):
        self.__dao.delete(task)

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

