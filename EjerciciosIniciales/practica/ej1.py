# pedir números para y devolver sus operaciones
print("Introduce dos números")
n1 = int(input())
n2 = int(input())
suma = n1 + n2
resta = n1 - n2
mult = n1 * n2
potencia = n1 ** n2
div = n1 / n2
divEntera = n1 // n2
print("Suma: {}, Resta: {}, Multiplicación: {}, División: {}, Potencia: {}, División entera: {}".format(
    suma, resta, mult, div, potencia, divEntera))
