from datetime import datetime
import uuid

class Message():

    def __init__(self, subject, body, sent_date) -> None:
        self.__id = uuid.uuid4()
        self.__subject = subject
        self.__body = body
        self.__sent_date = sent_date
        self.__chat = []
    
    @property
    def id(self) -> uuid.UUID:
        return self.__id

    @property
    def subject(self) -> str:
        return self.__subject
    
    @property
    def body(self) -> str:
        return self.__body
    
    @property
    def sent_date(self) -> datetime:
        return self.__sent_date
