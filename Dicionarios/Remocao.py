#Exercício 9: Remoção de Elementos por Lista de Chaves 🗑️
#Crie uma função que receba um dicionário e uma lista de chaves.
# A função deve retornar um novo dicionário com todos os pares chave-valor do dicionário original, exceto aqueles cujas chaves estão na lista fornecida.
#Exemplo:

#produto = {'id': 101, 'nome': 'Notebook', 'preco': 1500, 'estoque': 50}
#chaves_remover = ['id', 'estoque']
# Saída esperada: {'nome': 'Notebook', 'preco': 1500}


def remove_chave(dicionario, remover):
    for chave in remover:
        dicionario.pop(chave)
    return dicionario


produto = {'id': 101, 'nome': 'Notebook', 'preco': 1500, 'estoque': 50}
chaves_remover = ['id', 'estoque']
print(remove_chave(produto, chaves_remover))
