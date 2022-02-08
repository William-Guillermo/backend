# Iniciando con POO en Python ejercicio 1


# definimos la clase  Auto  por convension tiene que empezar con mayusculas
from turtle import color


class Auto:
    
    def __init__(self,modelo,color,cantidad_rudas,velocidad_maxima):    # definimos el contructor
        self.modelo = modelo
        self.color = color
        self.cantidad_ruedas = cantidad_rudas
        self.velocidad_maxima = velocidad_maxima
        self.gama= {"Alta":"Nissan Altima","baja":"Nissan Tsuru"}
        self.motor = 2.0
        

    def __str__(self):
        return f"Auto: {self.modelo},{self.color},{self.cantidad_ruedas},{self.velocidad_maxima}"
    
    def acelerar(self):
        print(f'en auto {self.modelo} a a celerado hasta {self.velocidad_maxima} km')

    def frenar(self):
        print(f'en auto {self.modelo} a frenado')

nissan = Auto('marsh','azul',4,'320')
print(nissan)
print(nissan.modelo)
nissan.acelerar()
nissan.frenar()


# se puede accesar a sus atributos y cambiarlos de la siguiente manera ejemplo   en nissan ya se mando color azul pero la siguiente linea lo cambia

nissan.color= "Amarillo"
print(nissan.color)
print (nissan.gama["Alta"])


