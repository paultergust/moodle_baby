from model.abstract.user import User

class Teacher(User):

    def __init__(self, name) -> None:
        super().__init__(name)

    
