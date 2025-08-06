#Exercício 10: Cálculo de Fatorial (Desafio - Recursão)
#Crie uma função chamada calcular_fatorial(numero) que recebe um número inteiro não negativo e retorna o seu fatorial. Lembre-se que o fatorial de 0 é 1, 
# e o fatorial de um número n é n
#times(n−1)
#times(n−2)
#times
#dots
#times1. Tente resolver este exercício usando recursão (a função chamando a si mesma).
#Exemplo de Uso:
#fatorial_5 = calcular_fatorial(5)
#print(fatorial_5)
# Saída esperada: 120 (5 * 4 * 3 * 2 * 1)
#fatorial_0 = calcular_fatorial(0)
#print(fatorial_0)
# Saída esperada: 1


def calcular_fatorial(numero):
    fatorial = 1
    numeros_list = []
    if numero == 0:
        return fatorial
    elif numero != 0:
        for i in range(1, numero + 1):
            fatorial *= i
            numeros_list.append(i)
        return f'{fatorial}, {tuple(numeros_list)}'
    
    
fatorial_5 = calcular_fatorial(5)
print(fatorial_5)
