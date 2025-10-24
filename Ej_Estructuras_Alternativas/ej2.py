#
# Programa que determina el tipo de triángulo a partir de la longitud de sus lados
# Autor: Antonio Castillo Jiménez
#

print("---Knowing the type of tryangle---")

length_a = float(input("Introduce the first length: "))
length_b = float(input("Introduce the second length: "))
length_c = float(input("Introduce the third length: "))

print("-" * 50)
if length_a + length_c > length_b or length_b + length_c > length_a or length_a + length_b > length_c:

    if length_a **2 + length_b **2 == length_c ** 2 or length_b **2 + length_c **2 == length_a ** 2 \
            or length_c **2 + length_a **2 == length_b ** 2:
        print("Is a RIGHT triangle.")
    elif length_b==length_c==length_a:
        print("Is a EQUILATERAL triangle.")
    elif length_b==length_c or length_c==length_a or length_a == length_b:
        print("Is a ISOSCELES triangle.")
    else:
        print("Is a SCALENE triangle.")

else:
    print("Its not a valid triangle.")