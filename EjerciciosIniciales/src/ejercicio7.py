import random

limit = 9
r = random.randint(1, limit)
print("Número Random creado entre 1 y {}. ¡Adivínalo!".format(limit))
n = int(input())
intentos = 1
while n != r:
    print("Has fallado.")
    if n < r:
        print("Pista: el número es mayor.")
    if n > r:
        print("Pista: el número es menor")
    print("Vuelve a intentarlo.")
    n = int(input())
    intentos += 1
print("Has acertado. Número de intentos: {}".format(intentos))