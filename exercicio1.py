class Bola():
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

    def trocarcor(self,cor):
        self.cor = cor

    def mostrarcor(self):
        return self.cor


bola1 = Bola("Marrom", 16, "couro")
print(bola1.mostrarcor())

bola1.trocarcor("Branca")
print(bola1.mostrarcor())