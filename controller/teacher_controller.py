from model import Teacher
from view import teacher_view_parent_constants as parent_constants
from view import message_view_constants as msg_constants

class TeacherController():

    def __init__(self) -> None:
        self.__teacher_model = Teacher
        self.__teachers = {}

    def list(self):
        title = parent_constants.LIST.ACTION.name
        teacher_list = self.stringify(self.__teachers)
        #update view
    
    def retireve(self, name):
        title = parent_constants.RETRIEVE.ACTION.name
        teacher = self.__teachers.get(name)
        #update view
    
    def create(self, name):
        title = parent_constants.CREATE.ACTION.name
        teacher  = self.__teacher_model(name=name)
        self.__teachers[name] = teacher
        
        teacher_list = self.stringify(self.__teachers)
        #update list

    def list_messages(self, teacher):
        title = msg_constants.LIST.ACTION.name
        msgs_list =  self.stringify(teacher.messages) 

        #update view

    def retrieve_message(self, teacher, msg_id):
        title = msg_constants.RETRIEVE.ACTION.name
        msg = None

        for cur_msg in teacher.messages:
            if cur_msg.id == msg_id:
                msg = cur_msg
        
        if msg:
            # update view
            pass
        # update view
        pass

    def delete_message(self, teacher, msg_id):
        title = msg_constants.DELETE.ACTION

        for idx, msg in enumerate(teacher.messages):
            if msg.id == msg_id:
                teacher.messages.pop(idx)
                
                # update view
                return
        
        # msg not found, update view
