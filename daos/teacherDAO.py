from dao import DAO

class TeacherDAO(DAO):
    def __init__(self):
        super().__init__('teachers.pkl')
    
    def add(self, teacher):
        super().add(teacher.id, teacher)
    
    def delete(self, teacher):
        super().delete(teacher.id)
    
    def get(self, key):
        return super().get(key)