# Crie uma lista de listas (matriz) 3x3 onde cada elemento seja a soma de seus índices de linha e coluna.
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]].

# resolução com loop for 

matriz = [[x + y for x in range(0, 3)]for y in range(0, 3) ]
print(matriz)