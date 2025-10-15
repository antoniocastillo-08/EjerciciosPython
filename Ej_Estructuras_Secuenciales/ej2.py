#
# Calcular la hipotenusa de un triángulo rectángulo
# Autor: Antonio Castillo Jiménez
#
import math

print("Calculo de la hipotenusa de un triángulo rectángulo")

lenght_a = float(input("Indique la longitud de uno de sus lados: "))
lenght_b = float(input("Indique la longitud del otro lado: "))

hypotenuse = math.hypot(lenght_a, lenght_b)
# math.hypot() aplica la fórmula de la hipotenusa (c**2 = a**2 + b**2) siendo a y b los parámetros recibidos

print("La hipotenusa del triángulo es:", hypotenuse)

