class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.nivel_combustivel = 0.0

    def abastecer(self, litros):
        self.nivel_combustivel += float(litros)
        print(f"{self.modelo} abastecido com {litros} L. Combustível: {self.nivel_combustivel:.2f} L")

    def dirigir(self, km):
        consumo = km * 0.1
        if consumo <= self.nivel_combustivel:
            self.nivel_combustivel -= consumo
            print(f"{self.modelo} andou {km} km. Restam {self.nivel_combustivel:.2f} L")
        else:
            print(f"{self.modelo} não tem combustível suficiente para {km} km.")

meu_carro = Carro("Gol")
meu_carro.abastecer(5)
meu_carro.dirigir(30)
meu_carro.dirigir(40)