# Exercício 1: Sistema de Gestão de Biblioteca (Herança e Composição)
# Chore como as seguintes classes:

# ItemBiblioteca: Uma classe base abstrata (ou com slots para performance,
# dica profissional!) com atributos: titulo(string)
#  e ano_publicacao(int). Deve ter um método detalhes() que retorna uma
# string formatada. ✔️

# Livro(Herda de ItemBiblioteca) : Adicionados os atributos autor(string) e
# isbn(string). Sobrescreva o método detalhes(). ✔️

# Revista(Herda de ItemBiblioteca) : Adicionado o atributo edicao(int).
#  Sobrescreva o método detalhes(). ✔️

# Biblioteca: Uma classe que compõe (tem uma lista de) objetos ItemBiblioteca.
#  Desenvolva métodos para:

# adicionar_item(item): Adiciona um item à lista.

# buscar_por_titulo(titulo): Retorna o item encontrado.


from abc import abstractmethod, ABC


class ItemBiblioteca(ABC):
    def __init__(self, titulo: str, ano_publicacao: int) -> None:
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao

    @abstractmethod
    def detalhes(self) -> str: ...


class Livro(ItemBiblioteca):
    def __init__(self, titulo: str, ano_publicacao: int, autor: str, isbn: str):
        super().__init__(titulo, ano_publicacao)
        self.autor = autor
        self.isbn = isbn

    def detalhes(self):
        return (
            f"Titulo: {self.titulo}\n"
            f"Ano de publicação: {self.ano_publicacao}\n"
            f"Autor: {self.autor}\n"
            f"Isbn: {self.isbn}"
        )


class Revista(ItemBiblioteca):
    def __init__(self, titulo: str, ano_publicacao: int, edicao: int):
        super().__init__(titulo, ano_publicacao)
        self.edicao = edicao

    def detalhes(self):
        return (
            f"Titulo: {self.titulo}\n"
            f"Ano de publicação: {self.ano_publicacao}\n"
            f"Edição: {self.edicao}"
        )

# class Biblioteca():
#     def __init__(self):
#         self.lista = []

#     def adicionar_item(self, *args):

#         for item in args:
#             print(item)


livro1 = Livro('Black Sheep', 2021, 'Pedro', "123456")
print(livro1.detalhes())

# from abc import ABC, abstractmethod

# class ItemBiblioteca(ABC):
#     """
#     Classe base abstrata para itens de biblioteca.
#     Uso de __slots__ para economia de memória (boa prática profissional).
#     """
#     __slots__ = ("titulo", "ano_publicacao")

#     def __init__(self, titulo: str, ano_publicacao: int):
#         self.titulo = titulo
#         self.ano_publicacao = ano_publicacao

#     @abstractmethod
#     def detalhes(self) -> str:
#         """Método que deve ser sobrescrito nas subclasses."""
#         pass


# class Livro(ItemBiblioteca):
#     __slots__ = ("autor", "isbn")

#     def __init__(self, titulo: str, ano_publicacao: int, autor: str, isbn: str):
#         super().__init__(titulo, ano_publicacao)
#         self.autor = autor
#         self.isbn = isbn

#     def detalhes(self) -> str:
#         return (f"[LIVRO]\n"
#                 f"  Título: {self.titulo}\n"
#                 f"  Autor: {self.autor}\n"
#                 f"  Ano: {self.ano_publicacao}\n"
#                 f"  ISBN: {self.isbn}\n")


# class Revista(ItemBiblioteca):
#     __slots__ = ("edicao",)

#     def __init__(self, titulo: str, ano_publicacao: int, edicao: int):
#         super().__init__(titulo, ano_publicacao)
#         self.edicao = edicao

#     def detalhes(self) -> str:
#         return (f"[REVISTA]\n"
#                 f"  Título: {self.titulo}\n"
#                 f"  Ano: {self.ano_publicacao}\n"
#                 f"  Edição: {self.edicao}\n")


# class Biblioteca:
#     """
#     Classe que compõe objetos ItemBiblioteca.
#     """
#     def __init__(self):
#         self.itens = []  # composição: a biblioteca TEM muitos itens

#     def adicionar_item(self, item: ItemBiblioteca):
#         """
#         Adiciona um item (Livro ou Revista) à biblioteca.
#         """
#         if not isinstance(item, ItemBiblioteca):
#             raise TypeError("O item deve herdar de ItemBiblioteca.")
#         self.itens.append(item)

#     def listar_itens(self):
#         """
#         Exibe detalhes de todos os itens armazenados.
#         """
#         if not self.itens:
#             print("A biblioteca está vazia.")
#             return

#         for item in self.itens:
#             print(item.detalhes())



# biblio = Biblioteca()

# livro1 = Livro("Clean Code", 2008, "Robert C. Martin", "9780132350884")
# revista1 = Revista("National Geographic", 2021, 345)

# biblio.adicionar_item(livro1)
# biblio.adicionar_item(revista1)

# biblio.listar_itens()
