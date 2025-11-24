class Usuario:
    def __init__(self, nome, apelido):
        self.nome = nome
        self.apelido = apelido


class Post:
    def __init__(self, texto, dono):
        self.texto = texto
        self.dono = dono


class RedeSocial:
    def __init__(self):
        self.banco_de_posts = []

    def criar_post(self, texto, usuario_logado):
        novo_post = Post(texto, usuario_logado)
        self.banco_de_posts.append(novo_post)
        print(f"  Post criado por {usuario_logado.apelido}!")

    def ver_meu_perfil(self, usuario_logado):
        print(f"\n   --- PERFIL DE {usuario_logado.nome.upper()} ---")
        print(f"   Usuário: {usuario_logado.apelido}")
        print("-" * 35)

        encontrou = False

        for post in self.banco_de_posts:
            if post.dono == usuario_logado:
                print(f"   {post.texto}  (Por: {post.dono.apelido})")
                encontrou = True

        if not encontrou:
            print("   (Nenhum post disponível)")

        print("-" * 35 + "\n")


usuario_principal = Usuario("Marina Fortes", "@marina_fortesfit")
usuario_secundario = Usuario("Rafa Treinador", "@coach_rafa")

rede = RedeSocial()

rede.criar_post("Treino de pernas concluído: se eu sentar agora, só levanto amanhã.", usuario_principal)
rede.criar_post("Atleta que não come direito vira estatística. Bora pra dieta!", usuario_secundario)
rede.criar_post("PR no agachamento hoje! A vida é pesada, mas eu também sou.", usuario_principal)
rede.criar_post("Cardio feito. Sofri? Sim. Valeu a pena? Ainda decidindo.", usuario_principal)
rede.criar_post("Turma das 6h mandou muito! Orgulho dos meus monstros!", usuario_secundario)

rede.ver_meu_perfil(usuario_principal)
