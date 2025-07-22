#Exercício 12: Contador de Vogais
#Crie uma função chamada contar_vogais(texto) que recebe uma string texto e retorna o número de vogais 
#(a, e, i, o, u, maiúsculas e minúsculas) presentes na string.
#Exemplo de Uso:
#print(contar_vogais("Python"))
# Saída esperada: 1 (apenas 'o')
#print(contar_vogais("Inteligencia Artificial"))
# Saída esperada: 11


def contar_vogais(texto):
    texto_formatado = texto.upper()
    contador = 0
    vogais = ['A', 'E', 'I', 'O', 'U']
    for letras in texto_formatado:
        if letras in vogais:
            contador += 1
    return contador


print(contar_vogais('Python'))
print(contar_vogais("Inteligencia Artificial"))
