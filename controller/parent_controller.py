from model import Parent
from datetime import datetime as dt
from view import parent_view_parent_constants as parent_constants
from view import message_view_constants as msg_constants



class ParentController():

    def __init__(self) -> None:
        self.__parent_model = Parent
        self.__parents = {}
    
    def list(self):
        title = parent_constants.LIST.ACTION.name
        parent_list = self.stringify(self.__parents)
        #update view
    
    def retireve(self, name) -> Parent:
        title = parent_constants.RETRIEVE.ACTION.name
        parent = self.__parents.get(name)
        #update view
    
    def add(self, parent):
        self.__parents[parent.name] = parent


    def list_messages(self, parent):
        title = msg_constants.LIST.ACTION.name
        msg_list =  self.stringify(parent.messages)

        # Update View

    def retrieve_message(self, parent, msg_id):
        title = msg_constants.RETRIEVE.ACTION.name
        msg = None

        for cur_msg in parent.messages:
            if cur_msg.id == msg_id:
                msg = cur_msg
        
        if msg:
            # update view
            pass
        # update view
        pass

    def send_message(self, parent, chat_id=None):
        # ask prompt for teacher
        sent_date = dt.now()
        

    def delete_message(self, parent, msg_id):
        title = msg_constants.DELETE.ACTION

        for idx, msg in enumerate(parent.messages):
            if msg.id == msg_id:
                parent.messages.pop(idx)
                
                # update view
                return
        
        # msg not found, update view



    
