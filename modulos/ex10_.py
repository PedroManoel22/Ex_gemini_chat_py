# Qual a diferença entre import modulo e from modulo import funcao? Explique com um exemplo prático.

# A diferença é: que no import módulo, quando vc for chamar uma função ou algo parecido, temos que 
# chamar o nome do módulo seguido do seu nome mais o nome da função que queremos chamar, por exemplo: import sys
# sys.exit()
# Já quando usamos o from sys import exit (aqui estou usando o módulo exit como exemplo), não precisamos chamar o nome 
# do módulo, apenas a função, por exemplo: from sys import exit
# exit()