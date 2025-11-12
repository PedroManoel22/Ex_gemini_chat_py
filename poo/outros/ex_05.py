# 4. Pedidos e Itens (Composição)
# Crie duas classes: ItemPedido e Pedido.

# ItemPedido: Atributos nome_produto, quantidade, preco_unitario. Método calcular_subtotal().

# Pedido: Atributo itens(lista de objetos ItemPedido).

# Relação de Composição : Um ItemPedido só existe no contexto de um Pedido. Se o Pedido for excluído, os ItemPedido associados não farão mais sentido
# (na prática, eles "morrem" com o pedido).

# Implemente métodos no Pedido :

# adicionar_item(nome, qtd, preco): Cria e adiciona um objeto ItemPedido(demonstrando a composição).

# calcular_valor_total(): Soma os subtotais de todos os itens.

class ItemPedido:
    def __init__(self, nome, qtd, preco_unitario):
        self.nome = nome
        self.qtd = qtd
        self.preco_unitario = preco_unitario

    
    def calcular_sub_total(self):
        ...


class Pedido:
    def __init__(self):
        self.itens: list[ItemPedido] = []
    

    def adicionar_item(self, nome, qtd, preco):
        novo_item = ItemPedido(nome, qtd, preco)
        self.itens.append(novo_item)
        print(f'Item "{nome}" adicionado com sucesso!')
    
    


meu_pedido = Pedido()
meu_pedido.adicionar_item('garrafa', 25, 2.5)

        
        