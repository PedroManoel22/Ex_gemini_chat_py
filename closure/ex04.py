# Memoização simples#

 #Crie uma closure que armazene resultados anteriores numa cache interna (por exemplo, de uma função custo-computacional) 
# e os retorne quando a mesma entrada ocorrer novamente.

def make_memoized(func):
    cache = {}  # Dicionário para guardar resultados anteriores
    
    def wrapper(arg):
        if arg not in cache:
            cache[arg] = func(arg)
        return cache[arg]
    
    return wrapper

# Exemplo de função "lenta"
import time

def slow_square(n):
    time.sleep(1)  # Simula operação dispendiosa
    return n * n

# Cria uma versão memoizada
memoized_square = make_memoized(slow_square)

# Testes
print(memoized_square(4))  # Leva ~1 segundo
print(memoized_square(4))  # Retorna instantaneamente, usando cache
