from enum import Enum


class Create(Enum):
    PROMPT = 'Digite o nome do aluno'
    PROMPT_PARENT = 'Digite o nome do responsável pelo aluno'
    ACTION= 'Criar aluno',
    SUCCESS= 'Aluno criado com sucesso',
    FAILURE= 'Erro ao criar aluno',

class Delete(Enum):
    ACTION= 'Deletar aluno',
    SUCCESS= 'Aluno deletado com sucesso',
    FAILURE= 'Erro ao deletar aluno',

class Update(Enum):
    PROMPT = 'Digite o nome do aluno'
    ACTION= 'Atualizar aluno',
    SUCCESS= 'Aluno atualizado com sucesso',
    FAILURE= 'Erro ao atualizar aluno',

class List(Enum):
    ACTION= 'Alunos',

