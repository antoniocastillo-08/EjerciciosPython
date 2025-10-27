"""
 Programa que genera un array con 20 números aleatorios y pasa todos los pares a las primeras posiciones
 y los impares a las últimas posiciones.
 Autor: Antonio Castillo Jiménez
"""
import random

print("---Array generado aleatoriamente y se posiciona en pares e impares ---")

array_generado = []

pares = []
impares = []

for i in range(20):
    array_generado.append(random.randint(1, 100))

print(array_generado)

for i in range(len(array_generado)):
    if array_generado[i] % 2 == 0:
        pares.append(array_generado[i])
    else:
        impares.append(array_generado[i])

array_generado = pares + impares
print(array_generado)