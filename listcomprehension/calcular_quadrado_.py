# 3. Calcular o quadrado de cada número
# Dada uma lista de números inteiros, crie uma nova lista onde cada elemento é o quadrado do número correspondente na lista original.

# Lista de entrada: [1, 2, 3, 4, 5]

lista_entrada = [1, 2, 3, 4, 5]
lista_quadrado = [num ** 2 for num in lista_entrada]

print(f'Lista de entrada: {lista_entrada}')
print(f'Lista dos quadrados: {lista_quadrado}')
