"""
Hacer un programa que le pida al usuario que ingrese su edad y su sexo,
si el usuario es mayor de edad y ademas es menor de 65 años le debe permitir
al usuario quedarse en el programa, en caso
contrario el programa debe deternese. Si es sexo es masculino que el programa
salude al usuario como un caballero y si el sexo es femino que el programa salude al
usuario como una dama
-Para que el usuario ingrese su sexo hacer un menu con condiciones.
"""
masculino = False
edad = int(input("Ingresa tu edad:"))
sexo = int(input("""
Ingresa tu sexo selecciona una opcion valida:
[1] Masculino
[2] Femenino
[3] salir
>>> """))

if sexo == 1:
    masculino = True
elif sexo ==2:
    femenino = True
elif sexo == 3:
    exit()
else:
    print("Opcion no valida")
    exit()

if edad >=18 and edad <=65:
    if masculino == True:
        print(f"Hola Caballero su edad es: {edad}")
    else:
        print(f"Hola Dama su edad es: {edad}")
else :
    print("Lo siento para usar el programa debe ser mayor de 18 y menor de 65")
    exit()
