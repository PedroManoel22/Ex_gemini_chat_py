# Exercício 6: Classe Contador(Modificando Atributos)
# Crie uma classe Contador com um único atributo de instância valor(int), inicializado como 0.

# Método__init__ : Inicializa valor = 0.

# Método incrementar() : Aumenta o valorem 1.

# Método resetar() : Defina o valorde volta para 0.

# Teste: Crie um contador, chame incrementar() duas vezes, e depois resetar(). Imprima o valor após cada operação.

class Contador:
    def __init__(self, valor=0):
        self.valor = valor
    
    
    def incrementar(self):
        self.valor += 1
        return self.valor
        
    
    def resetar(self):
        self.valor = 0
        return self.valor
    

x = Contador()
print(x.incrementar())
print(x.incrementar())
print(x.resetar())
        