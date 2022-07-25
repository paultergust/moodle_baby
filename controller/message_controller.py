from model import Message
from daos.messageDAO import MessageDAO
from datetime import datetime


class MessageController():

    def __init__(self) -> None:
        self.__model = Message
        self.__dao = MessageDAO()

    def list_messages(self, obj):
        msg_list = {}
        for msg in self.__dao.get_all():
            if msg.sender == obj or msg.receiver == obj:
                msg_list[msg.id] = msg
        
        return msg_list
    
    def create(self, sender, receiver, subject, body):
        new_msg  = self.__model(sender, receiver, subject, body, datetime.now())
        self.__dao.add(new_msg.id, new_msg)
    
    def get(self, id):
        return self.__dao.get(id)
    
    def delete(self, msg):
        self.__dao.delete(msg.id)