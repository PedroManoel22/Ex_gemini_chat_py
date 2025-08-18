# Crie uma lista de nomes e use a função iter()para criar um iterador . Use a função next() para imprimir os três primeiros nomes.

nomes = ['Pedro', 'João', 'Ana', 'José', 'Fernanda', 'Isabel']
nomes_iter = iter(nomes)

for i in range(3):
    print(next(nomes_iter))
    