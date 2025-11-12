# 3. Sistema de Funcionários (Herança Simples)
# Crie uma classe base Funcionario e duas classes derivadas: Gerente e Desenvolvedor.

# Funcionario: Atributos nome, salario. Método calcular_salario_anual()(simplesmente salario * 12). ✔️

# Gerente: Herda de Funcionario. Adicional o atributo bonus. Sobrescreva calcular_salario_anual() para incluir o bônus. ✔️

# Desenvolvedor: Herda de Funcionario. Adicional o atributo linguagem.

# Dica Profissional: Use o método super().__init__(...)para chamar o construtor da classe base de forma limpa.

class Funcionario:

    def __init__(self, nome:str, salario:float):
        self.nome = nome
        self.salario = salario
    

    def calcular_salario_anual(self, bonus = 0):
        if bonus == 0:
            return self.salario * 12
        
        else:
             return self.salario * 12 + bonus


class Gerente(Funcionario):
    def __init__(self,nome, salario, bonus):
        self.nome = nome
        self.salario = salario
        self.bonus = bonus
    
    def calcular_salario_anual(self):
        return super().calcular_salario_anual(self.bonus)



funcionario1 = Funcionario('Pedro', 2500) 
salario_f = funcionario1.calcular_salario_anual()
print(f"Salário Anual do {funcionario1.nome}: R$ {salario_f}")


gerente1 = Gerente('Ana', 5000, 10000) 
print(f"Nome do Gerente: {gerente1.nome}")
salario_g = gerente1.calcular_salario_anual()
print(f"Salário Anual da {gerente1.nome}: R$ {salario_g}")
