"""
 Programa que lee 5 números por teclado y los almacene en una lista y rota los elementos a la siguiente posición
 Autor: Antonio Castillo Jiménez
"""
print("---Lista introducido para rotarlo--")

array = []

for i in range(5):
    array.append(int(input("Introduzca los valores para el array: ")))

print(array)

for i in range(len(array)):
    print(i)
    if array[i] < array[i + 1]:
        array[i + 1] = array[i]
    else:
        array[i + 1] = array[i]

