# 2. Converter para maiúsculas
# Dada uma lista de strings, crie uma nova lista onde cada string está em letras maiúsculas.

# Lista de entrada: ["python", "list", "comprehension", "exercicio"]

lista_entrada = ["python", "list", "comprehension", "exercicio"]

letras_maiusculas = [palavra.upper() for palavra in lista_entrada]

print(f'Lista de entrada: {lista_entrada}')
print(f'Lista com as palavras em maiísculas: {letras_maiusculas}')
