# A partir da lista [10, 20, 30, 40, 50], crie uma nova lista onde cada número seja o dobro se for maior que 25, caso contrário, permaneça o mesmo.

numeros = [10, 20, 30, 40, 50]
dobro = [num if num > 25 else num for num in numeros ]
print(dobro)
