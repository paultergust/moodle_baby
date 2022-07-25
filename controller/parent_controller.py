from model import Parent
from daos.parentDAO import ParentDAO
from daos.messageDAO import MessageDAO
from view import parent_view_constants as parent_constants
from view import message_view_constants as msg_constants
from controller.main_controller import MainController

class ParentController(MainController):

    def __init__(self) -> None:
        self.__dao = ParentDAO()
        self.__msg_dao = MessageDAO()
    
    def list(self):
        parent_list = self.__dao.get_all()
    
    def retireve(self, id) -> Parent:
        parent =  self.__dao.get(id)
    
    def add(self, parent):
        self.__dao.add(parent.id, parent)


    def list_messages(self, parent):
        msg_list = {}
        for msg in self.__msg_dao.get_all().values():
            if msg.sender == parent or msg.receiver == parent:
                msg_list[msg.id] = msg
        

    def retrieve_message(self, parent, msg_id):
        msg = self.__msg_dao.get(msg_id)
        if msg:
            pass

    def delete_message(self, parent, msg_id):
        if self.__msg_dao.get(msg_id):
            self.__msg_dao.delete(msg_id)    
            msg_list = self.list_messages(parent)




    
