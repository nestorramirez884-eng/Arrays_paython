pares = 0
impares = 0

cantidad = int(input("¿Cuántos números vas a ingresar? "))

for i in range(cantidad):
    numero = int(input("Ingresa un número: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
