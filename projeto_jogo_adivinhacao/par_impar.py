# Desenvolva um programa que leia um número qualquer e informe se ele é par ou ímpar

def main():
    while True:
        try:

            num_str = input('Insira um número: ')
            num_int = int(num_str)

            if num_int % 2 == 0:
                print('Este número é par!')
            else:
                print('Este número é ímpar!')
            
            break

        except ValueError:
           
            print('Entrada inválida. Por favor, insira um número inteiro.')

if __name__ == '__main__':
    main()