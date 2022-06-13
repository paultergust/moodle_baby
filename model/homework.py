from os import linesep
from abstract.task import Task

class Homework(Task):

    def __init__(self, start: dt, finish: dt, description: str):
        super().__init__(start, finish, description)

    @property
    def description(self) -> str:
        desc = super().description
        #pretend i18n
        return f'Dever de casa: {linesep}{desc}'

