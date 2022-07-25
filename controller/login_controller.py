from view import BaseView
from controller.parent_controller import ParentController
from controller.teacher_controller import TeacherController

class LoginController:
    def __init__(self):
        self.view = BaseView()
        self.__parent_controller = ParentController()
        self.__teacher_controller = TeacherController()
        self.__user = None

    @property
    def user(self):
        return self.__user

    def logout(self):
        self.__user = None

    def login(self):
        options = {
            'teacher': self.__login_teacher,
            'parent': self.__login_parent
        }
        
        resp = input('Choose teacher or parent')

        if resp not in options:
            print('not valid')
            self.login()

        options.get(resp)()
    
    def __login_parent(self):
        email = input('email: ')
        parent = self.__parent_controller.get_by_email(email)

        if parent:
            self.__user = parent
        else:
            print('Email not found')
            self.__login_parent()

    def __login_teacher(self):
        email = input('email: ')
        teacher = self.__teacher_controller.get_by_email(email)
        
        if teacher:
            self.__user = teacher
        else:
            print('Email not found')
            self.__login_teacher()
