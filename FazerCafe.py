# Variáveis
aguaPanela = True
fogoAceso = True
ferver = False

# Solicitar quantidade de água
agua = float(input("Qual a quantidade de água quer usar? "))

# Verificação da quantidade de água
if agua <= 0:
    print("A quantidade de água precisa ser maior que zero.")
elif agua < 0.5:
    print("A quantidade de água é insuficiente para fazer café.")
else:
    print("Essa quantidade é boa, continuando o processo...")

    # Enquanto a água não estiver fervendo
    while not ferver:
        print("Colocando café no coador...")
        print("Abrindo a garrafa de café...")

        if aguaPanela and fogoAceso:
            print("A água ainda não ferveu. Esperando...")
            # Simulando que a água ferve após algum tempo
            ferver = True  # Aqui estamos dizendo que a água finalmente ferveu
        else:
            print("A água já ferveu. Apagando o fogo...")
            fogoAceso = False

    # Quando a água estiver fervida
    if ferver:
        print("Despejando a água no coador...")
        print("Esperando o café terminar de ser coado...")
        print("Colocando o coador para lavar...")
        print("Fechando a garrafa de café.")

    print("Fim do processo de fazer café.")
