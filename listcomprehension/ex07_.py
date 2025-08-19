# Crie uma lista com o comprimento de cada palavra na frase 'O Python é uma linguagem poderosa'.

frase = 'O Python é uma linguagem poderosa'.split()
tamanho_palavra = [len(x) for x in frase]
print(tamanho_palavra)
lista_formatada = zip(frase, tamanho_palavra)
print(*lista_formatada)