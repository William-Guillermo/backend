# Iniciando con POO en Python ejercicio 1


# definimos la clase  Auto  por convension tiene que empezar con mayusculas
from turtle import color


class Auto:
    
    def __init__(self,modelo,color,cantidad_rudas,velocidad_maxima):    # definimos el contructor
        self.modelo = modelo
        self.color = color
        self.cantidad_ruedas = cantidad_rudas
        self.velocidad_maxima = velocidad_maxima
        self.motor = 2.0

    def __str__(self):
        return f"Auto: {self.modelo},{self.color},{self.cantidad_ruedas},{self.velocidad_maxima}"

nissan = Auto('marsh','azul',4,'320')
print(nissan)
print(nissan.modelo)
