# Use uma função next() em uma lista vazia. O que acontece? (Dica: pesquisa sobre a exceção StopIteration).
lista = []
lista_iter = iter(lista)
print(next(lista_iter))