# Use uma função lambda com a função map() para dobrar todos os números da lista [1, 2, 3, 4, 5].

lista = [1, 2, 3, 4, 5]

dobra = map(lambda x: x * 2, lista)
dobra_lista = list(dobra)

print(dobra_lista)