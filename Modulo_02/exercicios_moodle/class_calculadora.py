class Retangulo:
    def __init__(self, base, altura):
        self.base = float(base)
        self.altura = float(altura)

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

ret = Retangulo(5, 3)
print("Área do retângulo:", ret.area())
print("Perímetro do retângulo:", ret.perimetro())
