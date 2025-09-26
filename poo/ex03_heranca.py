# Exercício 3: Herança - Sistema de Formas Geométricas
# Este exercício é para praticar a herança. Crie uma hierarquia de classes para formas geométricas.

# Crie uma classe base chamada Forma.

# Métodos :

# calcular_area(): Este método não fará nada (pode retornar None), mas ele deve estar lá para ser sobrescrito pelas classes filhas.

# calcular_perimetro(): Assim como o anterior, ele será sobrescrito.

# Crie uma classe filha chamada Retangulo que herde de Forma.

# Atributos :

# largura

# altura

# Métodos :

# __init__(largura, altura): para inicializar os atributos.

# calcular_area(): Retorna a área do retângulo.

# calcular_perimetro(): Retorna o perímetro do retângulo.

# Crie uma classe filha chamada Circuloque herde de Forma.

# Atributos :

# raio

# Métodos :

# __init__(raio): para inicializar o raio.

# calcular_area(): Retorna a área do círculo (use math.pi).

# calcular_perimetro(): Retorna a circunstâncias do círculo.

# Dica profissional: A herança é um dos pilares do POO e fundamental para reutilização de código. No Python, é comum ver esse tipo de arquitetura para resolver problemas complexos de forma organizada.