# Leia e valide as seguintes informações: 
# nome (maior que 3 caracteres), idade (entre 0 e 150), salário (maior que 0),
# sexo (feminino ou masculino), estado civil (solteiro, casado, divorciado, viúvo).

while True:

    nome = input('Nome: ')

    if len(nome) <= 3:

        print('\033[1;31mPor favor digite um nome válido\033[m')
        continue

    while True: # loop para idade (para caso o usuário digite sua idade incorreta, não precise adicionar seu nome novamente)
        try:

            idade = input('Idade: ')
            idade_int = int(idade)
            break
        
        except ValueError:

            print('\033[1;31mInsira uma idade válida\033[m')
    while True: # loop para o salário (para caso o usuário digite seu salário errado, não precise adicionar seu nome e idade novamente)

        salario = float('salário: ')

        if salario <= 0:

            print('Por favor insira um salário maior que R$0')
            continue


    break


