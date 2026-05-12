# Exercício 2: Classe ContaBancaria (Encapsulamento e Properties)
# Crie a classe ContaBancaria com as seguintes características:

# Atributos Privados: Use o padrão de convenção com _saldo (float) e
# _numero_conta (string).

# Propriedade (Property) para Saldo: Crie uma property saldo (usando @property)
# que permite apenas a leitura (getter), garantindo que o valor não possa ser 
# alterado diretamente.

# Métodos Públicos:

# depositar(valor): Adiciona o valor ao saldo. Deve verificar 
# se o valor é positivo.

# sacar(valor): Subtrai o valor do saldo. 
# Deve verificar se o valor é positivo e se há saldo suficiente.

# Dica Pythônica: Use o decorator @property para o getter e @saldo.setter
#  para o setter, se fosse o caso (mas, neste exercício, queremos apenas 
# o getter para proteger o saldo de alterações externas não rastreadas).