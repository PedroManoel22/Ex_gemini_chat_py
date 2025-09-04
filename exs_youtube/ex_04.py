# Calcule e escreva o número de anos necessários para que a população do país A (80.000 habitantes, crescimento de 3% ao ano)
# ultrapasse ou iguale a população do país B (200.000 habitantes, crescimento de 1.5% ao ano), mantidas as taxas de crescimento.

def calcular_anos(habitantes, crescimento, habitantes_b, crescimento_b):

    anos = 0

    while habitantes < habitantes_b:
            
            habitantes += habitantes * (crescimento / 100) # crescimento do país A 
            habitantes_b += habitantes_b * ( crescimento_b / 100)# crescimento do país B
            anos += 1

    return (
    f'Habitantes no país A: {habitantes:.0f}\n'
    f'Habitantes no país B: {habitantes_b:.0f}\n'
    f'Foram {anos} anos para chegar aqui'
            )

habitantes_a = 80000.0
cresciemento_a = 3
habitantes_b = 200000.0
cresciemento_b = 1.5
print(calcular_anos(habitantes_a, cresciemento_a, habitantes_b, cresciemento_b))
