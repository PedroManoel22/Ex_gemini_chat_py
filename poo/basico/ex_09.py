# Exercício 9: Classe Temperatura(Conversão Simples)
# Crie uma classe Temperatura com o atributo celsius(float).
# Método__init__ : Inicializa celsius.Método converter_para_fahrenheit() :
# Retorna o valor em Fahrenheit, usando a fórmula:$F = C \times (9/5) + 32$.

class Temperatura:
    def __init__(self, celsius:float):
        if not isinstance(celsius, (float, int)):
            raise TypeError (f'O valor de "Celsius" deve ser float ou int, e não {type(celsius).__name__}')
        
        self.celsius = celsius
    

    def conveter_para_fahrenheit(self):
        f = (self.celsius * 1.8) + 32
        return (f'Temperatura em Celsius: {self.celsius:.2f}\n'
                f'Temperatura em Fahrenheit: {f:.2f}')


conversao1 = Temperatura(25)
print(conversao1.conveter_para_fahrenheit())
