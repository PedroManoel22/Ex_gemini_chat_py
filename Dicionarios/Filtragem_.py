#Exercício 3: Filtragem de Dicionário por Valor 🔍
#Crie uma função que receba um dicionário e um valor mínimo como entrada.
#A função deve retornar um novo dicionário contendo apenas os pares chave-valor onde o valor é maior ou igual ao valor mínimo.

#Exemplo:

#notas = {'João': 8.5, 'Maria': 9.0, 'Pedro': 7.0, 'Ana': 6.5}
#valor_minimo = 7.5
# Saída esperada: {'João': 8.5, 'Maria': 9.0}

def maiores_notas(alunos, nota_minima):
    notas_acima_media = {}
    for k, v in alunos.items():
        if v >= nota_minima:
            notas_acima_media.setdefault(k,v)
    if len(notas_acima_media) == 0:
        notas_acima_media = 'Ninguém foi capaz de atingir a nota mínima'
    return notas_acima_media 


notas = {'João': 8.5, 'Maria': 9.0, 'Pedro': 7.0, 'Ana': 6.5}
valor_minimo = 7.5
resultado = maiores_notas(notas, valor_minimo)
#Outro exemplo
notas_1 = {'Pedro': 10, 'Ana': 8.5, 'Joana': 7.0, 'Fernando': 8}
resultado_1 = maiores_notas(notas_1, valor_minimo)
#Mais outro exemplo
notas_2 = {'Marcos': 2, 'Tamires': 3.5, 'Isabel': 7.2}
resultado_2 = maiores_notas(notas_2, valor_minimo)
print(resultado)
print()
print(resultado_1)
print()
print(resultado_2)
