# Filtre apenas os números pares da lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] usando list comprehension.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
print(pares)