#Exercício 2: Fusão de Dicionários 🔄
#Escreva uma função que receba dois dicionários como entrada e retorne um novo dicionário que é a fusão dos dois.
#  Se houver chaves em comum, os valores do segundo dicionário devem sobrescrever os valores do primeiro.

#Exemplo:
#dict1 = {'a': 1, 'b': 2, 'c': 3}
#dict2 = {'b': 4, 'd': 5}
# Saída esperada: {'a': 1, 'b': 4, 'c': 3, 'd': 5}


def fusao(x, y):
    fusao_dicionario = x.copy()
    fusao_dicionario.update(y)# Aqui ele o método .update() não colocar as chaves repetidas, pois ele só adiciona as chaves que não existem
    return fusao_dicionario


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5}
resultado = fusao(dict1, dict2)
print(resultado)
