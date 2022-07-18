from model import Parent
from view import parent_view_constants as parent_constants
from view import message_view_constants as msg_constants
from controller.main_controller import MainController

class ParentController(MainController):

    def __init__(self) -> None:
        self.__parents = {}
    
    def list(self):
        parent_list = self.stringify(self.__parents)
        self.view.right_panel(parent_list, parent_constants.LIST.ACTION.name)        
    
    def retireve(self, name) -> Parent:
        parent = self.__parents.get(name)        
        self.view.right_panel(parent, parent_constants.RETRIEVE.ACTION.name)
    
    def add(self, parent):
        self.__parents[parent.name] = parent


    def list_messages(self, parent):
        msg_list =  self.stringify(parent.messages)
        self.view.right_panel(msg_list, msg_constants.LIST.ACTION.name)
        

    def retrieve_message(self, parent, msg_id):
        msg = None
        for cur_msg in parent.messages:
            if cur_msg.id == msg_id:
                msg = cur_msg
        if msg:
            msg += msg.chat
            self.view.right_panel(msg, msg_constants.RETRIEVE.ACTION.name)
        self.view.bottom_panel(msg_constants.RETRIEVE.FAILED.name, msg_constants.RETRIEVE.ACTION.name)

    def delete_message(self, parent, msg_id):
        for idx, msg in enumerate(parent.messages):
            if msg.id == msg_id:
                parent.messages.pop(idx)
                
                msg_list = self.stringify(parent.messages)
                self.view.right_panel(msg_list, msg_constants.DELETE.ACTION.name)
                return
        self.view.bottom_panel(msg_constants.DELETE.ACTION.name, msg_constants.DELETE.FAILED.name)



    
