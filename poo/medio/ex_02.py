# Exercício 2: Classe ContaBancaria (Encapsulamento e Properties)
# Crie a classe ContaBancaria com as seguintes características:

# Atributos Privados: Use o padrão de convenção com _saldo (float) e
# _numero_conta (string).

# Propriedade (Property) para Saldo: Crie uma property saldo (usando @property)
# que permite apenas a leitura (getter), garantindo que o valor não possa ser 
# alterado diretamente. ✔️

# Métodos Públicos:

# depositar(valor): Adiciona o valor ao saldo. Deve verificar 
# se o valor é positivo. ✔️

# sacar(valor): Subtrai o valor do saldo. 
# Deve verificar se o valor é positivo e se há saldo suficiente. ✔️

# Dica Pythônica: Use o decorator @property para o getter e @saldo.setter
#  para o setter, se fosse o caso (mas, neste exercício, queremos apenas 
# o getter para proteger o saldo de alterações externas não rastreadas).


class ContaBancaria:
    def __init__(self, saldo: float, numero_conta: str) -> None:
        self._saldo = saldo
        self._numero_conta = numero_conta
    
    @property
    def saldo(self):
        return self._saldo

    @saldo.getter
    def saldo(self):
        return f"R${self._saldo}"
    
    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
        else:
            print("\n\033[31mPor favor insira um valor postivo!\n\033[m")

    def sacar(self, valor: float):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
        else:
            print("\n\033[31mO valor a ser sacado deve ser positivo e menor que o saldo!\n\033[m")
            
    