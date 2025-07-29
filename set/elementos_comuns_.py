# Exercício 1: Elementos Comuns e Únicos entre Listas 🤝
# Dadas duas listas de números inteiros, crie uma função que retorne dois sets:

# Um set contendo todos os números que aparecem em ambas as listas.

# Um set contendo todos os números que aparecem em apenas uma das listas 
# (exclusivos de cada uma).

# Exemplo:

# Python

# lista1 = [1, 2, 3, 4, 5]
# lista2 = [4, 5, 6, 7, 8]
# Saída esperada (aproximada, ordem não importa em sets):
# Comuns: {4, 5}
# Unicos: {1, 2, 3, 6, 7, 8}
def elementos_comuns(x, y):
    e_lista1 = type(x) is list # verifica se a primeira lista é realmente uma lista
    e_lista2 = type(y) is list # verfica se a segunda lista é realmente uma lista
    if e_lista1 and e_lista2:
        if len(x) > 0 and len(y) > 0:
             x = set(x)
             y = set(y)
             comum = x & y
             unico = x ^ y
             return f'Comuns: {comum}\nUnicos: {unico}'
             
        else:
            return 'Porfavor adicione listas com pelo menos 1 elemento!'

    else:
        return 'Adicione duas listas de números!'
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
print(elementos_comuns(lista1, lista2))


# daqui em diante temos um aprimoramento do código:


def elementos_comuns_melhorado(lista1, lista2):
    if not isinstance(lista1, list) or not isinstance(lista2, list):
        raise TypeError("Ambos os argumentos devem ser listas.")
    
    set1 = set(lista1)
    set2 = set(lista2)
    comum = set1 & set2
    unico = set1 ^ set2

    return comum, unico


lista_a =  [1, 2, 3, 4, 5]
lista_b = [4, 5, 6, 7, 8]
comuns_ab, unicos_ab = elementos_comuns_melhorado(lista_a, lista_b)
print(f"Listas: {lista_a}, {lista_b}")
print(f"Comuns: {comuns_ab}") 
print(f"Unicos: {unicos_ab}") 

lista_vazia = []
lista_c = [10, 20, 30]
comuns_vc, unicos_vc = elementos_comuns_melhorado(lista_vazia, lista_c)
print(f"\nListas: {lista_vazia}, {lista_c}")
print(f"Comuns: {comuns_vc}") # Saída: set()
print(f"Unicos: {unicos_vc}")   # Saída: {10, 20, 30}

# Exemplo de erro (sem try-except, o programa pararia aqui)
try:
    elementos_comuns_melhorado("isto não é lista", [1, 2])
except TypeError as e:
    print(f"\nErro capturado: {e}")
