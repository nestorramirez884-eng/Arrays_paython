cantidad = int(input("¿Cuántos elementos tendrá la lista? "))

lista = []

for i in range(cantidad):
    dato = input("Ingresa un elemento: ")
    lista.append(dato)

print("Lista original:", lista)

lista.reverse()

print("Lista invertida:", lista)
