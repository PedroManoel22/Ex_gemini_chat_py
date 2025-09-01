# Desenvolva uma calculadora rudimentar onde o usuário deve informar: qual operação ele deseja realizar, 
# quais os valores para a realização do cálculo (apenas dois valores) e o resultado da operação


def main():
    while True:
      
        operador = input('Insira um operador [+, -, *, /]: ')

        if operador in '+-*/':
            
            try:

                num_1_str = input('Primeiro número: ')
                
                try:

                    num_1 = int(num_1_str)

                except ValueError:

                    num_1 = float(num_1_str)

                num_2_str = input('Segundo número: ')

                try:

                    num_2 = int(num_2_str)

                except ValueError:

                    num_2 = float(num_2_str)

                if operador == '+':

                    print(f'A soma entre {num_1} + {num_2} = {num_1 + num_2}')

                elif operador == '-':

                    print(f'A substração entre {num_1} - {num_2} = {num_1 - num_2}')

                elif operador == '*':

                    print(f'A multiplicação entre {num_1} x {num_2} = {num_1 * num_2}')

                else:

                    print(f'A divisão entre {num_1} / {num_2} = {num_1 / num_2}')

                break  

            except ValueError:

                print('Entrada de número inválida. Por favor, insira um número inteiro ou com ponto flutuante.')

        else:
           
            print('Por favor, coloque um operador válido!')

if __name__ == '__main__':
    main()
    