# 1. Filtrar números pares
# Dada uma lista de números inteiros, crie uma nova lista contendo apenas os números pares.

# Lista de entrada: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

apenas_pares = [pares for pares in lista_entrada if pares % 2 ==0]

print(f'Lista de entrada: {lista_entrada}')
print(f'Lista de pares: {apenas_pares}')
