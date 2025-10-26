def main():
    numeros = []

    print("Introduce 5 números:")
    for i in range(5):
        num = int(input(f"Número {i + 1}: "))
        numeros.append(num)

    print("\nLista original:")
    print(numeros)

    ultimo = numeros[-1]

    for i in range(len(numeros) - 1, 0, -1):
        numeros[i] = numeros[i - 1]

    numeros[0] = ultimo

    print("\nLista después de rotar:")
    print(numeros)


if __name__ == "__main__":
    main()