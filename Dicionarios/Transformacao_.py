#Exercício 7: Transformação de Lista de Tuplas para Dicionário ↔️
#Crie uma função que receba uma lista de tuplas, onde cada tupla tem dois elementos (chave, valor), e retorne um dicionário a partir dessa lista.
#Exemplo:

#pares = [('nome', 'Carlos'), ('idade', 30), ('cidade', 'São Paulo')]
# Saída esperada: {'nome': 'Carlos', 'idade': 30, 'cidade': 'São Paulo'}


def transformar(x):
    return dict(x)


pares = [('nome', 'Carlos'), ('idade', 30), ('cidade', 'São Paulo')]
print(transformar(pares))
