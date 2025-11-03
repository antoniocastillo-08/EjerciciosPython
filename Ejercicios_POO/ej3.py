"""
En Python podemos manejar fechas pero no nos gusta, vamos a crear una clase Date. Debe permitir:

Crear fechas.
Ejemplo: f = Date(17, 11, 2022)
Ojo!!! Estas fechas son erróneas:
Date(78, -45, 0)
Date(31, 6, 2022)
Date(29, 2, 2022)
Las fechas se pueden comparar.
A las fechas se le pueden sumar y restar días.
Las fechas se pueden restar.
Se debe poder averiguar el día de la semana de una fecha.
"""
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def isvalid(self):
        if self.year < 0 or self.year > datetime.now().year: