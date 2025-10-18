#
# Programa que escribe cual es el numero mayor de 5 numeros pedidos
# Autor: Antonio Castillo
#
print("---Which one is bigger?---")

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))
num_4 = int(input("Enter fourth number: "))
num_5 = int(input("Enter fifth number: "))

highest = num_1

if highest < num_2:
    highest = num_2
if highest < num_3:
    highest = num_3
if highest < num_4:
    highest = num_4
if highest < num_5:
    highest = num_5

print("The highest number is", highest)