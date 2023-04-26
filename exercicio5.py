class Conta:
    def __init__(self, numero, nome, saldo ):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterarnome(self,nome):
        self.nome = nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
       if (self.saldo >= valor):
           self.saldo -= valor

m = Conta(123, "Maria", 3000)
m.deposito(500)
print(vars(m))