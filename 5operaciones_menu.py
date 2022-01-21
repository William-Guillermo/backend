#  Menu de operaciones para sumar restar dividir y multiplicar 

def suma(num1,num2):
    
    suma = num1 + num2
    print(f"la suma de los dos numero es: {suma}")
    

def resta(num1, num2):
    pass

def multiplicacion(num1, num2):
    pass

def division(num1, num2):
    pass


def salir():
    exit()

def menu():
    operacion = int(input(""" 

    
        [1]suma
        [2]resta
        [3]multiplicacion
        [4]division
        [5]salir

    Selecciona una opcion del menu: """))

    if operacion == 1:
        numero1 = int(input("Introduce numero1:"))
        numero2 = int(input("Introduce numero1:"))
        suma(numero1,numero2)
        
    if operacion == 5:
        salir()

while True:
    menu()

