# Calculadora con bucle for

numero = int(input("Ingrese el numero para calcular su tabla:"))
hasta_donde = int(input(f"Hasta donde deseas multiplicar el numero {numero}: "))

for i in range(hasta_donde):
    print(f" {numero} x {i+1} = {numero*(i+1)}")

