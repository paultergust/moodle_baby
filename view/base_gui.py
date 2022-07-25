from traceback import format_list
import PySimpleGUI as sg
from data_classes import FormField


class BaseGui:

    def __init__(self, user_type: str):
        sg.theme("DarkGrey15")
        self.__user_type = user_type

    def catch_and_return(self, layout):
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
        layout_with_menu = layout
        window = sg.Window("Moodle Baby", layout_with_menu, size=(400, 400),
                           margins=(2, 2), finalize=True, resizable=True)
        return window.Read()

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
        return self.catch_and_return([[frame], [sg.Submit(), sg.Cancel()]])

    def list_layout(self, items: list):
        frame = sg.Listbox(
            items,
            pad=(5, 3),
            expand_x=True,
            expand_y=True,
            background_color="#404040",
        )
        return self.catch_and_return([[frame], [sg.Button('Voltar')]])

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
        layout = [[frame], [sg.Submit(), sg.Cancel()]]
        window = sg.Window("Moodle Baby", layout, size=(400, 400),
                           margins=(2, 2), finalize=True, resizable=True)
        return window.read()
