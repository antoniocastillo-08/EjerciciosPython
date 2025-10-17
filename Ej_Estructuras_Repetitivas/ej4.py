#
# Programa que informa de la suma de los numeros introducidos dentro de un intervalo, y escribe
# cuantos están fuera del intervalo y cuantos son iguales a los límites del intervalo
# Autor: Antonio Castillo
#

print("---Report the sum of numbers within a range---")

sum_limit = 0
numbers_outside_range = 0
equal_limits = 0

lower_limit = int(input("Enter the lower limit: "))

while True:
    upper_limit = int(input("Enter the upper limit: "))
    if upper_limit > lower_limit :
        break
    print("Upper limit must be greater than lower limit")

while True :
    number = int(input("Enter a number (Type 0 to end the program): "))

    if lower_limit < number < upper_limit :
        sum_limit += number
    elif number < lower_limit or number > upper_limit :
        numbers_outside_range += 1
    else:
        equal_limits += 1

    if number == 0:
        print("-------------------------------------------")
        print("The sum of the numbers between the limits is", sum_limit)
        print("There are", numbers_outside_range, "numbers outside the range")
        print(equal_limits, "numbers are equal to limits")
        print("-------------------------------------------")
        break