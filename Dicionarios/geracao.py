# Exercício 8: Geração de Relatório de Vendas com Agregação 📈📊
# Dado uma lista de dicionários representando transações de vendas, gere um relatório sumarizado em um novo dicionário. O relatório deve conter:

# Total de vendas por produto.

# Total de vendas por cliente.

# A média de valor por transação.

# O produto mais vendido (em termos de quantidade ou valor, defina um).

# Dica: Use dicionários intermediários para acumular somas e contagens.

# Exemplo:

# Python

# vendas = [
#     {'id': 1, 'produto': 'TV', 'cliente': 'Maria', 'valor': 1500, 'quantidade': 1},
#     {'id': 2, 'produto': 'Celular', 'cliente': 'João', 'valor': 800, 'quantidade': 2},
#     {'id': 3, 'produto': 'TV', 'cliente': 'João', 'valor': 1500, 'quantidade': 1},
#     {'id': 4, 'produto': 'Fone', 'cliente': 'Maria', 'valor': 100, 'quantidade': 3},
#     {'id': 5, 'produto': 'Celular', 'cliente': 'Ana', 'valor': 800, 'quantidade': 1}
# ]
# Saída esperada (exemplo parcial):
# {
#   'total_por_produto': {'TV': 3000, 'Celular': 2400, 'Fone': 300},
#   'total_por_cliente': {'Maria': 1600, 'João': 2300, 'Ana': 800},
#   'media_por_transacao': 940.0,
#   'produto_mais_vendido_valor': 'TV',
#   'produto_mais_vendido_quantidade': 'Celular'
# }