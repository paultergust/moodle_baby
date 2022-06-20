

from view import GeneralView

class LoginController():
    def __init__(self):
        self.__general_view = GeneralView
        self.__parent_controller = None
        self.__teacher_controller = None
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
        
        resp = self.__general_view().display_menu(options)
        if resp not in options:
            self.__general_view().display_error(f'<{resp}> not in Options')
            self.login()

        options.get(resp)()
    
    def __log_parent(self):
        parents = self.__parent_controller.list_parents()
        self.__general_view().display_list(parents)
        resp = self.__general_view().display_menu([], input_display='Select a Parent by name')
    
        for parent in parents:
            if parent.name == resp:
                self.__parent_logged = parent
        else:
            self.__general_view().display_error(f'Parent with id <{resp}> does not exist')
            self.__log_parent()

    def __log_teacher(self):
        teachers = self.__teacher_controller.list_teachers()
        self.__general_view().display_list(teachers)
        resp = self.__general_view().display_menu([], input_display='Select a Teacher by name')
    
        for teacher in teachers:
            if teacher.name == resp:
                self.__teacher_logged = teacher
        else:
            self.__general_view().display_error(f'Teacher with id <{resp}> does not exist')
            self.__log_teacher()
             
