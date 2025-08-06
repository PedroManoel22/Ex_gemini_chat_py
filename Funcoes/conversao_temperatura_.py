#Exercício 9: Conversão de Temperatura e Lista
#Crie duas funções:
#celsius_para_fahrenheit(celsius): Recebe uma temperatura em Celsius e retorna o equivalente em Fahrenheit. (Fórmula: F=C
#times9/5+32)
#converter_lista_temperaturas(temperaturas_celsius): Recebe uma lista de temperaturas em Celsius e usa a primeira função (celsius_para_fahrenheit) para converter cada uma para Fahrenheit, retornando uma nova lista com as temperaturas convertidas.
#Exemplo de Uso:
#temp_c = 25
#temp_f = celsius_para_fahrenheit(temp_c)
#print(f"{temp_c}°C é igual a {temp_f}°F")
# Saída esperada: 25°C é igual a 77.0°F
#lista_c = [0, 10, 20, 30, 40]
#lista_f = converter_lista_temperaturas(lista_c)
#print(f"Temperaturas em Fahrenheit: {lista_f}")
# Saída esperada: Temperaturas em Fahrenheit: [32.0, 50.0, 68.0, 86.0, 104.0]


def celsius_para_fahrenheit(celsius):
    return  (celsius * 9/5) + 32


temp_c = 25
temp_f = celsius_para_fahrenheit(temp_c)
print(f'{temp_c}°C é igual a {temp_f}°F')


def converter_lista_temperaturas(temps):
    temps_f = []
    for temp in temps:
        temps_f.append((temp * 9/5) + 32)
    return temps_f


lista_c = [0, 10, 20, 30, 40]
lista_f = converter_lista_temperaturas(lista_c)
print(f"Temperaturas em Fahrenheit: {lista_f}")
print(f'Temperatura em celsius: {lista_c}')
