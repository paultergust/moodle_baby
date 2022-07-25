from model.abstract.user import User

class Teacher(User):

    def __init__(self, name, email) -> None:
        super().__init__(name, email)

    
