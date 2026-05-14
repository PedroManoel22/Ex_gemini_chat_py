# Exercício 3: Classe Vetor2D (Métodos Especiais - __add__ e __mul__)
# Crie a classe Vetor2D com os atributos x e y (float).

# Método __init__: Para inicializar x e y. ✔️

# Método __repr__: Para ter uma representação debugável do objeto (ex: Vetor2D(x=1.0, y=2.0)).✔️

# Método __add__: Permite somar dois objetos Vetor2D usando o operador +. O resultado deve ser um novo objeto Vetor2D (soma componente a componente).✔️

# Método __mul__: Permite multiplicar o vetor por um escalar (float/int) usando o operador *. O resultado deve ser um novo objeto Vetor2D. ✔️

from __future__ import annotations


class Vetor2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self.x:.1f}, y={self.y:.1f})"

    def __add__(self, other: Vetor2D) -> Vetor2D:
        x = self.x + other.x
        y = self.y + other.y
        return Vetor2D(x, y)

    def __mul__(self, num: float) -> Vetor2D:
        x = self.x * num
        y = self.y * num
        return Vetor2D(x, y)


if __name__ == "__main__":
    x1 = Vetor2D(1, 2)
    x2 = Vetor2D(2, 3)
    x3 = x1 + x2
    x4 = x1 * 2
