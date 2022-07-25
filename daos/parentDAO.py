from daos.dao import DAO

class ParentDAO(DAO):

    def __init__(self):
        super().__init__('pkls/parents.pkl')
    
    def add(self, parent):
        super().add(parent.id, parent)
    
    def delete(self, parent):
        super().delete(parent.id)
    
    def get(self, key):
        return super().get(key)
    