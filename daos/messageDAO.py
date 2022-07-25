from dao import DAO

class MessageDAO(DAO):
    
    def __init__(self):
        super().__init__('messages.pkl')
    
    def add(self, message):
        super().add(message.id, message)
    
    def delete(self, message):
        super().delete(message.id)
    
    def get(self, key):
        return super().get(key)