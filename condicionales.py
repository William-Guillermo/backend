# Ejemplo practico de Condicionales ,  que el usuario introduzca sus datos  y en base a ellos
#hacer las validaciones con if


print("Introduce tus datos para validacion de acceso:")
try:
    nombre = str(input("Introduce tu nombre:"))
    edad = int(input("Introduce tu edad:"))
    masculino = str(input("Eres Masculino True o False:"))

    if edad >= 18:
        print(f"Bienvenido {nombre},  tu edad es {edad},   eres mayo de edad puedes accesar al portal")
    elif edad<18:
        print("No eres mayo de edad  regresa cuando cumplas 18")
    else:
        print("favor de introducir una edad valida")
except ValueError:
    print("Introduce datos validos ")

