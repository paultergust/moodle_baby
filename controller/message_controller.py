from model import Message
from daos.messageDAO import MessageDAO


class MessageController():

    def __init__(self) -> None:
        self.__dao = MessageDAO()

    def list_messages(self, obj):
        msg_list = {}
        for msg in self.__dao.get_all():
            if msg.sender == obj or msg.receiver == obj:
                msg_list[msg.id] = msg
        
        return msg_list
    
    def get(self, id):
        return self.__dao.get(id)
    
    def delete(self, msg):
        self.__dao.delete(msg.id)