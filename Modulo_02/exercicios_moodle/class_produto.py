class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = float(preco)

    def __repr__(self):
        return f"{self.nome} custa R$ {self.preco:.2f}"

caderno = Produto("Caderno", 15.50)
caneta = Produto("Caneta", 3.00)

print(caderno)
print(caneta)