#Exercício 6: Encontrar Chave com Valor Máximo/Mínimo 📈
#Escreva uma função que receba um dicionário com valores numéricos e retorne a chave que corresponde ao maior valor e a chave que corresponde ao menor valor.
#  Se houver empates, retorne qualquer uma das chaves empatadas.
#Exemplo:

#temperaturas = {'segunda': 25, 'terça': 28, 'quarta': 22, 'quinta': 30, 'sexta': 26}
# Saída esperada: ('quinta', 'quarta') (maior, menor)


def max_min(dias):
    lista = list(dias.values())
    if len(lista) == 0:
        return None
    maior_temp = max(lista)
    menor_temp = min(lista)
    for k, v in dias.items():
        if v == maior_temp:
            maior_temp = k
        elif v == menor_temp:
            menor_temp = k
    return maior_temp , menor_temp

temperaturas = {'segunda': 25, 'terça': 28, 'quarta': 22, 'quinta': 30, 'sexta': 26}
print(max_min(temperaturas))
