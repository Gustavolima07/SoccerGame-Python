from player import *

team_one = []
team_one.append(Player("Jorge", 25, "Atacante", 10, 90))
team_one.append(Player("Carlos", 23, "Zagueiro", 5, 85))
team_one.append(Player("Lucas", 21, "Meio-Campo", 8, 80))
team_one.append(Player("Pedro", 22, "Goleiro", 1, 95))
    
def geral_time(): #Função que geral a média do time
    geral = 0
    for x in team_one:
        geral += x.get_atributos()
    if len(team_one) > 0:
        return geral / len(team_one)
    else:
        return 0
            
    
def escalacao():
    y = 0
    print("Time 1: ",geral_time())
    print("{:<4} {:<6} {:<7} {:<9} {:<7} {:<4}"
        .format("ID","Nome","Idade","Posição" , "Camisa", "Atributos") )
    for x in team_one:
        print("{:<4} {:<6} {:<7} {:<10} {:<7} {:<4}"
              .format(y,
                      x.get_nome(),
                      x.get_idade(),
                      x.get_posicao(),
                      x.get_num(),
                      x.get_atributos()
                      ))
        y += 1
escalacao()
