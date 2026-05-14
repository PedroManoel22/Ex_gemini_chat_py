# Exercício 7: Classe Temporizador (Dunder __enter__ e __exit__ - Context Manager)
# Crie a classe Temporizador para medir o tempo de execução de um bloco de código usando a instrução with.

# Método __enter__(self):

# Armazena o tempo de início (time.time()).

# Retorna a si mesma (ou um valor, se necessário).

# Método __exit__(self, exc_type, exc_val, exc_tb):

# Calcula o tempo decorrido.

# Imprime o tempo de execução.

# Retorna None (ou True se quiser suprimir exceções).

# Teste Pythônico:

# Python
# with Temporizador():
#     # Código demorado aqui, ex: time.sleep(1)
#     pass

from time import sleep, time
from types import TracebackType
from typing import Optional, Type


class Temporizador:
    def __enter__(self):
        self.inicio = time()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        tb: Optional[TracebackType],
    ):
        self.fim = time()
        tempo_total = self.fim - self.inicio
        print(f"Tempo de execução: {tempo_total:.2f} segundos")


if __name__ == "__main__":
    print("Iniciando")
    with Temporizador():
        sleep(1.5)
        print("Trabalhando...")
    print("Bloco finalizado")
