# Exercício 5: Classe Circulo(Método __str__)
# Crie uma classe Circulo n com o atributo raio(float).

# Método__init__ : Para inicializar o raio.

# Método __str__(Dunder Method): Sobrescreva este método para que, ao imprimir o objeto, ele retorne uma string formatada, por exemplo: "Círculo de raio [raio]".

# Teste Pythônico: Crie um objeto e use print()diretamente nele.

class Circulo:
    def __init__(self, raio):
        self.raio = raio


    def __str__(self):
        return f'círculo de raio {self.raio}'


print(Circulo(5)) 