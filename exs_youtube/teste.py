import getpass

# Solicita a senha sem exibir o que é digitado
senha = getpass.getpass("Digite sua senha: ")

# Para ocultar, você pode processar a senha ou salvá-la em uma variável
print("Senha recebida (não exibida de volta):", senha)

import pwinput

# Solicita a entrada usando um asterisco como máscara
entrada_mascarada = pwinput.pwinput(mask='*')

print("Entrada com máscara:", entrada_mascarada)