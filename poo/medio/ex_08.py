# Exercício 8: Sistema de Validação de Dados (Staticmethod)
# Crie a classe Validador com os seguintes métodos:

# staticmethod eh_email_valido(email): Recebe uma string e retorna True se for um e-mail válido (basta verificar se contém @ e .), False caso contrário.

# staticmethod eh_senha_forte(senha): Recebe uma string e retorna True se tiver pelo menos 8 caracteres.

# Propósito: Demonstra o uso de staticmethods para funções utilitárias que pertencem logicamente à classe, mas não dependem do estado da instância.


class Validador:
    @staticmethod
    def eh_email_valido(email: str) -> bool:
        if "@" in email and "." in email:
            return True

        else:
            return False

    @staticmethod
    def eh_senha_forte(senha: str) -> bool:
        return len(senha) >= 8


v = Validador.eh_email_valido("123456@gmail.com")
v1 = Validador.eh_senha_forte("pedr")
print(v)
print(v1)
