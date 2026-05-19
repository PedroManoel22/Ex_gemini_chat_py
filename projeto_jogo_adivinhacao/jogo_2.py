from random import randint
from typing import Any, Dict


def formatar_pontuacao(pontos: int) -> str:
    """Formata a pontuação final do jogador em uma string amigável.

    Recebe um valor inteiro representando a pontuação obtida pelo
    jogador durante a partida e retorna uma mensagem personalizada
    pronta para ser exibida na tela.

    Args:
        pontos (int): A quantidade total de pontos acumulados pelo jogador.

    Returns:
        str: A mensagem de pontuação formatada.

    Raises:
        ValueError: Se a pontuação fornecida for negativa.
    """

    return f"A sua pontuação final é {pontos} pontos"


DEBUG = False
TENTATIVAS = 6
TOTAL_RODADAS = TENTATIVAS - 1
PONTUACAO_MAXIMA = 100
MENSAGENS: Dict[str, Dict[str, Any]] = {
    "DEFAULT": {
        "SAUDACAO": "Escolhi um número entre 0 e 10. Tente adivinhar",
        "VITORIA": "Parabéns!! Você acertou",
        "DERROTA": "Que pena!! Você não acertou",
        "INPUT_JOGADOR": "Digite um número entre 0 e 10: ",
        "NOVA_PARTIDA": "Gostaria de jogar novamente? (1-Sim; 2-Não) ",
        "ENCERRAMENTO": "Até a próxima!!!",
        "PONTUACAO": formatar_pontuacao,
    },
    "ERRO": {
        "TENTATIVA_INVALIDA": "ERRO: São permitidos apenas números inteiros entre 0 e 10",
        "NOVA_PARTIDA_INVALIDA": "ERRO: São permitidas apenas as opções: 1-Sim ou 2-Não",
    },
}


def mensagem_tela(
    mensagem: str, pontuacao: int | None = None, mensagem_resultado: str | None = None
) -> None:
    TAMANHO_LINHA = 70
    ALINHAMENTO = f"^{TAMANHO_LINHA}"
    print(f"{'-' * TAMANHO_LINHA}")
    print(f"{mensagem.upper():{ALINHAMENTO}}")
    if mensagem_resultado is not None:
        print(f"{mensagem_resultado.upper():{ALINHAMENTO}}")
    print(f"{'-' * TAMANHO_LINHA}")


def get_input_jogador(mensagem: str) -> str:
    return str(input(mensagem))


def valida_tentativa_jogador(numero: str) -> bool:
    try:
        int(numero)
    except ValueError:
        return False
    return numero in range(11)


def valida_opcao_jogador(input: str) -> bool:
    try:
        int(input)
    except ValueError:
        return False
    return int(input) in range(3)


def nova_partida(input: str) -> bool:
    # 1 - Sim; 2 - Não
    return input == "1"


def verifica_acerto(numero_jogador: str, numero_computador: str) -> bool:
    return numero_jogador == numero_computador


def calcula_pontuacao(rodada: int, tentativas: int, pontuacao_maxima: int = 100) -> int:
    if rodada == 1:
        return pontuacao_maxima
    else:
        return int(
            pontuacao_maxima - (pontuacao_maxima / (tentativas - 1)) * (rodada - 1)
        )


while True:
    numero_computador = str(randint(0, 10))
    numero_jogador = None
    rodada = 1
    mensagem_tela(MENSAGENS["DEFAULT"]["SAUDACAO"])

    if DEBUG:
        print(numero_computador)

    while rodada < TENTATIVAS:
        print(f"Rodada {rodada}/{TOTAL_RODADAS}")
        numero_jogador = get_input_jogador(MENSAGENS["DEFAULT"]["INPUT_JOGADOR"])

        while not valida_tentativa_jogador(numero_jogador):
            mensagem_tela(MENSAGENS["ERRO"]["TENTATIVA_INVALIDA"])
            print(f"Rodada {rodada}/{TOTAL_RODADAS}")
            numero_jogador = get_input_jogador(MENSAGENS["DEFAULT"]["INPUT_JOGADOR"])

        if verifica_acerto(numero_jogador, numero_computador):
            break

        rodada += 1

    pontos = calcula_pontuacao(rodada, TENTATIVAS, PONTUACAO_MAXIMA)
    resultado = MENSAGENS["DEFAULT"]["PONTUACAO"]

    if rodada < TENTATIVAS:
        mensagem_tela(
            MENSAGENS["DEFAULT"]["VITORIA"],
            pontuacao=pontos,
            mensagem_resultado=resultado(pontos),
        )
    else:
        mensagem_tela(
            MENSAGENS["DEFAULT"]["DERROTA"],
            pontuacao=pontos,
            mensagem_resultado=resultado(pontos),
        )

    opcao = get_input_jogador(MENSAGENS["DEFAULT"]["NOVA_PARTIDA"])
    while not valida_opcao_jogador(opcao):
        mensagem_tela(MENSAGENS["ERRO"]["NOVA_PARTIDA_INVALIDA"])
        opcao = get_input_jogador(MENSAGENS["DEFAULT"]["NOVA_PARTIDA"])

    if not nova_partida(opcao):
        mensagem_tela(MENSAGENS["DEFAULT"]["ENCERRAMENTO"])
        break
