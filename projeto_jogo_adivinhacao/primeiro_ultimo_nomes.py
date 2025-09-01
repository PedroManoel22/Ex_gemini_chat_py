# Desenvolva um programa que leia o seu nome completo e que apresente somente o seu primeiro e último nomes

nome_completo = str(input('Insira seu nome completo: ')).split()
primeiro_ultimo = lambda x: [x[0], x[-1]]
print(primeiro_ultimo(nome_completo))
