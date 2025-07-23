#Exercício 5: Agrupamento de Dados por Chave 📊
#Imagine que você tem uma lista de dicionários, onde cada dicionário representa um registro (por exemplo, informações de alunos).
#Crie uma função que receba essa lista de dicionários e uma chave para agrupar. 
# A função deve retornar um dicionário onde as chaves são os valores da chave de agrupamento e os valores são listas de dicionários que correspondem a esse valor.
#Exemplo:

#alunos = [
#   {'nome': 'João', 'curso': 'Engenharia', 'idade': 20},
#    {'nome': 'Maria', 'curso': 'Medicina', 'idade': 22},
#    {'nome': 'Pedro', 'curso': 'Engenharia', 'idade': 21},
#    {'nome': 'Ana', 'curso': 'Direito', 'idade': 19},
#    {'nome': 'Luiza', 'curso': 'Medicina', 'idade': 23}
# ]
#chave_agrupamento = 'curso'
# Saída esperada (parcial):
# {
#   'Engenharia': [{'nome': 'João', 'curso': 'Engenharia', 'idade': 20},
#                  {'nome': 'Pedro', 'curso': 'Engenharia', 'idade': 21}],
#   'Medicina': [{'nome': 'Maria', 'curso': 'Medicina', 'idade': 22},
#                {'nome': 'Luiza', 'curso': 'Medicina', 'idade': 23}],
#   'Direito': [{'nome': 'Ana', 'curso': 'Direito', 'idade': 19}]
# }