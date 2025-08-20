#Faça make_counter() que retorna uma função que, a cada chamada, retorna contagem incrementada: 1, 2, 3…

def make_counter():
    count = 0
    def incrementa():
         nonlocal count
         count += 1
         return count
    return incrementa

icrementa_1 = make_counter()
print(icrementa_1())
print(icrementa_1())
print(icrementa_1())
