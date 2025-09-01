from random import randint

num_computador = randint(0, 10)
count = 0
print(f'número do computador: {num_computador}')

while True:

    try:
        
        num_usuario = input('Estou pensando em um número de 0 a 10, tente advinhar: ')
        num_usuario_int = int(num_usuario)
        count += 1

    except Exception as e:

        print('Por favor coloque um número inteiro!')
        print(e)

    if num_usuario_int == num_computador:

        break

    elif count == 5:

        break

print('Obrigado por jogar🥰, volte sempre!')
