# Use uma função zip() para iterar sobre duas listas simultaneamente: nomes = ['joão', 'maria']e idades = [25, 30]. Imprima cada nome com sua respectiva idade.

nomes = ['joão', 'maria']
idades = [25, 30]
sexo = ['M', 'F']
string_juntas = zip(nomes, idades, sexo)
print(*string_juntas, sep='\n')
