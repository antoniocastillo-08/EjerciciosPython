#
# Programa que de 3 numeros enteros dice cual es el mayor
# Autor: Antonio Castillo Jiménez
#
print("---Which one is bigger?---")

num_1 = int(input("Introduce the first number: "))
num_2 = int(input("Introduce the second number: "))
num_3 = int(input("Introduce the third number: "))

print("-" * 50)
if num_1 > num_2 and num_1 > num_3:
    print("Biggest number is", num_1)
elif num_2 > num_3 and num_2 > num_1:
    print("Biggest number is", num_2)
elif num_3 > num_1 and num_3 > num_2:
    print("Biggest number is", num_3)
