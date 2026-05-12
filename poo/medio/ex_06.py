# Exercício 6: Gerenciador de Configurações (Singleton Simples)
# Crie a classe Configuracao que implementa o padrão Singleton.

# Use um atributo de classe (_instancia = None) para rastrear a única instância. ✔️

# Sobrescreva o método mágico __new__(cls): ✔️

# Se cls._instancia for None, chame o super().__new__(cls) para criar a instância e armazene-a. ✔️

# Sempre retorne cls._instancia. ✔️

# Adicione um atributo de instância settings (um dicionário).

# Teste: Crie duas instâncias. Ambas devem ser o mesmo objeto (instancia1 is instancia2 deve ser True). ✔️


from typing import Any


class Configuracoes:
    _instacia = None
    settings: dict[str, Any]
    def __new__(cls):
        if cls._instacia is None:
            cls._instacia = super().__new__(cls)
        return cls._instacia

    def __init__(self) -> None:
        if not hasattr(self, "settings"):
            self.settings = {}


instancia1 = Configuracoes()
instancia2 = Configuracoes()

instancia1.settings["tema"] = 'dark'

print(f"instancia1 is instancia2: {instancia1 is instancia2}")  # True
print(f"Configuração na instancia2: {instancia2.settings['tema']}")  # dark

