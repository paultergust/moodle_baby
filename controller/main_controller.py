from abc import abstractmethod
from view import BaseView

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
        strings = [str(key) + " - " + str(value) + "\n" for (key, value) in items.items()]
        return ''.join(strings)

    #controller will need to have methods to interact with each type of view
    # form view, list view, prompt, result, etc
    def prompt(self, msg, title):
        self.view.bottom_panel(msg, title)
        return self.view.prompt()

