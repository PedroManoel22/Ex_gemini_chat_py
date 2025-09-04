# Leia um número e exiba o dia correspondente da semana (1-Domingo, 2-Segunda, etc.). 
# Se digitar outro valor, deve aparecer 'valor inválido'.
dias = ['Domingo','Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
while True:
    try:
        opcao = input('Insira um número de 1 a 7: ')
        opcao_int = int(opcao)
        if opcao_int >= 1 and opcao_int <= 7:
            print(dias[opcao_int-1])
        else:
            print('Por favor coloque um número entre 1 e 7')
    except ValueError:
        print('Por favor insira um número inteiro')
    except Exception:
        print('Erro inesperado')
    continuar = input('Deseja continuar? [S]/[N]: ').strip().upper()[0]

    if continuar != 'S':

        break