# Exercício 2: Fusão Profunda de Dicionários 🔄🔄
# Estenda o exercício de fusão. Crie uma função que receba dois dicionários. Se houver chaves em comum e ambos os valores para essa chave forem dicionários,
#  a função deve fundir esses dicionários aninhados recursivamente. Caso contrário (se não forem ambos dicionários), 
# o valor do segundo dicionário deve sobrescrever o valor do primeiro.

# Dica: Recursão novamente! E verifique o tipo dos valores.

# Exemplo:

# Python

# dict_a = {
#     'config': {'timeout': 10, 'retries': 3},
#     'user': {'name': 'Alice', 'role': 'admin'},
#     'status': 'active'
# }
# dict_b = {
#     'config': {'retries': 5, 'log_level': 'DEBUG'},
#     'user': {'name': 'Bob'},
#     'version': '1.0'
# }
# Saída esperada:
# {
#   'config': {'timeout': 10, 'retries': 5, 'log_level': 'DEBUG'},
#   'user': {'name': 'Bob', 'role': 'admin'}, # Bob sobrescreve Alice, mas 'role' é mantido
#   'status': 'active',
#   'version': '1.0'
# }