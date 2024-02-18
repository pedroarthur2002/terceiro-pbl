from classes import *
from datetime import datetime
# Aqui estão todas as variáveis utilizadas no programa.
sessões = []
pacientes = []
consultas = []
consultas_paciente = []
consultas_sessão = []
lista_atendimento = []
numero_sessões = 0
paciente_especifico = 0


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
    

print('CLÍNICA ODONTOLÓGICA DENTECLEAN\n')
print('Quem irá acessar?')
print('[1] Recepção')
print('[2] Dentista')
usuario = int(input('--> '))
while usuario != 1 and usuario != 2:
    print('Digite uma opção válida!')
    usuario = int(input('--> '))

while True:
    if usuario == 1:
        # Esse é o conjunto de opções que o recepcionista tem.
        print('\nBem vindo, recepcionista! O que pretende fazer? \n')
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
        opção = int(input('--> '))
        if opção == 1:
            # Esse trecho cadastra a sessão.
            print('\nADICIONANDO NOVA SESSÃO') 
            numero_sessões += 1
            while True:          
                data = input('Data (dia/mês/ano): ').strip()
                if validar_data(data):
                    break
                else:
                    print('DATA INVÁLIDA! O formato correto é dd/mm/aaaa') 
            while True:  
                horário = input('Horário (hora/minuto): ').strip()
                if validar_horario(horário):
                    break
                else:
                    print('HORÁRIO INVÁLIDO! O formato correto é hh:mm')
            while True:
                duração = int(input('Duração (horas): '))
                if duração <  0 or duração > 5:
                    print('A sessão deve durar no máximo 5 horas!')
                else:
                    break
            condição = int(input('Deseja acrescentar dados opcionais? [1] SIM [2] NÃO: '))
            if condição == 1:
                dados_opcionais = input('Dados Opcionais: ').strip()
            else:
                dados_opcionais = ''
            print('\nSESSÃO ADICIONADA')           
            sessão = Sessão(numero_sessões, data, horário, duração, dados_opcionais)
            sessões.append(sessão)
            with open('sessoes.json', 'w') as arquivo_sessoes:
                lista_sessoes = [sessão.para_dict() for sessão in sessões]
                json.dump(lista_sessoes, arquivo_sessoes, indent=4)

        if opção == 2:
            # Esse trecho exibe as informações das sessões.
            if not sessões:
                print('Não há sessões cadastradas!')
            else:
                print('MOSTRANDO SESSÕES\n')            
                for i in range(len(sessões)):
                    print(f'Sessão número: {sessões[i].id}')
                    print(f'Data: {sessões[i].data}')
                    print(f'Horário: {sessões[i].horário}')
                    if sessões[i].duração == 1:
                        print(f'Duração: {sessões[i].duração} hora')
                    else:                        
                        print(f'Duração: {sessões[i].duração} horas')
                    if sessões[i].dados_opcionais != '':
                        print(f'Dados opcionais: {sessões[i].dados_opcionais}')
                    print('')  

        if opção == 3:
            # Esse trecho é responsável por buscar e mostrar uma sessão existente.
            print('\nBUSCANDO SESSÃO')
            data = input('Digite a data: ').strip()
            horário = input('Digite o horário: ').strip()
            encontrou = False
            for i in range(len(sessões)):
                if sessões[i].data == data and sessões[i].horário == horário:
                  encontrou = True
                  print('\nSESSÃO ENCONTRADA!\n')
                  print(f'Sessão número: {sessões[i].id}')
                  print(f'Data: {sessões[i].data}')
                  print(f'Horário: {sessões[i].horário}')
                  if sessões[i].duração == 1:
                        print(f'Duração: {sessões[i].duração} hora')
                  else:                        
                        print(f'Duração: {sessões[i].duração} horas')
                  if sessões[i].dados_opcionais != '':
                        print(f'Dados opcionais: {sessões[i].dados_opcionais}')
                        print('') 
            if not encontrou:
                print('\nSESSÃO NÃO ENCONTRADA')           

        if opção == 4:
            # Esse trecho inicia a sessão com o horário do dia.
            data = input('Data da sessão: ').strip()
            horário = input('Horário da sessão: ').strip()
            encontrou_sessão = False
            for i in range(len(sessões)):                
                if sessões[i].data == data and sessões[i].horário == horário:
                    encontrou_sessão = True
                    data_hora_agora = datetime.now().strftime("%d-%m-%Y %H:%M")
                    data_hora_sessão = f"{sessões[i].data} {sessões[i].horário}"
                    if data_hora_sessão < data_hora_agora:
                        print('A sessão não pode ser iniciada pois seu horário ou data já ocorreram.')
                    else:
                        print('Sessão iniciada pela recepção.')
                        sessão_atual = sessões[i]
            
            if not encontrou_sessão:
                print('\nA sessão não foi cadastrada!')
                
        if opção == 5:
            # Esse trecho adiciona pacientes.
            print('\nCADASTRANDO UM PACIENTE')
            encontrou_paciente = False
            rg = input('RG: ').strip()

            for i in range(len(pacientes)):
                if pacientes[i].rg == rg:
                    print('Paciente já possui cadastro.')
                    encontrou_paciente = True

            if not encontrou_paciente:                
                nome = input('Nome: ').strip()
                condição_paciente = int(input('Deseja acrescentar outros dados? [1] SIM [2] NÃO: '))
                if condição_paciente == 1:
                    outros_dados = input('Outros dados: ').strip()
                else:
                    outros_dados = ''
                paciente = Paciente(rg, nome, outros_dados)
                print('PACIENTE CADASTRADO.')
                pacientes.append(paciente)
                with open ('pacientes.json','w') as arquivo_pacientes:
                    lista_pacientes = [paciente.para_dict() for paciente in pacientes]                    
                    json.dump(lista_pacientes, arquivo_pacientes, indent=4)
           
        if opção == 6:
            # Esse trecho agenda um horário para o paciente.
            print('MARCANDO HORÁRIO PARA PACIENTE\n')
            rg = input('RG: ').strip()
            id = int(input('ID: '))
            encontrou_paciente = False
            for i in range(len(pacientes)):
                if pacientes[i].rg == rg:
                    encontrou_paciente = True
                    paciente_disponivel = pacientes[i]
            if not encontrou_paciente:
                print('O paciente não está cadastrado.')
            encontrou_sessão = False
            for i in range(len(sessões)):                
                if sessões[i].id == id:
                    encontrou_sessão = True
                    data_hora_agora = datetime.now().strftime("%d-%m-%Y %H:%M")
                    data_hora_sessão = f"{sessões[i].data} {sessões[i].horário}"
                    if data_hora_sessão < data_hora_agora:
                        print('Essa sessão já ocorreu. Marque em outro horário')
                    else:
                        sessão_disponível = sessões[i]
            if not encontrou_sessão:
                print('Sessão não cadastrada.')
            if encontrou_paciente and encontrou_sessão:
                print('HORÁRIO MARCADO')
                consulta = Consulta(sessão_disponível, paciente_disponivel)
                consultas.append(consulta)
                with open ('consultas.json', 'w') as arquivo_consultas:
                    lista_consultas = [consulta.para_dict() for consulta in consultas]
                    json.dump(lista_consultas, arquivo_consultas, indent=4)                                   

        if opção == 7:
            # Esse trecho lista os horários da sessão do paciente.
            print('LISTANDO HORÁRIOS DO PACIENTE\n')
            rg = input('RG: ').strip()
            encontrou_paciente = False
            for i in range(len(pacientes)):
                if pacientes[i].rg == rg:
                    encontrou_paciente = True
                    paciente_especifico = pacientes[i]
            if not encontrou_paciente:
                print('O paciente não está cadastrado.')
            for i in range(len(consultas)):
                if consultas[i].paciente == paciente_especifico:
                    consultas_paciente.append(consultas[i])
            if consultas_paciente:
                print(f'Consultas para o paciente: {consultas_paciente[0].paciente.nome}')
                for i in range(len(consultas_paciente)):
                    print(f'Sessão {consultas[i].sessão.id}')
                    print(f'{consultas[i].sessão.data} -- {consultas[i].sessão.horário}')
                    print(f'Duração: {consultas[i].sessão.duração}h')
                    print('')
            else:
                print(f'O paciente não possui consultas marcadas.')                
            
        if opção == 8:
            # Esse trecho verifica se o paciente está marcado para a sessão iniciada.
            print('VERIFICANDO MARCAÇÃO')
            print('Inicie a sessão antes de fazer a confirmação')
            rg = input('RG: ').strip()
            encontrou_paciente = False
            encontrou_paciente_sessão_atual = False
            paciente_esp = None
            for i in range(len(pacientes)):
                if pacientes[i].rg == rg:                    
                    encontrou_paciente = True
                    paciente_esp = pacientes[i]
            if not encontrou_paciente:
                print('Paciente não cadastrado.')
            for i in range(len(consultas)):
                if isinstance(paciente_esp, Paciente):
                    if consultas[i].sessão.id == sessão_atual.id and consultas[i].paciente.rg == paciente_esp.rg:
                        encontrou_paciente_sessão_atual = True
                        print(f'O paciente {paciente_esp.nome} está marcado para a sessão na data {sessão_atual.data} às {sessão_atual.horário}')
            if not encontrou_paciente_sessão_atual and encontrou_paciente:
                print('O paciente não tem horário marcado na sessão atual!')               

        if opção == 9:
            # Esse trecho coloca o paciente na fila de atendimento
            print('Você deve iniciar a sessão antes de colocar os pacientes na fila')
            rg = input('RG: ').strip()
            encontrou_paciente = False
            paciente_específico_1 = None
            consulta_atual = None
            encontrou_consulta_atual = False
            for i in range(len(pacientes)):
                if pacientes[i].rg == rg:
                    encontrou_paciente = True
                    paciente_específico_1 = pacientes[i]
            if not encontrou_paciente:
                print('Paciente não cadastrado')
            for i in range(len(consultas)):
                if isinstance(paciente_específico_1, Paciente):
                    if consultas[i].sessão.id == sessão_atual.id and consultas[i].paciente.rg == rg:
                        consulta_atual = consultas[i]
                        encontrou_consulta_atual = True
            if not encontrou_consulta_atual:
                print('O paciente não está cadastrado para a consulta atual')
            if isinstance(consulta_atual, Consulta):
                lista_atendimento.append(consulta_atual)
                print(f'O paciente {consulta_atual.paciente.nome} foi adicionada à fila de espera da sessão de {consulta_atual.sessão.data} às {consulta_atual.sessão.horário}')

        if opção == 10:
            if not lista_atendimento:
                print('Não há ninguém na lista de atendimento')
            else:
                print(f'Próximo paciente para atendimento: {lista_atendimento[0].paciente.nome}')
                print(f'Sessão: {lista_atendimento[0].sessão.data} às {lista_atendimento[0].sessão.horário}')

        if opção == 11:
            # Esse trecho lista as consultas marcadas numa sessão
            id = int(input('ID: '))
            encontrou_sessão = False
            sessão_especifica = None
            consultas_sessão = []
            for i in range(len(sessões)):
                if sessões[i].id == id:
                    encontrou_sessão = True
                    sessão_especifica = sessões[i]
            if not encontrou_sessão:
                print('Sessão não cadastrada')
            for i in range(len(consultas)):
                if isinstance(sessão_especifica, Sessão):
                    if consultas[i].sessão.id == sessão_especifica.id:
                        consultas_sessão.append(consultas[i])
            if not consultas_sessão:
                print('Não há consultas nessa sessão.')
            else:
                print('\nCONSULTAS DA SESSÃO')
                for i in range(len(consultas_sessão)):
                    print(f'Paciente: {consultas_sessão[i].paciente.nome}')
                    print(f'Data: {consultas_sessão[i].sessão.data}')
                    print(f'Horário: {consultas_sessão[i].sessão.horário}')
                    print('') 

        if opção == 12:
            # Troca para o modo dentista.
            print('Trocando para dentista')
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
            data = input('Digite a data: ').strip()
            horário = input('Digite o horário: ').strip()
            encontrou = False
            for i in range(len(sessões)):
                if sessões[i].data == data and sessões[i].horário == horário:
                  encontrou = True
                  print('\nSESSÃO ENCONTRADA!\n')
                  print(f'Sessão número: {sessões[i].id}')
                  print(f'Data: {sessões[i].data}')
                  print(f'Horário: {sessões[i].horário}')
                  if sessões[i].duração == 1:
                        print(f'Duração: {sessões[i].duração} hora')
                  else:                        
                        print(f'Duração: {sessões[i].duração} horas')
                  if sessões[i].dados_opcionais != '':
                        print(f'Dados opcionais: {sessões[i].dados_opcionais}')
                        print('')  
            if not encontrou:                
                print('\nSESSÃO NÃO ENCONTRADA!')

        if opção == 2:
            # Esse trecho inicia a sessão com o horário do dia.
            data = input('Data da sessão: ').strip()
            horário = input('Horário da sessão: ').strip()
            encontrou_sessão = False
            for i in range(len(sessões)):                
                if sessões[i].data == data and sessões[i].horário == horário:
                    encontrou_sessão = True
                    data_hora_agora = datetime.now().strftime("%d-%m-%Y %H:%M")
                    data_hora_sessão = f"{sessões[i].data} {sessões[i].horário}"
                    if data_hora_sessão < data_hora_agora:
                        print('A sessão não pode ser iniciada pois seu horário ou data já ocorreram.')
                    else:
                        print('')
                        print('SESSÃO INICIADA PELO DENTISTA.')
                        sessão_atual = sessões[i]
            
            if not encontrou_sessão:
                print('\nA SESSÃO NÃO FOI CADASTRADA!')

        if opção == 3:           
            # Esse trecho é responsável por atender o próximo paciente na fila de atendimento.
            if lista_atendimento:
                prox_consulta = lista_atendimento.pop(0)
                prox_paciente = prox_consulta.paciente
                print(f'O paciente {prox_consulta.paciente.nome} será atendido agora.')                
                print(f'Sessão {prox_consulta.sessão.data} -- {prox_consulta.sessão.horário}')
                anotações = input('Faça anotações para o prontuário: ').strip()
                if anotações != '':               
                    prox_paciente.adicionar_prontuário(anotações)                
            else:
                print('Não há ninguém na fila de atendimento.')
            with open('pacientes.json', 'w') as arquivo_pacientes:
                lista_pacientes = [paciente.para_dict() for paciente in pacientes]
                json.dump(lista_pacientes, arquivo_pacientes, indent=4)

        if opção == 4:
            if not prox_consulta:
                print('Não há ninguém sendo atendido agora.')
            else:
                print('MOSTRANDO O PRONTUÁRIO DO PACIENTE ATUAL')
                for i in range(len(prox_paciente.prontuários)):
                    print(f'{i}: {prox_paciente.prontuários[i]}')
        
        if opção == 5:
            if not prox_consulta:
                print('Não há ninguém na fila de atendimento.')
            else:
                print(f'Primeira anotação do paciente {prox_paciente.nome}')
                print(f'{prox_paciente.prontuários[0]}')
        
        if opção == 6:
            if not prox_consulta:
                print('Não há ninguém na fila de atendimento.')
            else:
                print(f'Última anotação do paciente {prox_paciente.nome}')
                print(f'{prox_paciente.prontuários[-1]}')

        if opção == 8:
            # Troca para o modo recepção.
            print('Trocando para recepção')
            usuario = 1

        if opção == 0:
            # Fecha o programa.
            print('Fechando o programa...')
            break
        
       
    



