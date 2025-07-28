#Exercício 1: Achatamento de Dicionário Aninhado 🌲➡️🌳
# Crie uma função que receba um dicionário aninhado (com dicionários dentro de dicionários) e o transforme em um dicionário "achatado" (flat),
# onde todas as chaves são concatenadas com um separador (ex: _) para indicar o caminho.

# Dica: Pense em recursão!

# Exemplo:

# Python

# dados_aninhados = {
#     'user': {
#         'profile': {
#             'name': 'Alice',
#             'age': 30
#         },
#         'contact': {
#             'email': 'alice@example.com',
#             'phone': '123-456-7890'
#         }
#     },
#     'preferences': {
#         'theme': 'dark'
#     }
# }
# Saída esperada:
# {
#   'user_profile_name': 'Alice',
#   'user_profile_age': 30,
#   'user_contact_email': 'alice@example.com',
#   'user_contact_phone': '123-456-7890',
#   'preferences_theme': 'dark'
# }
    