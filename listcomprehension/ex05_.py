# Crie uma lista com os números de 1 a 100 que são divisíveis por 7.

lista = [x for x in range(1, 101) if x % 7 == 0]
print(lista)