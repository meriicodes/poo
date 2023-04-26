class Quadrado():
    def __init__(self, lado):
        self.lado = lado

    def setlado(self, lado):
        self.lado = lado

    def getlado(self):
        return self.lado
    
    def area(self):
        return self.lado * self.lado

q = Quadrado(5)
print(q.area())
