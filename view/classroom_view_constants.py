from enum import Enum


class Create(Enum):
    PROMPT = 'Digite o nome da turma'
    ACTION= 'Criar turma',
    SUCCESS= 'Turma criada com sucesso',
    FAILURE= 'Erro ao criar turma',

class Delete(Enum):
    ACTION= 'Deletar turma',
    SUCCESS= 'Turma deletada com sucesso',
    FAILURE= 'Erro ao deletar turma',

class Update(Enum):
    PROMPT = 'Digite o nome da turma'
    ACTION= 'Atualizar turma',
    SUCCESS= 'Turma atualizada com sucesso',
    FAILURE= 'Erro ao atualizar turma',

class List(Enum):
    ACTION= 'Turmas',

