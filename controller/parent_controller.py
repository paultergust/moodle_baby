from model import Parent
from daos.parentDAO import ParentDAO
from view import parent_view_constants as parent_constants
from view import message_view_constants as msg_constants
from controller.main_controller import MainController
from controller.message_controller import MessageController

class ParentController(MainController):

    def __init__(self) -> None:
        self.__dao = ParentDAO()
        self.__msg_controller = MessageController()
    
    def list(self):
        parent_list = self.__dao.get_all()
    
    def retireve(self, id) -> Parent:
        parent =  self.__dao.get(id)
    
    def add(self, parent):
        self.__dao.add(parent.id, parent)


    def list_messages(self, parent):
        msg_list = self.__msg_controller.list_messages(parent)
        

    def retrieve_message(self, parent, msg_id):
        msg = self.__msg_controller.get(msg_id)
        if msg:
            pass

    def delete_message(self, parent, msg_id):
        msg = self.__msg_controller.get(msg_id)
        if msg:
            self.__msg_controller.delete(msg)    
            msg_list = self.list_messages(parent)




    
