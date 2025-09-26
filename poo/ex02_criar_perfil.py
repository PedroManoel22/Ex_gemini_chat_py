# Exercício 2: Criação de um Perfil de Usuário
# Crie uma classe chamada Usuario que simule um perfil em uma plataforma.

# Atributos :

# nome_de_usuario(string)

# email(string)

# senha(string)

# posts(lista): uma lista que armazenará as postagens do usuário. Inicie-a como uma lista vazia.

# Métodos :

# criar_post(conteudo): Adiciona uma nova string (o post) à lista posts.

# mostrar_perfil(): Imprima o nome do usuário, e-mail e todas as postagens do usuário, formatadas de forma legível.

# alterar_senha(nova_senha): Altera a senha do usuário.

# Dica profissional: Para um portfólio, é uma boa prática adicionar validação básica nos métodos. 
# Por exemplo, antes de aceitar um nova_senha, você pode verificar se ela tem mais de 8 caracteres. 
# Isso demonstra um pensamento mais robusto sobre segurança e qualidade de código.


from email_validator import validate_email, EmailNotValidError

class Usuario():
    
    def __init__(self, nome_usuario, email, senha):
        self.nome_usuario = nome_usuario
        self.email = self._valida_gmail(email)
        self.senha = self._valida_senha(senha)
        self.posts = []
    # Métodos privados para validação.
    # O "_" indica que não devem ser chamados diretamente de fora da classe.
    def _valida_gmail(self, email):
        try:
            v = validate_email(email)
            return email
        except EmailNotValidError as e:
            print(f'\033[1;31m{e}\033[m')
            print('\033[1;31mPor favor coloque um email válido\033[m')
            return None 
    

    def _valida_senha(self, senha):

        if len(senha) < 8:
            raise ValueError('\033[1;31mInsira uma senha com 8 ou mais caracteres\033[m')
        return senha


    def criar_posts(self, conteudo):

        self.posts.append(conteudo)
        print(f'\033[1;36mPost sobre {conteudo} publicado com sucesso!\033[m')

    
    def mostrar_perfl(self):
        print(f'Nome: {self.nome_usuario}')
        print(f'Email: {self.email}')
        print(f'Senha: {self.senha}')
        print(f'Posts: ', end='')
        for post in self.posts:
            print(f'\t{post}')
    def alterar_senha(self):

       while True:
            senha_antiga_input = str(input("Insira sua senha antiga: "))
            
            if senha_antiga_input != self.senha:
                print("Senha antiga incorreta. Tente novamente.")
            else:
                senha_nova = str(input("Insira sua nova senha: "))
                try:
                    self.senha = self._valida_senha(senha_nova)
                    print("Senha alterada com sucesso!")
                    break
                except ValueError as e:
                    print(f"Erro ao alterar a senha: {e}")

if __name__ == "__main__":
    try:
        p1 = Usuario('Pedro', 'pedro@gmail.com', '12345678')
        p1.criar_posts('Férias no Brasil')
        p1.criar_posts('Fotos dos Jogos')
        p1.criar_posts('Foto na praia')
        p1.mostrar_perfl()
        
        # Chamada correta: Sem argumentos, pois o método solicita a senha ao usuário
        p1.alterar_senha()
        
    except ValueError as e:
        print(f"Erro na criação do usuário: {e}")
