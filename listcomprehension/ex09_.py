# Crie uma lista de tuplas (nome, comprimento) para cada nome na lista nomes = ['Ana', 'Bruno', 'Carlos'].
nomes = ['Ana', 'Bruno', 'Carlos']
comprimento = [(x, len(x)) for x in nomes]
print(comprimento)
