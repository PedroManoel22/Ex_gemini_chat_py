# Crie um for loop para iterar sobre a lista numeros = [10, 20, 30] e imprimir cada elemento. Explique como o for loop usa iteradores internamente.

numeros = [10, 20, 30]
numeros_iter = iter(numeros)

for i in range(len(numeros)):
    print(next(numeros_iter))  # O for loop vai de 0 até o tamanho da lista 'numeros', se o loop for fosse maior que o tamanho da lista iria aparecer um erro de StopInteration no terminal 