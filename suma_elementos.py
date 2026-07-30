cantidad = int(input("¿Cuántos números vas a ingresar? "))

suma = 0

for i in range(cantidad):
    numero = float(input("Ingresa un número: "))
    suma += numero

print("La suma de los elementos es:", suma)
