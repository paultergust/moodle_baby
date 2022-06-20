from abc import ABC, abstractproperty
from datetime import datetime as dt
from model import Classroom


class Task(ABC):

    def __init__(self, start: dt, finish: dt, description: str):
        self.__start = start
        self.__finish = finish
        self.__description = description

    @property
    def start(self) -> dt:
        return self.__start

    @start.setter
    def start(self, start: dt):
        self.__start = start

    @property
    def finish(self) -> dt:
        return self.__finish

    @finish.setter
    def finish(self, finish: dt):
        self.__finish = finish

    @abstractproperty
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    def __str__(self):
        return self.description

