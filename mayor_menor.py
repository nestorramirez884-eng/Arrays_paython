cantidad = int(input("¿Cuántos números vas a ingresar? "))

mayor = None
menor = None

for i in range(cantidad):
    numero = float(input("Ingresa un número: "))

    if mayor is None or numero > mayor:
        mayor = numero

    if menor is None or numero < menor:
        menor = numero

print("Número mayor:", mayor)
print("Número menor:", menor)