# Exercício 4: Sistema de Notificações (Polimorfismo e Classes Abstratas)
# Crie as seguintes classes:

# Notificador (Classe Abstrata): Use o módulo abc (from abc import ABC, abstractmethod). Deve ter um método abstrato enviar(mensagem). ✔️

# EmailNotificador (Herda de Notificador): Implementa o método enviar(mensagem) simulando o envio de um e-mail (ex: print(f"Enviando Email: {mensagem}")).✔️

# SMSNotificador (Herda de Notificador): Implementa o método enviar(mensagem) simulando o envio de um SMS. ✔️ 

# Função de Teste: Crie uma função notificar_cliente(notificador, mensagem) que aceita qualquer objeto que seja um Notificador e chama seu método enviar().


from abc import ABC, abstractmethod


class Notificador(ABC):

    @abstractmethod
    def enviar(self, msg: str):
        ...


class EmailNotificador(Notificador):
    def enviar(self, msg: str):
        print(f"Enviando Email: {msg}")
    

class SMSNotificador(Notificador):
    def enviar(self, msg: str):
        print(f"Enviando SMS: {msg}")


def notificar_cliente(notificador: Notificador, msg: str):
        notificador.enviar(msg)


if __name__ == "__main__":
    email = EmailNotificador()
    sms = SMSNotificador()
    msg = "Olá bom dia"
    
    notificar_cliente(email, msg)
    notificar_cliente(sms, msg)
    