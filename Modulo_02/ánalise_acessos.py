registros_acessos = []
usuarios_acesso = set()
tempo_total = 0

while True:
    usuario = input("Digite o nome de usuário (ou 'parar' para sair): ").strip()
    if usuario.lower() == "parar":
        break

    print("Selecione o status:")
    print("1 - Sucesso")
    print("2 - Falha")
    
    try:
        opcao = int(input("Opção: "))
        if opcao == 1:
            status = "sucesso"
        elif opcao == 2:
            status = "falha"
        else:
            print("!!! Opção invalida, registro descartado.\n")
            continue
    except ValueError:
        print("!!! Entrada inválida, registro descartado.\n")
        continue

    try:
        duracao = int(input("Digite a duração da sessão em minutos: "))
        if duracao < 0:
            print("!!! Duração nao pode ser negativa, registro descartado.\n")
            continue
    except ValueError:
        print("!!! Duração inválida, registro descartado.\n")
        continue

    tupla = (usuario, status, duracao)
    registros_acessos.append(tupla)
    
    if status == "sucesso":
        usuarios_acesso.add(usuario)
        tempo_total += duracao

    print("Registro adicionado!\n")

print("\n--- RESULTADOS ---")
print("Registros de acessos:")
print(registros_acessos)

print("\nUsuarios com acesso bem-sucedido:")
print(usuarios_acesso)

print(f"\nTempo total das sessões bem-sucedidas: {tempo_total} minutos")