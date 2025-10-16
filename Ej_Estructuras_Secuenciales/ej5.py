#
# Programa que calcula la hora a la que llegara un ciclista de una ciudad a otra según la hora de salida
# y los segundos del tiempo de viaje
# Autor: Antonio Castillo Jiménez
#
from _datetime import datetime, timedelta

print("---Estimación hora de llegada---")

hora_salida = int(input("Hora de salida (0-23): "))
minutos_salida = int(input("Minutos de salida (0-59): "))
segundos_salida = int(input("Segundos de salida (0-59): "))
segundos_viaje = int(input("Tiempo del viaje en segundos: "))

# Para guardar la hora con datetime es necesario añadir una fecha de un año especifico
salida = datetime(2000,1,1,hora_salida,minutos_salida,segundos_salida)

llegada = salida + timedelta(seconds=segundos_viaje)

print("Saliendo a las",salida.time(), "llegaras a las", llegada.time(), "a la ciudad")