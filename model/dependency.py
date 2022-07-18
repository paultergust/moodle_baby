from os import linesep
from datetime import timedelta
from datetime import datetime as dt
from model.abstract.task import Task

class Dependency(Task):

    def __init__(self, description: str, start: dt=dt.now(), finish: dt=dt.now()):
        finish = finish + timedelta(days=7)
        super().__init__(start, finish, description)

    @property
    def description(self) -> str:
        desc = super().description
        #pretend i18n
        return f'Entrega: {linesep} {desc}'

