# Pedir lista de elementos e imprimir la inversa
nelem = int(input("Dime el número de elementos que contendrá la lista\n"))
list = []
for i in range(nelem):
    elem = input("Introduce el elemento\n")
    list.append(elem)
for e in range(nelem - 1, -1, -1):
    print(list[e])
