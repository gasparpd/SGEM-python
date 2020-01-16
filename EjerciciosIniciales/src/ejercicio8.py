print("Introduce la longitud de la lista.")
lonlista = int(input())
lista = []

for i in range(0, lonlista):
    print("Introduce el elemento a la lista.")
    elem = input()
    lista.append(elem)
print("Se ha llenado la lista.")

for i in range(1, lonlista + 1):
    print(lista[-i])
print("Lista impresa.")