# Tabla de multiplicar del 1 al 12
for i in range(1, 13):
    for e in range(0, 13):
        mult = i * e
        print("{} * {} = {}".format(i, e, mult))
