'''
Autor: PEDRO ARTHUR NERY DA ROCHA COSTA
Componente Curricular: EXA 854 - MI - Algoritmos
Concluído em: 21/02/2024
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
'''

# CÓDIGO FEITO NO WINDOWS

import json

class Paciente:
    # Cria a classe dos pacientes com as informações pedidas pelo problema
    def __init__(self,rg, nome, outros_dados):
        self.rg = rg
        self.nome = nome       
        self.outros_dados = outros_dados
        self.prontuarios = []

    def adicionar_prontuario(self, anotacoes):
        # Adiciona um prontuário à lista de prontuários do paciente
        self.prontuarios.append([anotacoes])

    def para_dict(self):
        # Converte o objeto paciente em um dicionário
        return {
            'rg': self.rg,
            'nome': self.nome,
            'outros_dados': self.outros_dados,
            'prontuarios': self.prontuarios
        }
    
    @classmethod
    def from_dict(cls, paciente_dict):
        return cls(
            paciente_dict['rg'],
            paciente_dict['nome'],
            paciente_dict['outros_dados']
        )

class Sessao:
    # Cria a classe das sessões com as informações solicitadas pelo problema
    def __init__(self, id, data,horario, duracao, dados_opcionais):
        self.id = id
        self.data = data
        self.horario = horario
        self.duracao = duracao
        self.dados_opcionais = dados_opcionais
    
    def para_dict(self):
        # Converte o objeto sessão em um dicionário
        return {
            'id': self.id,
            'data': self.data,
            'horario': self.horario,
            'duracao': self.duracao,
            'dados_opcionais': self.dados_opcionais
        }
    
    @classmethod
    # Converte o dicionário para o objeto
    def from_dict(cls, sessao_dict):
        return cls(
            sessao_dict['id'],
            sessao_dict['data'],
            sessao_dict['horario'],
            sessao_dict['duracao'],
            sessao_dict['dados_opcionais']
        )

class Consulta:
    # Cria a classe das consultas dos pacientes numa determinada sessão
    def __init__(self, sessao, paciente):
        self.sessao = sessao
        self.paciente = paciente
    
    def para_dict(self):
        # Converte o objeto consulta em um dicionário
        return {
            'sessao': self.sessao.para_dict(),
            'paciente': self.paciente.para_dict()
        }
    
    @classmethod
    def from_dict(cls, consulta_dict):
        return cls(
            Sessao.from_dict(consulta_dict['sessao']),
            Paciente.from_dict(consulta_dict['paciente'])
        )
        