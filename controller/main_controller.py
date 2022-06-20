from abc import abstractmethod
from view import BaseView
from controller import LoginController


class MainController:

    def __init__(self):
        self.view = BaseView()
        self.__login_controller = None
        self.current_user = self.__login_controller.teacher_logged() or self.__login_controller.parent_logged()

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    def stringify(self, items):
        strings = [str(key) + " - " + str(obj) + "\n" for (key, value) in items.items()]
        return ''.join(strings)

    def prompt(self, msg, title):
        self.view.bottom_panel(msg, title)
        return self.view.prompt()

