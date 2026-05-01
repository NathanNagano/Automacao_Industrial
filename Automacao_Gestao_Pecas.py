pecas_aprovadas = []
pecas_reprovadas = []
caixas = []
caixa_atual = []


def validar_peca(peso, cor, comprimento):
    motivos = []

    if not (95 <= peso <= 105):
        motivos.append("Peso fora do padrão")

    if cor.lower() not in ["azul", "verde"]:
        motivos.append("Cor inválida")

    if not (10 <= comprimento <= 20):
        motivos.append("Comprimento fora do padrão")

    return motivos


def armazenar_caixa(peca):
    global caixa_atual

    caixa_atual.append(peca)

    if len(caixa_atual) == 10:
        caixas.append(caixa_atual.copy())
        caixa_atual.clear()


def cadastrar_peca():
    try:
        id_peca = input("ID da peça: ")
        peso = float(input("Peso (g): "))
        cor = input("Cor: ")
        comprimento = float(input("Comprimento (cm): "))

        peca = {
            "id": id_peca,
            "peso": peso,
            "cor": cor,
            "comprimento": comprimento
        }

        motivos = validar_peca(peso, cor, comprimento)

        if len(motivos) == 0:
            pecas_aprovadas.append(peca)
            armazenar_caixa(peca)
            print("Peça APROVADA.")
        else:
            peca["motivos"] = motivos
            pecas_reprovadas.append(peca)
            print("Peça REPROVADA.")

    except:
        print("Entrada inválida.")


def listar_pecas():
    print("\n--- APROVADAS ---")
    for p in pecas_aprovadas:
        print(p)

    print("\n--- REPROVADAS ---")
    for p in pecas_reprovadas:
        print(p)


def remover_peca():
    id_remover = input("Digite o ID da peça: ")

    for lista in [pecas_aprovadas, pecas_reprovadas]:
        for p in lista:
            if p["id"] == id_remover:
                lista.remove(p)
                print("Peça removida.")
                return

    print("Peça não encontrada.")


def listar_caixas():
    print("\n--- CAIXAS FECHADAS ---")
    for i, caixa in enumerate(caixas, start=1):
        print(f"Caixa {i}: {len(caixa)} peças")


def gerar_relatorio():
    print("\n===== RELATÓRIO FINAL =====")
    print("Total aprovadas:", len(pecas_aprovadas))
    print("Total reprovadas:", len(pecas_reprovadas))
    print("Caixas fechadas:", len(caixas))

    print("\nMotivos de reprovação:")
    for p in pecas_reprovadas:
        print(f"ID {p['id']} -> {', '.join(p['motivos'])}")


def menu():
    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar nova peça")
        print("2 - Listar peças aprovadas/reprovadas")
        print("3 - Remover peça cadastrada")
        print("4 - Listar caixas fechadas")
        print("5 - Gerar relatório final")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_peca()
        elif op == "2":
            listar_pecas()
        elif op == "3":
            remover_peca()
        elif op == "4":
            listar_caixas()
        elif op == "5":
            gerar_relatorio()
        elif op == "0":
            break
        else:
            print("Opção inválida.")


menu()