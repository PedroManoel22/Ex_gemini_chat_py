#Exercício 13: Inversor de String
#Crie uma função chamada inverter_string(texto) que recebe uma string texto e retorna a string invertida.
#Exemplo de Uso:
#print(inverter_string("programacao"))
# Saída esperada: oacamargorp
#print(inverter_string("Python"))
# Saída esperada: nohtyP


def inverter_string(texto):
    return texto[::-1]


print(inverter_string("programacao"))
print(inverter_string("Python"))
