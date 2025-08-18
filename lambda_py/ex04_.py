# Use uma função lambda com a função sorted() para ordenar uma lista de tuplas baseada no segundo elemento da tupla. A lista é [('maçã', 5), ('banana', 2), ('uva', 8)].

lista = [('maçã', 5), ('banana', 2), ('uva', 8)]

lista_ordenada = sorted(lista, key=lambda x: x[1])

print(lista_ordenada)