class Pessoa:
    def __init__(self, nome, profissao, idade):
        self.nome = nome
        self.profissao = profissao
        self.idade = idade

    def cumprimentar(self):
        print("Oi, meu nome é", self.nome)

    def aniversario(self):
        self.idade += 1
        print("Agora você tem", self.idade ,"anos")

    def mudar_profissao(self, nova_profissao):
        self.profissao = nova_profissao
        print("Sua nova profissão é: ", self.profissao)

p = Pessoa("Maria", "Psicóloga", 25)
p.cumprimentar()