from os import linesep
from model.abstract import Task

class Event(Task):

    def __init__(self, start: dt, finish: dt, description: str):
        super().__init__(start, finish, description)

    @property
    def description(self) -> str:
        desc = super().description
        #pretend i18n
        return f'Evento: {linesep}{desc}'

