# Exercício 4: Sistema de Notificações (Polimorfismo e Classes Abstratas)
# Crie as seguintes classes:

# Notificador (Classe Abstrata): Use o módulo abc (from abc import ABC, abstractmethod). Deve ter um método abstrato enviar(mensagem).

# EmailNotificador (Herda de Notificador): Implementa o método enviar(mensagem) simulando o envio de um e-mail (ex: print(f"Enviando Email: {mensagem}")).

# SMSNotificador (Herda de Notificador): Implementa o método enviar(mensagem) simulando o envio de um SMS.

# Função de Teste: Crie uma função notificar_cliente(notificador, mensagem) que aceita qualquer objeto que seja um Notificador e chama seu método enviar().