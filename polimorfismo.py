class Pessoa1:   

    def se_apresentar(self):
        print('Oi, sou a Pessoa 1')

class Pessoa2(Pessoa1):

    def __init__(self):
        super().__init__()

    def se_apresentar(self):
        print('Estou alternando este método')

class Pessoa3(Pessoa2):

    def __init__(self):
        super().__init__()

Alicia = Pessoa1()
Alicia.se_apresentar()

Bianca = Pessoa2()
Bianca.se_apresentar()
