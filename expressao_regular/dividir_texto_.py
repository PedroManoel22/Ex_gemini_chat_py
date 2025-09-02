# Exercício 6: Dividir um Texto por Delimitadores Variados
# Objetivo: Divida uma string em uma lista, usando vírgulas, ponto e vírgulas ou barras como delimitadores.

# Contexto: "Banana, Maçã; Pera/ Laranja"
# Dica: Use o método re.split() e o operador [] para agrupar os delimitadores.

import re

texto = "Banana, Maçã; Pera/ Laranja. eu"
print(re.split(r'[,;:/.]+', texto))