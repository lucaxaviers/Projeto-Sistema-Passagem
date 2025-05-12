voos = {}
passageiros = {}
opcaomenu = 0

while opcaomenu != 7:
    print("\nSeja Bem-Vindo ao Sistema de Passagem Aérea")
    print("Menu de Opções:")
    print("1 - Cadastrar Voo")
    print("2 - Consultar Voos")
    print("3 - Voo com menos escalas")
    print("4 - Listar Passageiros de um Voo")
    print("5 - Vender Passagem")
    print("6 - Cancelar Passagem")
    print("7 - Sair do Sistema")

    opcaomenu = int(input("Digite a opção desejada: "))

    if opcaomenu == 1:
        print("Cadastro de Voo")
        codigovoo = input("Digite o código do voo: ")

        if codigovoo in voos:
            print("Erro: esse código de voo já foi cadastrado.")
        else:
            origem = input("Digite a cidade de origem: ")
            destino = input("Digite a cidade de destino: ")
            escalas = int(input("Digite o número de escalas: "))
            preco = float(input("Digite o preço da passagem: "))
            lugaresdisp = int(input("Digite o número de lugares disponíveis: "))

            voos[codigovoo] = {
                "origem": origem,
                "destino": destino,
                "escalas": escalas,
                "preco": preco,
                "lugares_disponiveis": lugaresdisp
            }

            passageiros[codigovoo] = []  
            print(f"Voo {codigovoo} cadastrado com sucesso!")

    elif opcaomenu == 2:
        print("Consulta de Voos")
        print("Como você gostaria de consultar os voos?")
        print("1 - Pelo código do voo")
        print("2 - Por cidade de origem")
        print("3 - Por cidade de destino")
        print("4 - Voltar ao menu principal")
        consultaopcao = int(input("Digite a opção desejada: "))

        if consultaopcao == 1:
            codigovoo = input("Digite o código do voo: ")
            if codigovoo in voos:
                voo = voos[codigovoo]
                print(f"\nInformações do Voo {codigovoo}:")
                print(f"Origem: {voo['origem']}")
                print(f"Destino: {voo['destino']}")
                print(f"Escalas: {voo['escalas']}")
                print(f"Preço: R${voo['preco']:.2f}")
                print(f"Lugares disponíveis: {voo['lugares_disponiveis']}")
            else:
                print("Erro: voo não encontrado.")

        elif consultaopcao == 2:
            origem = input("Digite a cidade de origem: ")
            voos_encontrados = [codigo for codigo, voo in voos.items() if voo['origem'].lower() == origem.lower()]
            if voos_encontrados:
                for codigo in voos_encontrados:
                    voo = voos[codigo]
                    print(f"Código do Voo: {codigo}, Destino: {voo['destino']}, Preço: R${voo['preco']:.2f}")
            else:
                print("Erro: nenhum voo encontrado para essa cidade de origem.")

        elif consultaopcao == 3:
            destino = input("Digite a cidade de destino: ")
            voos_encontrados = [codigo for codigo, voo in voos.items() if voo['destino'].lower() == destino.lower()]
            if voos_encontrados:
                for codigo in voos_encontrados:
                    voo = voos[codigo]
                    print(f"Código do Voo: {codigo}, Origem: {voo['origem']}, Preço: R${voo['preco']:.2f}")
            else:
                print("Erro: nenhum voo encontrado para essa cidade de destino.")

        elif consultaopcao == 4:
            print("Voltando ao menu principal...")

    elif opcaomenu == 3:
        origem = input("Digite a cidade de origem: ")
        destino = input("Digite a cidade de destino: ")

        menor_escalas = float('inf')
        melhor_codigo = ""

        for codigo, voo in voos.items():
            if voo["origem"].lower() == origem.lower() and voo["destino"].lower() == destino.lower():
                if voo["escalas"] < menor_escalas:
                    menor_escalas = voo["escalas"]
                    melhor_codigo = codigo

        if melhor_codigo:
            print(f"\nO voo com menos escalas é o Voo de código: {melhor_codigo}")
            print(f"Escalas: {voos[melhor_codigo]['escalas']}")
            print(f"Preço: R${voos[melhor_codigo]['preco']:.2f}")
        else:
            print("Nenhum voo encontrado com essa origem e destino.")
