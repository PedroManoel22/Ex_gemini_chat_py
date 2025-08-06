#Exercício 8: Processar Perfil do Usuário (Argumentos Variáveis - **kwargs)
#Crie uma função chamada processar_perfil(**dados) que pode receber um número variável de argumentos de palavra-chave. 
#A função deve imprimir cada par chave-valor dos dados do perfil.
#Exemplo de Uso:
#processar_perfil(nome="Carlos", idade=40, email="carlos@example.com")
# Saída esperada:
# Nome: Carlos
# Idade: 40
# Email: carlos@example.com
#processar_perfil(usuario="admin", nivel="alto")
# Saída esperada:
# Usuario: admin
# Nivel: alto


def processar_perfil(**dados):
        if 'nome' in dados:
                print(f'Nome: {dados['nome']}')
        if 'idade' in dados:
                print(f'Idade: {dados['idade']}')
        if 'email' in dados:
                print(f'Email: {dados['email']}')
        if 'usuario' in dados:
                print(f'Usuário: {dados['usuario']}')
        if 'nivel' in dados:
                print(f'Nível: {dados['nivel']}')

processar_perfil(nome='Carlos', idade= 40, email="carlos@example.com")
processar_perfil(usuario='admin', nivel='alto')
