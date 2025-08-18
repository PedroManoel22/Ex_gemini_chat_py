# Usando map e lambda, converta uma lista de temperaturas em Celsius [0, 10, 20, 30]para Fahrenheit. A fórmula é (graus_c * 9/5) + 32.

celsius = [0, 10, 20, 30]
fahrenheit = map(lambda x: (x * 9/5) + 32, celsius)
print(*fahrenheit) 