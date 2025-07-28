# Exercício 2: Remoção de Duplicatas Mantendo a Ordem Original 📏
# Escreva uma função que receba uma lista contendo elementos duplicados e retorne uma nova lista com os elementos únicos, 
# mantendo a ordem original de suas primeiras ocorrências.
# Exemplo:

# Dica: Você pode usar um set para rastrear os elementos já vistos, mas construa a lista final iterando sobre a entrada.
# Python

# lista_com_duplicatas = [1, 5, 2, 8, 5, 1, 9, 2, 7]
# Saída esperada: [1, 5, 2, 8, 9, 7]


def remover_numeros_duplicados(x):
    novo_conjunto = set()
    lista_sem_duplicatas = []
    for elemento in x:
        if elemento not in novo_conjunto:
            lista_sem_duplicatas.append(elemento)
            novo_conjunto.add(elemento)
    return lista_sem_duplicatas



lista_com_duplicatas = [1, 5, 2, 8, 5, 1, 9, 2, 7]
print(remover_numeros_duplicados(lista_com_duplicatas))
