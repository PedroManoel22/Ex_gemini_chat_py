# 1. Sistema de Gestão de Livros (Associação Simples)
# Crie duas classes: Livro e Biblioteca. ✔️

# Livro: Deve ter atributos titulo, autor e isbn. ✔️

# Biblioteca: Deve ter um atributo acervo(uma lista de objetos Livro). ✔️

# Implemente métodos para:

# adicionar_livro(livro): Adicionado um objeto Livro ao acervo. ✔️

# listar_livros(): Imprime o título e o autor de todos os livros. ✔️

# buscar_por_titulo(titulo): Retorna o objeto Livro encontrado. ✔️


class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

        

class Biblioteca:
    def __init__(self):
        self.acervo: list[Livro] = [] 
    
    def adicionar_livro(self, livro: Livro):
        if livro not in self.acervo:
            self.acervo.append(livro)
            print(f'\033[1;32mLivro "{livro.titulo}" adicionado com sucesso!\033[m')
        
        else:
            print(f'\033[1;31mO livro "{livro.titulo}" não pode ser adicionado pois ja está adicionado!\033[m')

    def listar_livros(self):
        if len(self.acervo) > 0:
            print('Livros disponiveis na biblioteca:')
            print()
            for livro in self.acervo:
                print(f'Livro: {livro.titulo}  autor: {livro.autor}')
            print()

        else:
            print(f'\033[1;31mNão há livro para ser listado!\033[m')
    
    def buscar_por_titulo(self):
        titulo = input('Insira o titulo que do livro: ')
        print()
        for livro in self.acervo:
            if titulo == livro.titulo:
                print(f'Dados do livro "{livro.titulo}":\n'
                      f'Título: {livro.titulo}\n'
                      f'Autor: {livro.autor}\n'
                      f'Isbn: {livro.isbn}')
                break
            
            else:
                print(f'\033[1;31mLivro {titulo} não encontrado!\033[m')
                break
                
    


biblioteca = Biblioteca()
livro1 = Livro('oi', 'pedro', 123)
livro2 = Livro('livro2', 'sei nao', 14587)
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.listar_livros()
biblioteca.adicionar_livro(livro2)
biblioteca.buscar_por_titulo()
