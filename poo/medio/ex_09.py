# Exercício 9: Classe Pessoa com Controle de Idade (Property com Setter)
# Crie a classe Pessoa com os atributos nome (string) e _idade (int, privado por convenção).

# @property (Getter): Para o atributo idade.

# @idade.setter (Setter): Permite a alteração da idade, mas deve validar que:

# A nova idade é um número positivo (> 0).

# Se a validação falhar, levante uma exceção (ValueError).


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self._idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.getter
    def idade(self):
        return f"Idade: {self._idade}"

    @idade.setter
    def idade(self, nova_idade: int):
        if nova_idade > 0:
            self._idade = nova_idade

        else:
            raise ValueError("Por favor insira uma idade maior que 0!")


p1 = Pessoa("Pedro", 21)
print(p1.idade)
p1.idade = 2
print(p1.idade)
p1.idade = 0
