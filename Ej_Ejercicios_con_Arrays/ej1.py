"""
 Tres listas de 20 números aleatorios con los números, los cuadrados, y los cubos de esos números
 Autor: Antonio Castillo Jiménez
"""

import random

def main():
    number = []
    square = []
    cube = []

    for i in range(20):
        num = random.randint(0, 100)
        number.append(num)
        square.append(num ** 2)
        cube.append(num ** 3)

    print("=" * 50)
    print(f"{'Número':<15} {'Cuadrado':<15} {'Cubo':<15}")
    print("=" * 50)

    for i in range(20):
        print(f"{number[i]:<15} {square[i]:<15} {cube[i]:<15}")

    print("=" * 50)


if __name__ == "__main__":
    main()