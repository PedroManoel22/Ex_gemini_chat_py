# Exercício 10: Herança e Sobrescrita de Métodos (__str__)
# Crie as seguintes classes:

# Animal: Classe base com atributos nome e especie. Deve ter um método fazer_som().

# Cachorro (Herda de Animal):

# Inicializa especie como "Canina".

# Sobrescreve fazer_som() para retornar "Latido".

# Sobrescreve o método mágico __str__ para retornar uma descrição amigável (ex: "Cachorro de nome Rex, espécie Canina").


class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.especie = ""

    def fazer_som(self) -> str: ...


class Cachorro(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)
        self.especie = "Canina"

    def fazer_som(self) -> str:
        return "Latido"

    def __str__(self) -> str:
        return f"Cachorro de nome {self.nome}, espécie {self.especie}"


c1 = Cachorro("Rex")
print(c1)
print(c1.fazer_som())
