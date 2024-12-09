class Player: #Classe que representa um jogador de futebol
    def __init__(self, nome,idade , posicao, atributos):
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
        self.atributos = atributos
        
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome
        
    def get_idade(self):
        return self.idade
    
    def set_idade(self, idade):
        self.idade = idade
        
    def get_posicao(self):
        return self.posicao
    
    def set_posicao(self, posicao):
        self.posicao = posicao
        
    def get_atributos(self):
        return self.atributos
    
    def set_atributos(self, atributos):
        self.atributos = atributos
        
    