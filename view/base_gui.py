import PySimpleGUI as sg
from data_classes import FormField


class BaseGui:

    # this will probably be a general view for navigation
    # but we need more components for basic usages.
    # interface them with options for number of inputs, type of view, etc
    def __init__(self, user_type: str):
        sg.theme("DarkGrey15")
        self.__layout = []
        self.__user_type = user_type
        self.__layout = self.build_layout([])
        self.__values = None
        self.__event = None

    # decorator
    def render(function):
        def function_call(self, fields):
            function(self, fields)
            window = sg.Window("Moodle Baby", self.__layout, size=(400, 400),
                               margins=(2, 2), finalize=True, resizable=True)
            while True:
                self.__event, self.__values = window.read()
                if self.__event == sg.WINDOW_CLOSED:
                    break

            window.close()
        return function_call

    @render
    def form_layout(self, fields: list[FormField]):
        parsed_fields = []
        for field in fields:
            parsed_fields.append(
                [sg.Text(field.name, size=(15, 1)), sg.InputText('', key=field.key)])

        frame = sg.Frame(
            "",
            parsed_fields,
            pad=(5, 3),
            expand_x=True,
            expand_y=True,
            background_color="#404040",
            border_width=0,
        )
        self.build_layout([[frame], [sg.Submit(), sg.Cancel()]])

    def login_layout(self):
        frame = sg.Frame(
            "Login",
            [[sg.Text('E-mail', size=(15, 1)), sg.InputText('', key='email')]],
            pad=(5, 3),
            expand_x=True,
            expand_y=True,
            background_color="#404040",
            border_width=0,
        )
        self.build_layout([[frame], [sg.Submit(), sg.Cancel()]])
        window = sg.Window("Moodle Baby", self.__layout, size=(400, 400),
                           margins=(2, 2), finalize=True, resizable=True)
        while True:
            self.__event, self.__values = window.read()
            if self.__event == sg.WINDOW_CLOSED:
                break

        window.close()

    def build_layout(self, layout):
        if self.__user_type == 'Parent':
            menu_def = [['&Tarefa', ['&Dependencia', '&Evento', '&Dever de Casa', ]],
                        ['&Turma', ['&Alunos', '&Tarefas Por Turma'], ],
                        ['&Mensagens', ['---', '&Recebidas',
                                        '---', '&Enviadas']],
                        ['&Sair'], ]
        else:
            menu_def = [['&Tarefa', ['&Criar', '&Atualizar', '&Listar', ['&Dependencias', '&Eventos', 'Deveres de casa', ]]],
                        ['&Turma', ['&Alunos', '&Tarefas Por Turma'], ],
                        ['&Mensagens', ['---', '&Recebidas',
                                        '---', '&Enviadas']],
                        ['&Sair'], ]
        menu = sg.Menu(menu_def, tearoff=False, pad=(200, 1))
        layout.insert(0, [menu])
        self.__layout = layout

    def values(self):
        return self.__values

    def event(self):
        return self.__event

#     def form_fields(self):
#         return [
#             FormField(name='foo', key='foo'),
#             FormField(name='foo', key='foo'),
#             FormField(name='foo', key='foo'),
#             FormField(name='foo', key='foo'),
#             FormField(name='foo', key='foo'),
#             FormField(name='foo', key='foo'),
#             FormField(name='foo', key='foo'),
#             FormField(name='foo', key='foo'),
#         ]


# bg = BaseGui('')
# foo = bg.form_fields()
# bg.login_layout()
# print(bg.values())
