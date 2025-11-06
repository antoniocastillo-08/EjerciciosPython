#
# Programa que muestra los n primeros números primos
# Autor: Antonio Castillo Jiménez
#
print("---Giving existing prime numbers till a N number---")

try:
    limit = int(input("Enter the limit number: "))
except ValueError:
    print("Please enter a valid integer number.")
else:
    if limit < 2:
        print("There are no prime numbers below 2.")
    else:
        print(f"Prime numbers up to {limit}:")
        for i in range(1, limit + 1):
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                print(i, end=" | ")
