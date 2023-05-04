#! C:\Users\arlin\AppData\Local\Programs\Python\Python311\python.exe

# -*- coding: UTF-8 -*-

# header code

__author__ = 'Arlindo Martins Correa'
__copyright__ = 'Copyleft 2023, Agenda Unicesumar'
__credits__ = ['Arlindo Mhttps://opensource.org/license/mit/
__license__ = 'MIT License'  # https://opensource.org/license/mit/
__version__ = '0.0.1'
__maintainer__ = 'Arlindo Martins Correa'
__email__ = 'arlindom.correa@gmail.com'
__status__ = 'Prototype'
__course__ = 'pos_dev_python'
__teammates__ = ['Arlindo Martins Correa']
__laboratory__ = 'MAPA'
__date__ = '2023/01/13'
__username__ = 'arlindom.correa'
__description__ = 'My First Project Program.'

# Begin code

# variables
contatos_list=[]
conv_list=[]
match_list_2=[]
match_del_list_2=[]
match_list_4=[]
match_list_5=[]

# format input cursor
esc=chr(27)

# modules
import time

# Principal Menu

while True:

    print('\nAgenda Unicesumar')
    print('\nMenu de opções:\n')

    print('1. Cadastrar Pessoa na Agenda')
    print('2. Alterar dados da Pessoa')
    print('3. Listar Agenda')
    print('4. Procurar pessoa na Agenda')
    print('5. Excluir Pessoa da Agenda')
    print('6. Sair do sistema\n')

# Creating list of contacts

    try:
        user_input=int(input(f"{esc}[5mEscolha uma opção: {esc}[5m"))

        if user_input == 1:
            nome_reg=str(input(f"{esc}[5mDigite o nome completo: {esc}[5m"))
            telefone_reg=int(input(f'{esc}[5mDigite o número do telefone com DDD: {esc}[5m'))
            cidade_reg=str(input(f'{esc}[5mDigite o nome da cidade: {esc}[5m'))
            estado_reg=str(input(f'{esc}[5mDigite o estado com duas letras: {esc}[5m'))
            status_reg=str(input(f'{esc}[5mDigite (P-> Pessoal) ou (C-> Comercial): {esc}[5m'))
            contatos_list.append([nome_reg, telefone_reg, cidade_reg, estado_reg, status_reg])
            print('\nContato cadastrado com sucesso!\n')
            time.sleep(2) # Sleep for 2 seconds

# Change contacts

        elif user_input == 2:
            match_list_2=''
            search_reg=str(input(f'{esc}[5mDigite um nome: {esc}[5m'))

            for match_reg in range(len(contatos_list)):
                if  contatos_list[match_reg][0] == search_reg:
                    match_list_2 = contatos_list[match_reg]

            print('\n', match_list_2, '\n')
            
            if match_list_2 == '':
                print('-------------------------')
                print('|Contato não encontrado.|')
                print('-------------------------')
                print('Tente novamente digitando o nome completo exatamente como foi cadastrado.')
                print('-------------------------------------------------------------------------')
                time.sleep(2) # Sleep for 2 seconds
            
            
            if match_list_2 != '':

# Change Menu
                while True:
                    
                    print('\nMenu de alterações:\n')
                    print('1. Nome')
                    print('2. Telefone')
                    print('3. Cidade')
                    print('4. Estado')
                    print('5. Status')
                    print('6. Voltar ao menu inicial\n')

                    try:
                        alt_reg=int(input(f'{esc}[5mEscolha o campo que deseja alterar: {esc}[5m'))

                        if alt_reg == 1:
                            alt_reg_nome=str(input(f'{esc}[5mDigite o novo nome: {esc}[5m'))
                            match_reg=0
                            for match_reg in range(len(contatos_list)):
                                if  contatos_list[match_reg][0] == search_reg:
                                    contatos_list[match_reg].pop(0)
                                    contatos_list[match_reg].insert(0, alt_reg_nome)
                                    if contatos_list[match_reg][0] == alt_reg_nome:
                                        print('\n Contato atualizado:')
                                        print('\n', contatos_list[match_reg])

                        elif alt_reg == 2:
                            alt_reg_telefone=int(input(f'{esc}[5mDigite o novo Telefone: {esc}[5m'))
                            print('\n', contatos_list[match_reg])
                            match_reg=0
                            for match_reg in range(len(contatos_list)):
                                if  contatos_list[match_reg][0] == search_reg:
                                    contatos_list[match_reg].pop(1)
                                    contatos_list[match_reg].insert(1, alt_reg_telefone)
                                    if contatos_list[match_reg][1] == alt_reg_telefone:
                                        print('\n Contato atualizado:')
                                        print('\n', contatos_list[match_reg])

                        elif alt_reg == 3:
                            alt_reg_cidade=str(input(f'{esc}[5mDigite a nova cidade: {esc}[5m'))
                            print('\n', contatos_list[match_reg])
                            match_reg=0
                            for match_reg in range(len(contatos_list)):
                                if  contatos_list[match_reg][0] == search_reg:
                                    contatos_list[match_reg].pop(2)
                                    contatos_list[match_reg].insert(2, alt_reg_cidade)
                                    if contatos_list[match_reg][2] == alt_reg_cidade:
                                        print('\n Contato atualizado:')
                                        print('\n', contatos_list[match_reg])

                        elif alt_reg == 4:
                            alt_reg_estado=str(input(f'{esc}[5mDigite o novo estado: {esc}[5m'))
                            print('\n', contatos_list[match_reg])
                            match_reg=0
                            for match_reg in range(len(contatos_list)):
                                if  contatos_list[match_reg][0] == search_reg:
                                    contatos_list[match_reg].pop(3)
                                    contatos_list[match_reg].insert(3, alt_reg_estado)
                                    if contatos_list[match_reg][3] == alt_reg_estado:
                                        print('\n Contato atualizado:')
                                        print('\n', contatos_list[match_reg])
                        elif alt_reg == 5:
                            alt_reg_status=str(input(f'{esc}[5mDigite um novo status: {esc}[5m'))
                            print('\n', contatos_list[match_reg])
                            match_reg=0
                            for match_reg in range(len(contatos_list)):
                                if  contatos_list[match_reg][0] == search_reg:
                                    contatos_list[match_reg].pop(4)
                                    contatos_list[match_reg].insert(4, alt_reg_status)
                                    if contatos_list[match_reg][4] == alt_reg_status:
                                        print('\n Contato atualizado:')
                                        print('\n', contatos_list[match_reg])

                        elif alt_reg == 6:
                            break
                        else:
                            time.sleep(2) # Sleep for 2 seconds
                    except ValueError:
                        print('\nDigite apenas números!\n')
                        time.sleep(2) # Sleep for 2 seconds
                    
        elif user_input == 3:
            print('\nLista de contatos:\n')
            for lista_contatos_list in contatos_list:
                print(lista_contatos_list)
            print('\nFim da lista de contatos!\n')
            time.sleep(2) # Sleep for 2 seconds

        elif user_input == 4:
            match_list_4=''
            search_reg=str(input(f'{esc}[5mDigite um nome: {esc}[5m'))

            for match_reg in range(len(contatos_list)):
                if  contatos_list[match_reg][0] == search_reg:
                        match_list_4 = contatos_list[match_reg]

            print('\n', match_list_4, '\n')

            if match_list_4 == '':
                print('-------------------------')
                print('|Contato não encontrado.|')
                print('-------------------------')
                print('Tente novamente digitando o nome completo exatamente como foi cadastrado.')
                print('-------------------------------------------------------------------------')
                time.sleep(2) # Sleep for 2 seconds

        elif user_input == 5:
            match_list_5=''
            search_reg=str(input(f'{esc}[5mDigite um nome: {esc}[5m'))

            for match_reg in range(len(contatos_list)):
                if  contatos_list[match_reg][0] == search_reg:
                    match_list_5 = contatos_list[match_reg]

            print('\n', match_list_5, '\n')

            if match_list_5 == '':
                print('-------------------------')
                print('|Contato não encontrado.|')
                print('-------------------------')
                print('Tente novamente digitando o nome completo exatamente como foi cadastrado.')
                print('-------------------------------------------------------------------------')
                time.sleep(2) # Sleep for 2 seconds
            
            if match_list_5 != '':
                
# Change Menu
                while True:
                    
                    print('\nMenu de exclusão:\n')
                    print('1. Deletar registro')
                    print('2. Voltar ao menu inicial\n')
                    
                    try:
                        del_reg=int(input(f'{esc}[5mEscolha uma opção do menu: {esc}[5m'))

                        if del_reg == 1:
                            match_reg=0
                            for match_reg in range(len(contatos_list)):
                                if  contatos_list[match_reg][0] == search_reg:
                                    contatos_list[match_reg].clear()
                                    contatos_list.remove([])
                                    print('\n Contato excluído!')
                                    time.sleep(2) # Sleep for 2 seconds
                                    break
                            

                        elif del_reg == 2:
                            break
                        else:
                            time.sleep(2) # Sleep for 2 seconds
                    except ValueError:
                        print('\nDigite apenas números!\n')
                        time.sleep(2) # Sleep for 2 seconds

        elif user_input == 6:
            print('---------------------')
            print('|Sistema finalizado.|')
            print('---------------------\n')
            break

    except ValueError:
        print('\nDigite apenas números!\n')
        time.sleep(2) # Sleep for 2 seconds

    else:
        time.sleep(2) # Sleep for 2 seconds