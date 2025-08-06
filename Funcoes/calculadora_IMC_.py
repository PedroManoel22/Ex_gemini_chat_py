#Exercício 15: Calculadora de IMC
#Crie uma função chamada calcular_imc(peso, altura) que recebe o peso (em kg) e a altura (em metros) de uma pessoa e retorna o Índice de Massa Corporal (IMC).
#A função também deve imprimir uma classificação baseada no IMC:
#Menor que 18.5: Abaixo do peso
#18.5 a 24.9: Peso normal
#25.0 a 29.9: Sobrepeso
#30.0 ou mais: Obesidade
#Exemplo de Uso:
#print(calcular_imc(70, 1.75))
# Saída esperada:
# IMC: 22.86
# Classificação: Peso normal
#print(calcular_imc(90, 1.70))
# Saída esperada:
# IMC: 31.14
# Classificação: Obesidade


def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    if imc < 18.5:
        classificacao = 'Abaixo do peso'
    elif imc >= 18.5  and imc <= 24.9:
        classificacao = 'Peso normal'
    elif imc >= 25 and imc <= 29.9:
        classificacao = 'Sobrepeso'
    else:
        classificacao = 'Obesidade'
    return f'IMC: {imc:.2f}\nClassificação: {classificacao}'


print(calcular_imc(70, 1.75))
print(calcular_imc(90, 1.70))