from rich import print
from rich.panel import Panel
from rich.layout import Layout
from rich.prompt import Prompt

class BaseView:

    def __init__(self):
        self.__header == None
        self.__left_pannel  = None
        self.__right_pannel = None
        try:
            self.render()
        except KeyboardInterrupt:
            exit(0)


    def render(self):
        while True:
            prompt = Prompt.ask('> ')
            self.check_input(prompt)
            self.__layout = Layout()
            layout.split_column(
                Layout(name="header"),
                Layout(name="pannels"),
                Layout(name="bottom_pannel")
            )

            layout['header'].update(Panel(self.__header, padding=1))
            layout['header'].size = 5

            layout['pannels'].split_row(
                Layout(name="left"),
                Layout(name="right")
            )

            layout['left'].update(Panel(self.__left_pannel))
            layout['right'].update(Panel(self.__right_pannel))

            layout['bottom_pannel'].update(Panel(Prompt.ask('> '), title='Command'))
            layout['bottom_pannel'].size = 5
            print(layout)




    def check_input(self, prompt):
        if prompt in ['exit', 'sair', 'bye', 'xau']:
            exit(0)


    def err_out(self, msg):
        pass
