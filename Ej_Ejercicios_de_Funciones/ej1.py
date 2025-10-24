"""
 Programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones:
 sumar, restar, multiplicar, dividir y terminar. Cada opción llama
 a una función a la que se le pasan las dos variables y muestra el resultado de la operación.

 Autor: Antonio Castillo Jiménez
 """

def sum_of(a, b):
    return a + b
def rest(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "No se puede dividir por zero"
    else:
        return a / b

def input_variables():
    while True:
        try:
            first = float(input("Introduce un numero para hacer los cálculos: "))
            second = float(input("Introduce un segundo numero para las operaciones: "))
            return first, second
        except ValueError:
            print("El numero ingresado no es un valor válido")

def menu(options):
    print("--------MENU_DE_OPERACIONES---------")
    for i, option in enumerate(options):
        print(i+1, " - ", option)
    while True:
        try:
            option = int(input("Selecciona una opción: "))
            if 1 <= option <= len(options):
                return option
            else:
                print("Valor invalido. El valor opción debe estar entre 1 y" , len(options))
        except ValueError:
            print(f"Por favor introduzca un valor numérico entre 1 y {len(options)}")

def main():
    first, second = 0, 0
    valores_definidos = False #Comprobación de la introducción las variables

    options = ["Introducir las variables",
               "Sumar",
               "Restar",
               "Multiplicar",
               "Dividir",
               "Terminar"]


    while True:
        try:
            option = menu(options)
        except ValueError:
            print("Introduzca una opción valida")
            continue

        print("-" * 50)

        if option == 1:
            first, second = input_variables()
            valores_definidos = True
            print(f"Variables actualizadas: a = {first}, b = {second}")


        elif option in (2,3,4,5):
            if not valores_definidos:
                print("Debe darle valor a las variables primero")
            else:
                if option == 2:
                    print(f"Suma de {first} y {second}: {sum_of(first, second)}")
                elif option == 3:
                    print(f"Resta de {first} y {second}: {rest(first, second)}")
                elif option == 4:
                    print(f"Multiplicacion de {first} y {second}: {multiplication(first, second)}")
                elif option == 5:
                    print(f"Division de {first} y {second}: {divide(first, second)}")

        elif option == 6:
            print("Terminar pulsado. CERRANDO PROGRAMA")
            break

if __name__ == "__main__":

    main()




