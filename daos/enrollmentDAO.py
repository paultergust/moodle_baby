from dao import DAO

class EnrollmentDAO(DAO):
    
    def __init__(self):
        super().__init__('enrollments.pkl')
    
    def add(self, enrollment):
        super().add(enrollment.id, enrollment)
    
    def delete(self, enrollment):
        super().delete(enrollment.id)
    
    def get(self, key):
        return super().get(key)