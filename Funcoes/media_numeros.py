#Exercício 7: Média de Números (Argumentos Variáveis - *args)
#Crie uma função chamada calcular_media(*numeros) que pode receber um número variável de argumentos numéricos. A função deve calcular e retornar a média desses números.
#Exemplo de Uso:
#media1 = calcular_media(10, 20, 30)
#print(media1)
# Saída esperada: 20.0
#media2 = calcular_media(5, 10, 15, 20, 25)
#print(media2)
# Saída esperada: 15.0


def calcular_media(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma / len(numeros)

media1 = calcular_media(10, 20, 30)
print(media1)
media2 = calcular_media(5, 10, 15, 20, 25)
print(media2)
