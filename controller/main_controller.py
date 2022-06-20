from abc import abstractmethod
from view import BaseView


class MainController:

    def __init__(self):
        self.view = BaseView()

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
        strings = [str(obj) + "\n" for obj in items]
        return ''.join(strings)

    def prompt(self, msg, title):
        self.view.bottom_panel(msg, title)
        return self.view.prompt()

