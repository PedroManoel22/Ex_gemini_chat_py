# Exercício 3: Classe Pessoa(Método apresentar())
# Crie uma classe Pessoa com os atributos nome e idade.

# Método__init__ : Para inicializar nome e idade.

# Método apresentar() : Imprimir na tela uma mensagem de apresentação, por exemplo:"Olá, meu nome é [nome] e eu tenho [idade] anos."

# Teste: Crie um objeto e chame o método apresentar().

class Pessoa:
    def __init__(self, nome, idade):
        if not isinstance(nome, str):
            raise TypeError (f'\033[1;31mPor favor coloque um nome válido! "{nome}" é do tipo {type(nome).__name__} e precisa ser do tipo str\033[m')
        
        if not isinstance(idade, int):
            raise TypeError(f'\033[1;31mPor favor coloque uma idade válida! "{idade}" é do tipo {type(idade).__name__} e precisa ser do tipo int\033[m')
        
        self.nome = nome
        self.idade = idade
    

    def apresentar(self):
        return f'Olá, meu nome é {self.nome} e eu tenho {self.idade} anos'

p1 = Pessoa('Pedro', 23)
p2 = Pessoa('Manoel', 14)
#p3 = Pessoa('Fernado', 12.5)
print(p1.apresentar())
print(p2.apresentar())
#print(p3.apresentar())