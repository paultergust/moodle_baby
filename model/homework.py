from os import linesep
from datetime import datetime, timedelta
from model.abstract import Task

class Homework(Task):

    def __init__(self, description: str, start: dt=datetime.now(), finish: dt=datetime.now()):
        finish = finish + timedelta(days=1)
        super().__init__(start, finish, description)

    @property
    def description(self) -> str:
        desc = super().description
        #pretend i18n
        return f'Dever de casa: {linesep}{desc}'

