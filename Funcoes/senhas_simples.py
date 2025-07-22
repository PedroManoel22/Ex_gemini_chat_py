#Exercício 14: Gerador de Senhas Simples
#Crie uma função chamada gerar_senha(comprimento) que recebe um número inteiro comprimento e retorna uma senha aleatória composta por letras maiúsculas
#, minúsculas e dígitos. Você pode usar o módulo random e string do Python.
#Exemplo de Uso:
#senha1 = gerar_senha(8)
#print(senha1)
# Exemplo de Saída: "aB3cD7eF" (será aleatório)
#senha2 = gerar_senha(12)
#print(senha2)
# Exemplo de Saída: "XyZ123AbC456" (será aleatório)


import random
import string

def gerar_senha(comprimento):

  if not isinstance(comprimento, int) or comprimento <= 0:
    raise ValueError("O comprimento da senha deve ser um número inteiro positivo.")

  caracteres = string.ascii_letters + string.digits
  senha = ''.join(random.choice(caracteres) for i in range(comprimento))
  return senha

# Exemplos de Uso:
print("--- Exemplos de Senha ---")
senha1 = gerar_senha(8)
print(f"Senha de 8 caracteres: {senha1}")

senha2 = gerar_senha(12)
print(f"Senha de 12 caracteres: {senha2}")

senha3 = gerar_senha(16)
print(f"Senha de 16 caracteres: {senha3}")

# Exemplo de tratamento de erro para comprimento inválido:
try:
  gerar_senha(0)
except ValueError as e:
  print(f"\nErro ao gerar senha: {e}")  
