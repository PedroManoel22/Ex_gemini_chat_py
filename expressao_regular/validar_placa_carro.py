# Exercício 8: Validar uma Placa de Carro (Padrão Antigo e Mercosul)
# Objetivo: Valide se uma string corresponde ao padrão de placa de carro antigo (AAA-1234) ou ao padrão Mercosul (AAA-1A23).

# Contexto: 'ABC-1234', 'GHI-4J56'
# Dica: Use o operador de alternância | para combinar os dois padrões em uma única expressão regular.
import re 

def antigo_mercosul(placa):

    valida_antiga = re.findall(r'[A-Z]{3}\-[0-9]{4}', placa)
    valida_mercoul = re.findall(r'[A-Z]{3}\-[0-9A-Z]{4}', placa)

    if valida_antiga:

        return 'Modelo antigo'
    
    if valida_mercoul:

        return 'Modelo Mercosul'



placa_1 = 'ABC-1234'
placa_2 = 'GHI-4J56'
print(f'Placa: {placa_1}', antigo_mercosul(placa_1))
print(f'Placa: {placa_2}', antigo_mercosul(placa_2))