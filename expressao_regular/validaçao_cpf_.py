# Exercício 1: Validação de CPF
# Objetivo: Escreva um programa que valide se uma string é um CPF no formato XXX.XXX.XXX-XX.

# Contexto: Use a string '123.456.789-00' para testar.
# Dica: Use os metacaracteres para dígitos (\d) e caracteres literais (., -).
import re

def validacao(cpf):
    print()

    padrao = re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', cpf)

    if padrao == []:

        return f'{padrao} não está na forma padrão de um cpf\nPor favor insira um cpf válido!'

    else:

        return f'CPF válido!: {padrao}'
    


print(validacao('123.456.789-00')) # padrão válido 
print(validacao('12345678910')) # padrão inválido
print(validacao('123.456.789-12')) # padrão válido
