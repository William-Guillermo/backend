#  scrip  para accesar a modulos y paquetes en python
nombre = 'William'
edad = 37


#funcion saludar
def saludar(nombre):
    return print (f'Hola{nombre}')

class Usuario:

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.premium= False
        
    def premium(self):
        self.premium= True