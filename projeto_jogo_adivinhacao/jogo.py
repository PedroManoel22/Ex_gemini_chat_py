from random import randint

while True:  # loop para saber se o usuário quer continuar ou não
    num_computador = randint(0, 10)
    count = 1
    pontos = 0

    while (
        True
    ):  # loop para contabilizar as 5 jogadas legais (com números inteiros de 0 a 10)
        print(f"{count}° tentativa")

        try:
            num_usuario = input(
                "Estou pensando em um número de 0 a 10, tente advinhar: "
            )
            num_usuario = int(num_usuario)

        except ValueError:
            print("Por favor coloque um número inteiro!")
            continue

        if num_usuario > 10 or num_usuario < 0:
            print("Por favor coloque um número entre 0 a 10")
            continue

        if num_usuario == num_computador:
            if count == 1:
                pontos = 100

            elif count == 2:
                pontos = 70

            elif count == 3:
                pontos = 50

            elif count == 4:
                pontos = 30

            elif count == 5:
                pontos = 10

            break

        if 0 <= num_usuario <= 10:
            count += 1

        elif count == 6:
            pontos = 0
            break

    if pontos == 0:
        print("Você não acertou nenhuma")
        print(f"Pontuação: {pontos}")
        print(f"O númeor que pensei foi {num_computador}")

    else:
        print(f"Voce acertou! de {count}° vez")
        print(f"Pontuação: {pontos}")

    opcao = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]

    if opcao == "N":
        break

print("Obrigado por jogar🥰, volte sempre!")
