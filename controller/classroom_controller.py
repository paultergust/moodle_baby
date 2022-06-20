from controller import MainController
from model import Classroom

class ClassroomController(MainController):

    def __init__(self):
        self.__classrooms = []

    def create(self):
        title = 'Criar turma'
        self.prompt('Digite o nome da turma', title)
        self.__classrooms.append()
