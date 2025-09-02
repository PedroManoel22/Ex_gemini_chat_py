# Exercício 2: Encontrar Todos os Números de Telefone
# Objetivo: Encontre e extraia todos os números de telefone em um texto, no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX.

# Contexto: "Ligue para (11) 98765-4321 ou (21) 2345-6789 para mais informações."
# Dica: Use o método re.findall(). Lembre-se de escapar os caracteres especiais.


import re

texto = "Ligue para (11) 98765-4321 ou (21) 2345-6789 para mais informações."

def acha_telefone(texto):

    numeros = re.findall(r'\(\d{2}\) \d*\-\d*', texto)

    for numero in numeros:

        print(numero)
        

acha_telefone(texto)