# Exercício 4: Filtragem Dinâmica de Lista de Dicionários 🧩
# Crie uma função que receba uma lista de dicionários (registros) e um dicionário de critérios de filtro. 
# Os critérios de filtro podem especificar igualdade ('key': 'value') ou operadores de comparação ('key': {'op': 'gt', 'value': 10} para maior que, 'op': 'lt' para menor que, 'op': 'ge' para maior ou igual, 'op': 'le' para menor ou igual). A função deve retornar uma nova lista contendo apenas os dicionários que satisfazem todos os critérios.

# Dica: Você precisará de lógica condicional para cada tipo de operador e para cada registro.

# Exemplo:

# Python

# produtos = [
#     {'nome': 'Laptop', 'categoria': 'Eletrônicos', 'preco': 1200, 'estoque': 50},
#     {'nome': 'Mouse', 'categoria': 'Eletrônicos', 'preco': 25, 'estoque': 200},
#     {'nome': 'Teclado', 'categoria': 'Eletrônicos', 'preco': 75, 'estoque': 100},
#     {'nome': 'Mesa', 'categoria': 'Móveis', 'preco': 300, 'estoque': 20}
# ]

# criterios1 = {
#     'categoria': 'Eletrônicos',
#     'preco': {'op': 'lt', 'value': 100}
# }
# criterios2 = {
#     'estoque': {'op': 'ge', 'value': 100}
# }
# Saída esperada para criterios1:
# [
#   {'nome': 'Mouse', 'categoria': 'Eletrônicos', 'preco': 25, 'estoque': 200},
#   {'nome': 'Teclado', 'categoria': 'Eletrônicos', 'preco': 75, 'estoque': 100}
# ]
# Saída esperada para criterios2:
# [
#   {'nome': 'Mouse', 'categoria': 'Eletrônicos', 'preco': 25, 'estoque': 200},
#   {'nome': 'Teclado', 'categoria': 'Eletrônicos', 'preco': 75, 'estoque': 100}
# ]