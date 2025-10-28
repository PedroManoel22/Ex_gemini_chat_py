# Classe Livro:
# Atributos: titulo(string), autor(string), isbn(string, único), disponivel(booleano, padrão True). ✔️
# Métodos:__init__: para inicializar os atributos. ✔️
# emprestar(): muda disponivel para False.✔️
# devolver(): muda disponivel para True. ✔️
# Classe Biblioteca: 
# Atributos: catalogo(dicionário onde a chave é o isbn e o valor é o objeto Livro). ✔️
# Métodos:adicionar_livro(livro): Adicionado um objeto Livro ao catálogo. ✔️
# (Dica Pythônica: Use o isbn como chave para acesso rápido . ✔️
# buscar_livro(titulo_ou_isbn): Retorna o objeto Livro ou uma mensagem que não foi encontrada. ✔️
# emprestar_livro(isbn): Verifique se o livro está no catálogo e disponível, se sim, chama o método emprestar()do objeto 
# Livro.devolver_livro(isbn): 
# Verifique se o livro está no catálogo, se sim, chama o método devolver()do objeto Livro.


# paramos na linha 25 onde esta comentado
class Livro:
    def __init__(self, titulo:str, autor:str, isbn:str, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = disponivel
    

    # def emprestar(self, isbn):
    #     if self.disponivel:
    #         if isbn in Biblioteca.catalago:
    #             self.disponivel = False
    #             return f'Livro: "{self.titulo}" foi emprestado!'
        
    #     return f'Livro: {self.titulo} já esta emprestado!'
    

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return f'Não há como devolver o livro: {self.titulo} pois já está na preteleira'
    
        return f'Livro: "{self.titulo}" foi devolvido!'
    
    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f'Título: {self.titulo} | Autor: {self.autor} | ISBN: {self.isbn} | Status: {status}'


class Biblioteca:
    def __init__(self):
        self.catalogo = {}


    def adicionar_livro(self, livro: Livro):
        if livro.isbn in self.catalogo:
             return f"Erro: Livro com ISBN {livro.isbn} já existe no catálogo."
        
        self.catalogo[livro.isbn] = livro
        return f'Livro: "{livro.titulo}" foi adicionado com sucesso!'
    

    def buscar_livro(self, titulo_isbn, livro: Livro):
        if titulo_isbn in self.catalogo:
            return f'\033[1;32mLivro "{livro.titulo}" encontrado!\033[m'
        return f'livro: "{titulo_isbn}" não foi encontrado'
    

minha_biblioteca = Biblioteca()
livro1 = Livro(titulo='Black Sheep', autor='Pedro Manoel', isbn='123')
livro2 = Livro(titulo='Caderno', autor='Não tem,', isbn='354')
print(minha_biblioteca.adicionar_livro(livro2))
print(minha_biblioteca.buscar_livro(livro2.isbn, livro2))
print(minha_biblioteca.adicionar_livro(livro1))
print(minha_biblioteca.buscar_livro(livro1.isbn, livro1))


