#
# Programa que, dada la edad de dos personas, informa cual de ellas es mas joven
# Autor: Antonio Castillo Jiménez
#
print("---Who is younger?---")

first_age = int(input("Introduce first person age: "))
second_age = int(input("Introduce second person age: "))

print("-" * 40)
if (first_age > second_age):
    print("The second person is younger than the first.")
elif (first_age < second_age):
    print("The first person is younger than the second.")
else:
    print("They are same age")