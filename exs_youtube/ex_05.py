# Calcule o fatorial de um número inteiro fornecido pelo usuário.

from math import factorial
while True:
    try:
        num = input('Insira um número inteiro: ')
        num_int = int(num)
        break
    except ValueError:
        print('Por favor insira um número inteiro!')
    except Exception:
        print('Erro inesperado!')
    
print(factorial(num_int)) 