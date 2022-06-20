from view import BaseView
from controller.parent_controller import ParentController
from controller.teacher_controller import TeacherController

class LoginController:
    def __init__(self):
        self.view = BaseView()
        self.__parent_controller = ParentController()
        self.__teacher_controller = TeacherController()
        self.__teacher_logged = None
        self.__parent_logged = None

    @property
    def teacher_logged(self):
        return self.__teacher_logged
    
    @property
    def parent_logged(self):
        return self.__parent_logged

    def logout(self):
        self.__parent_logged = None
        self.__teacher_logged = None

    def login(self):
        options = {
            'teacher': self.__log_teacher,
            'parent': self.__log_parent
        }
        
        self.view.left_panel(str(options))
        resp = self.view.prompt()
        if resp not in options:
            self.view.bottom_panel(f'<{resp}> not in Options')
            self.login()

        options.get(resp)()
    
    def __log_parent(self):
        parents = self.__parent_controller.list()
        self.view.right_panel(parents)
        resp = self.view.bottom_panel([], input_display='Select a Parent by name')
    
        for parent in parents:
            if parent.name == resp:
                self.__parent_logged = parent
        else:
            self.view.bottom_panel(f'Parent with id <{resp}> does not exist')
            self.__log_parent()

    def __log_teacher(self):
        teachers = self.__teacher_controller.list()
        self.view.bottom_panel(teachers)
        resp = self.view.bottom_panel([], input_display='Select a Teacher by name')
    
        for teacher in teachers:
            if teacher.name == resp:
                self.__teacher_logged = teacher
        else:
            self.view.bottom_panel(f'Teacher with id <{resp}> does not exist')
            self.__log_teacher()
             
