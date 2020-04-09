# Pedir número e imprimir suma concurrente
num = int(input("Introduce un número\n"))
suma = 0
for i in range(1, num + 1):
    suma += i
print(suma)
