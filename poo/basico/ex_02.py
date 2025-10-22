# Exercício 2: Classe Retangulo(Métodos Simples)
# Crie uma classe Retangulo com os atributos largura e altura(float).

# Método__init__ : Para inicializar a largura e a altura.

# Método calcular_area() : Retorne à área do retângulo ( largura * altura).

# Método calcular_perimetro() : Retorna o perímetro do retângulo ( 2 * (largura + altura)).

class Retangulo:
    def __init__(self, largura:float, altura:float):
        if not isinstance(largura, (float, int)):
            raise TypeError(f'A "largura" deve ser um float e foi colocada {type(largura).__name__}')
        
        if not isinstance(altura, (float, int)):
            raise TypeError(f'A "altura" deve ser um float e foi colocada {type(altura).__name__}')
        
        if largura <= 0:
            raise ValueError('A "largura" deve ser positiva')
        
        if altura <= 0:
            raise ValueError('A "altura" deve ser positiva')
        
        self.largura = largura
        self.altura = altura
    

    def calcular_area(self):
       return f'Área = {self.largura * self.altura}'


    def calcular_perimetro(self):
        return f'Perímetro = {2 * (self.largura * self.altura)}'


x = Retangulo(largura=5, altura=2)
print(x.calcular_area())
print(x.calcular_perimetro())
