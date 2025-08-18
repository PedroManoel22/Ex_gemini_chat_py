# Use uma função lambda como a função filter() para filtrar os números ímpares da lista [1, 2, 3, 4, 5, 6, 7, 8, 9].

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

impares = filter(lambda x: x % 2 != 0, numeros)
impares = list(impares)
print(impares)