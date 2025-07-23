#Exercício 8: Validação de Dicionário com Esquema 📝
#Desenvolva uma função que receba um dicionário e um dicionário de esquema. O dicionário de esquema define os tipos esperados para cada chave. 
#A função deve retornar True se o dicionário de entrada estiver em conformidade com o esquema, e False caso contrário.
#Exemplo:

#dados_usuario = {'nome': 'Alice', 'idade': 25, 'email': 'alice@example.com'}
#esquema = {'nome': str, 'idade': int, 'email': str}
# Saída esperada: True

#dados_usuario_errado = {'nome': 'Bob', 'idade': '30', 'email': 'bob@example.com'}
# Saída esperada: False (idade deveria ser int, não str)
