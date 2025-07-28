#Exercício 10: Contagem de Elementos Aninhados 🌳
#Imagine um dicionário onde alguns valores são listas, e dentro dessas listas podem haver outros elementos. Crie uma função que percorra um dicionário e, 
#para cada valor que for uma lista, conte o número de elementos dentro dela. 
#O resultado deve ser um novo dicionário com as chaves originais e os valores sendo a contagem dos elementos se o valor original for uma lista, ou o valor original se não for.
#Exemplo:

#dados_variados = {
#    'frutas': ['maçã', 'banana', 'laranja'],
#    'numero': 123,
#    'cores': ['azul', 'verde'],
#    'vazio': []
#}
# Saída esperada:
# {
#   'frutas': 3,
#   'numero': 123,
#   'cores': 2,
#   'vazio': 0
# }


def contagem(dados):
    novo_dict = {}
    for k,v in dados.items():
        if type(v) == list:
            tamanho = len(v)
            novo_dict.setdefault(k,tamanho)
        else:
            novo_dict.setdefault(k,v)
    return novo_dict

dados_variados = {
    'frutas': ['maçã', 'banana', 'laranja'],
    'numero': 123,
    'cores': ['azul', 'verde'],
    'vazio': []
}
print(contagem(dados_variados))
