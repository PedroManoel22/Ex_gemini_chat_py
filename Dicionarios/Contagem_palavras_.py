#Crie uma função que receba uma string como entrada e retorne um dicionário onde as chaves são as palavras da string (ignorando maiúsculas/minúsculas
# e pontuação simples como vírgulas e pontos finais)
# e os valores são a frequência de cada palavra.


import re # Módulo para expressões regulares, útil para remover pontuação

def contar_frequencia_palavras(texto):
    texto_limpo = re.sub(r'[^\w\s]', '', texto).lower() # no re.sub o '\w' é para substituir o que não for letra e o '\s' é espaço 
    palavras = texto_limpo.split() # Aqui dividimos o texto em palavras
    frequencia = {}
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    return frequencia

# Exemplo de uso:
texto_exemplo = "Olá mundo, olá Python. Python é legal!"
resultado = contar_frequencia_palavras(texto_exemplo)
print(resultado)

# Outro exemplo para testar:
texto_maior = "Este é um exemplo de texto. Um texto com mais palavras, este texto!"
resultado_maior = contar_frequencia_palavras(texto_maior)
print(resultado_maior)
