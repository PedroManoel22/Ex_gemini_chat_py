# Exercício 7: Categorização de Itens Baseada em Tags 🏷️
# Você tem uma lista de dicionários, onde cada dicionário representa um item e possui uma chave 'tags' que é uma lista de strings. 
# Crie uma função que, dada essa lista de itens e um set de tags_de_interesse, retorne um dicionário. As chaves do dicionário de saída devem ser as tags_de_interesse, 
# e os valores devem ser sets de nomes de itens que possuem aquela tag.

# Exemplo:

# Python

# itens = [
#     {'nome': 'Laptop', 'tags': ['eletronico', 'portatil', 'tecnologia']},
#     {'nome': 'Livro', 'tags': ['educacao', 'leitura', 'ficcao']},
#     {'nome': 'Mouse', 'tags': ['eletronico', 'periferico']},
#     {'nome': 'Teclado', 'tags': ['eletronico', 'periferico', 'acessorio']}
# ]
# tags_de_interesse = {'eletronico', 'leitura', 'portatil'}

# Saída esperada (aproximada):
# {
#   'eletronico': {'Laptop', 'Mouse', 'Teclado'},
#   'leitura': {'Livro'},
#   'portatil': {'Laptop'}
# }
