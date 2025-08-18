# 4. Filtrar palavras que começam com uma vogal
# Dada uma lista de palavras, crie uma nova lista contendo apenas as palavras que começam com uma vogal ('a', 'e', 'i', 'o', 'u'). 
# A verificação deve ser insensível a maiúsculas e minúsculas.

# Lista de entrada: ["banana", "abacaxi", "uva", "morango", "elefante"]

lista_entrada = ["banana", "abacaxi", "Uva", "morango", "elefante"]

iniciadas_por_vogais = [palavra for palavra in lista_entrada if palavra[0] in 'aAeEiIoOuU']

print(f'Lista de entrada: {lista_entrada}')
print(f'Palavra que começam com vogais: {iniciadas_por_vogais}')
