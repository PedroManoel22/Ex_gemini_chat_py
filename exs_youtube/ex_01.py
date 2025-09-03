# Peça uma nota entre 0 e 10, mostre uma mensagem caso o valor seja inválido e continue pedindo 
# até que o usuário informe um valor válido.

while True:

    try:

        num = input('Insira uma nota entre 0 e 10: ')
        num_float = float(num)

        if num_float > 10 or num_float < 0:

            print('Por favor insira um número entre 0 e 10')
            continue

        break
    
    except ValueError:

        print('Por favor insira um número inteiro')
    
    except Exception:

        print('Erro inesperado')
    