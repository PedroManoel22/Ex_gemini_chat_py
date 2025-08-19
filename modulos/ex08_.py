# Importe o módulo json e converta o seguinte dicionário {'nome': 'joão', 'idade': 30} em uma string JSON.

import json

# Dicionário Python a ser convertido
dados_dict = {'nome': 'joao', 'idade': 30}

# Converte o dicionário para uma string JSON
dados_json = json.dumps(dados_dict)

# Imprime o tipo e o valor da string JSON
print(type(dados_json))
print(dados_json)

