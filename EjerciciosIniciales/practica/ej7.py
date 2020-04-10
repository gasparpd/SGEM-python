# El usuario debe adivinar un número random dándole pistas
import random

nmax = 20
nmin = 1
n = random.randint(nmin, nmax)
nuser = int(input("Adivina el número (entre {} y {})\n".format(nmin, nmax)))
while nuser != n:
    if nuser < n:
        print("El número secreto es mayor que {}".format(nuser))
    else:
        print("El número secreto es menor que {}".format(nuser))
    nuser = int(input("Adivina el número (entre {} y {})\n".format(nmin, nmax)))
print("¡Has acertado! el número secreto era {}".format(n))
