# Exercício 4: Substituir Múltiplos Espaços por um Único
# Objetivo: Substitua todas as ocorrências de um ou mais espaços em branco por apenas um espaço.

# Contexto: 'Este     texto     tem         espaços     múltiplos.'
# Dica: Use o método re.sub() e o quantificador +.

import re

texto = 'Este     texto     tem         espaços     múltiplos.'

print(re.sub(r'\s+', ' ', texto))
