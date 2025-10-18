#
# Programa que da la calificación cualitativa de la nota de un examen
# Autor: Antonio Castillo Jiménez
#
print("---Calificación de un Examen---")

try:
    nota = int(input("Indique la nota numerica obtenida (0-10): "))

    if nota > 0:
        if nota < 5:
            print("Nota obtenida: SUSPENSO")
        elif 5 <= nota < 7:
            print("Nota obtenida: APROBADO")
        elif 7 <= nota < 9:
            print("Nota obtenida: NOTABLE")
        elif 9 <= nota < 10:
            print("Nota obtenida: SOBRESALIENTE")
        elif nota ==10 :
            print("Nota obtenida: MATRICULA DE HONOR")
        else:
            print("La nota esta fuera de rango")
    else:
        print("La nota no puede ser negativa")

except ValueError:
    print("Solo notas del 1 al 10")