# Fábrica de multiplicadores
# Crie make_multiplier(n) que retorna uma função para multiplicar seu argumento por n. Use e teste para n=2, n=5.


def make_multiplier(n):
    # Essa é a função externa. Ela define o multiplicador (n)
    def multiplier(x):
        # Esta é a função interna (closure), que usa 'n' do escopo externo
        return n * x
    return multiplier  # Retorna a função interna como closure

dobro = make_multiplier(2)

print(dobro(10))