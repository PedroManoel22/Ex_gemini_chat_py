# Exercício 7: Validação de Esquema com Tipos Aninhados e Opcionais 📝
# Expanda o Exercício 8. Crie uma função que valide um dicionário de dados contra um esquema mais complexo. O esquema pode definir:

# Tipos esperados para chaves simples ('chave': str).

# Tipos para chaves aninhadas ('chave': {'sub_chave': int}).

# Chaves opcionais (indicadas por um tipo especial ou um valor padrão, talvez um tuple (str, True) para obrigatório, (str, False) para opcional).

# Tipos para elementos de lista ('chave_lista': [int]).

# Retorne True se o dicionário estiver conforme, False caso contrário, e opcionalmente, uma lista de erros encontrados.

# Dica: Recursão para estruturas aninhadas e verificação de isinstance().

# Exemplo de Esquema:

# Python

# schema = {
#     'id': int,
#     'nome': str,
#     'endereco': {
#         'rua': str,
#         'numero': int,
#         'complemento': (str, False) # Opcional
#     },
#     'tags': [str], # Lista de strings
#     'ativo': bool
# }

# dados_validos = {
#     'id': 1,
#     'nome': 'Teste',
#     'endereco': {'rua': 'Rua X', 'numero': 123},
#     'tags': ['a', 'b'],
#     'ativo': True
# }
# dados_invalidos = {
#     'id': '1', # Tipo errado
#     'nome': 'Teste',
#     'endereco': {'rua': 'Rua Y'}, # 'numero' faltando
#     'tags': ['a', 1], # Tipo errado na lista
#     'ativo': True
# }
# Sua função deve retornar False para dados_invalidos e indicar os erros.