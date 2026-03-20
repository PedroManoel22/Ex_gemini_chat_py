# Fábrica de multiplicadores
# Crie make_multiplier(n) que retorna uma função para multiplicar seu argumento por n. Use e teste para n=2, n=5.
from typing import Callable

def make_multiplier(n: int) -> Callable[[int], int ] :
    # Essa é a função externa. Ela define o multiplicador (n)
    def multiplier(x: int) -> int:
        # Esta é a função interna (closure), que usa 'n' do escopo externo
        return n * x
    return multiplier  # Retorna a função interna como closure

dobro = make_multiplier(2)

print(dobro(10))