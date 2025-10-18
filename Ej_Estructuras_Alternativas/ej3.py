#
# Programa que indica si un año es o no bisiesto
# Autor: Antonio Castillo
#
print("---Knowing if it is a leap year---")
year = int(input("Introduce the year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("The year IS a leap year")
else:
    print("The year IS NOT a leap year")