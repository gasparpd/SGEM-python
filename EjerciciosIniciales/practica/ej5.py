# Imprimir suma de los múltiplos de 3 y 5
num = int(input("Introduce un número\n"))
suma = 0
for i in range(1, num + 1):
    mult = False
    for m3 in range(3, num + 1, 3):
        if m3 == i:
            mult = True
    for m5 in range(5, num + 1, 5):
        if m5 == i:
            mult = True
    if mult:
        suma += i
print("Suma de los múltiplos de 3 y 5: {}".format(suma))
