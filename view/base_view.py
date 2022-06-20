from rich import print as rprint
from rich.panel import Panel
from rich.layout import Layout
from rich.prompt import Prompt
DEFAULT_TITLE = 'Moodle Baby'

class BaseView:

    def __init__(self):
        self.build_panels()

    #decorator
    def render(function):
        def function_call(self, msg, title=DEFAULT_TITLE):
            function(self, msg, title)
            rprint(self.__layout)
        return function_call

    def prompt(self):
        return Prompt.ask('> ')

    @render
    def bottom_panel(self, msg, title=DEFAULT_TITLE):
        self.__bottom_panel.update(Panel(msg, title=title))

    @render
    def top_panel(self, msg, title=DEFAULT_TITLE):
        self.__top_panel.update(Panel(msg, title=title))

    @render
    def left_panel(self, msg, title=DEFAULT_TITLE):
        self.__left_panel.update(Panel(msg, title=title))

    @render
    def right_panel(self, msg, title=DEFAULT_TITLE):
        self.__right_panel.update(Panel(msg, title=title))

    def build_panels(self):
        self.__layout = Layout()
        self.__layout.split_column(
            Layout(name="top_panel"),
            Layout(name="panels"),
            Layout(name="bottom_panel")
        )

        self.__layout['panels'].split_row(
            Layout(name="left_panel"),
            Layout(name="right_panel")
        )

        self.__top_panel =    self.__layout['top_panel']
        self.__bottom_panel = self.__layout['bottom_panel']
        self.__left_panel  =  self.__layout['panels']['left_panel']
        self.__right_panel =  self.__layout['panels']['right_panel']
        self.__layout['top_panel'].size = 5
        self.__layout['bottom_panel'].size = 4

        self.top_panel(DEFAULT_TITLE, DEFAULT_TITLE)
        self.left_panel(DEFAULT_TITLE, DEFAULT_TITLE)
        self.right_panel(DEFAULT_TITLE, DEFAULT_TITLE)
        self.bottom_panel(DEFAULT_TITLE, DEFAULT_TITLE)

