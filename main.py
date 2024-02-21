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

from classes import *
from datetime import datetime
import json
import re
# Aqui estão todas as variáveis utilizadas no programa
sessoes = []
pacientes = []
consultas = []
consultas_sessao = []
lista_atendimento = []
numero_sessoes = 0
paciente_especifico = 0
sessão_atual = None

def validar_data(data):
    try:
        # Tenta converter a string de data para o formato correto
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        # Se houver erro na conversão, a data é inválida
        return False

def validar_horario(horario):
    try:
        # Tenta converter a string de horário para o formato correto
        datetime.strptime(horario, '%H:%M')
        return True
    except ValueError:
        # Se houver erro na conversão, o horário é inválido
        return False   

def maior_id():
    if not sessoes:
        return 0
    else:
        return max(sessao.id for sessao in sessoes)

def validar_rg(rg):
    # Verifica se o RG tem exatamente 9 dígitos e contém apenas números de 0 a 9
    return bool(re.match(r'^\d{10}$', rg))


print('CLÍNICA ODONTOLÓGICA DENTECLEAN\n')
print('Quem irá acessar?')
print('[1] Recepção')
print('[2] Dentista')
while True:
    usuario_string = input('--> ').strip()
    if usuario_string not in ['1','2']:
        print('Digite uma tipo de usuário VÁLIDO!')
    else:
        usuario = int(usuario_string)
        break

while True:
    # Faz uma validação para quando o arquivo está vazio
    try:
        # Carrega o arquivo das sessões, colocando de volta na forma de objeto
        with open('sessoes.json', 'r') as arquivo_sessoes:
            lista_sessoes = json.load(arquivo_sessoes)
            if not lista_sessoes:
                print('')
            else:
                sessoes = [Sessao.from_dict(sessao_dict) for sessao_dict in lista_sessoes]
    except FileNotFoundError:
        print('')
    except json.JSONDecodeError:
        print('')

    # Faz uma validação para quando o arquivo está vazio
    try:     
    # Carrega o arquivo dos pacientes, colocando de volta na forma de objeto
        with open('pacientes.json', 'r') as arquivo_pacientes:
            lista_pacientes = json.load(arquivo_pacientes)
            if not lista_pacientes:
                print('')
            else:
                pacientes = [Paciente.from_dict(paciente_dict) for paciente_dict in lista_pacientes]
    except FileNotFoundError:
        print('')
    except json.JSONDecodeError:
        print('')

    # Faz uma validação para quando o arquivo está vazio
    try:
    # Carrega o arquivo das consultas, colocando de volta na forma de objeto
        with open('consultas.json', 'r') as arquivo_consultas:
            lista_consultas = json.load(arquivo_consultas)
            if not lista_consultas:
                print('')
            else:
                consultas = [Consulta(Sessao.from_dict(consulta_dict['sessao']), Paciente.from_dict(consulta_dict['paciente'])) for consulta_dict in lista_consultas]       
    except FileNotFoundError:
        print('')
    except json.JSONDecodeError:
        print('')

    numero_sessoes = 1 + maior_id()

    if usuario == 1:
        # Esse é o conjunto de opções que o recepcionista tem.
        print('Bem vindo, recepcionista! O que pretende fazer?\n')
        print('[1] Adicionar nova sessão clínica')
        print('[2] Listar sessões clínicas')
        print('[3] Buscar sessão clínica')
        print('[4] Iniciar sessão clínica')
        print('[5] Adicionar novo paciente')
        print('[6] Marcar horário para o paciente')
        print('[7] Listar horários marcados do paciente')
        print('[8] Confirmar se o paciente está marcado para a sessão atual')
        print('[9] Colocar paciente na fila de atendimento')
        print('[10] Listar próximo paciente da fila de atendimento')
        print('[11] Listar consultas realizadas numa sessão clínica')
        print('[12] Trocar para área do dentista')
        print('[0] Sair')

        while True:
            opção_string = input('--> ').strip()
            if opção_string not in ['0','1','2','3','4','5','6','7','8','9','10','11','12']:
                print('Digite uma opção VÁLIDA!')
            else:
                opção = int(opção_string)
                break

        if opção == 1:
            # Esse trecho cadastra a sessão
            print('\nADICIONANDO NOVA SESSÃO')

            # Validação para a data
            while True:          
                data = input('Data (dd/mm/aaaa): ').strip()
                if validar_data(data):
                    break
                else:
                    print('DATA INVÁLIDA! O formato correto é dd/mm/aaaa')

            # Validação para o horário
            while True:  
                horario = input('Horário (hh:mm): ').strip()
                if validar_horario(horario):
                    break
                else:
                    print('HORÁRIO INVÁLIDO! O formato correto é hh:mm')

            # Validação para a duração da sessão
            while True:
                duracao_string = input('Duração (h): ').strip()
                if duracao_string not in ['0','1','2','3','4','5']:               
                    print('A sessão deve durar no máximo 5 horas!')
                else:
                    duracao = int(duracao_string)
                    break

            condicao = int(input('Deseja acrescentar dados opcionais? [1] SIM [2] NÃO: '))
            if condicao == 1:
                dados_opcionais = input('Dados Opcionais: ').strip()
            else:
                dados_opcionais = ''

            print('\nSESSÃO ADICIONADA')           
            sessao = Sessao(numero_sessoes, data, horario, duracao, dados_opcionais)
            sessoes.append(sessao)
            with open('sessoes.json', 'w') as arquivo_sessoes:
                lista_sessoes = [sessao.para_dict() for sessao in sessoes]
                json.dump(lista_sessoes, arquivo_sessoes, indent=2)
            numero_sessoes += 1          

        if opção == 2:
            # Esse trecho exibe as informações das sessões.
            if not sessoes:
                print('Não há sessões cadastradas!')
            else:
                print('MOSTRANDO SESSÕES\n')            
                for i in range(len(sessoes)):
                    print(f'Sessão número: {sessoes[i].id}')
                    print(f'Data: {sessoes[i].data}')
                    print(f'Horário: {sessoes[i].horario}')
                    if sessoes[i].duracao == 1:
                        print(f'Duração: {sessoes[i].duracao} hora')
                    else:                        
                        print(f'Duração: {sessoes[i].duracao} horas')
                    if sessoes[i].dados_opcionais != '':
                        print(f'Dados opcionais: {sessoes[i].dados_opcionais}')
                    print('')  

        if opção == 3:
            # Esse trecho é responsável por buscar e mostrar uma sessão existente.
            print('\nBUSCANDO SESSÃO')

            # Validação para a data
            while True:
                data = input('Data (dd/mm/aaaa): ').strip()
                if validar_data(data):
                    break
                else:
                    print('DATA INVÁLIDA! O formato correto é dd/mm/aaaa')

            # Validação para o horário
            while True:
                horario = input('Horário (hh:mm): ').strip()
                if validar_horario(horario):
                    break
                else:
                    print('HORÁRIO INVÁLIDO! O formato correto é hh:mm')

            encontrou = False
            for i in range(len(sessoes)):
                if sessoes[i].data == data and sessoes[i].horario == horario:
                  encontrou = True
                  print('\nSESSÃO ENCONTRADA!\n')
                  print(f'Sessão número: {sessoes[i].id}')
                  print(f'Data: {sessoes[i].data}')
                  print(f'Horário: {sessoes[i].horario}')
                  if sessoes[i].duracao == 1:
                        print(f'Duração: {sessoes[i].duracao} hora')
                  else:                        
                        print(f'Duração: {sessoes[i].duracao} horas')
                  if sessoes[i].dados_opcionais != '':
                        print(f'Dados opcionais: {sessoes[i].dados_opcionais}')
                        print('') 
            if not encontrou:
                print('\nSESSÃO NÃO ENCONTRADA')           

        if opção == 4:
            # Esse trecho inicia a sessão com o horário do dia.

            # Validação para a data
            while True:
                data = input('Data (dd/mm/aaaa): ').strip()
                if validar_data(data):
                    break
                else:
                    print('DATA INVÁLIDA! O formato correto é dd/mm/aaaa')

            # Validação para o horário
            while True:
                horario = input('Horário (hh:mm): ').strip()
                if validar_horario(horario):
                    break
                else:
                    print('HORÁRIO INVÁLIDO! O formato correto é hh:mm')

            encontrou_sessão = False
            for i in range(len(sessoes)):                
                if sessoes[i].data == data and sessoes[i].horario == horario:
                    encontrou_sessão = True
                    data_hora_agora = datetime.now().strftime("%d-%m-%Y %H:%M")
                    data_hora_sessão = f"{sessoes[i].data} {sessoes[i].horario}"
                    if data_hora_sessão < data_hora_agora:
                        print('\nA sessão não pôde ser iniciada pois seu horário ou data já ocorreram.')
                    else:
                        print('\nSessão iniciada pela recepção.')
                        sessão_atual = sessoes[i]
            
            if not encontrou_sessão:
                print('\nA sessão não foi cadastrada!')
                
        if opção == 5:
            # Esse trecho adiciona pacientes no sistema
            print('\nCADASTRANDO UM PACIENTE')
            encontrou_paciente = False

            # Validação do formato do RG
            while True:
                rg = input('RG: ').strip()               
                if validar_rg(rg):
                    break
                else:
                    print('Digite um RG VÁLIDO!')     

            # Validação de existência do RG
            for i in range(len(pacientes)):
                if pacientes[i].rg == rg:
                    print('Paciente já possui cadastro.')
                    encontrou_paciente = True

            if not encontrou_paciente:
                # Validação para o nome
                while True:              
                    nome = input('Nome: ').strip()
                    if nome in ['']:
                        print('Digite um nome VÁLIDO!')
                    else:
                        break

                condição_paciente = int(input('Deseja acrescentar outros dados? [1] SIM [2] NÃO: '))
                if condição_paciente == 1:
                    outros_dados = input('Outros dados: ').strip()
                else:
                    outros_dados = ''

                paciente = Paciente(rg, nome, outros_dados)
                print('PACIENTE CADASTRADO.')
                pacientes.append(paciente)
                with open('pacientes.json', 'w') as arquivo_pacientes:
                    lista_pacientes = [paciente.para_dict() for paciente in pacientes]
                    json.dump(lista_pacientes, arquivo_pacientes, indent=2)
           
        if opção == 6:
            # Esse trecho agenda um horário para o paciente.
            print('MARCANDO HORÁRIO PARA PACIENTE\n')

            # Validação para o formato do RG
            while True:
                rg = input('RG: ').strip()
                if validar_rg(rg):
                    break
                else:
                    print('Digite um RG VÁLIDO!')

            id = int(input('ID: '))

            encontrou_paciente = False
            for i in range(len(pacientes)):
                if pacientes[i].rg == rg:
                    encontrou_paciente = True
                    paciente_disponivel = pacientes[i]
            if not encontrou_paciente:
                print('O paciente não está cadastrado.')
            encontrou_sessão = False
            for i in range(len(sessoes)):                
                if sessoes[i].id == id:
                    encontrou_sessão = True
                    data_hora_agora = datetime.now().strftime("%d-%m-%Y %H:%M")
                    data_hora_sessão = f"{sessoes[i].data} {sessoes[i].horario}"
                    if data_hora_sessão < data_hora_agora:
                        print('Essa sessão já ocorreu. Marque em outro horário')
                    else:
                        sessão_disponível = sessoes[i]
            if not encontrou_sessão:
                print('Sessão não cadastrada.')
            if encontrou_paciente and encontrou_sessão:
                print('HORÁRIO MARCADO')
                consulta = Consulta(sessão_disponível, paciente_disponivel)
                consultas.append(consulta)
                with open('consultas.json', 'w') as arquivo_consultas:
                    lista_consultas = [consulta.para_dict() for consulta in consultas]
                    json.dump(lista_consultas, arquivo_consultas, indent=2)                               

        if opção == 7:
            # Esse trecho lista os horários da sessão do paciente.

            # Validação para o formato do RG
            print('LISTANDO HORÁRIOS DO PACIENTE\n')
            while True:
                rg = input('RG: ').strip()
                if validar_rg(rg):
                    break
                else:
                    print('Digite um RG VÁLIDO!')
            
            encontrou_paciente = False
            for i in range(len(pacientes)):
                if pacientes[i].rg == rg:
                    encontrou_paciente = True
                    paciente_especifico = pacientes[i]
            if not encontrou_paciente:
                print('O paciente não está cadastrado.')
            consultas_paciente = []
            for i in range(len(consultas)):
                if consultas[i].paciente.rg == paciente_especifico.rg:
                    consultas_paciente.append(consultas[i])
            if consultas_paciente:
                print(f'Consultas para o paciente: {consultas_paciente[0].paciente.nome}')
                for i in range(len(consultas_paciente)):
                    print(f'Sessão {consultas_paciente[i].sessao.id}')
                    print(f'{consultas_paciente[i].sessao.data} -- {consultas_paciente[i].sessao.horario}')
                    print(f'Duração: {consultas_paciente[i].sessao.duracao}h')
                    print('')
            else:
                print(f'O paciente não possui consultas marcadas.')                
            
        if opção == 8:
            # Esse trecho verifica se o paciente está marcado para a sessão iniciada.            
            print('VERIFICANDO MARCAÇÃO')
            print('Inicie a sessão antes de fazer a confirmação')

            # Validação para o formato do RG
            while True:
                rg = input('RG: ').strip()
                if validar_rg(rg):
                    break
                else:
                    print('Digite um RG VÁLIDO!')

            encontrou_paciente = False
            encontrou_paciente_sessão_atual = False
            paciente_esp = None            
            if isinstance(sessão_atual, Sessao):
                for i in range(len(pacientes)):
                    if pacientes[i].rg == rg:                    
                        encontrou_paciente = True
                        paciente_esp = pacientes[i]
                if not encontrou_paciente:
                    print('Paciente não cadastrado.')
                for i in range(len(consultas)):
                    if isinstance(paciente_esp, Paciente):
                        if consultas[i].sessao.id == sessão_atual.id and consultas[i].paciente.rg == paciente_esp.rg:
                            encontrou_paciente_sessão_atual = True
                            print(f'O paciente {paciente_esp.nome} está marcado para a sessão na data {sessão_atual.data} às {sessão_atual.horario}')
                if not encontrou_paciente_sessão_atual and encontrou_paciente:
                    print('O paciente não tem horário marcado na sessão atual!')
            else:
                print('\nA SESSÃO NÃO FOI INICIADA!')               

        if opção == 9:
            # Esse trecho coloca o paciente na fila de atendimento
            print('Você deve iniciar a sessão antes de colocar os pacientes na fila')
            
            # Validação para o formato do RG
            while True:
                rg = input('RG: ').strip()
                if validar_rg(rg):
                    break
                else:
                    print('Digite um RG VÁLIDO!')            
                
            encontrou_paciente = False
            paciente_específico_1 = None
            consulta_atual = None
            encontrou_consulta_atual = False
            if isinstance(sessão_atual, Sessao):
                for i in range(len(pacientes)):
                    if pacientes[i].rg == rg:
                        encontrou_paciente = True
                        paciente_específico_1 = pacientes[i]
                if not encontrou_paciente:
                    print('Paciente não cadastrado')
                for i in range(len(consultas)):
                    if isinstance(paciente_específico_1, Paciente):
                        if consultas[i].sessao.id == sessão_atual.id and consultas[i].paciente.rg == rg:
                            consulta_atual = consultas[i]
                            encontrou_consulta_atual = True
                if not encontrou_consulta_atual:
                    print('O paciente não está cadastrado para a consulta atual')
                if isinstance(consulta_atual, Consulta):
                    lista_atendimento.append(consulta_atual)
                    print(f'O paciente {consulta_atual.paciente.nome} foi adicionada à fila de espera da sessão de {consulta_atual.sessao.data} às {consulta_atual.sessao.horario}')
            else:
                print('\nA SESSÃO NÃO FOI INICIADA')
                
        if opção == 10:
            # Esse trecho mostra o próximo paciente na fila para ser atendido
            if not lista_atendimento:
                print('Não há ninguém na lista de atendimento')
            else:
                print(f'Próximo paciente para atendimento: {lista_atendimento[0].paciente.nome}')
                print(f'Sessão: {lista_atendimento[0].sessao.data} às {lista_atendimento[0].sessao.horario}')

        if opção == 11:
            # Esse trecho lista as consultas marcadas numa sessão
            id = int(input('ID: '))
            encontrou_sessão = False
            sessão_especifica = None
            consultas_sessão = []
            for i in range(len(sessoes)):
                if sessoes[i].id == id:
                    encontrou_sessão = True
                    sessão_especifica = sessoes[i]
            if not encontrou_sessão:
                print('Sessão não cadastrada')
            for i in range(len(consultas)):
                if isinstance(sessão_especifica, Sessao):
                    if consultas[i].sessao.id == sessão_especifica.id:
                        consultas_sessão.append(consultas[i])
            if not consultas_sessão:
                print('Não há consultas nessa sessão.')
            else:
                print('\nCONSULTAS DA SESSÃO')
                for i in range(len(consultas_sessão)):
                    print(f'Paciente: {consultas_sessão[i].paciente.nome}')
                    print(f'Data: {consultas_sessão[i].sessao.data}')
                    print(f'Horário: {consultas_sessão[i].sessao.horario}')
                    print('') 

        if opção == 12:
            # Troca para o modo dentista.
            print('Trocando para DENTISTA')
            usuario = 2

        if opção == 0:
            # Fecha o programa.
            print('Fechando o programa...')
            break


    elif usuario == 2:
        # Esse é o conjunto de opções que o dentista tem.
        print('\nBem vindo, dentista! O que pretende fazer? \n')
        print('[1] Localizar sessão clínica')
        print('[2] Iniciar sessão clínica')
        print('[3] Atender próximo paciente')
        print('[4] Ler prontuário completo do paciente atual')
        print('[5] Ler primeira anotação do paciente atual')
        print('[6] Ler última anotação do paciente atual')
        print('[7] Trocar para área da recepção')
        print('[0] Sair')
        opção = int(input('--> '))

        if opção == 1:
            # Esse trecho é responsável por buscar e mostrar uma sessão existente.
            print('\nBUSCANDO SESSÃO')

            # Validação para a data
            while True:
                data = input('Data (dd/mm/aaaa): ').strip()
                if validar_data(data):
                    break
                else:
                    print('DATA INVÁLIDA! O formato correto é dd/mm/aaaa')

            # Validação para o horário
            while True:
                horario = input('Horário (hh:mm): ').strip()
                if validar_horario(horario):
                    break
                else:
                    print('HORÁRIO INVÁLIDO! O formato correto é hh:mm')

            encontrou = False
            for i in range(len(sessoes)):
                if sessoes[i].data == data and sessoes[i].horario == horario:
                  encontrou = True
                  print('\nSESSÃO ENCONTRADA!\n')
                  print(f'Sessão número: {sessoes[i].id}')
                  print(f'Data: {sessoes[i].data}')
                  print(f'Horário: {sessoes[i].horario}')
                  if sessoes[i].duracao == 1:
                        print(f'Duração: {sessoes[i].duracao} hora')
                  else:                        
                        print(f'Duração: {sessoes[i].duracao} horas')
                  if sessoes[i].dados_opcionais != '':
                        print(f'Dados opcionais: {sessoes[i].dados_opcionais}')
                        print('') 
            if not encontrou:
                print('\nSESSÃO NÃO ENCONTRADA') 

        if opção == 2:
            # Esse trecho inicia a sessão com o horário do dia.

            # Validação para a data
            while True:
                data = input('Data (dd/mm/aaaa): ').strip()
                if validar_data(data):
                    break
                else:
                    print('DATA INVÁLIDA! O formato correto é dd/mm/aaaa')

            # Validação para o horário
            while True:
                horario = input('Horário (hh:mm): ').strip()
                if validar_horario(horario):
                    break
                else:
                    print('HORÁRIO INVÁLIDO! O formato correto é hh:mm')

            encontrou_sessão = False
            for i in range(len(sessoes)):                
                if sessoes[i].data == data and sessoes[i].horario == horario:
                    encontrou_sessão = True
                    data_hora_agora = datetime.now().strftime("%d-%m-%Y %H:%M")
                    data_hora_sessão = f"{sessoes[i].data} {sessoes[i].horario}"
                    if data_hora_sessão < data_hora_agora:
                        print('\nA sessão não pôde ser iniciada pois seu horário ou data já ocorreram.')
                    else:
                        print('\nSessão iniciada pelo DENTISTA.')
                        sessão_atual = sessoes[i]
            
            if not encontrou_sessão:
                print('\nA sessão não foi cadastrada!')
            
            if not encontrou_sessão:
                print('\nA SESSÃO NÃO FOI CADASTRADA!')

        if opção == 3:           
            # Esse trecho é responsável por atender o próximo paciente na fila de atendimento.
            if lista_atendimento:
                prox_consulta = lista_atendimento.pop(0)
                prox_paciente = prox_consulta.paciente
                print(f'O paciente {prox_consulta.paciente.nome} será atendido agora.')                
                print(f'Sessão {prox_consulta.sessao.data} -- {prox_consulta.sessao.horario}')
                anotações = input('Faça anotações para o prontuário: ').strip()
                if anotações != '':               
                    prox_paciente.adicionar_prontuario(anotações)                
            else:
                print('Não há ninguém na fila de atendimento.')
            with open('pacientes.json', 'w') as arquivo_pacientes:
                lista_pacientes = [paciente.para_dict() for paciente in pacientes]
                json.dump(lista_pacientes, arquivo_pacientes, indent=2)

        if opção == 4:
            # Mostra o prontuário completo do paciente que está sendo atendido
            if not prox_consulta:
                print('Não há ninguém sendo atendido agora.')
            else:
                print('MOSTRANDO O PRONTUÁRIO DO PACIENTE ATUAL')
                for i in range(len(prox_paciente.prontuarios)):
                    print(f'{i}: {prox_paciente.prontuarios[i]}')
        
        if opção == 5:
            # Mostra a primeira anotação do prontuário do paciente que está sendo atendido
            if not prox_consulta:
                print('Não há ninguém na fila de atendimento.')
            else:
                print(f'Primeira anotação do paciente {prox_paciente.nome}')
                print(f'{prox_paciente.prontuarios[0]}')
        
        if opção == 6:
            # Mostra a última anotação do prontuário do paciente que está sendo atendido
            if not prox_consulta:
                print('Não há ninguém na fila de atendimento.')
            else:
                print(f'Última anotação do paciente {prox_paciente.nome}')
                print(f'{prox_paciente.prontuarios[-1]}')

        if opção == 7:
            # Troca para o modo recepção
            print('Trocando para recepção')
            usuario = 1

        if opção == 0:
            # Fecha o programa
            print('Fechando o programa...')
            break
        
       
    



