from enum import Enum


class Create(Enum):
    PROMPT = 'Digite a descrição da atividade'
    PROMPT_TYPE = 'Escolha o tipo de atividade'
    ACTION= 'Criar atividade',
    SUCCESS= 'Atividade criada com sucesso',
    FAILURE= 'Erro ao criar atividade',

class Delete(Enum):
    ACTION= 'Deletar atividade',
    SUCCESS= 'Atividade deletada com sucesso',
    FAILURE= 'Erro ao deletar atividade',

class Update(Enum):
    PROMPT = 'Digite a descrição da atividade'
    ACTION= 'Atualizar atividade',
    SUCCESS= 'Atividade atualizada com sucesso',
    FAILURE= 'Erro ao atualizar atividade',

class List(Enum):
    ACTION= 'Atividades',
    
    def types():
        return {
                0: 'Dependência',
                1: 'Evento',
                2: 'Dever de Casa',
                }
