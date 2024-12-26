from player import *
from teams import *
import os
import random as chances

def clear(): #Limpa o terminal
    os.system('cls')
    
clear()

dream_team = [] #Time criado pelo usuário


def adicionar_jogador(): #Função para cadastrar um jogador
    clear()
    x = int(input("Digite se voce quer criar os seus propríos jogadores ou usar um elenco padrão: \n1 - Criar Jogador \n2 - Elenco padrão \n3 - Sair\n"))
    if(x == 1):
        nome = str(input("Digite o nome do jogador: "))
        idade = int(input("Digite a idade do jogador: "))
        posicao = int(input("Digite a posição do jogador: 1 - Goleiro, 2 - Zagueiro, 3 - Meio-Campo, 4 - Atacante: \n"))
        num = int(input("Digite o número da camisa do jogador: "))
        atributo = int(input("Digite o atributos geral do jogador: "))
        if(posicao == 1): posicao = "Goleiro"
        elif(posicao == 2): posicao = "Zagueiro"
        elif(posicao == 3): posicao = "Meio-Campo"
        elif(posicao == 4): posicao = "Atacante"
        dream_team.append(Player(nome,idade,posicao,num,atributo))
        adicionar_novamente = int(input("Deseja adicionar mais alguém? 1 - Sim ou 0 - Não: "))
        if(adicionar_novamente == 1):
            adicionar_jogador()
        else:
            clear()
            menu()
            
    if(x == 2):
        dream_team.append(Player("Hugo", 25, "Goleiro", 1, 99))
        dream_team.append(Player("André", 28, "Zagueiro", 2, 99))
        dream_team.append(Player("Garro", 22, "Meio-Campo", 3, 99))
        dream_team.append(Player("Yuri", 30, "Atacante", 4, 99))
        menu()  
        
    if(x == 3): menu()
       
    else:
        print("Valor incorreto!")
        adicionar_jogador()
        
def geral_dream(): #Função que geral a média do time
    geral = 0
    for x in dream_team:
        geral += x.get_atributos()
    if len(dream_team) > 0:
        return geral / len(dream_team)
    else:
        return 0
        
def lista_jogadores():
    y = 0
    clear()
    print("Dream Team: ",geral_dream())
    print("{:<4} {:<6} {:<7} {:<9} {:<7} {:<4}"
        .format("ID","Nome","Idade","Posição" , "Camisa", "Atributos") )
    for x in dream_team:
        print("{:<4} {:<6} {:<7} {:<10} {:<7} {:<4}"
              .format(y,
                      x.get_nome(),
                      x.get_idade(),
                      x.get_posicao(),
                      x.get_num(),
                      x.get_atributos()
                      ))
        y += 1
    menu()
    
def alterar_jogador():
    x = int(input("Digite o ID do jogador: "))
    opcao = int(input("Digite a opção que deseja alterar: \n1 - Nome \n2 - Idade \n3 - Posição \n4 - Atributos \n"))
    if(opcao == 1):
        valor = str(input("Escreva o novo nome: "))
        dream_team[x].set_nome(valor)
    elif(opcao == 2): 
        valor = int(input("Escreva o novo valor da idade: "))
        dream_team[x].set_idade(valor)
    elif(opcao == 3):
        valor = int(input("Escreva o valor da nova idade: 1 - Goleiro, 2 - Zagueiro, 3 - Meio-Campo, 4 - Atacante: \n"))
        if(valor == 1): valor = "Goleiro"
        elif(valor == 2): valor = "Zagueiro"
        elif(valor == 3): valor = "Meio-Campo"
        elif(valor == 4): valor = "Atacante"
        dream_team[x].set_posicao(valor)
    elif(opcao == 4): 
        valor = str(input("Escreva o novo valor dos atributos geral: "))
        dream_team[x].set_atributos(valor)
    else:
        print("Valor incorreto!")
    menu()
    
def remover_jogador():
    x = int(input("Digite o ID do jogador que deseja remover: "))
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
    x = int(input("Digite a opção desejada: \n1 - Adicionar jogador \n2 - Listar jogadores \n3 - Alterar Dados  \n4 - Remover jogador \n5 - Tela inicial \n6 - Sair\n"))
    if(x == 1): adicionar_jogador()
    elif(x == 2): lista_jogadores()
    elif(x == 3): alterar_jogador()
    elif(x == 4): remover_jogador()
    elif(x == 5): tela_inicial()
    elif(x == 6): exit()
    else:
        print("Valor incorreto!")
        menu()
        
        
def simular():
    clear()
    print("Jogo simulado!\n")
    print("Seu time: ")
    y = 0
    print("Dream Team: ",geral_time())
    print("{:<4} {:<6} {:<7} {:<9} {:<7} {:<4}"
        .format("ID","Nome","Idade","Posição" , "Camisa", "Atributos") )
    for x in dream_team:
        print("{:<4} {:<6} {:<7} {:<10} {:<7} {:<4}"
              .format(y,
                      x.get_nome(),
                      x.get_idade(),
                      x.get_posicao(),
                      x.get_num(),
                      x.get_atributos()
                      ))
        
        y += 1
    x = int(input("\nSelecione o time adversário: 1 - Time 1\n"))
    if(x == 1):    
        team_one
        escalacao()
    
        if(geral_time() > geral_adversario()):
            a = chances.randint(0,10)
            b = chances.randint(0,10)
            c = chances.randint(0,10)
            vitoria = a + b
            if(vitoria > c):
                placar_dreamteam = chances.randint(1,5)
                print("\nVitória! Placar: ",placar_dreamteam, "x 0")
                tela_inicial()
            else:
                placar_adversario = chances.randint(1,5)
                print("\nDerrota!Placar: 0 x ",placar_adversario)
                tela_inicial()
        else:
            a = chances.randint(0,10)
            b = chances.randint(0,10)
            if(a > b):
                placar_dreamteam = chances.randint(1,5)
                print("\nVitória! Placar: ",placar_dreamteam, "x 0")
                tela_inicial()   
                
            else:
                placar_adversario = chances.randint(1,5)
                print("\nDerrota! Placar: 0 x ",placar_adversario)
                tela_inicial()

def tela_inicial():
    print("Bem vindo Soccer-Game!\n")
    x = int(input("Digite a opção para iniciar o jogo: \n1 - Jogo simulado \n2 - Seu time \n3 - Sair\n"))
    if(x ==1): simular()
    elif(x == 2): menu()
    elif(x == 3): exit()
    else:
        print("Valor incorreto!")
        tela_inicial()
tela_inicial()      


    
