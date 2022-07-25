from model import Teacher
from daos.teacherDAO import TeacherDAO
from view import teacher_view_constants as teacher_constants
from view import message_view_constants as msg_constants
from controller.main_controller import MainController
from controller.message_controller import MessageController

class TeacherController(MainController):

    def __init__(self) -> None:
        self.__teacher_model = Teacher
        self.__dao = TeacherDAO()
        self.__msg_controller = MessageController()

    def list(self):
        teacher_list = self.__dao.get_all()

    
    def retireve(self, id):
        teacher = self.__dao.get(id)
    
    def get_by_email(self, email):
        for teacher in self.__dao.get_all():
            if teacher.email == email:
                return email
        return None

    
    def create(self):
        name = '' # get name
        email = '' #get email

        teacher  = self.__teacher_model(name=name, email=email)
        self.__dao.add(teacher.id, teacher)

        teacher_list = self.__dao.get_all()

    def list_messages(self, teacher):
        msg_list =  self.__msg_controller.list_messages(teacher)

    def retrieve_message(self, msg_id):
        msg = self.__msg_controller.get(msg_id)
        
        if msg:
            msg += msg.chat

    def delete_message(self, teacher, msg_id):
        if self.__msg_controller.get(msg_id):
            self.__msg_controller.delete(msg_id)
            msg_list = self.list(teacher)
            return
