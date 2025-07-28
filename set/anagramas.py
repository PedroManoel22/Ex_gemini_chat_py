# Exercício 8: Encontrar Anagramas 🧩
# Crie uma função que receba uma lista de palavras (strings) e retorne um dicionário onde as chaves são as "assinaturas" 
# de anagramas (uma tupla de letras ordenadas, por exemplo, ('a', 'e', 'l', 'p') para 'apple') e os valores são sets de palavras que são anagramas umas das outras.

# Dica: Como você pode transformar uma palavra para que ela tenha a mesma "assinatura" que seus anagramas?

# Exemplo:

# Python

# palavras = ["listen", "silent", "enlist", "hello", "ehllo", "car", "arc"]
# Saída esperada (aproximada, chaves e valores são sets):
# {
#   ('e', 'i', 'l', 'n', 's', 't'): {'listen', 'silent', 'enlist'},
#   ('e', 'h', 'l', 'l', 'o'): {'hello', 'ehllo'},
#   ('a', 'c', 'r'): {'car', 'arc'}
# }
