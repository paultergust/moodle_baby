from dao import DAO

class StudentDAO(DAO):
    def __init__(self):
        super().__init__('students.pkl')
    
    def add(self, student):
        super().add(student.id, student)
    
    def delete(self, student):
        super().delete(student.id)
    
    def get(self, key):
        return super().get(key)