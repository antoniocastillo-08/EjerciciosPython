#
# Programa que desglosa una cantidad de dinero exacta en monedas y billetes
# Autor: Antonio Castillo Jiménez
#

print("---Desglose en billetes y monedas de una cantidad de euros---")

cantidad = float(input("Introduce la cantidad de dinero (€): "))

billetes = [500,200,100,50,20,10,5]
#Si el usuario añade una cantidad con decimales se ignora ya que no hay monedas de céntimos en este ejercicio
monedas = [2,1]

resto = cantidad

if cantidad > 0:

    for billete in billetes:
        numero = int(resto//billete)
        resto %= billete
        if numero > 0:
            print(numero, "billetes de", billete,"€")

    for moneda in monedas:
        numero = int(resto//moneda)
        resto %= moneda
        if numero > 0:
            print(numero, "monedas de", moneda, "€")
else:
    print("No puede ser un valor negativo")