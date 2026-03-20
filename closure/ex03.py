# Lista acumuladora
# make_appender() retorna função que recebe um item e o adiciona a uma lista interna, retornando a lista atualizada.

from typing import Callable

def make_appender() -> Callable[[str],list[str]]:
    lista: list[str] = []
    def interna(x: str):
        nonlocal lista
        lista.append(x)
        return lista
    return interna


adiciona = make_appender()
print(adiciona('oi'))
print(adiciona('Tudo bem'))
