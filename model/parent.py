from model.abstract.user import User

class Parent(User):

    def __init__(self, name) -> None:
        super().__init__(name)

