# Exercício 1 – Criar um conjunto
# Crie um conjunto chamado frutas que contenha: "maçã", "banana", "laranja" e "abacaxi". Em seguida, exiba o conjunto.

'''
frutas = {'maça', 'banana', 'laranja','abacaxi'}
print(frutas)
'''

# Exercício 2 – Adicionar elementos
# Adicione a fruta "uva" ao conjunto frutas. O que acontece se você tentar adicionar "banana" novamente?

'''
frutas.add('uva')
print(frutas)
frutas.add('banana')
print(frutas)
frutas.add('melão')
print(frutas)
'''

# Exercício 3 – Remover elementos
# Remova "laranja" do conjunto frutas usando o método remove(). Depois, tente remover "melancia" com remove() e veja o que acontece. Tente novamente com discard().

'''
frutas.remove('laranja')
print(frutas)
frutas.discard('melancia')
print(frutas)
frutas.add('melancia')
print(frutas)
'''
# Exercício 4 – Verificar existência
# Verifique se "maçã" está no conjunto frutas. E "kiwi"?

'''
fruta = 'maça'
if fruta in frutas:
    print(True)
else:
    print(False)
'''
# Exercício 5 – União de conjuntos
# Crie um conjunto carnes com os itens "frango", "carne", "peixe". Faça a união entre frutas e carnes.
'''
frutas = {'maça', 'banana', 'laranja','abacaxi', 'melão', 'melancia'}
carnes = {'frango', 'carne', 'peixe'}
uniao = frutas | carnes
print(uniao)
'''
# Exercício 6 – Interseção
# Crie um conjunto alimentos com os itens "banana", "carne", "abacaxi", "arroz". Encontre a interseção entre frutas e alimentos.
'''
alimentos = {'banana', 'carne', 'abacaxi', 'arroz'}
frutas = {'maça', 'banana', 'laranja','abacaxi', 'melão', 'melancia'}
inter = alimentos & frutas
print(f'Frutas: {frutas}')
print(f'Alimentos: {alimentos}')
print(inter)
'''
# Exercício 7 – Diferença
# Utilize os conjuntos frutas e alimentos para descobrir quais elementos existem em frutas mas não em alimentos.
'''
alimentos = {'banana', 'carne', 'abacaxi', 'arroz'}
frutas = {'maça', 'banana', 'laranja','abacaxi', 'melão', 'melancia'}
diferenca = frutas - alimentos
print(diferenca)
'''
# Exercício 8 – Diferença simétrica
# Encontre os elementos que estão em frutas ou alimentos, mas não em ambos.
'''
alimentos = {'banana', 'carne', 'abacaxi', 'arroz'}
frutas = {'maça', 'banana', 'laranja','abacaxi', 'melão', 'melancia'}
diferenca_simetrica = alimentos ^ frutas
print(diferenca_simetrica)
'''

# Exercício 9 – Set comprehension
# Use um set comprehension para criar um conjunto com o quadrado dos números de 0 a 9 que sejam múltiplos de 3.
# numeros = (range(0,10))
# novo_conjunto = {x**2 for x in numeros if x % 3 == 0} # set comprehension
# print(novo_conjunto)

# Exercício 10 – Congelando conjuntos
# Crie um frozenset com os elementos "a", "b", "c". Tente adicionar um novo elemento e observe o que acontece.

# frozen_set = frozenset({'a', 'b', 'c'})
# print(frozen_set)
# frozen_set.add('d')
#print(frozen_set)


# lista = [numero for numero in range(11) if numero % 2 == 0] 
#print(lista)
# for numeros in range(0,11):
#     if numeros % 2 == 0:
#         lista.append(numeros)
# print(lista)
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [{**produto, 'preco': '{:.2f}'.format(produto['preco'] * 1.1)}for produto in copy.deepcopy(produtos)]
print('Tabela com novos preços:')
print()
print(*novos_produtos, sep='\n')
print()
print('Tabela com preços antigos:')
print()
print(*produtos, sep='\n')
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)