# Exercício 9: Diferença Simétrica entre Listas de Strings ↔️
# Dadas duas listas de strings, retorne um set contendo todos os elementos que estão presentes em uma lista OU na outra, mas não em ambas.

# Exemplo:

# Python

# set1_strings = ["apple", "banana", "orange", "grape"]
# set2_strings = ["banana", "kiwi", "apple", "melon"]
# Saída esperada: {'orange', 'grape', 'kiwi', 'melon'} (ordem não importa)

set1_strings = ["apple", "banana", "orange", "grape"]
set2_strings = ["banana", "kiwi", "apple", "melon"]
set3 = set(set1_strings)
set4 = set(set2_strings)
diferenca_simetrica = set3 ^ set4
print(diferenca_simetrica)
