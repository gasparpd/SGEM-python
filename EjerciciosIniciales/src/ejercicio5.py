print("Introduce un número")
n = int(input())
op = 0
for i in range(1, n + 1):
    mult3 = False
    mult5 = False
    cont = 1
    while cont <= n:
        if i == cont * 3:
            mult3 = True
        if i == cont * 5:
            mult5 = True
        cont += 1
    if mult3 or mult5:
        op = i + op
print("La suma de los números múltiplos de 3 o 5 del 1 a {} da un total de: {}".format(n, op))