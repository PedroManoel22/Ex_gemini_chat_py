# Exercício 3: Verificação de Subconjunto e Superconjunto ⊆ ⊇
# Crie uma função que receba dois sets e determine se o primeiro set é um subconjunto do segundo (todos os elementos do primeiro estão no segundo) 
# e se o primeiro set é um superconjunto do segundo (contém todos os elementos do segundo). A função deve retornar uma tupla (is_subconjunto, is_superconjunto).

# Exemplo:

# Python

# set_a = {1, 2, 3}
# set_b = {1, 2, 3, 4, 5}
# set_c = {1, 2}
# set_d = {1, 2, 3}

# Saída esperada:
# (set_a, set_b): (True, False)
# (set_a, set_c): (False, True)
# (set_a, set_d): (True, True)