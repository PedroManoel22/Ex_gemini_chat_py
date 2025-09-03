# Leia e valide as seguintes informações: 
# nome (maior que 3 caracteres), idade (entre 0 e 150), salário (maior que 0),
# sexo (feminino ou masculino), estado civil (solteiro, casado, divorciado, viúvo).

dados = dict()
while True: # loop principal

    nome = input('Nome: ')
    dados['nome'] = nome

    if len(nome) <= 3:

        print('\033[1;31mPor favor digite um nome válido\033[m')
        continue

    while True: # loop para idade (para caso o usuário digite sua idade incorreta, não precise adicionar seu nome novamente)
        try:

            idade = input('Idade: ')
            idade_int = int(idade)
            dados['idade'] = idade
            break # break do loop da idade 
        
        except ValueError:

            print('\033[1;31mInsira uma idade válida\033[m')
    while True: # loop para o salário (para caso o usuário digite seu salário errado, não precise adicionar seu nome e idade novamente)

        salario = float(input('salário: '))
        
 
        if salario <= 0:

            print('\033[1;31mPor favor insira um salário maior que R$0\033[m')
            continue
        
        dados['salario'] = salario
        break # break do loop do salário 

    while True: # loop para o sexo

        sexo = input('Sexo [F/M]: ').upper().strip()[0]

        if sexo not in 'FM':

            print('\033[1;31mPor favor insira um sexo válido!\033[m')
            continue
        
        dados['sexo'] = sexo
        break # break do loop do sexo

    while True: # loop para o estado civil 

        estado_civil = input('Estado civil: [(c)asado, (s)olteiro, (d)ivorciado, (v)iúvo]: ').upper().strip()[0]

        if estado_civil not in 'CSDV':

            print('\033[1;31mPor favor coloque um estado civil válido!\033[m')
            continue
        dados['estado civil'] = estado_civil
        break

    break # break do loop principal

print('Obrigado volte sempre')
for _, v in enumerate(dados.items()):
    print(v)

