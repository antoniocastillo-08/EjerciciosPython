#
# Programa que calcula la cuota de una hipoteca y su tabla de amortización
# Autor: Antonio Castillo Jiménez
#

print("---Programa para calcular la cuota de una hipoteca y tabla de amortización---")

while True:
    try:
        importe_prestamo = round(float(input("Introduzca el importe del prestamo: ")),2)
        tasa_interes= float(input("Introduzca la tasa de interes anual: ")) / 100 / 12
        plazo_pagos= int(input("Introduzca el plazo del pago en meses: "))

        if importe_prestamo < 0 or tasa_interes < 0 or plazo_pagos <= 0:
            print("No se puede introducir datos negativos.")
            continue
        break
    except ValueError:
        print("Porfavor ingresa un numero valido.")

cuota = importe_prestamo * tasa_interes *(1 + tasa_interes)**plazo_pagos / ((1+tasa_interes)**plazo_pagos - 1)
cuota = round(cuota,2)
print("Cuota mensual:", cuota)

saldo = importe_prestamo

print("MES | CUOTA | INTERES | AMORTIZACION | SALDO RESTANTE")
print("-" * 55)

for mes in range(1, plazo_pagos+1):

    interes = round(saldo * tasa_interes, 2)
    amortizacion = round(cuota - interes, 2)
    saldo = round(saldo - amortizacion, 2)

    if saldo < 0:
        saldo = 0
    print(f"{mes} {cuota} {interes} {amortizacion} {saldo}")