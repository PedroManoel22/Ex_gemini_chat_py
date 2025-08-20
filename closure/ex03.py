# Lista acumuladora
# make_appender() retorna função que recebe um item e o adiciona a uma lista interna, retornando a lista atualizada.

def make_appender():
    lista = []
    def interna(x):
        nonlocal lista
        lista.append(x)
        return lista
    return interna
adiciona = make_appender()
print(adiciona('oi'))
print(adiciona('Tudo bem'))
