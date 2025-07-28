# Exercício 9: Remoção de Chaves Múltiplas com Profundidade 🗑️
# Crie uma função que receba um dicionário (que pode ser aninhado) e uma lista de chaves a serem removidas. 
# A função deve remover todas as ocorrências dessas chaves em qualquer nível do dicionário.

# Dica: Recursão será sua amiga novamente. Tome cuidado ao modificar dicionários enquanto itera sobre eles. 
# Uma boa prática é criar uma cópia ou acumular as chaves a serem removidas antes de agir.

# Exemplo:

# Python

# config = {
#     'db': {
#         'host': 'localhost',
#         'port': 5432,
#         'user': 'admin',
#         'password': 'secret_password'
#     },
#     'api_keys': {
#         'google': 'abc123xyz',
#         'stripe': 'def456uvw'
#     },
#     'log_level': 'INFO',
#     'user': {
#         'password': 'user_pass',
#         'name': 'guest'
#     }
# }
# chaves_sensitivas = ['password', 'api_keys']
# Saída esperada (sem as chaves 'password' e 'api_keys'):
# {
#   'db': {
#     'host': 'localhost',
#     'port': 5432,
#     'user': 'admin'
#   },
#   'log_level': 'INFO',
#   'user': {
#     'name': 'guest'
#   }
# }