# Exercício 10: Ordenação Complexa de Dicionários em uma Lista ↕️
# Dado uma lista de dicionários, ordene-a com base em uma ou mais chaves especificadas, em ordem ascendente ou descendente. 
# Os critérios de ordenação podem ser passados como uma lista de tuplas (chave, ordem), onde ordem é 'asc' ou 'desc'.

# Dica: Use a função sorted() com um lambda complexo para a chave key. Considere a ordem das chaves de ordenação.

# Exemplo:

# Python

# pessoas = [
#     {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'},
#     {'nome': 'Ana', 'idade': 25, 'cidade': 'Rio de Janeiro'},
#     {'nome': 'Pedro', 'idade': 30, 'cidade': 'Belo Horizonte'},
#     {'nome': 'Maria', 'idade': 25, 'cidade': 'São Paulo'}
# ]

# criterios_ordenacao1 = [('idade', 'asc'), ('nome', 'desc')] # Idade ascendente, depois nome descendente
# criterios_ordenacao2 = [('cidade', 'asc'), ('idade', 'asc')] # Cidade ascendente, depois idade ascendente

# Saída esperada para criterios_ordenacao1:
# [
#   {'nome': 'Maria', 'idade': 25, 'cidade': 'São Paulo'},
#   {'nome': 'Ana', 'idade': 25, 'cidade': 'Rio de Janeiro'},
#   {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'},
#   {'nome': 'Pedro', 'idade': 30, 'cidade': 'Belo Horizonte'}
# ]