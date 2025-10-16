#
# Programa que calcula las horas y minutos correspondientes a una cantidad de minutos
# Autor: Antonio Castillo Jiménez
#
print("---Conversión de minutos a horas---")

minutos_introducidos = int(input("Introduzca los minutos a convertir: "))

horas = minutos_introducidos // 60
minutos = minutos_introducidos % 60

print(minutos_introducidos, "minutos son", horas, "horas y", minutos, "minutos." )