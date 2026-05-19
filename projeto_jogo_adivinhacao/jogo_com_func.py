import random


def get_valid_guess() -> int:
    """Pede um palpite válido ao usuário e o retorna como um inteiro."""
    while True:
        try:
            guess_str = input(
                "Estou pensando em um número de 0 a 10, tente adivinhar: "
            )
            guess_int = int(guess_str)

            if 0 <= guess_int <= 10:
                return guess_int
            else:
                print("Por favor, digite um número entre 0 e 10.")

        except ValueError:
            print("Por favor, digite um número inteiro!")


def play_game() -> None:
    """Lógica principal do jogo de adivinhação."""
    num_computador = random.randint(0, 10)

    # Dicionário para gerenciar a pontuação de forma mais limpa
    pontuacoes = {1: 100, 2: 70, 3: 50, 4: 30, 5: 10}
    max_tentativas = 5

    print(f"O computador pensou em um número. Você tem {max_tentativas} tentativas.")

    for tentativa in range(1, max_tentativas + 2):
        if tentativa > max_tentativas:
            print("\nVocê não acertou desta vez. Suas tentativas acabaram.")
            print(f"O número que pensei foi {num_computador}.")
            return

        print(f"\n{tentativa}ª tentativa:")

        palpite = get_valid_guess()

        if palpite == num_computador:
            pontos = pontuacoes.get(tentativa, 0)
            print(f"\nParabéns! Você acertou na {tentativa}ª tentativa.")
            print(f"Sua pontuação foi de {pontos} pontos.")
            return


def main() -> None:
    """Função principal que gerencia o fluxo do jogo."""
    while True:
        play_game()

        opcao = input("\nDeseja jogar novamente? [S/N]: ").upper().strip()
        if opcao != "S":
            break

    print("\nObrigado por jogar! Volte sempre! 👋")


if __name__ == "__main__":
    main()
