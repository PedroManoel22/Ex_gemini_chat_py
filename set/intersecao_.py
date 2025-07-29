# Exercício 6: Interseção de Múltiplos Sets ∩
# Escreva uma função que receba uma lista de sets e retorne um único set contendo apenas os elementos que estão presentes em todos os sets da lista.

# Dica: Pense em como você começaria a interseção e como a acumularia.

# Exemplo:

# Python

# conjuntos_numericos = [
#     {1, 2, 3, 4, 5},
#     {3, 4, 5, 6, 7},
#     {4, 5, 8, 9}
# ]
# Saída esperada: {4, 5}


def intersecao_multiplos_sets(lista_de_sets):
    if not isinstance(lista_de_sets, list):
        raise TypeError("A entrada deve ser uma lista de sets.")
    if not lista_de_sets: #se a lista estiver vazio retorna um set vazio 
        return set()
    if len(lista_de_sets) == 1:
        if not isinstance(lista_de_sets[0], set):
             raise TypeError("Todos os elementos da lista devem ser sets.")
        return lista_de_sets[0]
    
    resultado_intersecao = lista_de_sets[0]

    # Itera sobre os sets restantes (a partir do segundo)
    for i in range(1, len(lista_de_sets)):
        current_set = lista_de_sets[i]
        resultado_intersecao = resultado_intersecao.intersection(current_set)
        if not resultado_intersecao:# Otimização, caso a interseção seja um set vazio, não há necessidade de continuar
            break
    return resultado_intersecao



conjuntos = [
    {1, 2, 3, 4, 5},
    {3, 4, 5, 6, 7},
    {4, 5, 8, 9}
]
print(f"Conjuntos: {conjuntos}")
print(f"Interseção : {intersecao_multiplos_sets(conjuntos)}")
# Saída esperada: {4, 5}

