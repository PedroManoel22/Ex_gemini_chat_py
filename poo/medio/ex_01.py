# Exercício 1: Sistema de Gestão de Biblioteca (Herança e Composição)
# Chore como as seguintes classes:

# ItemBiblioteca: Uma classe base abstrata (ou com slots para performance, dica profissional!) com atributos: titulo(string)
#  e ano_publicacao(int). Deve ter um método detalhes()que retorna uma string formatada.

# Livro(Herda de ItemBiblioteca) : Adicionados os atributos autor(string) e isbn(string). Sobrescreva o método detalhes().

# Revista(Herda de ItemBiblioteca) : Adicionado o atributo edicao(int). Sobrescreva o método detalhes().

# Biblioteca: Uma classe que compõe (tem uma lista de) objetos ItemBiblioteca. Desenvolva métodos para:

# adicionar_item(item): Adiciona um item à lista.

# buscar_por_titulo(titulo): Retorna o item encontrado.

class ItemBiblioteca:
    def __init__(self, titulo, ano_publicacao):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao