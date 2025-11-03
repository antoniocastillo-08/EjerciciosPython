"""
Crea una clase, y pruébala, que modele fracciones. Debe permitir:

Crear fracciones indicando numerador y denominador.

Las fracciones pueden operar entre sí.
Sumar, multiplicar, dividir, restar.
Las fracciones se pueden comparar.

Autor: Antonio Castillo Jiménez
"""


class Fraction:
    def __init__(self, num, den=1):
        if den == 0:
            raise ValueError("El denominador no puede ser 0")

        # Simplificación
        divisor = self._mcd(num, den)
        self.num = num // divisor
        self.den = den // divisor

    def __repr__(self):
        return f"{self.num}/{self.den}"

    # ---- Máximo común divisor (sin gcd)
    @staticmethod
    def _mcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # ---- Conversión a Fraction
    @staticmethod
    def _to_fraction(value):
        return value if isinstance(value, Fraction) else Fraction(value, 1)

    # ---- Operaciones aritméticas
    def __add__(self, other):
        other = self._to_fraction(other)
        return Fraction(self.num * other.den + other.num * self.den,
                        self.den * other.den)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        other = self._to_fraction(other)
        return Fraction(self.num * other.den - other.num * self.den,
                        self.den * other.den)

    def __rsub__(self, other):
        other = self._to_fraction(other)
        return other - self

    def __mul__(self, other):
        other = self._to_fraction(other)
        return Fraction(self.num * other.num, self.den * other.den)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        other = self._to_fraction(other)
        if other.num == 0:
            raise ZeroDivisionError("División por cero")
        return Fraction(self.num * other.den, self.den * other.num)

    def __rtruediv__(self, other):
        other = self._to_fraction(other)
        return other / self

    def __eq__(self, other):
        other = self._to_fraction(other)
        return self.num == other.num and self.den == other.den

    def __lt__(self, other):
        other = self._to_fraction(other)
        return self.num * other.den < other.num * self.den

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __ne__(self, other):
        return not self == other

def main():
    t= Fraction(1, 2)
    f = Fraction(2, 4)
    print(t)
    print(f)
    print(t == f)
    print(f == t)

    print(f != t)
    print(f > t)
    print(f < t)
    print(f >= t)
    print(f <= t)

    print(f + t)
    print(f - t)
    print(f * t)
    print(f / t)

    print(f + 1.5)
    print(f - 0.5)

if __name__ == '__main__':
    main()