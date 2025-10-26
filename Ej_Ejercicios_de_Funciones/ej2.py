""" 
 Biblioteca de funciones
 Autor: Antonio Castillo
"""

def digits(number):
    n_digits = 1
    while number != 0:
        number = number// 10
        if number != 0:
            n_digits += 1
    return n_digits


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True
    return None

def next_prime(number):
    number += 1
    while not is_prime(number):
        number += 1
    return number



def paste_behind(number, n):
    if 10 > n > -10:
        number = number * 10 + n
    else:
        print("Esta función solo sirve para 1 dígito")
        return None
    return number

def paste_ahead(number, n):
    if 10 > n > -10:
        number = number +  (10 ** digits(number)) * n
        return number
    else:
        print("Esta función solo sirve para 1 dígito")
        return None


def remove_behind(number, n):
    number = number // (10 ** n)
    return number

def remove_ahead(number, n):
    total_digits = digits(number)
    if n >= total_digits:
        return 0
    elif n <= 0:
        return number
    else:
        return number % (10 ** (total_digits - n))

def reverse(number):
    reversed_number = 0
    for i in range(1,digits(number) + 1):
        last_digit = number % 10
        reversed_number = paste_behind(reversed_number, last_digit)
        number //= 10
    return reversed_number

def is_palindromic(number):
    if number == reverse(number):
        return True
    else:
        return False

def digit_n(number , n):
    number = remove_ahead(number, n)
    digit = remove_behind(number, digits(number)-1)
    return digit

def digit_position(number, digit):
    total_digits = digits(number)

    for position in range(total_digits):
        if digit_n(number, position) == digit:
            return position

    return -1

def piece_of_number(number, start, end):
    piece = remove_ahead(number, start)
    piece = remove_behind(piece, digits(piece) - (end - start))
    return piece

def concatenate(number , number_concat):
    final_number = number * (10 ** digits(number_concat)) + number_concat
    return final_number

def main():
    test = 12321
    test1 = 12345
    print("---BIBLIOTECA DE FUNCIONES---")
    print(f"El número {test} es palíndromo:", is_palindromic(test))
    print(f"El número {test} es primo:", is_prime(test))
    print(f"El siguiente primo a {test} es:", next_prime(test))
    print(f"El número {test} tiene:", digits(test), "dígitos.")
    print(f"El número {test1} al revés es:", reverse(test1))
    print(f"El dígito que está en la posición 3 de {test1} es:", digit_n(test1, 3))
    print(f"El número 3 aparece por primera vez en {test1} en la posición:", digit_position(test1, 3))
    print(f"El número {test1} quitándole 2 dígitos por detrás es:", remove_behind(test1, 2))
    print(f"El número {test1} quitándole 2 dígitos por delante es:", remove_ahead(test1, 2))
    print(f"El número {test} añadiéndole el dígito 9 por detrás es:", paste_behind(test, 9))
    print(f"El número {test} añadiéndole el dígito 9 por delante es:", paste_ahead(test, 9))
    print(f"El trozo del número {test1} desde la posición 1 hasta la 3 es:", piece_of_number(test1, 1, 3))
    print(f"Concatenando {test} y {test1} obtenemos:", concatenate(test, test1))
    print("---FIN DE LAS PRUEBAS---")

if __name__ == "__main__":
    main()