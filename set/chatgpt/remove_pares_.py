# Crie um conjunto com os números de 1 a 10. Remova os números pares do conjunto.

conjunto = set(range(1,11))

pares = {num for num in conjunto if num % 2 == 0}
conjunto -= pares
print(conjunto)
