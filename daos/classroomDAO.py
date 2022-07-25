from daos.dao import DAO

class ClassroomDAO(DAO):
    
    def __init__(self):
        super().__init__('pkls/classrooms.pkl')
    
    def add(self, classroom):
        super().add(classroom.id, classroom)
    
    def delete(self, classroom):
        super().delete(classroom.id)
    
    def get(self, key):
        return super().get(key)