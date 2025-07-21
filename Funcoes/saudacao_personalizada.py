#Exercício 2: Saudação Personalizada
#Crie uma função chamada saudar_nome(nome) que recebe um argumento nome (uma string) e imprime uma saudação personalizada, como "Olá, [nome]! Bem-vindo(a) às funções!".
#Exemplo de Uso:
#saudar_nome("Alice")
# Saída esperada: Olá, Alice! Bem-vindo(a) às funções!
#saudar_nome("Bob")
# Saída esperada: Olá, Bob! Bem-vindo(a) às funções!
def saudar_nome(nome):
    print(f'olá, {nome}! Bem-Vindo(a) ás funções!')
saudar_nome('Alice')
saudar_nome('Bob')
