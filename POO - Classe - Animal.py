class Animal():
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print(f'O {self.nome} foi comer')
    def emitirSom(self):
        print(f'{self.nome} está emitido som')
class Gato(Animal):
    def __init__(self,nome, cor):
        super().__init__(nome,cor)
    def emitirSom(self):
        print(f'{self.nome} está miando')
class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)
    def emitirSom(self):
        print(f'{self.nome} está latindo')
class Vaca(Animal):
    def __init__(self,nome, cor):
        super().__init__(nome,cor)

A1=Cachorro("Mimosa","branca")
A1.comer()
A1.emitirSom()