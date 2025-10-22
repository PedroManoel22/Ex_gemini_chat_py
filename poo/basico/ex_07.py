# Exercício 7: Classe Produto(Preço e Desconto)
# Crie uma classe Produto com os atributos nome(string) e preco(float).

# Método__init__ : Para inicializar nome e preco.

# Método aplicar_desconto(percentual) : Recebe um percentual (ex: 10 para 10%) e devolve o novo preço após aplicar o desconto.
# O método não deve alterar o preço original do produto .

class Produto:
    def __init__(self, nome:str, preco:float):
        self.nome = nome
        self.preco = preco
    

    def aplicar_desconto(self, percentual):
        novo_preco = self.preco - (self.preco * (percentual / 100))
        return novo_preco


p1 = Produto('celular', 1000)
print(p1.aplicar_desconto(10))
