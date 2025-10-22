# Exercício 1: Classe Carro(Atributos e Inicialização)
# Crie uma aula Carro com as seguintes características:

# Atributos de Instância: marca (string), modelo(string) e ano(int).

# Método__init__ : Para receber e inicializar esses três atributos quando um novo objeto Carro for criado.

# Crie um Objeto: Instancie um objeto meu_carro e imprima seus atributos. 

class Carro:
    def __init__(self, marca:str, modelo:str, ano:int):

        if not isinstance(marca, str):
            raise TypeError (f"A 'marca' deve ser uma string, mas foi recebido {type(marca).__name__}")
        
        if not isinstance(modelo, str):
            raise TypeError(f"O 'modelo' deve ser uma string, mas foi recebido {type(modelo).__name__}")
            
        if not isinstance(ano, int):
            raise TypeError(f"O 'ano' deve ser um inteiro, mas foi recebido {type(ano).__name__}")
        
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


    def __str__(self):
        return ('Dados do carro:\n'
              f'Marca: {self.marca}\n'
              f'Modelo: {self.modelo}\n'
              f'Ano: {self.ano}\n')


carro1 = Carro('Chevrolet', 'celta', 2010) 
carro2 = Carro('Fiat', 'uno', 2021)
print(carro1)
print(carro1)
