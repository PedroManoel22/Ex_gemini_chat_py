# 5. Multiplicar cada elemento por um fator
# Dada uma lista de números e um fator multiplicador, crie uma nova lista onde cada número da lista original é multiplicado por esse fator.

# Lista de entrada: [10, 20, 30, 40]
# Fator: 2

lista_entrada = [10, 20, 30, 40]
fator = 3

def multiplicar(x, y):
    return x * y


lista_multiplicada = [multiplicar(num,fator) for num in lista_entrada]
print(f'Lista de entrada: {lista_entrada}')
print(f'Lista multiplicada: {lista_multiplicada}')
