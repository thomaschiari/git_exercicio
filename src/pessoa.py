class Pessoa:
    
    def __init__(self, idade, nome):
        self.idade = idade
        self.nome = nome
    
    def falar(self):
        return f'Oi! Meu nome é {self.nome}.'