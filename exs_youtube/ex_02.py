# Leia o nome de usuário e a senha e não aceite a senha igual ao nome de usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:

    nome = input('Insira seu nome de usuário: ')
    nome_de_usuario = nome.upper()
    senha = input('Senha: ').upper()

    if nome_de_usuario == senha:

        print('A senha não pode ser igual ao nome de usuário')
        continue

    else:

        break

print(f'Bem-Vindo {nome_de_usuario}🥰')
