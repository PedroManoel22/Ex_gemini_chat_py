# Exercício 5: Agrupamento Multi-Nível (Pivotamento) 📊
# Aprimore o Exercício 5 original. Crie uma função que agrupe uma lista de dicionários por múltiplas chaves, 
# retornando um dicionário aninhado que reflete essa hierarquia de agrupamento.

# Dica: Pense em recursão ou em iterar sobre as chaves de agrupamento, construindo o dicionário camada por camada.

# Exemplo:

# Python

# transacoes = [
#     {'data': '2023-01-01', 'tipo': 'venda', 'produto': 'A', 'valor': 100},
#     {'data': '2023-01-01', 'tipo': 'devolução', 'produto': 'B', 'valor': 50},
#     {'data': '2023-01-02', 'tipo': 'venda', 'produto': 'A', 'valor': 120},
#     {'data': '2023-02-01', 'tipo': 'venda', 'produto': 'C', 'valor': 200}
# ]
# chaves_agrupamento = ['data', 'tipo']
# Saída esperada:
# {
#   '2023-01-01': {
#     'venda': [{'data': '2023-01-01', 'tipo': 'venda', 'produto': 'A', 'valor': 100}],
#     'devolução': [{'data': '2023-01-01', 'tipo': 'devolução', 'produto': 'B', 'valor': 50}]
#   },
#   '2023-01-02': {
#     'venda': [{'data': '2023-01-02', 'tipo': 'venda', 'produto': 'A', 'valor': 120}]
#   },
#   '2023-02-01': {
#     'venda': [{'data': '2023-02-01', 'tipo': 'venda', 'produto': 'C', 'valor': 200}]
#   }
# }