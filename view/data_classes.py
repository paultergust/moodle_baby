from dataclasses import dataclass


@dataclass
class FormField:
    name:str
    key:str


@dataclass
class RecordField:
    name:str
    value:str

