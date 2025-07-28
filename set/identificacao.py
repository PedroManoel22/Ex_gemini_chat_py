# Exercício 5: Identificação de Permissões Faltantes 🚫
# Você tem um set de permissoes_necessarias para uma funcionalidade e uma lista de sets, onde cada set representa as permissoes_do_usuario de um usuário diferente. 
# Crie uma função que, para cada usuário, identifique quais permissões necessárias estão faltando. Retorne um dicionário onde a chave é o índice do usuário na lista
#  e o valor é um set das permissões faltantes.

# Exemplo:

# Python

# permissoes_necessarias = {'read', 'write', 'execute', 'delete'}
# permissoes_usuarios = [
#     {'read', 'write', 'execute'},
#     {'read', 'delete'},
#     {'write', 'execute', 'delete', 'admin'}
# ]
# Saída esperada (aproximada):
# {
#   0: {'delete'},
#   1: {'write', 'execute'},
#   2: {'read'}
# }