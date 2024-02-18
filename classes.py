import json

class Paciente:
    # Cria a classe dos pacientes com as informações pedidas pelo problema
    def __init__(self,rg, nome, outros_dados):
        self.rg = rg
        self.nome = nome       
        self.outros_dados = outros_dados
        self.prontuarios = []
    def adicionar_prontuário(self, anotações):
        # Adiciona um prontuário à lista de prontuários do paciente
        self.prontuarios.append([anotações])

    def para_dict(self):
        # Converte o objeto paciente em um dicionário
        return {
            'rg': self.rg,
            'nome': self.nome,
            'outros_dados': self.outros_dados,
            'prontuarios': self.prontuarios
        }
    

class Sessão:
    # Cria a classe das sessões com as informações solicitadas pelo problema
    def __init__(self, id, data,horário, duração, dados_opcionais):
        self.id = id
        self.data = data
        self.horário = horário
        self.duração = duração
        self.dados_opcionais = dados_opcionais
    
    def para_dict(self):
        # Converte o objeto sessão em um dicionário
        return {
            'id': self.id,
            'data': self.data,
            'horario': self.horário,
            'duracao': self.duração,
            'dados_opcionais': self.dados_opcionais
        }
    

class Consulta:
    # Cria a classe das consultas dos pacientes numa determinada sessão
    def __init__(self, sessão, paciente):
        self.sessão = sessão
        self.paciente = paciente
    
    def para_dict(self):
        # Converte o objeto consulta em um dicionário
        return {
            'sessao': self.sessão.para_dict(),
            'paciente': self.paciente.para_dict()
        }

        