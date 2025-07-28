#Exercício 8: Validação de Dicionário com Esquema 📝
#Desenvolva uma função que receba um dicionário e um dicionário de esquema. O dicionário de esquema define os tipos esperados para cada chave. 
#A função deve retornar True se o dicionário de entrada estiver em conformidade com o esquema, e False caso contrário.
#Exemplo:

#dados_usuario = {'nome': 'Alice', 'idade': 25, 'email': 'alice@example.com'}
#esquema = {'nome': str, 'idade': int, 'email': str}
# Saída esperada: True

#dados_usuario_errado = {'nome': 'Bob', 'idade': '30', 'email': 'bob@example.com'}
# Saída esperada: False (idade deveria ser int, não str)

def validação_dicionario(dados, x):
    dados_lista = []
    tipos_esquema = []
    tipos_dados_lista = []
    for _,v in dados.items():
        dados_lista.append(v)
    for tipo in x:
        tipos_esquema.append(x[tipo])
    for i in range(len(dados_lista)):
        tipos_dados_lista.append(type(dados_lista[i]))
    if tipos_dados_lista == tipos_esquema:
        return True
    else:
        return False
            

dados_usuario = {'nome': 'Alice', 'idade': 25, 'email': 'alice@example.com'}
esquema = {'nome': str, 'idade': int, 'email': str}
print(validação_dicionario(dados_usuario, esquema))
dados_usuario_errado = {'nome': 'Bob', 'idade': '30', 'email': 'bob@example.com'}
print(validação_dicionario(dados_usuario_errado, esquema))
