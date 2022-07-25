from model.abstract.user import User

class Parent(User):

    def __init__(self, name, email) -> None:
        super().__init__(name, email)

