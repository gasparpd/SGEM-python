# Imprimir los 20 años bisiestos siguientes a 2016
"""
Para que un año sea bisiesto debe ser divisible por 4, excepto aquellos divisibles entre 100 pero no entre 400
"""
maxBisiestos = 20
n = 2017
for i in range(maxBisiestos):
    bisiesto = False
    while not bisiesto:
        if n % 4 == 0 or n % 400 == 0 and not n % 100 == 0:
            bisiesto = True
            print("{} es bisiesto.".format(n))
        n += 1
print("FIN\nAños imprimidos: {}".format(i + 1))
