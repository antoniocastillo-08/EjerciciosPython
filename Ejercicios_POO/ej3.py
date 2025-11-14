"""
En Python podemos manejar fechas, pero no nos gusta, vamos a crear una clase Date. Debe permitir:

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
    def __init__(self, day, month, year):
        if not self._is_valid_date(day, month, year):
            raise ValueError("Date invalid")
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def _is_leap(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def _days_in_month(year, month):
        if month < 1 or month > 12:
            return 0

        months = [31, 28 + Date._is_leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return months[month - 1]

    @staticmethod
    def _is_valid_date(day, month, year):
        if year <= 0 or month <= 0 or day <= 0:
            return False
        if month > 12:
            return False
        if day > Date._days_in_month(year, month):
            return False
        return True

    def to_days(self):
        y= self.year
        m= self.month
        d= self.day

        total = (y - 1) * 365
        total += (y -1) //4 - (y - 1)//100 + (y - 1)//400

        for month in range(1, m):
            total += Date._days_in_month(y, month)

        total += d
        return total

    @staticmethod
    def _from_days(total_days):
        year = 1
        while True:
            dias_anio = 365 + Date._is_leap(year)
            if total_days > dias_anio:
                total_days -= dias_anio
                year += 1
            else:
                break

        month = 1
        while True:
            dim = Date._days_in_month(year, month)
            if total_days > dim:
                total_days -= dim
                month += 1
            else:
                break

        day = total_days
        return Date(day, month, year)

    def __eq__(self, other):
        return self.to_days() == other.to_days()
    def __lt__(self, other):
        return self.to_days() < other.to_days()
    def __le__(self, other):
        return self.to_days() <= other.to_days()
    def __gt__(self, other):
        return self.to_days() > other.to_days()
    def __ge__(self, other):
        return self.to_days() >= other.to_days()

    def __add__(self, days):
        if not isinstance(days, int):
            raise TypeError("Solo se pueden sumar dias enteros")
        return Date._from_days(self.to_days() + days)
    def __radd__(self, days):
        return days + Date._from_days(self.to_days())


    def __sub__(self, days):
        if isinstance(days, int):
            return Date._from_days(self.to_days() - days)
        else:
            raise TypeError("Solo se pueden restar dias enteros")

    def weekday(self):
        d = self.day
        m = self.month
        y = self.year

        if m < 3:
            m += 12
            y -= 1

        K = y % 100
        J = y // 100

        h = (d + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7

        # h = 0 → sábado
        dias = ["Sábado", "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        return dias[h]

    def __repr__(self):
        return f"Date({self.day}, {self.month}, {self.year})"


# ---------------------------------------------------------
# TEST BÁSICO PARA LA CLASE DATE
# ---------------------------------------------------------

print("=== FECHAS INVÁLIDAS ===")

try:
    Date(78, -45, 0)
    print("ERROR: Esta fecha debería fallar")
except ValueError:
    print("Correcto: Date(78, -45, 0) es inválida")

try:
    Date(31, 6, 2022)
    print("ERROR: Esta fecha debería fallar")
except ValueError:
    print("Correcto: Date(31, 6, 2022) es inválida")

try:
    Date(29, 2, 2022)
    print("ERROR: Esta fecha debería fallar")
except ValueError:
    print("Correcto: Date(29, 2, 2022) es inválida")

print("\n=== COMPARACIONES ===")

a = Date(1, 1, 2022)
b = Date(5, 1, 2022)

print("a < b:", a < b)          # True
print("a <= b:", a <= b)        # True
print("b > a:", b > a)          # True
print("a == Date(1,1,2022):", a == Date(1, 1, 2022))  # True

print("\n=== SUMA Y RESTA DE DÍAS ===")

f = Date(28, 2, 2024)  # año bisiesto

print("f + 1 =", f + 1)   # -> Date(29, 2, 2024)
print("f + 2 =", f + 2)   # -> Date(1, 3, 2024)
print("f - 30 =", f - 30) # -> Fecha correcta 30 días antes

print("\n=== RESTA DE FECHAS ===")

d1 = Date(10, 1, 2022)


print("d1 - 1 =", d1 - 1)  # -> 9

print("\n=== DÍA DE LA SEMANA ===")

f = Date(17, 11, 2022)
print("17/11/2022 fue:", f.weekday())  # "Jueves"

