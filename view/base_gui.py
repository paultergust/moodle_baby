import PySimpleGUI as sg
from data_classes import FormField


class BaseGui:

    #this will probably be a general view for navigation
    #but we need more components for basic usages.
    #interface them with options for number of inputs, type of view, etc
    def __init__(self):
        sg.theme("DarkGrey15")
        self.__layout = []
        self.__layout = self.build_layout([])
        self.__values = None
        self.__event = None

    #decorator
    def render(function):
        def function_call(self, fields):
            function(self, fields)
            window = sg.Window("Moodle Baby", self.__layout, margins=(2, 2), finalize=True, resizable=True)
            while True:
                self.__event, self.__values = window.read()
                print(event, values)
                if event == sg.WINDOW_CLOSED:
                    break

            window.close()
        return function_call

    @render
    def form_layout(self, fields: list[FormField]):
        parsed_fields = []
        for field in fields:
            parsed_fields.append([sg.Text(field.name, size=(15,1)), sg.InputText('', key=field.key)])

        frame = sg.Frame(
            "",
            parsed_fields,
            pad=(5, 3),
            expand_x=True,
            expand_y=True,
            background_color="#404040",
            border_width=0,
        )
        self.__layout = [[frame],[sg.Submit(), sg.Cancel()]]

    def build_layout(self, layout):
        #TODO fix this menu insertion
        #this is supposed to be used as a navigation helper.
        #then on results each obj can be a button with its crud options as menu results (see tests.py)
        menu_def = [['&File', ['&Open     Ctrl-O', '&Save       Ctrl-S', '&Properties', 'E&xit']],
                    ['&Edit', ['&Paste', ['Special', 'Normal', ], 'Undo'], ],
                    ['&Toolbar', ['---', 'Command &1', 'Command &2',
                                  '---', 'Command &3', 'Command &4']],
                    ['&Help', '&About...'], ]
        menu = sg.Menu(menu_def, tearoff=False, pad=(200,1))
        layout.insert(0, menu)
        self.__layout = layout

    def values(self):
        return self.__values

    def event(self):
        return self.__event

