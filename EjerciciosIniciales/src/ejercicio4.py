print("Introduce un número")
n = int(input())
op = 0
for i in range(1, n + 1):
    op = i + op
print("La suma de los números de 1 a {} da un total de: {}".format(n, op))