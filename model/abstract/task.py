import uuid
from abc import ABC, abstractproperty
from datetime import datetime as dt
from datetime import datetime
from model import Classroom


class Task(ABC):

    def __init__(self, description: str, start: dt=datetime.now(), finish: dt=datetime.now()):
        self.__id = uuid.uuid4()
        self.__start = start
        self.__finish = finish
        self.__description = description
        
    @property
    def id(self):
        return self.__id

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

