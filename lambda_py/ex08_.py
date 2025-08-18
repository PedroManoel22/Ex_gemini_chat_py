# Use filter e lambda para selecionar apenas as strings que possuem mais de 5 caracteres da lista ['Python', 'Java', 'C++', 'JavaScript'].
lista = ['Python', 'Java', 'C++', 'JavaScript', 'Pedro Manoel', 'oiiiii']
mais_de_5_caractere = filter(lambda x: len(x) > 5, lista)
print(*mais_de_5_caractere, sep=' - ')