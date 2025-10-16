#
# Programa para saber dentro de una secuencia de numeros cuantos son mayores que 0, menores
# que 0 e iguales que 0
# Autor: Antonio Castillo Jiménez
#

print("---Showing how many numbers are greater, lower or equal to 0---")

greater = 0
lower = 0
equal = 0

quantity = int(input("How many numbers are going to be introduced:"))

for i in range(quantity):
    number = int(input(f"Write a number: "))
    if number > 0 :
        greater += 1
    if number < 0 :
        lower += 1
    if number == 0 :
        equal += 1

print(f"Greater number is {greater}")
print(f"Lower number is {lower}")
print(f"Equal is {equal}")