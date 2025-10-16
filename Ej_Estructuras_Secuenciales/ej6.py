#
# Programa que calcula la nota final de un examen
# Autor: Antonio Castillo
#
print("---Nota Final de un Examen---")

valores_respuestas ={
    "correcta": 5,
    "incorrecta": -1,
    "blanco": 0
}

correctas = int(input("Número de respuestas correctas: "))
incorrectas = int(input("Número de respuestas incorrectas: "))
blanco = int(input("Número de respuestas en blanco: "))

puntos_totales = (correctas * valores_respuestas["correcta"] + incorrectas * valores_respuestas["incorrecta"]
                  + blanco * valores_respuestas["blanco"])

print("Puntos totales obtenidos:", puntos_totales)

total_preguntas = correctas + incorrectas + blanco
nota_maxima = total_preguntas * 5

nota_normalizada = round(puntos_totales / nota_maxima * 10, 1)

print("---------------")
print("Su nota normalizada (1 - 10) es :", nota_normalizada)

'''
---------
¿Qué tendrías que hacer para facilitar que los puntos que suman los diferentes tipos de respuestas 
puedan cambiar en el futuro?
--------

Se ha creado una colección con los puntos que suman cada tipo de respuesta lo cual lo hace facilmente
modificable a futuro si fuese necesario.
'''
