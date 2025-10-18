#
# Programa que nos dice el dia de la semana por su numero
# Autor:Antonio Castillo Jiménez
#
print("---Día de la semana---")

try:
    dia = int(input("Introduce el numero del día: "))

    match dia:
        case 1:
            print("Es LUNES")
        case 2:
            print("Es MARTES")
        case 3:
            print("Es MIERCOLES")
        case 4:
            print("Es JUEVES")
        case 5:
            print("Es VIERNES")
        case 6:
            print("Es SABADO")
        case 7:
            print("Es DOMINGO")
        case _:
            print("El numero no es un dia de la semana")

except ValueError:
    print("El numero es invalido")