"""
En Python existen clases para manipular duraciones de tiempo (horas:minutos:segundos),
pero no nos gustan, vamos a hacer una nueva que se llamará Duration y será inmutable.

Crear duraciones de tiempos.
Las duraciones de tiempo se pueden comparar.
A las duraciones de tiempo les puedo sumar y restar segundos.
Las duraciones de tiempo se pueden sumar y restar.
"""

class Duration:
    def __init__(self, hours, minutes, seconds):
        total = hours * 3600 + minutes * 60 + seconds
        self.__hours = total // 3600
        self.__minutes = (total % 3600) // 60
        self.__seconds = total % 60

    def __str__(self):
        return f"{self.__hours} horas::{self.__minutes} minutos::{self.__seconds} segundos"

    def to_seconds(self):
        return (self.__hours * 3600) + (self.__minutes * 60) + self.__seconds

    @property
    def hours(self):
        return self.__hours
    @property
    def minutes(self):
        return self.__minutes
    @property
    def seconds(self):
        return self.__seconds

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()
    def __ne__(self, other):
        return not self == other
    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()
    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def __add__(self, other):
        if isinstance(other, Duration):
            return Duration(0,0,self.to_seconds() + other.to_seconds())
        elif isinstance(other, int):
            return Duration(0,0,self.to_seconds() + other)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Duration):
            return Duration(0,0,self.to_seconds() - other.to_seconds())
        elif isinstance(other, int):
            return Duration(0,0,self.to_seconds() - other)
        else:
            raise TypeError

def main():

    t = Duration(1, 120, 12022)
    d = Duration(1, 120, 120)
    print(t)
    print(d)

    print(t < d)
    print(t > d)
    print(t == d)

    print(t.to_seconds())
    print(t +d)
    print(t + 120)

if __name__ == '__main__':
    main()