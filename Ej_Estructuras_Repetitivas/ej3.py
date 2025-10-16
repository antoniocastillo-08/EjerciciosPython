#
# Adivinar el numero random que el programa genera en 10 intentos
# Autor: Antonio Castillo Jiménez
#
from random import randint

random_number = randint(1, 100)
tries= 10

user_number = 0

print("---Adivina el numero generado del 1 al 100---")

while user_number != random_number :
    user_number = int(input("Ingresa un numero entre 1 y 100: "))
    if user_number < random_number :
        tries -= 1
        print("El numero es mayor")
    if user_number > random_number :
        tries -= 1
        print("El numero es menor")
    if tries == 0:
        print(f"ERROR. El numero generado era {random_number}")
        break
    if user_number == random_number :
        print(f"CORRECTO. El numero generado era {random_number}")
        break