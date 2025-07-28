# Exercício 3: Consulta de Caminho em Dicionário Aninhado 🗺️
# Desenvolva uma função que receba um dicionário aninhado e uma lista de chaves representando um "caminho". 
# A função deve retornar o valor encontrado no final desse caminho. Se qualquer parte do caminho não existir, a função deve retornar None.

# Dica: Itere sobre o caminho e trate os casos onde uma chave não é encontrada ou o valor não é um dicionário.

# Exemplo:

# Python

# dados = {
#     'a': {
#         'b': {
#             'c': 10,
#             'd': 20
#         },
#         'e': 30
#     },
#     'f': 40
# }
# caminho1 = ['a', 'b', 'c']
# caminho2 = ['a', 'e']
# caminho3 = ['a', 'z', 'x'] # Caminho inexistente
# caminho4 = ['f', 'g'] # 'f' não é um dicionário

# Saída esperada:
# para caminho1: 10
# para caminho2: 30
# para caminho3: None
# para caminho4: None