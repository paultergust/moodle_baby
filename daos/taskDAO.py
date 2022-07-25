from sqlite3 import DatabaseError
from daos.dao import DAO

class TaskDAO(DAO):
    
    def __init__(self):
        super().__init__('pkls/tasks.pkl')
    
    def add(self, task):
        super().add(task.id, task)
    
    def delete(self, task):
        super().delete(task.id)
    
    def get(self, key):
        return super().get(key)