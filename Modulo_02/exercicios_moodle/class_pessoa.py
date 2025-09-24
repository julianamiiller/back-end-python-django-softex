class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = int(idade)

    def apresentar(self):
        print(f"Olá, eu sou {self.nome} e tenho {self.idade} anos.")

joao = Pessoa("João", 25)
maria = Pessoa("Maria", 30)

print("João -", joao.nome, joao.idade)
print("Maria -", maria.nome, maria.idade)

joao.apresentar()
maria.apresentar()
