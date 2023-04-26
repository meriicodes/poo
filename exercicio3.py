class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def setbase(self,base):
        self.base = base

    def setaltura(self,altura):
        self.largura = altura

    def getBase(self):
        return self.base
    
    def getAltura(self):
        return self.altura
    
    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return (2 * self.base) + (2 * self.altura)
    
base = float(input('valor da base: '))
alt = float(input('valor da altura: '))

r = Retangulo(base, alt)
print('a area é: ', r.area())
print("o perimetro é:", r.perimetro())