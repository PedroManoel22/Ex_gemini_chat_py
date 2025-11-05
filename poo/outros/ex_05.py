# 4. Pedidos e Itens (Composição)
# Crie duas classes: ItemPedidoe Pedido.

# ItemPedido: Atributos nome_produto, quantidade, preco_unitario. Método calcular_subtotal().

# Pedido: Atributo itens(lista de objetos ItemPedido).

# Relação de Composição : Um ItemPedidosó existe no contexto de um Pedido. Se o Pedidofor excluído, os ItemPedidoassociados não farão mais sentido (na prática, eles "morrem" com o pedido).

# Implemente métodos noPedido :

# adicionar_item(nome, qtd, preco): Cria e adiciona um objeto ItemPedido(demonstrando a composição).

# calcular_valor_total(): Soma os subtotais de todos os itens.