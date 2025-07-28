# Exercício 10: Rastreamento de Itens Vistos Recentemente (Cache Simples) 💾
# Implemente uma classe RecentItemsTracker que usa um set internamente. Esta classe deve ter os seguintes métodos:

# __init__(self, capacity): Inicializa o tracker com uma capacidade máxima de itens a serem lembrados.

# add_item(self, item): Adiciona um item ao tracker. Se o item já existe, ele é "atualizado" (simplesmente permanece no set, mas a lógica para um cache LRU seria mais complexa). 
# Se o set exceder a capacidade, o item mais antigo (ou um item arbitrário se não implementar LRU) deveria ser removido. Para este exercício, 
# apenas garanta que o set não exceda a capacidade, removendo um item arbitrário se necessário (você pode simular 'o mais antigo' 
# removendo o primeiro adicionado ou apenas um aleatório se a capacidade for excedida).

# has_item(self, item): Retorna True se o item estiver no tracker, False caso contrário.

# get_all_items(self): Retorna um set com todos os itens rastreados atualmente.

# Dica: Sets são ótimos para verificar a existência de itens. Para a capacidade, você pode precisar combinar o set com outra estrutura de dados 
# (como uma collections.deque para a ordem, mas um set simples já é um bom começo para a capacidade se a ordem não for rigorosa para remoção). 
# Para simplicidade neste exercício, remova um item arbitrário se o tamanho exceder a capacidade após a adição.

# Exemplo de Uso:

# Python

# tracker = RecentItemsTracker(capacity=3)
# tracker.add_item('item1')
# tracker.add_item('item2')
# print(tracker.has_item('item1')) # Saída: True
# print(tracker.get_all_items()) # Saída: {'item1', 'item2'}

# tracker.add_item('item3')
# print(tracker.get_all_items()) # Saída: {'item1', 'item2', 'item3'}

# tracker.add_item('item4') # Agora a capacidade é excedida, um item antigo deve ser removido
# print(tracker.has_item('item1')) # Pode ser True ou False dependendo de qual foi removido
# print(tracker.get_all_items()) # Saída: Um set com 3 itens (ex: {'item2', 'item3',