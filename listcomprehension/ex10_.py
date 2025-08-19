# Remova as vogais de uma string usando list comprehension. A string de entrada é 'programação'.

string = 'programação'
remove_vogais = [letra for letra in string if letra not in 'aeiou']
print(*remove_vogais)