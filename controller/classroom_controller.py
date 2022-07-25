from controller import MainController
from daos.classroomDAO import ClassroomDAO
from model import Classroom
from view import classroom_view_constants as constants


class ClassroomController(MainController):

    def __init__(self):
        self.__dao = ClassroomDAO()

    def create(self):
        classroom_name = input('Class name: ')
        
        new_classroom = Classroom(classroom_name, self.current_user)
        self.__dao(new_classroom.id, new_classroom)


    def list(self):
        class_list = self.__dao.get_all()

        return class_list

    def update(self, id):
        classroom_name = input('Class name: ')

        classroom = self.__dao.get(id)
        if classroom:
            classroom.name = classroom_name
            
            self.__dao.add(classroom.id, classroom)

    def delete(self, id):
        classroom =  self.__dao.get(id)
        if classroom:
            self.__dao.delete(classroom)
        
    def fetch_by_name(self, name):
        return [_class for _class in self.__classrooms.values() if _class.name == name][0]

