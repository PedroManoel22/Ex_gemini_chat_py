# Exercício 10: Aula Triangulo(Validação no __init__)
# Crie uma classe Triangulo com atributos lado1, lado2 e lado3(float).
# Método__init__ : Inicialize os três lados.Adicione uma Validação Simples: Dentro do __init__, 
# verifique se todos os lados são maiores que zero. Se qualquer lado for <= 0, imprima uma mensagem de erro 
# (ou, para um toque profissional, levante uma exceção ValueError, mas o print já atende ao nível básico).

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        if lado1 <= 0:
            raise ValueError('O "lado 1" deve ser maior que 0')
        
        if lado2 <= 0:
            raise ValueError('O "lado 2" deve ser maior que 0')
        
        if lado3 <= 0:
            raise ValueError('O "lado 3" deve ser maior que 0')
            
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        



triangulo1 = Triangulo(1, 2, 3)
#triangulo_invalido = Triangulo(0, 2, 3)
    
