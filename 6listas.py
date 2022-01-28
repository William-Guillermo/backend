# Scrip de listas en python

nombre = ["william","Guillermo","Alonso"]
print(nombre)
nombre.append("Camila") # para agregar un elemnto a la lista al final
print(nombre)
nombre.pop() # elimina el ultimo elemento de una lista
print(nombre)
numero_elemntos = len(nombre)

edades = [25, 30, 45, 18,52]
print(f"los numeros de la lista son: {edades}")
print(f"el numero maximo de la lista es:{max(edades)}")
print(f"el numero minimo de la lista es:{min(edades)}")
print(len(edades))

for edad in edades:
    print(edad)

# scrip de numero pares  con listas de 1 al 100 y un for y solo guarda en la lista los numeros pares

pares = []
for i in range (100):
    if i % 2 == 0:
        pares.append(i)
print(pares)

