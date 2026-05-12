# Exercício 5: Classe RegistroHistorico (Classmethod - Construtor Alternativo)
# Crie a classe RegistroHistorico com atributos nome (string) e timestamp (datetime).

# Método __init__: Aceita nome e timestamp. ✔️

# classmethod: Crie um classmethod chamado criar_agora(nome) que:

# Usa o módulo datetime para obter o timestamp atual (datetime.now()). ✔️

# Cria e retorna uma nova instância de RegistroHistorico com o nome fornecido e o timestamp atual. ✔️

# Propósito: Demonstrar como usar classmethods como construtores alternativos, úteis para inicializar objetos de diferentes formas. ✔️

import datetime


class RegistroHistorico:
    nome: str
    timestamp: datetime.datetime

    def __init__(self, nome: str, timestamp: datetime.datetime) -> None:
        self.nome = nome
        self.timestamp = timestamp
    
    @classmethod
    def criar_agora(cls, nome: str):
        timestamp_atual = datetime.datetime.now()

        return cls(nome=nome, timestamp=timestamp_atual)

if __name__ == "__main__":
    novo_registro = RegistroHistorico.criar_agora("Acesso de Usuário")
    print(novo_registro.nome)
    