#
# Programa que dice si un numero es primo
# Autor: Antonio Castillo Jiménez
#

print("---Knowing if a number is prime number---")
while True:
    try:
        number = int(input("Enter a number: "))
        break  # sale del bucle si la conversión fue correcta
    except ValueError:
        print("Please enter a valid integer number.")

if number >= 2:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("-----------------------------")
        print(number, "is a prime number")
    else:
        print("-----------------------------")
        print(number, "is NOT a prime_number")
else:
    print("The number must be equal or greater 2")