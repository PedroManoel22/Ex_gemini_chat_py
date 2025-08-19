# Qual a principal vantagem de usar uma função lambda em vez de uma função def? Dê um exemplo.SSS

# a principal vantagem do uso de funções lambdas é um número menor de linhas no código, como por exemplo uma função soma() que recebe dois parametros,
# e retorna a soma destes dois, seria mais ou menos assim:
"""
def soma(x, y):
    return x + y 

soma(10, 9)

saída: 19
"""

# Mas com lambda podemos fazer da seguinte maneira:

"""
soma = lambda x, y: x + y
print(soma(10, 9))

saída: 19
"""
