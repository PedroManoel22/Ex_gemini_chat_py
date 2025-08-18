# Escreva uma lambda para verificar se um número é par.
while True:
    try:
        num = input('Insira um número: ')
        num_int = int(num)
        if isinstance(num_int, int):
            break
    except ValueError:
        print('Insira um número inteiro por favor!')

e_par = lambda x: x % 2 == 0
print(e_par(num_int))


