# Exercício 5: Encontrar Todas as Palavras com 5 Letras
# Objetivo: Encontre todas as palavras em um texto que tenham exatamente 5 letras.

# Contexto: "O rato roeu a roupa do rei de Roma."
# Dica: Use re.findall(). Lembre-se de usar \b para delimitar as palavras e {} para especificar a quantidade de caracteres.

import re

texto = "O rato roeu a roupa do rei de Roma."

print(re.findall(r'\b\w{5}\b', texto))

