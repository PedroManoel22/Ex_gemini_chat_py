# Exercício 4: Classe Cachorro(Atributo de Classe)
# Chore uma aula Cachorro:

# Atributo de Classe: Crie um atributo chamado especie e defina seu valor como "Canis familiaris".

# Atributos de Instância: nome e idade.

# Método__init__ : Para inicializar nome e idade.

# Teste: Crie um objeto e imprima tanto o atributo de instância ( nome) quanto o atributo de classe ( especie).

class Cachorro:
    especie = 'Canis familiaris'

    def __init__(self, nome:str, idade:int):
        if not isinstance(nome, str):
            raise TypeError(f'O "nome" não pode ser do tipo {type(nome).__name__} tem que ser do tipo str')
        
        if not isinstance(idade, int):
            raise TypeError(f'A "idade" não pode ser do tipo {type(idade).__name__} tem que ser do tipo int')
        
        self.nome = nome
        self.idade = idade
    

    def __str__(self):
        return (f'Especie: {Cachorro.especie}\n'
               f'Nome: {self.nome}\n'
               f'Idade: {self.idade}\n')


cachorro1 = Cachorro('charles', 2)
print(cachorro1)
cachorro2 = Cachorro('Pedro', 5)
print(cachorro2)
