# Crie uma lista com o quadrado de cada número da lista numeros = [1, 2, 3, 4, 5].

numeros = [1, 2, 3, 4, 5]
numeros_elevado_2 = [x**2 for x in numeros ]
print(f'Lista original: {numeros}')
print(f'Lista dos números elevado a 2: {numeros_elevado_2}')