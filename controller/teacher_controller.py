from model import Teacher
from view import teacher_view_constants as teacher_constants
from view import message_view_constants as msg_constants
from controller.main_controller import MainController

class TeacherController(MainController):

    def __init__(self) -> None:
        self.__teacher_model = Teacher
        self.__teachers = {}

    def list(self):
        teacher_list = self.stringify(self.__teachers)
        self.view.right_panel(teacher_list, teacher_constants.LIST.ACTION.name)        

    
    def retireve(self, name):
        teacher = self.__teachers.get(name)
        self.view.right_panel(teacher, teacher_constants.RETRIEVE.ACTION.name)

    
    def create(self):
        teacher_name = self.prompt(teacher_constants.PROMPT.name, teacher_constants.CREATE.ACTION.name)
        teacher  = self.__teacher_model(name=teacher_name)
        self.__teachers[teacher_name] = teacher

        teacher_list = self.stringify(self.__teachers)
        self.view.right_panel(teacher_list, teacher_constants.CREATE.ACTION.name)

    def list_messages(self, teacher):
        msg_list =  self.stringify(teacher.messages) 
        self.view.right_panel(msg_list, msg_constants.LIST.ACTION.name)

    def retrieve_message(self, teacher, msg_id):
        msg = None
        for cur_msg in teacher.messages:
            if cur_msg.id == msg_id:
                msg = cur_msg
        
        if msg:
            msg += msg.chat
            self.view.right_panel(msg, msg_constants.RETRIEVE.ACTION.name)
        self.view.bottom_panel(msg_constants.RETRIEVE.FAILED.name, msg_constants.RETRIEVE.ACTION.name)

    def delete_message(self, teacher, msg_id):
        for idx, msg in enumerate(teacher.messages):
            if msg.id == msg_id:
                teacher.messages.pop(idx)
                msg_list = self.stringify(teacher.messages)
                self.view.right_panel(msg_list, msg_constants.DELETE.ACTION.name)
                return
        self.view.bottom_panel(msg_constants.DELETE.ACTION.name, msg_constants.DELETE.FAILED.name)
