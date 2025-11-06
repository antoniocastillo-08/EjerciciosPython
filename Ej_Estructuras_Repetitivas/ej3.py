#
# Adivinar el numero random que el programa genera en 10 intentos
# Autor: Antonio Castillo Jiménez
#
from random import randint

N1 = 1
N2 = 100

random_number = randint(N1 , N2)
TRIES= 10

user_number = 0

print("---Adivina el numero generado del 1 al 100---")

#Podria hacerse con un for

while user_number != random_number :
    user_number = int(input("Ingresa un numero entre 1 y 100: "))
    if user_number < random_number :
        TRIES -= 1
        print("El numero es mayor")
    if user_number > random_number :
        TRIES -= 1
        print("El numero es menor")
    if TRIES == 0:
        print(f"ERROR. El numero generado era {random_number}")
        break
    if user_number == random_number :
        print(f"CORRECTO. El numero generado era {random_number}")
        break