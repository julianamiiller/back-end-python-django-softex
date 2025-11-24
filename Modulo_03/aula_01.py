class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome  
        self.idade = idade

    # Getter para o nome
    def get_nome(self):
        return self._nome


    from pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)  #
        self.matricula = matricula
        self.notas = {}  

    def adicionar_nota(self, materia, nota):
        if materia not in self.notas:
            self.notas[materia] = []
        self.notas[materia].append(nota)


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.estudantes = []  #

    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)

    def mostrar_relatorio(self):
        print(f"\nRelatório da Escola {self.nome}:")
        for estudante in self.estudantes:
            print(f"\nNome: {estudante.get_nome()}")
            print(f"Idade: {estudante.idade}")
            print(f"Matrícula: {estudante.matricula}")
            for materia, notas in estudante.notas.items():
                print(f"  {materia}: {notas}")

