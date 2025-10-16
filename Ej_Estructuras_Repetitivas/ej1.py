#
# Programa que escribe los numero pares entre dos numeros dados
# Autor: Antonio Castillo Jiménez
#

print("---Printing straight numbers between a limit---")

start = int(input("Write first limit: "))
end = int(input("Write second limit: "))

if start < end:
    for i in range(start, end+1):
        if i % 2 == 0:
            print(i, end= ",")
else:
    for i in range(start, end-1, -1):
        if i % 2 == 1:
            print(i, end = ",")