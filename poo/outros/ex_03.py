# 2. Loja e Produtos (Agregação)
# Crie duas classes: Produto e CarrinhoDeCompras.

# Produto: Atributos nome, preco. ✔️

# CarrinhoDeCompras: Atributo itens(lista de objetos Produto). ✔️

# Relação de Agregação : Os produtos (objetos Produto) podem existir independentemente do carrinho. ✔️

# Implemente métodos no CarrinhoDeCompras :

# adicionar_produto(produto): Adicionado um produto.  ✔️

# remover_produto(nome_produto): Remova um produto pelo nome. ✔️

# calcular_total(): Retorna a soma dos preços de todos os itens. ✔️

class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return f'Nome = {self.nome}, Preço = {self.preco:.2f}'
    

class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []
    
    
    def adcionar_produto(self, *produtos:Produtos):
        self.itens += produtos
        print(f'\033[1;32mProduto adicionado com sucesso!\033[m')
        
    
    def listar_produtos(self):
        if len(self.itens) != 0:
            print('Lista de produtos:')
            print()
            for produto in self.itens:
                print(produto)

            print()
        else:
            print('\033[1;31mNão há nada para listar!\033[m')
    

    def remover_produto(self, nome):
        for produto in self.itens:
            if produto.nome == nome:
                self.itens.remove(produto)
                print(f'\033[1;31m{produto.nome} removido com sucesso!\033[m\n')

            else:
                print(f'\033[1;36m{nome} não pode ser removido pois não existe!\033[m\n')
    

    def soma_total(self):
        soma = 0
        for produto in self.itens:
            soma += produto.preco
        
        print(f'O preço total do seu carrinho foi de \033[1;32mR${soma:.2f}\033[m')



carrinho = CarrinhoDeCompras()
produto1 = Produtos('Caderno', 25)
produto2 = Produtos('CD', 1.5)
carrinho.adcionar_produto(produto1)
carrinho.adcionar_produto(produto2)
carrinho.listar_produtos()
# carrinho.remover_produto('Caderno')
carrinho.listar_produtos()
carrinho.soma_total()
