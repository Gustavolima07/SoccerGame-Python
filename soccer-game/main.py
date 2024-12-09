from player import *
import os

def clear(): #Limpa o terminal
    os.system('cls')
    
clear()

dream_team = [] #Time criado pelo usuário

def adicionar_jogador(): #Função para cadastrar um jogador
    clear()
    nome = str(input("Digite o nome do jogador: "))
    idade = int(input("Digite a idade do jogador: "))
    posicao = str(input("Digite a posição do jogador: "))
    atributo = int(input("Digite o atributos geral do jogador: "))
    
    dream_team.append(Player(nome,idade,posicao,atributo)) #Adiciona o jogador na lista
    adicionar_novamente = int(input("Deseja adicionar mais alguém? 1 - Sim ou 0 - Não: "))
    if(adicionar_novamente == 1):
        adicionar_jogador()
    else:
        clear()
        menu()
        
def lista_jogadores():
    y = 0
    clear()
    print("{:<4} {:<10} {:<7} {:<10}"
          .format("N°","Nome","Idade","Posição") )
    for x in dream_team:
        print("{:<4} {:<10} {:<7} {:<10}"
              .format(y,
                      x.get_nome(),
                      x.get_idade(),
                      x.get_posicao(),
                      x.get_atributos()
                      ))
        y += 1
    menu()
    
def alterar_jogador():
    x = int(input("Digite o N° do jogador: "))
    opcao = int(input("Digite a opção que deseja alterar: \n1 - Nome \n2 - Idade \n3 - Posição \n"))
    valor = str(input("Escreva o novo valor da opção: "))
    if(opcao == 1): dream_team[x].set_nome(valor)
    elif(opcao == 2): dream_team[x].set_idade(valor)
    elif(opcao == 3): dream_team[x].set_posicao(valor)
    else:
        print("Valor incorreto!")
    menu()
    
def remover_jogador():
    x = int(input("Digite o número do jogador que deseja remover: "))
    res = int(input("Tem certeza que deseja remover o jogador número?\n1 - Sim \n2 - Não\n"))
    if (res == 1):
        dream_team.pop(x)
        clear()
        menu()
    else:
        print("Operação cancelada!")
        menu()
        
def menu():
    print("Bem vindo Soccer-Game!\n")
    x = int(input("Digite a opção desejada: \n1 - Adicionar jogador \n2 - Listar jogadores \n3 - Alterar jogador \n4 - Remover jogador \n5 - Sair\n"))
    if(x == 1): adicionar_jogador()
    elif(x == 2): lista_jogadores()
    elif(x == 3): alterar_jogador()
    elif(x == 4): remover_jogador()
    elif(x == 5): exit()
    else:
        print("Valor incorreto!")
        menu()     
menu()    

    
