#
# Programa que determina el tipo de triángulo a partir de la longitud de sus lados
# Autor: Antonio Castillo Jiménez
#

print("---Knowing the type of tryangle---")

lenght_a = float(input("Introduce the first lenght: "))
lenght_b = float(input("Introduce the second lenght: "))
lenght_c = float(input("Introduce the third lenght: "))

print("-" * 50)
if lenght_a + lenght_c > lenght_b or lenght_b + lenght_c > lenght_a or lenght_a + lenght_b > lenght_c:

    if lenght_a **2 + lenght_b **2 == lenght_c ** 2 or lenght_b **2 + lenght_c **2 == lenght_a ** 2 \
            or lenght_c **2 + lenght_a **2 == lenght_b ** 2:
        print("Is a RIGHT triangle.")
    elif lenght_b==lenght_c==lenght_a:
        print("Is a EQUILATERAL triangle.")
    elif lenght_b==lenght_c or lenght_c==lenght_a or lenght_a == lenght_b:
        print("Is a ISOSCELES triangle.")
    else:
        print("Is a SCALENE triangle.")

else:
    print("Its not a valid triangle.")